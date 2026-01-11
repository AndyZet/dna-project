"""
Graphviz-based family tree generation with dynasty-based styling
"""
import graphviz
from typing import Dict, List, Optional, Tuple
from pathlib import Path


class DynastyTreeGenerator:
    """Generate family trees using Graphviz with dynasty-based styling"""
    
    # Dynasty color schemes (based on Bodzia diagram)
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
    
    # Node shapes for different roles
    NODE_SHAPES = {
        'king': 'box',
        'prince': 'ellipse',
        'duke': 'diamond',
        'default': 'box'
    }
    
    def __init__(self, output_dir: str = "output/visualizations"):
        """
        Initialize tree generator.
        
        Args:
            output_dir: Directory for output files
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def create_tree(
        self,
        data: Dict[str, any],
        dynasty_map: Optional[Dict[str, str]] = None,
        title: str = "Family Tree",
        format: str = 'svg',
        engine: str = 'dot',
        orientation: str = 'TB'  # TB=Top-Bottom, LR=Left-Right
    ) -> graphviz.Digraph:
        """
        Create Graphviz tree from genealogy data.
        
        Args:
            data: Genealogy data dictionary with 'individuals' and 'families'
            dynasty_map: Dictionary mapping individual IDs to dynasty names
            title: Tree title
            format: Output format ('svg', 'png', 'pdf', 'dot')
            engine: Graphviz engine ('dot', 'neato', 'fdp', 'sfdp', 'twopi', 'circo')
            orientation: Graph orientation ('TB', 'LR', 'BT', 'RL')
            
        Returns:
            Graphviz Digraph object
        """
        # Create graph
        dot = graphviz.Digraph(
            name=title.replace(' ', '_'),
            format=format,
            engine=engine,
            graph_attr={
                'rankdir': orientation,
                'bgcolor': 'white',
                'fontname': 'Arial',
                'fontsize': '12',
                'splines': 'ortho',  # Orthogonal edges for cleaner trees
                'nodesep': '0.5',
                'ranksep': '1.0'
            },
            node_attr={
                'style': 'filled',
                'fontname': 'Arial',
                'fontsize': '10'
            },
            edge_attr={
                'color': '#666666',
                'arrowsize': '0.7'
            }
        )
        
        # Add title
        dot.attr(label=title, labelloc='t', fontsize='16', fontname='Arial Bold')
        
        # Create individual nodes
        individuals = {ind['id']: ind for ind in data.get('individuals', [])}
        
        for ind_id, ind in individuals.items():
            # Determine dynasty
            dynasty = 'default'
            if dynasty_map and ind_id in dynasty_map:
                dynasty = dynasty_map[ind_id]
            elif 'dynasty' in ind:
                dynasty = ind['dynasty']
            
            # Get color
            color = self.DYNASTY_COLORS.get(dynasty, self.DYNASTY_COLORS['default'])
            
            # Determine shape
            role = ind.get('role', 'default').lower()
            shape = self.NODE_SHAPES.get(role, self.NODE_SHAPES['default'])
            
            # Create label
            label = self._create_node_label(ind)
            
            # Add node
            dot.node(
                ind_id,
                label=label,
                fillcolor=color,
                color='black',
                shape=shape,
                style='filled,rounded'
            )
        
        # Create family relationships
        for family in data.get('families', []):
            husband_id = family.get('husband_id')
            wife_id = family.get('wife_id')
            children = family.get('children', [])
            
            # Create marriage node (invisible connector)
            if husband_id and wife_id:
                marriage_id = f"m_{family['id']}"
                dot.node(
                    marriage_id,
                    '',
                    shape='point',
                    width='0.1',
                    height='0.1',
                    style='invis'
                )
                
                # Connect spouses to marriage node
                dot.edge(husband_id, marriage_id, style='solid')
                dot.edge(wife_id, marriage_id, style='solid')
                
                # Connect marriage node to children
                for child_id in children:
                    if child_id in individuals:
                        dot.edge(marriage_id, child_id, style='solid')
        
        return dot
    
    def _create_node_label(self, individual: Dict) -> str:
        """Create formatted label for individual node"""
        name = individual.get('name', 'Unknown')
        
        # Add dates if available
        birth = individual.get('birth', {})
        death = individual.get('death', {})
        
        birth_date = birth.get('date', '') if isinstance(birth, dict) else ''
        death_date = death.get('date', '') if isinstance(death, dict) else ''
        
        # Format dates
        date_str = ''
        if birth_date or death_date:
            date_str = f"\\n{birth_date}"
            if death_date:
                date_str += f" - {death_date}"
            elif birth_date:
                date_str += " -"
        
        # Add role/title if available
        role = individual.get('role', '')
        title_text = individual.get('title', '')
        
        label_parts = [name]
        if title_text:
            label_parts.append(title_text)
        if role:
            label_parts.append(f"({role})")
        if date_str:
            label_parts.append(date_str)
        
        return '\\n'.join(label_parts)
    
    def generate_dot_file(
        self,
        data: Dict[str, any],
        dynasty_map: Optional[Dict[str, str]] = None,
        title: str = "Family Tree",
        output_filename: Optional[str] = None
    ) -> str:
        """
        Generate DOT file for tree.
        
        Args:
            data: Genealogy data dictionary
            dynasty_map: Dictionary mapping individual IDs to dynasty names
            title: Tree title
            output_filename: Output filename (without extension)
            
        Returns:
            Path to generated DOT file
        """
        dot = self.create_tree(data, dynasty_map, title, format='dot')
        
        if not output_filename:
            output_filename = title.replace(' ', '_').lower()
        
        output_path = self.output_dir / f"{output_filename}.dot"
        dot.save(str(output_path))
        
        return str(output_path)
    
    def render_tree(
        self,
        data: Dict[str, any],
        dynasty_map: Optional[Dict[str, str]] = None,
        title: str = "Family Tree",
        formats: List[str] = ['svg', 'png', 'pdf'],
        output_filename: Optional[str] = None
    ) -> Dict[str, str]:
        """
        Render tree in multiple formats.
        
        Args:
            data: Genealogy data dictionary
            dynasty_map: Dictionary mapping individual IDs to dynasty names
            title: Tree title
            formats: List of output formats
            output_filename: Base output filename (without extension)
            
        Returns:
            Dictionary mapping format to file path
        """
        if not output_filename:
            output_filename = title.replace(' ', '_').lower()
        
        rendered_files = {}
        
        for fmt in formats:
            dot = self.create_tree(data, dynasty_map, title, format=fmt)
            output_path = self.output_dir / output_filename
            file_path = dot.render(str(output_path), cleanup=False)
            rendered_files[fmt] = file_path
        
        return rendered_files
    
    def create_dynasty_legend(self, dynasties: List[str]) -> graphviz.Digraph:
        """
        Create legend showing dynasty colors.
        
        Args:
            dynasties: List of dynasty names to include in legend
            
        Returns:
            Graphviz Digraph with legend
        """
        legend = graphviz.Digraph(
            name='Dynasty_Legend',
            format='svg',
            graph_attr={
                'rankdir': 'LR',
                'bgcolor': 'white',
                'fontname': 'Arial',
                'fontsize': '12'
            },
            node_attr={
                'style': 'filled',
                'fontname': 'Arial',
                'fontsize': '10',
                'shape': 'box',
                'width': '1.5',
                'height': '0.5'
            }
        )
        
        legend.attr(label='Dynasty Legend', labelloc='t', fontsize='14', fontname='Arial Bold')
        
        for i, dynasty in enumerate(dynasties):
            color = self.DYNASTY_COLORS.get(dynasty, self.DYNASTY_COLORS['default'])
            legend.node(
                f"legend_{i}",
                dynasty,
                fillcolor=color,
                color='black'
            )
        
        return legend
