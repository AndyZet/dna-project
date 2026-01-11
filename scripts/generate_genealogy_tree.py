#!/usr/bin/env python3
"""
Example script demonstrating the genealogy visualization pipeline
"""
import sys
import os
from pathlib import Path

# Add src to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root / "src"))

from visualization.genealogy_pipeline import GenealogyVisualizationPipeline
from genealogical.data_manager import GenealogyDataManager


def main():
    """Example usage of the genealogy visualization pipeline"""
    
    print("=" * 70)
    print("Genealogy Visualization Pipeline - Example Script")
    print("=" * 70)
    
    # Initialize pipeline
    pipeline = GenealogyVisualizationPipeline(
        data_dir="data/processed/genealogy",
        output_dir="output/visualizations"
    )
    
    # Example 1: Create sample data (Bodzia-style royal houses)
    print("\n📝 Example 1: Creating sample Bodzia-style data...")
    sample_data = create_sample_bodzia_data()
    
    # Save sample data as JSON
    data_manager = GenealogyDataManager()
    json_path = data_manager.save_json(sample_data, "bodzia_sample")
    print(f"   ✓ Saved sample data: {json_path}")
    
    # Export as GEDCOM
    gedcom_path = data_manager.export_gedcom(sample_data, "data/processed/genealogy/bodzia_sample.ged")
    print(f"   ✓ Exported GEDCOM: {gedcom_path}")
    
    # Example 2: Process JSON to visualizations
    print("\n🎨 Example 2: Processing JSON to visualizations...")
    dynasty_map = {
        'I001': 'Rurikid',
        'I002': 'Rurikid',
        'I003': 'Piast',
        'I004': 'Piast',
        'I005': 'Premyslid',
        'I006': 'Premyslid',
        'I007': 'Rurikid',
        'I008': 'Rurikid'
    }
    
    results = pipeline.process_json_to_visualizations(
        json_path=json_path,
        dynasty_map=dynasty_map,
        title="Bodzia Early Medieval Royal Houses",
        formats=['svg', 'png', 'pdf', 'dot'],
        include_legend=True
    )
    
    print("\n✅ Generated files:")
    for key, value in results.items():
        if isinstance(value, dict):
            print(f"   {key}:")
            for fmt, path in value.items():
                print(f"     - {fmt}: {path}")
        else:
            print(f"   {key}: {value}")
    
    # Example 3: Prepare for Topola viewer
    print("\n🌐 Example 3: Preparing for Topola viewer...")
    topola_gedcom = pipeline.prepare_for_topola_viewer(gedcom_path)
    
    # Example 4: Export for SVG-FTG
    print("\n📄 Example 4: Exporting for SVG-FTG...")
    svgftg_gedcom = pipeline.export_for_svg_ftg(gedcom_path)
    
    print("\n" + "=" * 70)
    print("✅ Pipeline complete!")
    print("=" * 70)
    print("\nNext steps:")
    print("1. View SVG/PNG/PDF files in: output/visualizations/")
    print("2. Open Topola viewer: https://pewu.github.io/topola-viewer/")
    print("3. Upload GEDCOM file from: output/web/")
    print("4. Use SVG-FTG with GEDCOM from: output/web/")


def create_sample_bodzia_data() -> dict:
    """Create sample data structure based on Bodzia diagram"""
    return {
        'individuals': [
            {
                'id': 'I001',
                'name': 'Svyatopolk I of Kiev',
                'birth': {'date': '980', 'place': 'Kiev'},
                'death': {'date': '1019', 'place': 'Kiev'},
                'sex': 'M',
                'role': 'king',
                'title': 'Grand Prince of Kiev',
                'dynasty': 'Rurikid'
            },
            {
                'id': 'I002',
                'name': 'Boleslaw I the Brave',
                'birth': {'date': '967', 'place': 'Poznan'},
                'death': {'date': '1025', 'place': 'Krakow'},
                'sex': 'M',
                'role': 'king',
                'title': 'King of Poland',
                'dynasty': 'Piast'
            },
            {
                'id': 'I003',
                'name': 'Mieszko II Lambert',
                'birth': {'date': '990', 'place': 'Poznan'},
                'death': {'date': '1034', 'place': 'Poznan'},
                'sex': 'M',
                'role': 'king',
                'title': 'King of Poland',
                'dynasty': 'Piast'
            },
            {
                'id': 'I004',
                'name': 'Richeza of Lotharingia',
                'birth': {'date': '995', 'place': 'Lotharingia'},
                'death': {'date': '1063', 'place': 'Saalfeld'},
                'sex': 'F',
                'role': 'queen',
                'title': 'Queen of Poland',
                'dynasty': 'Piast'
            },
            {
                'id': 'I005',
                'name': 'Bretislaus I',
                'birth': {'date': '1002', 'place': 'Bohemia'},
                'death': {'date': '1055', 'place': 'Bohemia'},
                'sex': 'M',
                'role': 'duke',
                'title': 'Duke of Bohemia',
                'dynasty': 'Premyslid'
            },
            {
                'id': 'I006',
                'name': 'Vratislaus II',
                'birth': {'date': '1032', 'place': 'Bohemia'},
                'death': {'date': '1092', 'place': 'Bohemia'},
                'sex': 'M',
                'role': 'king',
                'title': 'King of Bohemia',
                'dynasty': 'Premyslid'
            },
            {
                'id': 'I007',
                'name': 'Yaroslav I the Wise',
                'birth': {'date': '978', 'place': 'Kiev'},
                'death': {'date': '1054', 'place': 'Kiev'},
                'sex': 'M',
                'role': 'prince',
                'title': 'Grand Prince of Kiev',
                'dynasty': 'Rurikid'
            },
            {
                'id': 'I008',
                'name': 'Iziaslav I',
                'birth': {'date': '1024', 'place': 'Kiev'},
                'death': {'date': '1078', 'place': 'Nezhyn'},
                'sex': 'M',
                'role': 'prince',
                'title': 'Grand Prince of Kiev',
                'dynasty': 'Rurikid'
            }
        ],
        'families': [
            {
                'id': 'F001',
                'husband_id': 'I002',
                'wife_id': None,
                'children': ['I003'],
                'marriage': None
            },
            {
                'id': 'F002',
                'husband_id': 'I003',
                'wife_id': 'I004',
                'children': [],
                'marriage': {'date': '1013', 'place': 'Merseburg'}
            },
            {
                'id': 'F003',
                'husband_id': 'I005',
                'wife_id': None,
                'children': ['I006'],
                'marriage': None
            },
            {
                'id': 'F004',
                'husband_id': 'I001',
                'wife_id': None,
                'children': [],
                'marriage': None
            },
            {
                'id': 'F005',
                'husband_id': 'I007',
                'wife_id': None,
                'children': ['I008'],
                'marriage': None
            }
        ],
        'sources': [],
        'notes': []
    }


if __name__ == "__main__":
    main()
