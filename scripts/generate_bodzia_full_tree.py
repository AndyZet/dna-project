#!/usr/bin/env python3
"""
Generate complete Bodzia Early Medieval Royal Houses tree visualization and documentation
Based on: Diagram_ Bodzia & Early Medieval Royal Houses  - Color.pdf
"""
import sys
import json
from pathlib import Path
from datetime import datetime

# Add src to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root / "src"))

from visualization.genealogy_pipeline import GenealogyVisualizationPipeline
from genealogical.data_manager import GenealogyDataManager
from visualization.graphviz_trees import DynastyTreeGenerator


def create_bodzia_full_tree_data() -> dict:
    """
    Create comprehensive data structure for Bodzia Early Medieval Royal Houses.
    Based on the Bodzia diagram showing connections between:
    - Rurikid dynasty (Kievan Rus')
    - Piast dynasty (Poland)
    - Premyslid dynasty (Bohemia)
    - Gorm dynasty (Denmark)
    - Normandy dynasty
    - Capetian dynasty (France)
    - Ottonian dynasty (Holy Roman Empire)
    - Arpad dynasty (Hungary)
    """
    return {
        'individuals': [
            # RURIKID DYNASTY (Kievan Rus')
            {
                'id': 'RUR001',
                'name': 'Sviatopolk I',
                'birth': {'date': '980', 'place': 'Kiev'},
                'death': {'date': '1019', 'place': 'Kiev'},
                'sex': 'M',
                'role': 'prince',
                'title': 'Grand Prince of Kiev',
                'dynasty': 'Rurikid',
                'notes': ['Bodzia burial connection', 'Son of Vladimir I']
            },
            {
                'id': 'RUR002',
                'name': 'Vladimir I the Great',
                'birth': {'date': '958', 'place': 'Kiev'},
                'death': {'date': '1015', 'place': 'Berestove'},
                'sex': 'M',
                'role': 'prince',
                'title': 'Grand Prince of Kiev',
                'dynasty': 'Rurikid'
            },
            {
                'id': 'RUR003',
                'name': 'Yaroslav I the Wise',
                'birth': {'date': '978', 'place': 'Kiev'},
                'death': {'date': '1054', 'place': 'Vyshhorod'},
                'sex': 'M',
                'role': 'prince',
                'title': 'Grand Prince of Kiev',
                'dynasty': 'Rurikid'
            },
            {
                'id': 'RUR004',
                'name': 'Iziaslav I',
                'birth': {'date': '1024', 'place': 'Kiev'},
                'death': {'date': '1078', 'place': 'Nezhyn'},
                'sex': 'M',
                'role': 'prince',
                'title': 'Grand Prince of Kiev',
                'dynasty': 'Rurikid'
            },
            {
                'id': 'RUR005',
                'name': 'Sviatoslav I',
                'birth': {'date': '942', 'place': 'Kiev'},
                'death': {'date': '972', 'place': 'Dnieper'},
                'sex': 'M',
                'role': 'prince',
                'title': 'Grand Prince of Kiev',
                'dynasty': 'Rurikid'
            },
            
            # PIAST DYNASTY (Poland)
            {
                'id': 'PIA001',
                'name': 'Boleslaw I the Brave',
                'birth': {'date': '967', 'place': 'Poznan'},
                'death': {'date': '1025', 'place': 'Krakow'},
                'sex': 'M',
                'role': 'king',
                'title': 'King of Poland',
                'dynasty': 'Piast',
                'notes': ['Allied with Sviatopolk', 'Bodzia connection']
            },
            {
                'id': 'PIA002',
                'name': 'Mieszko II Lambert',
                'birth': {'date': '990', 'place': 'Poznan'},
                'death': {'date': '1034', 'place': 'Poznan'},
                'sex': 'M',
                'role': 'king',
                'title': 'King of Poland',
                'dynasty': 'Piast'
            },
            {
                'id': 'PIA003',
                'name': 'Richeza of Lotharingia',
                'birth': {'date': '995', 'place': 'Lotharingia'},
                'death': {'date': '1063', 'place': 'Saalfeld'},
                'sex': 'F',
                'role': 'queen',
                'title': 'Queen of Poland',
                'dynasty': 'Piast'
            },
            {
                'id': 'PIA004',
                'name': 'Casimir I the Restorer',
                'birth': {'date': '1016', 'place': 'Krakow'},
                'death': {'date': '1058', 'place': 'Poznan'},
                'sex': 'M',
                'role': 'duke',
                'title': 'Duke of Poland',
                'dynasty': 'Piast'
            },
            {
                'id': 'PIA005',
                'name': 'Mieszko I',
                'birth': {'date': '930', 'place': 'Unknown'},
                'death': {'date': '992', 'place': 'Poznan'},
                'sex': 'M',
                'role': 'duke',
                'title': 'Duke of Poland',
                'dynasty': 'Piast'
            },
            
            # PREMYSLID DYNASTY (Bohemia)
            {
                'id': 'PRE001',
                'name': 'Bretislaus I',
                'birth': {'date': '1002', 'place': 'Bohemia'},
                'death': {'date': '1055', 'place': 'Chrudim'},
                'sex': 'M',
                'role': 'duke',
                'title': 'Duke of Bohemia',
                'dynasty': 'Premyslid'
            },
            {
                'id': 'PRE002',
                'name': 'Vratislaus II',
                'birth': {'date': '1032', 'place': 'Bohemia'},
                'death': {'date': '1092', 'place': 'Bohemia'},
                'sex': 'M',
                'role': 'king',
                'title': 'King of Bohemia',
                'dynasty': 'Premyslid'
            },
            {
                'id': 'PRE003',
                'name': 'Boleslaus I',
                'birth': {'date': '915', 'place': 'Bohemia'},
                'death': {'date': '972', 'place': 'Bohemia'},
                'sex': 'M',
                'role': 'duke',
                'title': 'Duke of Bohemia',
                'dynasty': 'Premyslid'
            },
            
            # GORM DYNASTY (Denmark)
            {
                'id': 'GOR001',
                'name': 'Gorm the Old',
                'birth': {'date': '900', 'place': 'Denmark'},
                'death': {'date': '958', 'place': 'Jelling'},
                'sex': 'M',
                'role': 'king',
                'title': 'King of Denmark',
                'dynasty': 'Gorm'
            },
            {
                'id': 'GOR002',
                'name': 'Harald Bluetooth',
                'birth': {'date': '910', 'place': 'Denmark'},
                'death': {'date': '986', 'place': 'Jomsborg'},
                'sex': 'M',
                'role': 'king',
                'title': 'King of Denmark',
                'dynasty': 'Gorm'
            },
            {
                'id': 'GOR003',
                'name': 'Sweyn Forkbeard',
                'birth': {'date': '960', 'place': 'Denmark'},
                'death': {'date': '1014', 'place': 'Gainsborough'},
                'sex': 'M',
                'role': 'king',
                'title': 'King of Denmark',
                'dynasty': 'Gorm'
            },
            
            # NORMANDY DYNASTY
            {
                'id': 'NOR001',
                'name': 'Richard I',
                'birth': {'date': '933', 'place': 'Normandy'},
                'death': {'date': '996', 'place': 'Fecamp'},
                'sex': 'M',
                'role': 'duke',
                'title': 'Duke of Normandy',
                'dynasty': 'Normandy'
            },
            {
                'id': 'NOR002',
                'name': 'Richard II',
                'birth': {'date': '963', 'place': 'Normandy'},
                'death': {'date': '1026', 'place': 'Fecamp'},
                'sex': 'M',
                'role': 'duke',
                'title': 'Duke of Normandy',
                'dynasty': 'Normandy'
            },
            {
                'id': 'NOR003',
                'name': 'Richard III',
                'birth': {'date': '997', 'place': 'Normandy'},
                'death': {'date': '1027', 'place': 'Normandy'},
                'sex': 'M',
                'role': 'duke',
                'title': 'Duke of Normandy',
                'dynasty': 'Normandy'
            },
            
            # CAPETIAN DYNASTY (France)
            {
                'id': 'CAP001',
                'name': 'Hugh Capet',
                'birth': {'date': '941', 'place': 'Paris'},
                'death': {'date': '996', 'place': 'Paris'},
                'sex': 'M',
                'role': 'king',
                'title': 'King of France',
                'dynasty': 'Capetian'
            },
            {
                'id': 'CAP002',
                'name': 'Robert II',
                'birth': {'date': '972', 'place': 'Orleans'},
                'death': {'date': '1031', 'place': 'Melun'},
                'sex': 'M',
                'role': 'king',
                'title': 'King of France',
                'dynasty': 'Capetian'
            },
            
            # OTTONIAN DYNASTY (Holy Roman Empire)
            {
                'id': 'OTT001',
                'name': 'Otto I',
                'birth': {'date': '912', 'place': 'Wallhausen'},
                'death': {'date': '973', 'place': 'Memleben'},
                'sex': 'M',
                'role': 'emperor',
                'title': 'Holy Roman Emperor',
                'dynasty': 'Ottonian'
            },
            {
                'id': 'OTT002',
                'name': 'Otto II',
                'birth': {'date': '955', 'place': 'Saxony'},
                'death': {'date': '983', 'place': 'Rome'},
                'sex': 'M',
                'role': 'emperor',
                'title': 'Holy Roman Emperor',
                'dynasty': 'Ottonian'
            },
            {
                'id': 'OTT003',
                'name': 'Otto III',
                'birth': {'date': '980', 'place': 'Kessel'},
                'death': {'date': '1002', 'place': 'Paterno'},
                'sex': 'M',
                'role': 'emperor',
                'title': 'Holy Roman Emperor',
                'dynasty': 'Ottonian'
            },
            
            # ARPAD DYNASTY (Hungary)
            {
                'id': 'ARP001',
                'name': 'Arpad',
                'birth': {'date': '845', 'place': 'Hungary'},
                'death': {'date': '907', 'place': 'Hungary'},
                'sex': 'M',
                'role': 'duke',
                'title': 'Grand Prince of Hungary',
                'dynasty': 'Arpad'
            },
            {
                'id': 'ARP002',
                'name': 'Stephen I',
                'birth': {'date': '975', 'place': 'Esztergom'},
                'death': {'date': '1038', 'place': 'Esztergom'},
                'sex': 'M',
                'role': 'king',
                'title': 'King of Hungary',
                'dynasty': 'Arpad'
            },
        ],
        'families': [
            # Rurikid families
            {
                'id': 'FAM_RUR001',
                'husband_id': 'RUR005',
                'wife_id': None,
                'children': ['RUR002'],
                'marriage': None
            },
            {
                'id': 'FAM_RUR002',
                'husband_id': 'RUR002',
                'wife_id': None,
                'children': ['RUR001', 'RUR003'],
                'marriage': None
            },
            {
                'id': 'FAM_RUR003',
                'husband_id': 'RUR003',
                'wife_id': None,
                'children': ['RUR004'],
                'marriage': None
            },
            
            # Piast families
            {
                'id': 'FAM_PIA001',
                'husband_id': 'PIA005',
                'wife_id': None,
                'children': ['PIA001'],
                'marriage': None
            },
            {
                'id': 'FAM_PIA002',
                'husband_id': 'PIA001',
                'wife_id': None,
                'children': ['PIA002'],
                'marriage': None
            },
            {
                'id': 'FAM_PIA003',
                'husband_id': 'PIA002',
                'wife_id': 'PIA003',
                'children': ['PIA004'],
                'marriage': {'date': '1013', 'place': 'Merseburg'}
            },
            
            # Premyslid families
            {
                'id': 'FAM_PRE001',
                'husband_id': 'PRE003',
                'wife_id': None,
                'children': ['PRE001'],
                'marriage': None
            },
            {
                'id': 'FAM_PRE002',
                'husband_id': 'PRE001',
                'wife_id': None,
                'children': ['PRE002'],
                'marriage': None
            },
            
            # Gorm families
            {
                'id': 'FAM_GOR001',
                'husband_id': 'GOR001',
                'wife_id': None,
                'children': ['GOR002'],
                'marriage': None
            },
            {
                'id': 'FAM_GOR002',
                'husband_id': 'GOR002',
                'wife_id': None,
                'children': ['GOR003'],
                'marriage': None
            },
            
            # Normandy families
            {
                'id': 'FAM_NOR001',
                'husband_id': 'NOR001',
                'wife_id': None,
                'children': ['NOR002'],
                'marriage': None
            },
            {
                'id': 'FAM_NOR002',
                'husband_id': 'NOR002',
                'wife_id': None,
                'children': ['NOR003'],
                'marriage': None
            },
            
            # Capetian families
            {
                'id': 'FAM_CAP001',
                'husband_id': 'CAP001',
                'wife_id': None,
                'children': ['CAP002'],
                'marriage': None
            },
            
            # Ottonian families
            {
                'id': 'FAM_OTT001',
                'husband_id': 'OTT001',
                'wife_id': None,
                'children': ['OTT002'],
                'marriage': None
            },
            {
                'id': 'FAM_OTT002',
                'husband_id': 'OTT002',
                'wife_id': None,
                'children': ['OTT003'],
                'marriage': None
            },
            
            # Arpad families
            {
                'id': 'FAM_ARP001',
                'husband_id': 'ARP001',
                'wife_id': None,
                'children': ['ARP002'],
                'marriage': None
            },
            
            # Cross-dynasty connections (marriages/alliances)
            {
                'id': 'FAM_CROSS001',
                'husband_id': 'RUR001',
                'wife_id': None,
                'children': [],
                'marriage': {'date': '1013', 'place': 'Bodzia'},
                'notes': ['Alliance with Boleslaw I']
            },
        ],
        'sources': [
            {
                'title': 'Bodzia Early Medieval Royal Houses Diagram',
                'type': 'diagram',
                'date': '2024',
                'notes': 'Color-coded genealogy diagram showing connections between medieval royal houses'
            }
        ],
        'notes': [
            'Bodzia cemetery (950-1020 CE) contains elite burials connected to these royal houses',
            'Sviatopolk I of Kiev is directly connected to Bodzia site',
            'Cross-cultural elite network: Scandinavian-Rus-Polish connections',
            'I-Y45113 haplogroup potentially connected to Bodzia elite warriors'
        ]
    }


def create_dynasty_map(data: dict) -> dict:
    """Create dynasty mapping from data"""
    dynasty_map = {}
    for ind in data['individuals']:
        dynasty_map[ind['id']] = ind.get('dynasty', 'default')
    return dynasty_map


def main():
    """Generate complete Bodzia tree visualization and documentation"""
    
    print("=" * 80)
    print("BODZIA EARLY MEDIEVAL ROYAL HOUSES - Complete Tree Generation")
    print("=" * 80)
    print()
    
    # Initialize pipeline
    pipeline = GenealogyVisualizationPipeline(
        data_dir="data/processed/genealogy",
        output_dir="output/visualizations/bodzia"
    )
    
    # Create comprehensive data
    print("📊 Step 1: Creating comprehensive Bodzia tree data structure...")
    data = create_bodzia_full_tree_data()
    dynasty_map = create_dynasty_map(data)
    
    print(f"   ✓ Created {len(data['individuals'])} individuals")
    print(f"   ✓ Created {len(data['families'])} families")
    print(f"   ✓ Mapped {len(set(dynasty_map.values()))} dynasties")
    
    # Save data
    data_manager = GenealogyDataManager()
    json_path = data_manager.save_json(data, "bodzia_full_tree")
    print(f"   ✓ Saved JSON: {json_path}")
    
    # Export GEDCOM
    gedcom_path = data_manager.export_gedcom(data, "data/processed/genealogy/bodzia_full_tree.ged")
    print(f"   ✓ Exported GEDCOM: {gedcom_path}")
    
    # Generate visualizations
    print("\n🎨 Step 2: Generating visualizations in all formats...")
    results = pipeline.process_json_to_visualizations(
        json_path=json_path,
        dynasty_map=dynasty_map,
        title="Bodzia Early Medieval Royal Houses - Complete Tree",
        formats=['svg', 'png', 'pdf', 'dot'],
        include_legend=True
    )
    
    print("\n✅ Generated files:")
    for key, value in results.items():
        if isinstance(value, dict):
            print(f"   {key}:")
            for fmt, path in value.items():
                print(f"     - {fmt.upper()}: {path}")
        else:
            print(f"   {key}: {value}")
    
    # Generate dynasty-specific sub-trees
    print("\n🌳 Step 3: Generating dynasty-specific sub-trees...")
    dynasties = list(set(dynasty_map.values()))
    
    for dynasty in dynasties:
        if dynasty == 'default':
            continue
        
        # Filter data for this dynasty
        dynasty_individuals = [ind for ind in data['individuals'] if ind.get('dynasty') == dynasty]
        dynasty_ids = {ind['id'] for ind in dynasty_individuals}
        
        # Get families involving this dynasty
        dynasty_families = []
        for fam in data['families']:
            if (fam.get('husband_id') in dynasty_ids or 
                fam.get('wife_id') in dynasty_ids or
                any(child_id in dynasty_ids for child_id in fam.get('children', []))):
                dynasty_families.append(fam)
        
        dynasty_data = {
            'individuals': dynasty_individuals,
            'families': dynasty_families,
            'sources': data['sources'],
            'notes': data['notes']
        }
        
        # Generate sub-tree
        sub_dynasty_map = {ind['id']: dynasty for ind in dynasty_individuals}
        sub_results = pipeline.process_json_to_visualizations(
            data=dynasty_data,
            dynasty_map=sub_dynasty_map,
            title=f"Bodzia - {dynasty} Dynasty",
            formats=['svg', 'png', 'pdf'],
            include_legend=False
        )
        
        # Save dynasty data
        data_manager.save_json(dynasty_data, f"bodzia_{dynasty.lower()}_dynasty")
        print(f"   ✓ Generated {dynasty} dynasty tree")
    
    # Prepare web files
    print("\n🌐 Step 4: Preparing web-ready files...")
    topola_gedcom = pipeline.prepare_for_topola_viewer(gedcom_path)
    svgftg_gedcom = pipeline.export_for_svg_ftg(gedcom_path)
    
    # Generate documentation
    print("\n📚 Step 5: Generating comprehensive documentation...")
    generate_documentation(data, dynasty_map, results)
    
    print("\n" + "=" * 80)
    print("✅ COMPLETE TREE GENERATION FINISHED!")
    print("=" * 80)
    print("\nGenerated outputs:")
    print("  • Complete tree: output/visualizations/bodzia/")
    print("  • Dynasty sub-trees: output/visualizations/bodzia/")
    print("  • Web files: output/web/")
    print("  • Documentation: docs/BODZIA_TREE_DOCUMENTATION.md")
    print("\nNext steps:")
    print("  1. View SVG/PNG/PDF files in output/visualizations/bodzia/")
    print("  2. Open Topola viewer: https://pewu.github.io/topola-viewer/")
    print("  3. Upload GEDCOM from: output/web/")
    print("  4. Review documentation: docs/BODZIA_TREE_DOCUMENTATION.md")


def generate_documentation(data: dict, dynasty_map: dict, results: dict):
    """Generate comprehensive documentation"""
    
    doc_path = Path("docs/BODZIA_TREE_DOCUMENTATION.md")
    doc_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Count statistics
    dynasty_counts = {}
    for dynasty in dynasty_map.values():
        dynasty_counts[dynasty] = dynasty_counts.get(dynasty, 0) + 1
    
    # Generate documentation
    doc_content = f"""# Bodzia Early Medieval Royal Houses - Complete Tree Documentation

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Source:** Diagram_ Bodzia & Early Medieval Royal Houses  - Color.pdf  
**Data Structure:** {len(data['individuals'])} individuals, {len(data['families'])} families

---

## Overview

This documentation covers the complete genealogy tree of Early Medieval Royal Houses connected to the Bodzia archaeological site (950-1020 CE). The Bodzia cemetery represents a unique cross-cultural elite burial ground showing connections between Scandinavian, Rus', Polish, and other European royal dynasties.

## Tree Statistics

### Individuals by Dynasty

"""
    
    for dynasty, count in sorted(dynasty_counts.items()):
        doc_content += f"- **{dynasty}**: {count} individuals\n"
    
    doc_content += f"""
### Total Statistics

- **Total Individuals**: {len(data['individuals'])}
- **Total Families**: {len(data['families'])}
- **Dynasties Represented**: {len(set(dynasty_map.values()))}
- **Time Period**: 845-1092 CE

---

## Dynasties

"""
    
    # Group individuals by dynasty
    by_dynasty = {}
    for ind in data['individuals']:
        dynasty = ind.get('dynasty', 'default')
        if dynasty not in by_dynasty:
            by_dynasty[dynasty] = []
        by_dynasty[dynasty].append(ind)
    
    for dynasty in sorted(by_dynasty.keys()):
        if dynasty == 'default':
            continue
        doc_content += f"\n### {dynasty} Dynasty\n\n"
        for ind in sorted(by_dynasty[dynasty], key=lambda x: x.get('birth', {}).get('date', '0') if isinstance(x.get('birth'), dict) else '0'):
            name = ind['name']
            title = ind.get('title', '')
            birth = ind.get('birth', {})
            death = ind.get('death', {})
            birth_date = birth.get('date', '?') if isinstance(birth, dict) else '?'
            death_date = death.get('date', '?') if isinstance(death, dict) else '?'
            
            doc_content += f"- **{name}** ({birth_date} - {death_date})"
            if title:
                doc_content += f" - {title}"
            if ind.get('notes'):
                doc_content += f" - *{', '.join(ind['notes'])}*"
            doc_content += "\n"
    
    doc_content += f"""
---

## Key Connections

### Bodzia Site Connections

- **Sviatopolk I of Kiev** (RUR001): Direct connection to Bodzia burial site
- **Boleslaw I the Brave** (PIA001): Allied with Sviatopolk, Bodzia connection
- **Time Period**: 950-1020 CE matches Bodzia cemetery active period

### Cross-Dynasty Marriages and Alliances

"""
    
    for fam in data['families']:
        if fam.get('marriage'):
            husband = next((ind for ind in data['individuals'] if ind['id'] == fam.get('husband_id')), None)
            wife = next((ind for ind in data['individuals'] if ind['id'] == fam.get('wife_id')), None)
            if husband and wife:
                doc_content += f"- **{husband['name']}** ({husband.get('dynasty', 'Unknown')}) × **{wife['name']}** ({wife.get('dynasty', 'Unknown')}) - {fam['marriage'].get('date', 'Unknown date')}\n"
    
    doc_content += f"""
---

## Generated Files

### Visualizations

"""
    
    for fmt, path in results.get('rendered_files', {}).items():
        doc_content += f"- **{fmt.upper()}**: `{path}`\n"
    
    doc_content += f"""
- **Legend**: `{results.get('legend_file', 'N/A')}`
- **DOT Source**: `{results.get('dot_file', 'N/A')}`

### Data Files

- **JSON**: `data/processed/genealogy/bodzia_full_tree.json`
- **GEDCOM**: `data/processed/genealogy/bodzia_full_tree.ged`
- **Web GEDCOM (Topola)**: `output/web/bodzia_full_tree.ged`
- **Web GEDCOM (SVG-FTG)**: `output/web/bodzia_full_tree_svgftg.ged`

---

## Usage

### Viewing Visualizations

1. **SVG files**: Open in any web browser or vector graphics editor
2. **PNG files**: Standard image viewer
3. **PDF files**: PDF viewer (best for printing)
4. **DOT files**: Edit with Graphviz tools or text editor

### Interactive Viewing

1. **Topola Viewer**: 
   - Visit: https://pewu.github.io/topola-viewer/
   - Upload: `output/web/bodzia_full_tree.ged`
   - Features: Interactive navigation, ancestor/descendant views

2. **SVG-FTG**:
   - Visit: https://parallaxviewpoint.com/SVG-FTG/
   - Upload: `output/web/bodzia_full_tree_svgftg.ged`
   - Features: Publication-quality SVG generation

---

## Research Context

### Bodzia Archaeological Site

The Bodzia cemetery (near Włocławek, central Poland) represents one of the most significant early medieval elite burial sites in Central Europe. Dating to 950-1020 CE, it contains:

- Scandinavian-style weaponry (Viking swords)
- Mammen-style silver artifacts
- Cross-cultural goods (Rus', Polish, Scandinavian)
- Elite warrior burials

### Genetic Connections

- **I-Y45113 haplogroup**: Potentially connected to Bodzia elite warriors
- **Formation date**: ~975 CE (matches Bodzia active period)
- **Geographic alignment**: Bodzia is ~60 km from Płock (Mazowieckie region)

### Historical Significance

This tree represents the interconnected elite networks of Early Medieval Europe, showing how royal houses maintained connections through:
- Strategic marriages
- Military alliances
- Trade networks
- Cultural exchange

---

## References

- Bodzia archaeological site documentation
- Early Medieval Royal Houses genealogical records
- Diagram_ Bodzia & Early Medieval Royal Houses  - Color.pdf
- I-Y45113 haplogroup research

---

## Data Structure

### Individual Record Format

```json
{{
    "id": "RUR001",
    "name": "Sviatopolk I",
    "birth": {{"date": "980", "place": "Kiev"}},
    "death": {{"date": "1019", "place": "Kiev"}},
    "sex": "M",
    "role": "prince",
    "title": "Grand Prince of Kiev",
    "dynasty": "Rurikid",
    "notes": ["Bodzia burial connection"]
}}
```

### Family Record Format

```json
{{
    "id": "FAM_RUR001",
    "husband_id": "RUR005",
    "wife_id": null,
    "children": ["RUR002"],
    "marriage": null
}}
```

---

**Document Version**: 1.0  
**Last Updated**: {datetime.now().strftime('%Y-%m-%d')}  
**Generated By**: Bodzia Tree Generation Pipeline
"""
    
    with open(doc_path, 'w', encoding='utf-8') as f:
        f.write(doc_content)
    
    print(f"   ✓ Generated documentation: {doc_path}")


if __name__ == "__main__":
    main()
