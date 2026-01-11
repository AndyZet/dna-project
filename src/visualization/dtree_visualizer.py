"""
dTree integration for interactive family tree visualization
Based on: https://github.com/ErikGartner/dTree
"""
import json
from pathlib import Path
from typing import Dict, List, Optional, Any, Set
from collections import defaultdict


class DTreeVisualizer:
    """Convert genealogy data to dTree format and generate interactive HTML"""
    
    # Dynasty color schemes (matching Graphviz colors)
    DYNASTY_COLORS = {
        'Rurikid': '#FF6B6B',      # Red
        'Piast': '#4ECDC4',         # Teal
        'Premyslid': '#95E1D3',     # Light teal
        'Gorm': '#F38181',          # Pink
        'Normandy': '#AA96DA',      # Purple
        'Capetian': '#FCBAD3',      # Light pink
        'Ottonian': '#A8D8EA',      # Light blue
        'Arpad': '#FFD93D',         # Yellow
        'default': '#E8E8E8'        # Light gray
    }
    
    def __init__(self, output_dir: str = "output/web"):
        """
        Initialize dTree visualizer.
        
        Args:
            output_dir: Directory for HTML output files
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def convert_to_dtree_format(
        self,
        data: Dict[str, Any],
        root_individual_id: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Convert genealogy JSON to dTree format.
        
        dTree expects:
        [
          {
            "name": "Person",
            "marriages": [
              {
                "spouse": {"name": "Spouse"},
                "children": [{"name": "Child"}]
              }
            ]
          }
        ]
        
        Args:
            data: Genealogy data with 'individuals' and 'families'
            root_individual_id: Optional root individual to start tree from
            
        Returns:
            List of dTree-formatted nodes
        """
        individuals = {ind['id']: ind for ind in data.get('individuals', [])}
        families = data.get('families', [])
        
        # Build index: person_id -> list of families where they're husband/wife
        person_families = defaultdict(list)
        for fam in families:
            if fam.get('husband_id'):
                person_families[fam['husband_id']].append(fam)
            if fam.get('wife_id'):
                person_families[fam['wife_id']].append(fam)
        
        # Build index: person_id -> list of families where they're a child
        child_families = defaultdict(list)
        for fam in families:
            for child_id in fam.get('children', []):
                child_families[child_id].append(fam)
        
        # Find root individuals (those who are not children in any family)
        if root_individual_id:
            root_ids = [root_individual_id]
        else:
            all_child_ids = set()
            for fam in families:
                all_child_ids.update(fam.get('children', []))
            root_ids = [
                ind_id for ind_id in individuals.keys()
                if ind_id not in all_child_ids
            ]
        
        # If no clear roots, use all individuals (will create multiple trees)
        if not root_ids:
            root_ids = list(individuals.keys())
        
        # Convert each root to dTree format
        converted_nodes = []
        processed = set()
        
        for root_id in root_ids[:10]:  # Limit to first 10 roots to avoid too many trees
            if root_id in processed:
                continue
            node = self._convert_individual_to_dtree(
                root_id,
                individuals,
                person_families,
                child_families,
                processed
            )
            if node:
                converted_nodes.append(node)
        
        return converted_nodes
    
    def _convert_individual_to_dtree(
        self,
        person_id: str,
        individuals: Dict[str, Dict],
        person_families: Dict[str, List],
        child_families: Dict[str, List],
        processed: Set[str]
    ) -> Optional[Dict[str, Any]]:
        """Recursively convert an individual and their descendants to dTree format."""
        if person_id in processed or person_id not in individuals:
            return None
        
        processed.add(person_id)
        person = individuals[person_id]
        
        # Build node name with title/dynasty info
        name_parts = [person.get('name', 'Unknown')]
        if person.get('title'):
            name_parts.append(f"\n{person['title']}")
        if person.get('dynasty'):
            name_parts.append(f"\n({person['dynasty']})")
        
        # Add DNA marker if tested
        if person.get('dna_tested'):
            dna_marker = person.get('dna_marker', 'DNA tested')
            name_parts.append(f"\n[{dna_marker}]")
        
        node_name = "".join(name_parts)
        
        # Determine CSS class based on dynasty
        dynasty = person.get('dynasty', 'default')
        node_class = f"node dynasty-{dynasty.lower()}"
        
        # Build extra data for tooltips/callbacks
        extra = {
            'id': person_id,
            'dynasty': dynasty,
            'birth': person.get('birth', {}),
            'death': person.get('death', {}),
            'dna_tested': person.get('dna_tested', False),
            'dna_marker': person.get('dna_marker', ''),
            'notes': person.get('notes', [])
        }
        
        # Convert marriages
        marriages = []
        for fam in person_families.get(person_id, []):
            spouse_id = None
            if fam.get('husband_id') == person_id:
                spouse_id = fam.get('wife_id')
            elif fam.get('wife_id') == person_id:
                spouse_id = fam.get('husband_id')
            
            if not spouse_id or spouse_id not in individuals:
                # Handle families with children but no spouse (single parent)
                children = []
                for child_id in fam.get('children', []):
                    child_node = self._convert_individual_to_dtree(
                        child_id,
                        individuals,
                        person_families,
                        child_families,
                        processed
                    )
                    if child_node:
                        children.append(child_node)
                
                if children:
                    marriages.append({
                        'spouse': {'name': 'Unknown'},
                        'children': children
                    })
                continue
            
            # Convert spouse
            spouse = individuals[spouse_id]
            spouse_name_parts = [spouse.get('name', 'Unknown')]
            if spouse.get('title'):
                spouse_name_parts.append(f"\n{spouse['title']}")
            if spouse.get('dynasty'):
                spouse_name_parts.append(f"\n({spouse['dynasty']})")
            if spouse.get('dna_tested'):
                spouse_dna = spouse.get('dna_marker', 'DNA tested')
                spouse_name_parts.append(f"\n[{spouse_dna}]")
            
            spouse_name = "".join(spouse_name_parts)
            
            # Convert children
            children = []
            for child_id in fam.get('children', []):
                child_node = self._convert_individual_to_dtree(
                    child_id,
                    individuals,
                    person_families,
                    child_families,
                    processed
                )
                if child_node:
                    children.append(child_node)
            
            marriages.append({
                'spouse': {
                    'name': spouse_name,
                    'class': f"node dynasty-{spouse.get('dynasty', 'default').lower()}",
                    'extra': {
                        'id': spouse_id,
                        'dynasty': spouse.get('dynasty', 'default'),
                        'birth': spouse.get('birth', {}),
                        'death': spouse.get('death', {}),
                        'dna_tested': spouse.get('dna_tested', False),
                        'dna_marker': spouse.get('dna_marker', '')
                    }
                },
                'children': children
            })
        
        node = {
            'name': node_name,
            'class': node_class,
            'textClass': 'nodeText',
            'extra': extra
        }
        
        if marriages:
            node['marriages'] = marriages
        
        return node
    
    def generate_html(
        self,
        data: Dict[str, Any],
        output_filename: str = "bodzia_dtree.html",
        title: str = "Bodzia Family Tree - Interactive",
        root_individual_id: Optional[str] = None,
        width: int = 1200,
        height: int = 800
    ) -> str:
        """
        Generate HTML file with dTree visualization.
        
        Args:
            data: Genealogy data dictionary
            output_filename: Output HTML filename
            title: Page title
            root_individual_id: Optional root individual ID
            width: Canvas width
            height: Canvas height
            
        Returns:
            Path to generated HTML file
        """
        # Convert data to dTree format
        dtree_data = self.convert_to_dtree_format(data, root_individual_id)
        
        # Generate CSS for dynasty colors
        css_styles = self._generate_css_styles()
        
        # Generate HTML
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <script src="https://d3js.org/d3.v4.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/d3-dtree@2.4.1/dist/dTree.min.js"></script>
    <style>
        {css_styles}
        
        * {{
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }}
        
        .container {{
            max-width: 1600px;
            margin: 20px auto;
            background-color: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
        }}
        
        .header {{
            border-bottom: 3px solid #4ECDC4;
            padding-bottom: 20px;
            margin-bottom: 25px;
        }}
        
        h1 {{
            color: #2d3748;
            margin: 0 0 10px 0;
            font-size: 2.2em;
            font-weight: 700;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
        
        .subtitle {{
            color: #718096;
            font-size: 0.95em;
            margin-bottom: 15px;
        }}
        
        .info {{
            color: #4a5568;
            margin-bottom: 20px;
            font-size: 14px;
            padding: 12px 16px;
            background: linear-gradient(135deg, #f7fafc 0%, #edf2f7 100%);
            border-left: 4px solid #4ECDC4;
            border-radius: 4px;
            line-height: 1.6;
        }}
        
        .info strong {{
            color: #2d3748;
        }}
        
        #graph {{
            width: 100%;
            height: {height}px;
            border: 2px solid #e2e8f0;
            border-radius: 8px;
            overflow: hidden;
            background: linear-gradient(135deg, #fafafa 0%, #f0f0f0 100%);
            box-shadow: inset 0 2px 4px rgba(0,0,0,0.05);
        }}
        
        .controls {{
            margin-top: 25px;
            padding: 18px;
            background: linear-gradient(135deg, #f7fafc 0%, #edf2f7 100%);
            border-radius: 8px;
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
        }}
        
        .controls button {{
            padding: 10px 20px;
            background: linear-gradient(135deg, #4ECDC4 0%, #3ba8a0 100%);
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 14px;
            font-weight: 600;
            transition: all 0.3s ease;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        
        .controls button:hover {{
            background: linear-gradient(135deg, #3ba8a0 0%, #2d8a82 100%);
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }}
        
        .controls button:active {{
            transform: translateY(0);
        }}
        
        .legend {{
            margin-top: 25px;
            padding: 20px;
            background: linear-gradient(135deg, #f7fafc 0%, #edf2f7 100%);
            border-radius: 8px;
            border: 1px solid #e2e8f0;
        }}
        
        .legend h3 {{
            margin: 0 0 15px 0;
            font-size: 18px;
            color: #2d3748;
            font-weight: 600;
        }}
        
        .legend-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
            gap: 12px;
        }}
        
        .legend-item {{
            display: flex;
            align-items: center;
            padding: 8px 12px;
            background: white;
            border-radius: 6px;
            border: 1px solid #e2e8f0;
            transition: all 0.2s ease;
        }}
        
        .legend-item:hover {{
            transform: translateX(4px);
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        
        .legend-color {{
            display: inline-block;
            width: 24px;
            height: 24px;
            border-radius: 4px;
            margin-right: 10px;
            vertical-align: middle;
            border: 2px solid rgba(0,0,0,0.1);
            box-shadow: 0 1px 3px rgba(0,0,0,0.2);
        }}
        
        .legend-text {{
            font-weight: 500;
            color: #2d3748;
            font-size: 14px;
        }}
        
        .dna-badge {{
            display: inline-block;
            margin-left: 8px;
            padding: 2px 6px;
            background: rgba(255, 215, 0, 0.2);
            border: 1px solid rgba(255, 215, 0, 0.5);
            border-radius: 4px;
            font-size: 11px;
            font-weight: 600;
            color: #856404;
        }}
        
        .modal {{
            display: none;
            position: fixed;
            z-index: 1000;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0,0,0,0.5);
            backdrop-filter: blur(4px);
        }}
        
        .modal-content {{
            background-color: white;
            margin: 5% auto;
            padding: 30px;
            border-radius: 12px;
            max-width: 500px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.3);
            animation: slideIn 0.3s ease;
        }}
        
        @keyframes slideIn {{
            from {{
                transform: translateY(-50px);
                opacity: 0;
            }}
            to {{
                transform: translateY(0);
                opacity: 1;
            }}
        }}
        
        .modal-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
            padding-bottom: 15px;
            border-bottom: 2px solid #e2e8f0;
        }}
        
        .modal-title {{
            font-size: 1.5em;
            font-weight: 700;
            color: #2d3748;
            margin: 0;
        }}
        
        .close {{
            color: #a0aec0;
            font-size: 28px;
            font-weight: bold;
            cursor: pointer;
            transition: color 0.2s;
        }}
        
        .close:hover {{
            color: #2d3748;
        }}
        
        .modal-body {{
            color: #4a5568;
            line-height: 1.8;
        }}
        
        .modal-info-row {{
            margin: 12px 0;
            padding: 8px 0;
            border-bottom: 1px solid #f0f0f0;
        }}
        
        .modal-info-label {{
            font-weight: 600;
            color: #2d3748;
            display: inline-block;
            min-width: 100px;
        }}
        
        .modal-dna-badge {{
            display: inline-block;
            padding: 4px 10px;
            background: linear-gradient(135deg, #ffd700 0%, #ffed4e 100%);
            border-radius: 6px;
            font-weight: 600;
            color: #856404;
            margin-left: 8px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>{title}</h1>
            <div class="subtitle">Early Medieval Royal Houses Connected to Bodzia Archaeological Site (950-1020 CE)</div>
        </div>
        
        <div class="info">
            <strong>📖 How to use:</strong> Click and drag to pan the tree • Scroll to zoom in/out • 
            Click on nodes to see detailed information • Nodes with 🧬 indicate DNA-tested individuals
        </div>
        
        <div id="graph"></div>
        
        <div class="controls">
            <button onclick="tree.resetZoom()">🔄 Reset Zoom</button>
            <button onclick="tree.zoomToFit()">🔍 Fit to View</button>
            <button onclick="highlightDNATested()">🧬 Highlight DNA Tested</button>
        </div>
        
        <div class="legend">
            <h3>🏛️ Dynasty Legend</h3>
            <div class="legend-grid">
                {self._generate_legend_html()}
            </div>
            <div style="margin-top: 15px; padding-top: 15px; border-top: 1px solid #e2e8f0;">
                <span class="dna-badge">🧬 DNA Tested</span> - Individuals with genetic markers identified
            </div>
        </div>
    </div>
    
    <div id="nodeModal" class="modal">
        <div class="modal-content">
            <div class="modal-header">
                <h2 class="modal-title" id="modalTitle"></h2>
                <span class="close" onclick="closeModal()">&times;</span>
            </div>
            <div class="modal-body" id="modalBody"></div>
        </div>
    </div>
    
    <script>
        const data = {json.dumps(dtree_data, indent=8, ensure_ascii=False)};
        
        // Add DNA-tested class to nodes after tree initialization
        function addDNAClasses() {{
            d3.selectAll('.node').each(function(d) {{
                const node = d3.select(this);
                const nodeData = node.datum();
                if (nodeData && nodeData.extra && nodeData.extra.dna_tested) {{
                    node.classed('dna-tested', true);
                }}
            }});
        }}
        
        // Highlight DNA-tested individuals
        function highlightDNATested() {{
            d3.selectAll('.node').each(function(d) {{
                const node = d3.select(this);
                const nodeData = node.datum();
                if (nodeData && nodeData.extra && nodeData.extra.dna_tested) {{
                    node.transition()
                        .duration(500)
                        .style('box-shadow', '0 0 0 4px rgba(255, 215, 0, 0.6), 0 8px 16px rgba(0,0,0,0.3)')
                        .style('transform', 'scale(1.1)');
                    
                    setTimeout(() => {{
                        node.transition()
                            .duration(500)
                            .style('box-shadow', null)
                            .style('transform', null);
                    }}, 2000);
                }}
            }});
        }}
        
        // Show modal with node details
        function showModal(name, extra) {{
            const modal = document.getElementById('nodeModal');
            const title = document.getElementById('modalTitle');
            const body = document.getElementById('modalBody');
            
            title.innerHTML = name;
            if (extra && extra.dna_tested) {{
                title.innerHTML += ' <span class="modal-dna-badge">🧬 DNA Tested</span>';
            }}
            
            let html = '';
            if (extra) {{
                html += `<div class="modal-info-row"><span class="modal-info-label">Dynasty:</span> ${{extra.dynasty || 'Unknown'}}</div>`;
                
                if (extra.birth) {{
                    const birthDate = extra.birth.date || 'Unknown';
                    const birthPlace = extra.birth.place || '';
                    html += `<div class="modal-info-row"><span class="modal-info-label">Birth:</span> ${{birthDate}}${{birthPlace ? ' - ' + birthPlace : ''}}</div>`;
                }}
                
                if (extra.death) {{
                    const deathDate = extra.death.date || 'Unknown';
                    const deathPlace = extra.death.place || '';
                    html += `<div class="modal-info-row"><span class="modal-info-label">Death:</span> ${{deathDate}}${{deathPlace ? ' - ' + deathPlace : ''}}</div>`;
                }}
                
                if (extra.dna_tested) {{
                    html += `<div class="modal-info-row"><span class="modal-info-label">DNA Marker:</span> <strong>${{extra.dna_marker || 'DNA tested'}}</strong></div>`;
                }}
                
                if (extra.notes && extra.notes.length > 0) {{
                    html += `<div class="modal-info-row"><span class="modal-info-label">Notes:</span> ${{extra.notes.join(', ')}}</div>`;
                }}
            }}
            
            body.innerHTML = html || '<div class="modal-info-row">No additional information available.</div>';
            modal.style.display = 'block';
        }}
        
        // Close modal
        function closeModal() {{
            document.getElementById('nodeModal').style.display = 'none';
        }}
        
        // Close modal when clicking outside
        window.onclick = function(event) {{
            const modal = document.getElementById('nodeModal');
            if (event.target == modal) {{
                closeModal();
            }}
        }}
        
        const options = {{
            target: '#graph',
            debug: false,
            width: {width},
            height: {height},
            hideMarriageNodes: false,
            marriageNodeSize: 10,
            callbacks: {{
                nodeClick: function(name, extra, id) {{
                    showModal(name, extra);
                }},
                nodeRightClick: function(name, extra, id) {{
                    console.log('Right-clicked:', name, extra);
                }},
            }},
            margin: {{
                top: 30,
                right: 30,
                bottom: 30,
                left: 30
            }},
            nodeWidth: 160,
            styles: {{
                node: 'node',
                linage: 'linage',
                marriage: 'marriage',
                text: 'nodeText'
            }}
        }};
        
        const tree = dTree.init(data, options);
        
        // Add DNA classes after tree is rendered
        setTimeout(addDNAClasses, 1000);
        
        // Also add DNA classes when nodes are clicked (in case they're dynamically created)
        d3.select('#graph').on('click', function() {{
            setTimeout(addDNAClasses, 100);
        }});
    </script>
</body>
</html>"""
        
        # Write HTML file
        output_path = self.output_dir / output_filename
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return str(output_path)
    
    def _generate_css_styles(self) -> str:
        """Generate CSS styles for dynasty colors."""
        css = """
        .linage {
            fill: none;
            stroke: #4a5568;
            stroke-width: 2.5px;
            opacity: 0.8;
        }
        
        .marriage {
            fill: none;
            stroke: #718096;
            stroke-width: 1.5px;
            opacity: 0.7;
        }
        
        .node {
            border-style: solid;
            border-width: 3px;
            border-radius: 6px;
            padding: 8px 10px;
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            font-weight: 500;
            min-width: 120px;
            text-align: center;
        }
        
        .node:hover {
            transform: scale(1.08) translateY(-2px);
            box-shadow: 0 8px 16px rgba(0,0,0,0.25);
            z-index: 10;
        }
        
        .node.dna-tested {
            border-width: 4px;
            box-shadow: 0 0 0 2px rgba(255, 215, 0, 0.5), 0 4px 8px rgba(0,0,0,0.15);
            position: relative;
        }
        
        .node.dna-tested::before {
            content: "🧬";
            position: absolute;
            top: -8px;
            right: -8px;
            font-size: 16px;
            background: white;
            border-radius: 50%;
            width: 24px;
            height: 24px;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        }
        
        .node.dna-tested:hover {
            box-shadow: 0 0 0 3px rgba(255, 215, 0, 0.7), 0 8px 16px rgba(0,0,0,0.3);
        }
        
        .nodeText {
            font: 12px 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            text-anchor: middle;
            pointer-events: none;
            font-weight: 500;
            line-height: 1.4;
        }
        
        .marriageNode {
            background-color: #4a5568;
            border-radius: 50%;
            border: 2px solid white;
            box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        }
        """
        
        # Add dynasty-specific colors with gradients
        for dynasty, color in self.DYNASTY_COLORS.items():
            dynasty_class = dynasty.lower()
            darker_color = self._darken_color(color)
            css += f"""
        .dynasty-{dynasty_class} {{
            background: linear-gradient(135deg, {color} 0%, {darker_color} 100%);
            border-color: {darker_color};
            color: {self._get_text_color(color)};
        }}
        
        .dynasty-{dynasty_class}:hover {{
            background: linear-gradient(135deg, {self._lighten_color(color)} 0%, {color} 100%);
        }}
        """
        
        return css
    
    def _generate_legend_html(self) -> str:
        """Generate HTML for dynasty legend."""
        legend_items = []
        for dynasty, color in self.DYNASTY_COLORS.items():
            if dynasty != 'default':
                darker_color = self._darken_color(color)
                legend_items.append(
                    f'<div class="legend-item">'
                    f'<span class="legend-color" style="background: linear-gradient(135deg, {color} 0%, {darker_color} 100%);"></span>'
                    f'<span class="legend-text">{dynasty}</span>'
                    f'</div>'
                )
        return '\n                '.join(legend_items)
    
    def _darken_color(self, hex_color: str) -> str:
        """Darken a hex color for borders."""
        # Simple darkening - remove #, convert to int, reduce by 30%, add #
        hex_color = hex_color.lstrip('#')
        rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        darkened = tuple(max(0, int(c * 0.7)) for c in rgb)
        return f"#{darkened[0]:02x}{darkened[1]:02x}{darkened[2]:02x}"
    
    def _lighten_color(self, hex_color: str) -> str:
        """Lighten a hex color for hover effects."""
        hex_color = hex_color.lstrip('#')
        rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        lightened = tuple(min(255, int(c * 1.2)) for c in rgb)
        return f"#{lightened[0]:02x}{lightened[1]:02x}{lightened[2]:02x}"
    
    def _get_text_color(self, bg_color: str) -> str:
        """Determine text color (black or white) based on background brightness."""
        hex_color = bg_color.lstrip('#')
        rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        brightness = (rgb[0] * 299 + rgb[1] * 587 + rgb[2] * 114) / 1000
        return '#000' if brightness > 128 else '#fff'
