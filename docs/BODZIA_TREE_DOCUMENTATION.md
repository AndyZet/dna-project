# Bodzia Early Medieval Royal Houses - Complete Tree Documentation

**Generated:** 2026-01-11 00:15:54  
**Source:** Diagram_ Bodzia & Early Medieval Royal Houses  - Color.pdf  
**Data Structure:** 26 individuals, 17 families

---

## Overview

This documentation covers the complete genealogy tree of Early Medieval Royal Houses connected to the Bodzia archaeological site (950-1020 CE). The Bodzia cemetery represents a unique cross-cultural elite burial ground showing connections between Scandinavian, Rus', Polish, and other European royal dynasties.

## Tree Statistics

### Individuals by Dynasty

- **Arpad**: 2 individuals
- **Capetian**: 2 individuals
- **Gorm**: 3 individuals
- **Normandy**: 3 individuals
- **Ottonian**: 3 individuals
- **Piast**: 5 individuals
- **Premyslid**: 3 individuals
- **Rurikid**: 5 individuals

### Total Statistics

- **Total Individuals**: 26
- **Total Families**: 17
- **Dynasties Represented**: 8
- **Time Period**: 845-1092 CE

---

## Dynasties


### Arpad Dynasty

- **Arpad** (845 - 907) - Grand Prince of Hungary
- **Stephen I** (975 - 1038) - King of Hungary

### Capetian Dynasty

- **Hugh Capet** (941 - 996) - King of France
- **Robert II** (972 - 1031) - King of France

### Gorm Dynasty

- **Gorm the Old** (900 - 958) - King of Denmark
- **Harald Bluetooth** (910 - 986) - King of Denmark
- **Sweyn Forkbeard** (960 - 1014) - King of Denmark

### Normandy Dynasty

- **Richard I** (933 - 996) - Duke of Normandy
- **Richard II** (963 - 1026) - Duke of Normandy
- **Richard III** (997 - 1027) - Duke of Normandy

### Ottonian Dynasty

- **Otto I** (912 - 973) - Holy Roman Emperor
- **Otto II** (955 - 983) - Holy Roman Emperor
- **Otto III** (980 - 1002) - Holy Roman Emperor

### Piast Dynasty

- **Casimir I the Restorer** (1016 - 1058) - Duke of Poland
- **Mieszko I** (930 - 992) - Duke of Poland
- **Boleslaw I the Brave** (967 - 1025) - King of Poland - *Allied with Sviatopolk, Bodzia connection*
- **Mieszko II Lambert** (990 - 1034) - King of Poland
- **Richeza of Lotharingia** (995 - 1063) - Queen of Poland

### Premyslid Dynasty

- **Bretislaus I** (1002 - 1055) - Duke of Bohemia
- **Vratislaus II** (1032 - 1092) - King of Bohemia
- **Boleslaus I** (915 - 972) - Duke of Bohemia

### Rurikid Dynasty

- **Iziaslav I** (1024 - 1078) - Grand Prince of Kiev
- **Sviatoslav I** (942 - 972) - Grand Prince of Kiev
- **Vladimir I the Great** (958 - 1015) - Grand Prince of Kiev
- **Yaroslav I the Wise** (978 - 1054) - Grand Prince of Kiev
- **Sviatopolk I** (980 - 1019) - Grand Prince of Kiev - *Bodzia burial connection, Son of Vladimir I*

---

## Key Connections

### Bodzia Site Connections

- **Sviatopolk I of Kiev** (RUR001): Direct connection to Bodzia burial site
- **Boleslaw I the Brave** (PIA001): Allied with Sviatopolk, Bodzia connection
- **Time Period**: 950-1020 CE matches Bodzia cemetery active period

### Cross-Dynasty Marriages and Alliances

- **Mieszko II Lambert** (Piast) × **Richeza of Lotharingia** (Piast) - 1013

---

## Generated Files

### Visualizations

- **SVG**: `output/visualizations/bodzia/bodzia_full_tree.svg`
- **PNG**: `output/visualizations/bodzia/bodzia_full_tree.png`
- **PDF**: `output/visualizations/bodzia/bodzia_full_tree.pdf`
- **DOT**: `output/visualizations/bodzia/bodzia_full_tree.dot`

- **Legend**: `output/visualizations/bodzia/bodzia_full_tree_legend.svg`
- **DOT Source**: `output/visualizations/bodzia/bodzia_full_tree.dot`

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
{
    "id": "RUR001",
    "name": "Sviatopolk I",
    "birth": {"date": "980", "place": "Kiev"},
    "death": {"date": "1019", "place": "Kiev"},
    "sex": "M",
    "role": "prince",
    "title": "Grand Prince of Kiev",
    "dynasty": "Rurikid",
    "notes": ["Bodzia burial connection"]
}
```

### Family Record Format

```json
{
    "id": "FAM_RUR001",
    "husband_id": "RUR005",
    "wife_id": null,
    "children": ["RUR002"],
    "marriage": null
}
```

---

**Document Version**: 1.0  
**Last Updated**: 2026-01-11  
**Generated By**: Bodzia Tree Generation Pipeline
