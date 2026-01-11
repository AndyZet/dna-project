#!/usr/bin/env python3
"""
Generate interactive dTree visualization for Bodzia family tree
Based on: https://github.com/ErikGartner/dTree
"""
import sys
import os
from pathlib import Path

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from visualization.genealogy_pipeline import GenealogyVisualizationPipeline


def main():
    print("================================================================================")
    print("BODZIA DTREE INTERACTIVE VISUALIZATION GENERATION")
    print("================================================================================")
    
    # Initialize pipeline
    pipeline = GenealogyVisualizationPipeline()
    
    # Path to complete tree JSON
    json_path = "data/processed/genealogy/bodzia_complete_tree.json"
    
    if not Path(json_path).exists():
        print(f"❌ Error: JSON file not found: {json_path}")
        print("   Please run generate_bodzia_complete_tree.py first")
        return 1
    
    print(f"\n📖 Loading data from: {json_path}")
    
    # Generate dTree visualization
    print("\n🌳 Generating dTree interactive visualization...")
    html_path = pipeline.generate_dtree_visualization(
        json_path=json_path,
        output_filename="bodzia_complete_dtree.html",
        title="Bodzia Early Medieval Royal Houses - Interactive Family Tree",
        width=1400,
        height=900
    )
    
    print("\n================================================================================")
    print("✅ DTREE VISUALIZATION GENERATION COMPLETE!")
    print("================================================================================")
    
    print(f"\n📄 Generated file: {html_path}")
    print("\n📋 Usage:")
    print(f"   1. Open in browser: file://{Path(html_path).absolute()}")
    print("   2. Click and drag to pan the tree")
    print("   3. Scroll to zoom in/out")
    print("   4. Click on nodes to see detailed information")
    print("   5. Use 'Reset Zoom' and 'Fit to View' buttons for navigation")
    print("\n💡 Features:")
    print("   • Interactive pan and zoom")
    print("   • Dynasty-based color coding")
    print("   • DNA-tested individuals highlighted")
    print("   • Click nodes for detailed information")
    print("   • Multiple parent support (complex family relationships)")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
