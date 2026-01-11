"""
Genealogy visualization pipeline: Data → DOT → SVG → Multiple formats
"""
import json
import shutil
from pathlib import Path
from typing import Dict, List, Optional, Any
import webbrowser

import sys
from pathlib import Path

# Add src to path for imports
src_path = Path(__file__).parent.parent
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

from genealogical.data_manager import GenealogyDataManager
from visualization.graphviz_trees import DynastyTreeGenerator
from visualization.dtree_visualizer import DTreeVisualizer


class GenealogyVisualizationPipeline:
    """Complete pipeline for genealogy visualization"""
    
    def __init__(
        self,
        data_dir: str = "data/processed/genealogy",
        output_dir: str = "output/visualizations"
    ):
        """
        Initialize pipeline.
        
        Args:
            data_dir: Directory for genealogy data files
            output_dir: Directory for output visualizations
        """
        self.data_manager = GenealogyDataManager(data_dir)
        self.tree_generator = DynastyTreeGenerator(output_dir)
        web_dir = Path(output_dir).parent / "web"
        self.dtree_visualizer = DTreeVisualizer(str(web_dir))
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def process_gedcom_to_visualizations(
        self,
        gedcom_path: str,
        dynasty_map: Optional[Dict[str, str]] = None,
        title: str = "Family Tree",
        formats: List[str] = ['svg', 'png', 'pdf', 'dot'],
        include_legend: bool = True
    ) -> Dict[str, Any]:
        """
        Complete pipeline: GEDCOM → JSON → DOT → Multiple formats.
        
        Args:
            gedcom_path: Path to input GEDCOM file
            dynasty_map: Dictionary mapping individual IDs to dynasty names
            title: Tree title
            formats: List of output formats
            include_legend: Whether to generate dynasty legend
            
        Returns:
            Dictionary with paths to generated files
        """
        results = {
            'input_file': gedcom_path,
            'json_file': None,
            'dot_file': None,
            'rendered_files': {},
            'legend_file': None
        }
        
        # Step 1: Load GEDCOM and convert to JSON
        print(f"📖 Loading GEDCOM file: {gedcom_path}")
        data = self.data_manager.load_gedcom(gedcom_path)
        
        # Save as JSON
        json_filename = Path(gedcom_path).stem
        json_path = self.data_manager.save_json(data, json_filename)
        results['json_file'] = json_path
        print(f"💾 Saved JSON: {json_path}")
        
        # Step 2: Generate DOT file
        print(f"🌳 Generating DOT file...")
        dot_path = self.tree_generator.generate_dot_file(
            data,
            dynasty_map=dynasty_map,
            title=title,
            output_filename=json_filename
        )
        results['dot_file'] = dot_path
        print(f"📝 Generated DOT: {dot_path}")
        
        # Step 3: Render in multiple formats
        print(f"🎨 Rendering in formats: {formats}")
        rendered = self.tree_generator.render_tree(
            data,
            dynasty_map=dynasty_map,
            title=title,
            formats=formats,
            output_filename=json_filename
        )
        results['rendered_files'] = rendered
        for fmt, path in rendered.items():
            print(f"   ✓ {fmt.upper()}: {path}")
        
        # Step 4: Generate legend if requested
        if include_legend and dynasty_map:
            dynasties = list(set(dynasty_map.values()))
            legend = self.tree_generator.create_dynasty_legend(dynasties)
            legend_path = self.output_dir / f"{json_filename}_legend.svg"
            legend.render(str(self.output_dir / f"{json_filename}_legend"), cleanup=False)
            results['legend_file'] = str(legend_path)
            print(f"📋 Generated legend: {results['legend_file']}")
        
        return results
    
    def process_json_to_visualizations(
        self,
        json_path: Optional[str] = None,
        data: Optional[Dict[str, Any]] = None,
        dynasty_map: Optional[Dict[str, str]] = None,
        title: str = "Family Tree",
        formats: List[str] = ['svg', 'png', 'pdf', 'dot'],
        include_legend: bool = True
    ) -> Dict[str, Any]:
        """
        Pipeline: JSON → DOT → Multiple formats.
        
        Args:
            json_path: Path to input JSON file
            dynasty_map: Dictionary mapping individual IDs to dynasty names
            title: Tree title
            formats: List of output formats
            include_legend: Whether to generate dynasty legend
            
        Returns:
            Dictionary with paths to generated files
        """
        results = {
            'input_file': json_path if json_path else 'provided_data',
            'dot_file': None,
            'rendered_files': {},
            'legend_file': None
        }
        
        # Load JSON data or use provided data
        if data is None:
            if json_path is None:
                raise ValueError("Either json_path or data must be provided")
            print(f"📖 Loading JSON file: {json_path}")
            data = self.data_manager.load_json(json_path)
            json_filename = Path(json_path).stem
        else:
            print(f"📖 Using provided data structure")
            json_filename = title.replace(' ', '_').lower() if title else 'tree'
        
        # Generate DOT file
        print(f"🌳 Generating DOT file...")
        dot_path = self.tree_generator.generate_dot_file(
            data,
            dynasty_map=dynasty_map,
            title=title,
            output_filename=json_filename
        )
        results['dot_file'] = dot_path
        print(f"📝 Generated DOT: {dot_path}")
        
        # Render in multiple formats
        print(f"🎨 Rendering in formats: {formats}")
        rendered = self.tree_generator.render_tree(
            data,
            dynasty_map=dynasty_map,
            title=title,
            formats=formats,
            output_filename=json_filename
        )
        results['rendered_files'] = rendered
        for fmt, path in rendered.items():
            print(f"   ✓ {fmt.upper()}: {path}")
        
        # Generate legend if requested
        if include_legend and dynasty_map:
            dynasties = list(set(dynasty_map.values()))
            legend = self.tree_generator.create_dynasty_legend(dynasties)
            legend_path = self.output_dir / f"{json_filename}_legend.svg"
            legend.render(str(self.output_dir / f"{json_filename}_legend"), cleanup=False)
            results['legend_file'] = str(legend_path)
            print(f"📋 Generated legend: {results['legend_file']}")
        
        return results
    
    def prepare_for_topola_viewer(
        self,
        gedcom_path: str,
        output_dir: Optional[str] = None
    ) -> str:
        """
        Prepare GEDCOM file for Topola viewer.
        Topola viewer can be used at: https://pewu.github.io/topola-viewer/
        
        Args:
            gedcom_path: Path to GEDCOM file
            output_dir: Directory to copy GEDCOM file (default: output/web/)
            
        Returns:
            Path to prepared GEDCOM file
        """
        if not output_dir:
            output_dir = self.output_dir.parent / "web"
        
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        # Copy GEDCOM file
        gedcom_file = Path(gedcom_path)
        target_path = output_path / gedcom_file.name
        shutil.copy2(gedcom_path, target_path)
        
        print(f"🌐 Prepared GEDCOM for Topola viewer: {target_path}")
        print(f"   Open in browser: https://pewu.github.io/topola-viewer/")
        print(f"   Then upload: {target_path}")
        
        return str(target_path)
    
    def export_for_svg_ftg(
        self,
        gedcom_path: str,
        output_dir: Optional[str] = None
    ) -> str:
        """
        Export GEDCOM file for SVG-FTG (SVG Family-Tree Generator).
        SVG-FTG requires GEDCOM 5.5.1 or 7.0 format.
        
        Args:
            gedcom_path: Path to GEDCOM file
            output_dir: Directory to copy GEDCOM file (default: output/web/)
            
        Returns:
            Path to exported GEDCOM file
        """
        if not output_dir:
            output_dir = self.output_dir.parent / "web"
        
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        # Copy GEDCOM file directly (already in correct format)
        gedcom_file = Path(gedcom_path)
        target_path = output_path / f"{gedcom_file.stem}_svgftg.ged"
        
        # Copy file
        import shutil
        shutil.copy2(gedcom_path, target_path)
        
        print(f"📄 Exported GEDCOM for SVG-FTG: {target_path}")
        print(f"   SVG-FTG can be used with: https://parallaxviewpoint.com/SVG-FTG/")
        
        return str(target_path)
    
    def generate_dtree_visualization(
        self,
        json_path: Optional[str] = None,
        data: Optional[Dict[str, Any]] = None,
        output_filename: str = "bodzia_dtree.html",
        title: str = "Bodzia Family Tree - Interactive",
        root_individual_id: Optional[str] = None,
        width: int = 1200,
        height: int = 800
    ) -> str:
        """
        Generate interactive dTree HTML visualization.
        
        Args:
            json_path: Path to JSON file (optional if data provided)
            data: Genealogy data dictionary (optional if json_path provided)
            output_filename: Output HTML filename
            title: Page title
            root_individual_id: Optional root individual ID to start tree
            width: Canvas width
            height: Canvas height
            
        Returns:
            Path to generated HTML file
        """
        # Load data if needed
        if data is None:
            if json_path is None:
                raise ValueError("Either json_path or data must be provided")
            data = self.data_manager.load_json(json_path)
        
        # Generate dTree HTML
        html_path = self.dtree_visualizer.generate_html(
            data=data,
            output_filename=output_filename,
            title=title,
            root_individual_id=root_individual_id,
            width=width,
            height=height
        )
        
        print(f"🌐 Generated dTree visualization: {html_path}")
        print(f"   Open in browser: file://{html_path}")
        
        return html_path
    
    def batch_process(
        self,
        input_files: List[str],
        dynasty_maps: Optional[List[Dict[str, str]]] = None,
        titles: Optional[List[str]] = None,
        formats: List[str] = ['svg', 'png', 'pdf']
    ) -> List[Dict[str, Any]]:
        """
        Process multiple files in batch.
        
        Args:
            input_files: List of input file paths (GEDCOM or JSON)
            dynasty_maps: List of dynasty maps (one per file)
            titles: List of titles (one per file)
            formats: Output formats
            
        Returns:
            List of result dictionaries
        """
        results = []
        
        if not dynasty_maps:
            dynasty_maps = [None] * len(input_files)
        if not titles:
            titles = [None] * len(input_files)
        
        for i, input_file in enumerate(input_files):
            file_path = Path(input_file)
            dynasty_map = dynasty_maps[i] if i < len(dynasty_maps) else None
            title = titles[i] if titles[i] else file_path.stem.replace('_', ' ').title()
            
            print(f"\n{'='*60}")
            print(f"Processing file {i+1}/{len(input_files)}: {file_path.name}")
            print(f"{'='*60}")
            
            if file_path.suffix.lower() == '.ged':
                result = self.process_gedcom_to_visualizations(
                    str(input_file),
                    dynasty_map=dynasty_map,
                    title=title,
                    formats=formats
                )
            elif file_path.suffix.lower() == '.json':
                result = self.process_json_to_visualizations(
                    str(input_file),
                    dynasty_map=dynasty_map,
                    title=title,
                    formats=formats
                )
            else:
                print(f"⚠️  Skipping unsupported file type: {file_path.suffix}")
                continue
            
            results.append(result)
        
        return results
