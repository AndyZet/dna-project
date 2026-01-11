"""
DNA-focused visualization module for Bodzia tree documentation
Extracts and prepares data for DNA-specific visualizations
"""
import json
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any
from datetime import datetime


class DNAVisualizer:
    """Extract and prepare DNA data from Bodzia tree documentation and JSON"""
    
    def __init__(self, json_path: str = "data/processed/genealogy/bodzia_complete_tree.json"):
        """
        Initialize DNA visualizer.
        
        Args:
            json_path: Path to Bodzia complete tree JSON file
        """
        self.json_path = Path(json_path)
        self.data = None
        self.dna_individuals = []
        self.dynasty_colors = {
            'Rurikid': '#FF6B6B',
            'Piast': '#4ECDC4',
            'Premyslid': '#95E1D3',
            'Gorm': '#F38181',
            'Normandy': '#AA96DA',
            'Capetian': '#FCBAD3',
            'Ottonian': '#A8D8EA',
            'Arpad': '#FFD93D',
            'default': '#E8E8E8'
        }
    
    def load_data(self) -> Dict[str, Any]:
        """Load JSON data from file"""
        if not self.json_path.exists():
            raise FileNotFoundError(f"JSON file not found: {self.json_path}")
        
        with open(self.json_path, 'r', encoding='utf-8') as f:
            self.data = json.load(f)
        
        return self.data
    
    def extract_dna_tested_individuals(self) -> List[Dict[str, Any]]:
        """
        Extract DNA-tested individuals from JSON data.
        
        Returns:
            List of individuals with DNA test data
        """
        if self.data is None:
            self.load_data()
        
        dna_individuals = []
        for ind in self.data.get('individuals', []):
            if ind.get('dna_tested', False):
                dna_individuals.append(ind)
        
        self.dna_individuals = dna_individuals
        return dna_individuals
    
    def get_dna_markers(self) -> Dict[str, List[Dict[str, Any]]]:
        """
        Extract DNA markers grouped by type.
        
        Returns:
            Dictionary with 'Y-DNA' and 'mtDNA' keys containing lists of individuals
        """
        if not self.dna_individuals:
            self.extract_dna_tested_individuals()
        
        markers = {
            'Y-DNA': [],
            'mtDNA': []
        }
        
        for ind in self.dna_individuals:
            marker = ind.get('dna_marker', '')
            if marker.startswith('Y-DNA'):
                markers['Y-DNA'].append(ind)
            elif marker.startswith('mtDNA'):
                markers['mtDNA'].append(ind)
        
        return markers
    
    def get_bodzia_connections(self) -> Dict[str, Any]:
        """
        Find relationships between DNA-tested individuals and others.
        
        Returns:
            Dictionary with connection data for network visualization
        """
        if self.data is None:
            self.load_data()
        
        if not self.dna_individuals:
            self.extract_dna_tested_individuals()
        
        connections = {
            'nodes': [],
            'edges': []
        }
        
        # Add DNA-tested individuals as nodes
        dna_ids = {ind['id'] for ind in self.dna_individuals}
        
        for ind in self.dna_individuals:
            connections['nodes'].append({
                'id': ind['id'],
                'name': ind['name'],
                'dna_marker': ind.get('dna_marker', ''),
                'dynasty': ind.get('dynasty', 'default'),
                'is_dna_tested': True,
                'burial_code': self._extract_burial_code(ind)
            })
        
        # Find connections through families
        for family in self.data.get('families', []):
            husband_id = family.get('husband_id')
            wife_id = family.get('wife_id')
            children = family.get('children', [])
            
            # Check if any family member is DNA-tested
            family_dna_members = []
            if husband_id and husband_id in dna_ids:
                family_dna_members.append(husband_id)
            if wife_id and wife_id in dna_ids:
                family_dna_members.append(wife_id)
            if any(child_id in dna_ids for child_id in children):
                family_dna_members.extend([c for c in children if c in dna_ids])
            
            # Add edges for DNA-tested individuals
            if len(family_dna_members) > 1:
                # Connect DNA-tested individuals within family
                for i in range(len(family_dna_members)):
                    for j in range(i + 1, len(family_dna_members)):
                        connections['edges'].append({
                            'source': family_dna_members[i],
                            'target': family_dna_members[j],
                            'type': 'family',
                            'relationship': 'spouse' if (husband_id in family_dna_members and wife_id in family_dna_members) else 'sibling'
                        })
            
            # Add connections to non-DNA-tested family members
            for dna_id in family_dna_members:
                if husband_id and husband_id not in dna_ids:
                    connections['edges'].append({
                        'source': dna_id,
                        'target': husband_id,
                        'type': 'family',
                        'relationship': 'spouse' if dna_id == wife_id else 'parent'
                    })
                if wife_id and wife_id not in dna_ids:
                    connections['edges'].append({
                        'source': dna_id,
                        'target': wife_id,
                        'type': 'family',
                        'relationship': 'spouse' if dna_id == husband_id else 'parent'
                    })
                for child_id in children:
                    if child_id not in dna_ids:
                        connections['edges'].append({
                            'source': dna_id,
                            'target': child_id,
                            'type': 'family',
                            'relationship': 'parent'
                        })
        
        # Add non-DNA-tested connected individuals as nodes
        connected_ids = set()
        for edge in connections['edges']:
            connected_ids.add(edge['target'])
        
        for ind in self.data.get('individuals', []):
            if ind['id'] in connected_ids and ind['id'] not in dna_ids:
                connections['nodes'].append({
                    'id': ind['id'],
                    'name': ind['name'],
                    'dynasty': ind.get('dynasty', 'default'),
                    'is_dna_tested': False
                })
        
        return connections
    
    def _extract_burial_code(self, individual: Dict[str, Any]) -> Optional[str]:
        """Extract burial code from notes"""
        notes = individual.get('notes', [])
        for note in notes:
            if 'E864' in note or 'VK' in note:
                # Extract code like E864/I, E864/II, VK155, VK157
                match = re.search(r'(E\d+/\w+|VK\d+)', note)
                if match:
                    return match.group(1)
        return None
    
    def prepare_timeline_data(self) -> List[Dict[str, Any]]:
        """
        Organize individuals by birth/death dates for timeline visualization.
        
        Returns:
            List of timeline entries with dates and DNA marker info
        """
        if not self.dna_individuals:
            self.extract_dna_tested_individuals()
        
        timeline_data = []
        
        for ind in self.dna_individuals:
            birth = ind.get('birth', {})
            death = ind.get('death', {})
            
            birth_date = None
            death_date = None
            
            if isinstance(birth, dict):
                birth_date = birth.get('date')
            if isinstance(death, dict):
                death_date = death.get('date')
            
            # Parse dates (handle year-only format)
            birth_year = self._parse_year(birth_date) if birth_date else None
            death_year = self._parse_year(death_date) if death_date else None
            
            timeline_data.append({
                'id': ind['id'],
                'name': ind['name'],
                'birth_year': birth_year,
                'death_year': death_year,
                'dna_marker': ind.get('dna_marker', ''),
                'marker_type': 'Y-DNA' if ind.get('dna_marker', '').startswith('Y-DNA') else 'mtDNA',
                'dynasty': ind.get('dynasty', 'default'),
                'burial_code': self._extract_burial_code(ind)
            })
        
        return timeline_data
    
    def _parse_year(self, date_str: str) -> Optional[int]:
        """Parse year from date string"""
        if not date_str or date_str == 'Unknown':
            return None
        
        # Extract first 4-digit number (year)
        match = re.search(r'\d{4}', str(date_str))
        if match:
            return int(match.group())
        return None
    
    def get_dynasty_dna_distribution(self) -> Dict[str, Dict[str, Any]]:
        """
        Get distribution of DNA-tested individuals by dynasty.
        
        Returns:
            Dictionary mapping dynasty names to counts and individuals
        """
        if self.data is None:
            self.load_data()
        
        if not self.dna_individuals:
            self.extract_dna_tested_individuals()
        
        distribution = {}
        
        # Count all individuals by dynasty
        total_by_dynasty = {}
        for ind in self.data.get('individuals', []):
            dynasty = ind.get('dynasty', 'default')
            total_by_dynasty[dynasty] = total_by_dynasty.get(dynasty, 0) + 1
        
        # Count DNA-tested by dynasty
        dna_by_dynasty = {}
        for ind in self.dna_individuals:
            dynasty = ind.get('dynasty', 'default')
            if dynasty not in dna_by_dynasty:
                dna_by_dynasty[dynasty] = []
            dna_by_dynasty[dynasty].append(ind)
        
        # Combine data
        for dynasty in set(list(total_by_dynasty.keys()) + list(dna_by_dynasty.keys())):
            distribution[dynasty] = {
                'total': total_by_dynasty.get(dynasty, 0),
                'dna_tested': len(dna_by_dynasty.get(dynasty, [])),
                'dna_individuals': dna_by_dynasty.get(dynasty, []),
                'color': self.dynasty_colors.get(dynasty, self.dynasty_colors['default'])
            }
        
        return distribution
    
    def get_bodzia_period(self) -> Tuple[int, int]:
        """Get Bodzia active period dates"""
        return (950, 1020)
    
    def create_dna_markers_chart(self, output_path: str = "output/visualizations/dna/dna_markers_chart.png"):
        """
        Create bar chart showing DNA markers by type.
        
        Args:
            output_path: Path to save the chart
        """
        import matplotlib.pyplot as plt
        import seaborn as sns
        
        markers = self.get_dna_markers()
        
        # Prepare data
        chart_data = []
        for marker_type, individuals in markers.items():
            for ind in individuals:
                marker = ind.get('dna_marker', '')
                # Extract marker code (e.g., "I1-S2077" from "Y-DNA I1-S2077")
                marker_code = marker.replace('Y-DNA ', '').replace('mtDNA ', '')
                chart_data.append({
                    'Individual': ind['name'],
                    'Marker Type': marker_type,
                    'Marker': marker_code,
                    'Burial Code': self._extract_burial_code(ind) or 'N/A'
                })
        
        if not chart_data:
            print("No DNA markers found")
            return
        
        # Create figure
        fig, ax = plt.subplots(figsize=(12, 6))
        
        # Group by marker type
        y_dna_data = [d for d in chart_data if d['Marker Type'] == 'Y-DNA']
        mtdna_data = [d for d in chart_data if d['Marker Type'] == 'mtDNA']
        
        x_pos = 0
        width = 0.35
        
        # Plot Y-DNA markers
        if y_dna_data:
            y_positions = list(range(len(y_dna_data)))
            y_labels = [f"{d['Individual']}\n({d['Marker']})" for d in y_dna_data]
            colors_y = ['#2E86AB' if 'I1' in d['Marker'] else '#A23B72' for d in y_dna_data]
            
            bars1 = ax.barh([y - width/2 for y in y_positions], 
                           [1] * len(y_dna_data), 
                           width, 
                           label='Y-DNA',
                           color=colors_y,
                           alpha=0.8)
            
            # Add burial codes as annotations
            for i, (bar, data) in enumerate(zip(bars1, y_dna_data)):
                if data['Burial Code'] != 'N/A':
                    ax.text(0.5, y_positions[i] - width/2, 
                           f"  {data['Burial Code']}", 
                           va='center', fontsize=9, style='italic')
        
        # Plot mtDNA markers
        if mtdna_data:
            mtdna_start = len(y_dna_data) if y_dna_data else 0
            mtdna_positions = list(range(mtdna_start, mtdna_start + len(mtdna_data)))
            mtdna_labels = [f"{d['Individual']}\n({d['Marker']})" for d in mtdna_data]
            colors_mt = ['#F18F01'] * len(mtdna_data)
            
            bars2 = ax.barh([y + width/2 for y in mtdna_positions], 
                           [1] * len(mtdna_data), 
                           width, 
                           label='mtDNA',
                           color=colors_mt,
                           alpha=0.8)
            
            # Add burial codes as annotations
            for i, (bar, data) in enumerate(zip(bars2, mtdna_data)):
                if data['Burial Code'] != 'N/A':
                    ax.text(0.5, mtdna_positions[i] + width/2, 
                           f"  {data['Burial Code']}", 
                           va='center', fontsize=9, style='italic')
        
        # Combine labels
        all_labels = []
        if y_dna_data:
            all_labels.extend(y_labels)
        if mtdna_data:
            all_labels.extend(mtdna_labels)
        
        all_positions = []
        if y_dna_data:
            all_positions.extend([y - width/2 for y in y_positions])
        if mtdna_data:
            all_positions.extend([y + width/2 for y in mtdna_positions])
        
        ax.set_yticks(all_positions)
        ax.set_yticklabels(all_labels, fontsize=10)
        ax.set_xlabel('DNA Marker Type', fontsize=12, fontweight='bold')
        ax.set_title('Bodzia DNA-Tested Individuals - Genetic Markers', 
                    fontsize=14, fontweight='bold', pad=20)
        ax.set_xlim(0, 1.2)
        ax.set_xticks([])
        ax.legend(loc='upper right', fontsize=11)
        ax.grid(axis='x', alpha=0.3, linestyle='--')
        
        plt.tight_layout()
        
        # Save
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"✓ Created DNA markers chart: {output_path}")
    
    def create_dna_network(self, output_path: str = "output/visualizations/dna/bodzia_dna_network.svg"):
        """
        Create network diagram showing DNA-tested individuals and connections.
        
        Args:
            output_path: Path to save the network diagram
        """
        import graphviz
        
        connections = self.get_bodzia_connections()
        
        # Create graph
        dot = graphviz.Digraph(
            name='Bodzia_DNA_Network',
            format='svg',
            engine='fdp',  # Force-directed layout
            graph_attr={
                'bgcolor': 'white',
                'fontname': 'Arial',
                'fontsize': '12',
                'splines': 'curved',
                'overlap': 'false'
            },
            node_attr={
                'style': 'filled',
                'fontname': 'Arial',
                'fontsize': '10',
                'shape': 'ellipse'
            },
            edge_attr={
                'color': '#666666',
                'arrowsize': '0.7'
            }
        )
        
        dot.attr(label='Bodzia DNA-Tested Individuals Network', 
                labelloc='t', fontsize='16', fontname='Arial Bold')
        
        # Add nodes
        for node in connections['nodes']:
            if node.get('is_dna_tested'):
                # DNA-tested individuals - highlighted
                marker = node.get('dna_marker', '')
                marker_type = 'Y-DNA' if marker.startswith('Y-DNA') else 'mtDNA'
                color = '#2E86AB' if marker_type == 'Y-DNA' else '#F18F01'
                
                label = f"{node['name']}\\n{marker}"
                if node.get('burial_code'):
                    label += f"\\n({node['burial_code']})"
                
                dot.node(
                    node['id'],
                    label=label,
                    fillcolor=color,
                    color='black',
                    style='filled,bold',
                    penwidth='3'
                )
            else:
                # Connected individuals - lighter
                dynasty_color = self.dynasty_colors.get(node['dynasty'], self.dynasty_colors['default'])
                dot.node(
                    node['id'],
                    label=node['name'],
                    fillcolor=dynasty_color,
                    color='black',
                    style='filled',
                    penwidth='1'
                )
        
        # Add edges
        for edge in connections['edges']:
            dot.edge(
                edge['source'],
                edge['target'],
                label=edge.get('relationship', ''),
                style='solid' if edge.get('type') == 'family' else 'dashed'
            )
        
        # Render
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        dot.render(str(output_file.with_suffix('')), cleanup=False)
        
        print(f"✓ Created DNA network diagram: {output_path}")
    
    def create_dna_timeline(self, output_path: str = "output/visualizations/dna/dna_timeline.png"):
        """
        Create timeline visualization with Bodzia period highlighted.
        
        Args:
            output_path: Path to save the timeline
        """
        import matplotlib.pyplot as plt
        import matplotlib.patches as mpatches
        
        timeline_data = self.prepare_timeline_data()
        bodzia_start, bodzia_end = self.get_bodzia_period()
        
        if not timeline_data:
            print("No timeline data available")
            return
        
        # Create figure
        fig, ax = plt.subplots(figsize=(14, 8))
        
        # Shade Bodzia period
        ax.axvspan(bodzia_start, bodzia_end, alpha=0.2, color='gray', 
                  label=f'Bodzia Active Period ({bodzia_start}-{bodzia_end} CE)')
        
        # Plot timeline bars for each individual
        y_pos = 0
        y_labels = []
        y_positions = []
        
        for ind in timeline_data:
            birth_year = ind['birth_year']
            death_year = ind['death_year']
            
            if birth_year is None or death_year is None:
                continue
            
            # Determine color based on marker type
            if ind['marker_type'] == 'Y-DNA':
                color = '#2E86AB'
            else:
                color = '#F18F01'
            
            # Draw lifespan bar
            width = death_year - birth_year
            bar = ax.barh(y_pos, width, left=birth_year, height=0.6, 
                         color=color, alpha=0.8, edgecolor='black', linewidth=1.5)
            
            # Add label
            label = f"{ind['name']} ({ind['marker_type']})"
            if ind.get('burial_code'):
                label += f" [{ind['burial_code']}]"
            y_labels.append(label)
            y_positions.append(y_pos)
            
            # Add marker annotation
            ax.plot(birth_year, y_pos, 'o', color='black', markersize=8)
            ax.plot(death_year, y_pos, 's', color='black', markersize=8)
            
            y_pos += 1
        
        # Set y-axis
        ax.set_yticks(y_positions)
        ax.set_yticklabels(y_labels, fontsize=10)
        ax.invert_yaxis()
        
        # Set x-axis
        min_year = min([ind['birth_year'] for ind in timeline_data if ind['birth_year']], default=800)
        max_year = max([ind['death_year'] for ind in timeline_data if ind['death_year']], default=1200)
        ax.set_xlim(min_year - 50, max_year + 50)
        ax.set_xlabel('Year (CE)', fontsize=12, fontweight='bold')
        ax.set_title('DNA-Tested Individuals Timeline - Bodzia Period Context', 
                    fontsize=14, fontweight='bold', pad=20)
        
        # Add legend
        y_dna_patch = mpatches.Patch(color='#2E86AB', label='Y-DNA')
        mtdna_patch = mpatches.Patch(color='#F18F01', label='mtDNA')
        ax.legend(handles=[y_dna_patch, mtdna_patch], loc='upper left', fontsize=11)
        
        ax.grid(axis='x', alpha=0.3, linestyle='--')
        
        plt.tight_layout()
        
        # Save
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"✓ Created DNA timeline: {output_path}")
    
    def create_dynasty_distribution(self, output_path: str = "output/visualizations/dna/dynasty_dna_distribution.png"):
        """
        Create dynasty DNA distribution chart.
        
        Args:
            output_path: Path to save the chart
        """
        import matplotlib.pyplot as plt
        
        distribution = self.get_dynasty_dna_distribution()
        
        # Prepare data
        dynasties = []
        totals = []
        dna_counts = []
        colors_list = []
        
        for dynasty, data in sorted(distribution.items()):
            if data['total'] > 0:  # Only include dynasties with individuals
                dynasties.append(dynasty)
                totals.append(data['total'])
                dna_counts.append(data['dna_tested'])
                colors_list.append(data['color'])
        
        if not dynasties:
            print("No dynasty data available")
            return
        
        # Create figure with subplots
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
        
        # Pie chart for total distribution
        ax1.pie(totals, labels=dynasties, colors=colors_list, autopct='%1.1f%%',
               startangle=90, textprops={'fontsize': 10})
        ax1.set_title('Total Individuals by Dynasty', fontsize=12, fontweight='bold')
        
        # Bar chart showing DNA-tested vs total
        x_pos = range(len(dynasties))
        width = 0.35
        
        bars1 = ax2.bar([x - width/2 for x in x_pos], totals, width, 
                       label='Total Individuals', color=colors_list, alpha=0.7)
        bars2 = ax2.bar([x + width/2 for x in x_pos], dna_counts, width,
                       label='DNA Tested', color=['#FF0000'] * len(dynasties), alpha=0.9)
        
        ax2.set_xlabel('Dynasty', fontsize=12, fontweight='bold')
        ax2.set_ylabel('Count', fontsize=12, fontweight='bold')
        ax2.set_title('DNA-Tested Individuals by Dynasty', fontsize=12, fontweight='bold')
        ax2.set_xticks(x_pos)
        ax2.set_xticklabels(dynasties, rotation=45, ha='right', fontsize=10)
        ax2.legend(fontsize=11)
        ax2.grid(axis='y', alpha=0.3, linestyle='--')
        
        # Add value labels on bars
        for bars in [bars1, bars2]:
            for bar in bars:
                height = bar.get_height()
                if height > 0:
                    ax2.text(bar.get_x() + bar.get_width()/2., height,
                           f'{int(height)}',
                           ha='center', va='bottom', fontsize=9)
        
        plt.suptitle('Bodzia Tree - Dynasty Distribution and DNA Testing', 
                    fontsize=14, fontweight='bold', y=1.02)
        plt.tight_layout()
        
        # Save
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"✓ Created dynasty distribution chart: {output_path}")
    
    def create_interactive_dashboard(self, output_path: str = "output/visualizations/dna/bodzia_dna_dashboard.html"):
        """
        Create interactive Plotly HTML dashboard combining all visualizations.
        
        Args:
            output_path: Path to save the HTML dashboard
        """
        import plotly.graph_objects as go
        from plotly.subplots import make_subplots
        import plotly.express as px
        
        # Get data
        markers = self.get_dna_markers()
        timeline_data = self.prepare_timeline_data()
        distribution = self.get_dynasty_dna_distribution()
        bodzia_start, bodzia_end = self.get_bodzia_period()
        
        # Create subplots
        fig = make_subplots(
            rows=3, cols=2,
            subplot_titles=(
                'DNA Markers by Type',
                'Timeline with Bodzia Period',
                'Dynasty Distribution (Total)',
                'DNA-Tested by Dynasty',
                'DNA Marker Summary',
                'Bodzia Site Connections'
            ),
            specs=[[{"type": "bar"}, {"type": "scatter"}],
                   [{"type": "pie"}, {"type": "bar"}],
                   [{"type": "table"}, {"type": "scatter"}]],
            vertical_spacing=0.12,
            horizontal_spacing=0.1
        )
        
        # 1. DNA Markers Bar Chart
        marker_types = []
        marker_names = []
        marker_codes = []
        colors = []
        
        for marker_type, individuals in markers.items():
            for ind in individuals:
                marker_types.append(marker_type)
                marker_names.append(ind['name'])
                marker_code = ind.get('dna_marker', '').replace('Y-DNA ', '').replace('mtDNA ', '')
                marker_codes.append(marker_code)
                colors.append('#2E86AB' if marker_type == 'Y-DNA' else '#F18F01')
        
        fig.add_trace(
            go.Bar(
                x=marker_types,
                y=[1] * len(marker_types),
                text=[f"{name}<br>{code}" for name, code in zip(marker_names, marker_codes)],
                textposition='inside',
                marker_color=colors,
                name='DNA Markers',
                hovertemplate='<b>%{text}</b><br>Type: %{x}<extra></extra>'
            ),
            row=1, col=1
        )
        
        # 2. Timeline
        for ind in timeline_data:
            if ind['birth_year'] and ind['death_year']:
                marker_color = '#2E86AB' if ind['marker_type'] == 'Y-DNA' else '#F18F01'
                fig.add_trace(
                    go.Scatter(
                        x=[ind['birth_year'], ind['death_year']],
                        y=[ind['name'], ind['name']],
                        mode='lines+markers',
                        name=ind['name'],
                        line=dict(color=marker_color, width=4),
                        marker=dict(size=10, color=marker_color),
                        hovertemplate=f"<b>{ind['name']}</b><br>" +
                                    f"Marker: {ind['dna_marker']}<br>" +
                                    f"Lifespan: {ind['birth_year']}-{ind['death_year']} CE<extra></extra>"
                    ),
                    row=1, col=2
                )
        
        # Add Bodzia period shading
        fig.add_vrect(
            x0=bodzia_start, x1=bodzia_end,
            fillcolor="gray", opacity=0.2,
            layer="below", line_width=0,
            annotation_text=f"Bodzia Period ({bodzia_start}-{bodzia_end} CE)",
            annotation_position="top left",
            row=1, col=2
        )
        
        # 3. Dynasty Distribution Pie
        dynasties = []
        totals = []
        colors_list = []
        
        for dynasty, data in sorted(distribution.items()):
            if data['total'] > 0:
                dynasties.append(dynasty)
                totals.append(data['total'])
                colors_list.append(data['color'])
        
        fig.add_trace(
            go.Pie(
                labels=dynasties,
                values=totals,
                marker_colors=colors_list,
                name="Dynasty Distribution",
                hovertemplate='<b>%{label}</b><br>Total: %{value}<br>Percentage: %{percent}<extra></extra>'
            ),
            row=2, col=1
        )
        
        # 4. DNA-Tested by Dynasty Bar
        dna_counts = [distribution[d]['dna_tested'] for d in dynasties]
        fig.add_trace(
            go.Bar(
                x=dynasties,
                y=dna_counts,
                marker_color=['#FF0000' if count > 0 else colors_list[i] for i, count in enumerate(dna_counts)],
                name='DNA Tested',
                hovertemplate='<b>%{x}</b><br>DNA Tested: %{y}<extra></extra>',
                text=dna_counts,
                textposition='outside'
            ),
            row=2, col=2
        )
        
        # 5. Summary Table
        table_data = []
        for ind in self.dna_individuals if hasattr(self, 'dna_individuals') and self.dna_individuals else []:
            burial_code = self._extract_burial_code(ind)
            table_data.append([
                ind['name'],
                ind.get('dna_marker', ''),
                burial_code or 'N/A',
                ind.get('dynasty', 'default'),
                f"{ind.get('birth', {}).get('date', '?')} - {ind.get('death', {}).get('date', '?')}"
            ])
        
        if table_data:
            fig.add_trace(
                go.Table(
                    header=dict(
                        values=['Name', 'DNA Marker', 'Burial Code', 'Dynasty', 'Lifespan'],
                        fill_color='paleturquoise',
                        align='left',
                        font=dict(size=12, color='black')
                    ),
                    cells=dict(
                        values=list(zip(*table_data)),
                        fill_color='white',
                        align='left',
                        font=dict(size=11)
                    )
                ),
                row=3, col=1
            )
        
        # 6. Connections scatter (placeholder - showing DNA-tested individuals)
        connections = self.get_bodzia_connections()
        dna_nodes = [n for n in connections['nodes'] if n.get('is_dna_tested')]
        
        x_pos = [i for i in range(len(dna_nodes))]
        y_pos = [1] * len(dna_nodes)
        node_names = [n['name'] for n in dna_nodes]
        node_markers = [n.get('dna_marker', '') for n in dna_nodes]
        
        fig.add_trace(
            go.Scatter(
                x=x_pos,
                y=y_pos,
                mode='markers+text',
                text=node_names,
                textposition='top center',
                marker=dict(
                    size=20,
                    color=['#2E86AB' if 'Y-DNA' in m else '#F18F01' for m in node_markers]
                ),
                hovertemplate='<b>%{text}</b><br>%{customdata}<extra></extra>',
                customdata=node_markers,
                name='DNA-Tested Individuals'
            ),
            row=3, col=2
        )
        
        # Update layout
        fig.update_layout(
            title_text="Bodzia DNA-Tested Individuals - Interactive Dashboard",
            title_x=0.5,
            title_font_size=20,
            height=1400,
            showlegend=False,
            template='plotly_white'
        )
        
        # Update axes
        fig.update_xaxes(title_text="Marker Type", row=1, col=1)
        fig.update_yaxes(title_text="", row=1, col=1, showticklabels=False)
        fig.update_xaxes(title_text="Year (CE)", row=1, col=2)
        fig.update_yaxes(title_text="Individual", row=1, col=2)
        fig.update_xaxes(title_text="Dynasty", row=2, col=2)
        fig.update_yaxes(title_text="Count", row=2, col=2)
        fig.update_xaxes(showticklabels=False, row=3, col=2)
        fig.update_yaxes(showticklabels=False, row=3, col=2)
        
        # Save
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        fig.write_html(output_file)
        
        print(f"✓ Created interactive dashboard: {output_path}")
