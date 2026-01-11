#!/usr/bin/env python3
"""
Generate DNA-focused visualizations from Bodzia tree documentation
"""
import sys
from pathlib import Path

# Add src to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root / "src"))

from visualization.dna_visualizer import DNAVisualizer


def main():
    """Generate all DNA-focused visualizations"""
    
    print("=" * 80)
    print("BODZIA DNA-FOCUSED VISUALIZATION GENERATION")
    print("=" * 80)
    print()
    
    # Initialize visualizer
    print("📊 Step 1: Initializing DNA visualizer...")
    visualizer = DNAVisualizer()
    
    # Load data
    print("📖 Step 2: Loading data...")
    visualizer.load_data()
    dna_individuals = visualizer.extract_dna_tested_individuals()
    print(f"   ✓ Found {len(dna_individuals)} DNA-tested individuals")
    
    # Get markers
    markers = visualizer.get_dna_markers()
    print(f"   ✓ Y-DNA markers: {len(markers['Y-DNA'])}")
    print(f"   ✓ mtDNA markers: {len(markers['mtDNA'])}")
    
    # Create output directory
    output_dir = Path("output/visualizations/dna")
    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"   ✓ Output directory: {output_dir}")
    
    # Generate visualizations
    print("\n🎨 Step 3: Generating visualizations...")
    
    # 1. DNA Markers Chart
    print("\n   1. Creating DNA markers chart...")
    visualizer.create_dna_markers_chart(str(output_dir / "dna_markers_chart.png"))
    
    # 2. DNA Network Diagram
    print("\n   2. Creating DNA network diagram...")
    visualizer.create_dna_network(str(output_dir / "bodzia_dna_network.svg"))
    
    # 3. Timeline Visualization
    print("\n   3. Creating timeline visualization...")
    visualizer.create_dna_timeline(str(output_dir / "dna_timeline.png"))
    
    # 4. Dynasty Distribution
    print("\n   4. Creating dynasty distribution chart...")
    visualizer.create_dynasty_distribution(str(output_dir / "dynasty_dna_distribution.png"))
    
    # 5. Interactive Dashboard
    print("\n   5. Creating interactive dashboard...")
    visualizer.create_interactive_dashboard(str(output_dir / "bodzia_dna_dashboard.html"))
    
    # Summary
    print("\n" + "=" * 80)
    print("✅ DNA VISUALIZATION GENERATION COMPLETE!")
    print("=" * 80)
    print("\nGenerated files:")
    print(f"  • DNA Markers Chart: {output_dir / 'dna_markers_chart.png'}")
    print(f"  • DNA Network Diagram: {output_dir / 'bodzia_dna_network.svg'}")
    print(f"  • Timeline Visualization: {output_dir / 'dna_timeline.png'}")
    print(f"  • Dynasty Distribution: {output_dir / 'dynasty_dna_distribution.png'}")
    print(f"  • Interactive Dashboard: {output_dir / 'bodzia_dna_dashboard.html'}")
    print("\nSummary:")
    print(f"  • DNA-tested individuals: {len(dna_individuals)}")
    print(f"  • Y-DNA markers: {len(markers['Y-DNA'])}")
    print(f"  • mtDNA markers: {len(markers['mtDNA'])}")
    print("\nNext steps:")
    print("  1. View static visualizations in: output/visualizations/dna/")
    print("  2. Open interactive dashboard: output/visualizations/dna/bodzia_dna_dashboard.html")
    print("  3. Review documentation: docs/BODZIA_COMPLETE_TREE_DOCUMENTATION.md")


if __name__ == "__main__":
    main()
