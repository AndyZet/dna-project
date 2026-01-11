# Genealogy Visualization Pipeline

Complete workflow for creating genealogy visualizations from GEDCOM or JSON data, with support for dynasty-based styling and multiple output formats.

## Overview

The genealogy visualization pipeline provides:

1. **Data Layer**: GEDCOM and JSON management
2. **Processing**: Graphviz-based tree generation with dynasty styling
3. **Visualization**: Multiple format output (SVG, PNG, PDF, DOT)
4. **Web Integration**: Support for Topola viewer and SVG-FTG

## Architecture

```
Data (GEDCOM/JSON) 
    ↓
Data Manager (load/export)
    ↓
Tree Generator (Graphviz with dynasty styling)
    ↓
Pipeline (DOT → SVG → Multiple formats)
    ↓
Output (SVG, PNG, PDF, DOT + Web-ready GEDCOM)
```

## Quick Start

### Basic Usage

```python
from visualization.genealogy_pipeline import GenealogyVisualizationPipeline

# Initialize pipeline
pipeline = GenealogyVisualizationPipeline()

# Process GEDCOM file
results = pipeline.process_gedcom_to_visualizations(
    gedcom_path="data/raw/genealogical/family_tree.ged",
    dynasty_map={
        'I001': 'Rurikid',
        'I002': 'Piast',
        'I003': 'Premyslid'
    },
    title="Early Medieval Royal Houses",
    formats=['svg', 'png', 'pdf']
)

# Access generated files
print(f"SVG: {results['rendered_files']['svg']}")
print(f"PNG: {results['rendered_files']['png']}")
print(f"PDF: {results['rendered_files']['pdf']}")
```

### Using the Example Script

```bash
# Activate virtual environment
source genealogy_env/bin/activate

# Run example script
python scripts/generate_genealogy_tree.py
```

This will:
1. Create sample Bodzia-style data
2. Export as JSON and GEDCOM
3. Generate visualizations in multiple formats
4. Prepare files for Topola viewer and SVG-FTG

## Data Layer

### Loading GEDCOM Files

```python
from genealogical.data_manager import GenealogyDataManager

data_manager = GenealogyDataManager()

# Load GEDCOM
data = data_manager.load_gedcom("family_tree.ged")

# Save as JSON
json_path = data_manager.save_json(data, "family_tree")

# Load JSON
data = data_manager.load_json("family_tree.json")
```

### Data Structure

The internal data format is a dictionary with:

```python
{
    'individuals': [
        {
            'id': 'I001',
            'name': 'John Doe',
            'birth': {'date': '1900', 'place': 'City'},
            'death': {'date': '1980', 'place': 'City'},
            'sex': 'M',
            'role': 'king',  # Optional: king, prince, duke, etc.
            'title': 'King of Example',  # Optional
            'dynasty': 'Rurikid'  # Optional
        }
    ],
    'families': [
        {
            'id': 'F001',
            'husband_id': 'I001',
            'wife_id': 'I002',
            'children': ['I003', 'I004'],
            'marriage': {'date': '1920', 'place': 'City'}
        }
    ],
    'sources': [],
    'notes': []
}
```

## Dynasty-Based Styling

### Supported Dynasties

Based on the Bodzia Early Medieval Royal Houses diagram:

- **Rurikid** - Red (#FF6B6B)
- **Piast** - Teal (#4ECDC4)
- **Premyslid** - Light teal (#95E1D3)
- **Gorm** - Pink (#F38181)
- **Normandy** - Purple (#AA96DA)
- **Capetian** - Light pink (#FCBAD3)
- **Ottonian** - Light blue (#A8D8EA)
- **Arpad** - Yellow (#FFD93D)

### Creating Dynasty Map

```python
dynasty_map = {
    'I001': 'Rurikid',
    'I002': 'Rurikid',
    'I003': 'Piast',
    'I004': 'Premyslid'
}
```

## Tree Generation

### Basic Tree Generation

```python
from visualization.graphviz_trees import DynastyTreeGenerator

generator = DynastyTreeGenerator()

# Create tree
dot = generator.create_tree(
    data=data,
    dynasty_map=dynasty_map,
    title="My Family Tree",
    format='svg',
    engine='dot',  # dot, neato, fdp, sfdp, twopi, circo
    orientation='TB'  # TB=Top-Bottom, LR=Left-Right
)

# Render
dot.render('output/tree')
```

### Multiple Formats

```python
results = generator.render_tree(
    data=data,
    dynasty_map=dynasty_map,
    title="Family Tree",
    formats=['svg', 'png', 'pdf', 'dot']
)
```

## Pipeline Workflow

### Complete Pipeline: GEDCOM → Visualizations

```python
pipeline = GenealogyVisualizationPipeline()

results = pipeline.process_gedcom_to_visualizations(
    gedcom_path="input.ged",
    dynasty_map=dynasty_map,
    title="Family Tree",
    formats=['svg', 'png', 'pdf', 'dot'],
    include_legend=True
)
```

### Pipeline: JSON → Visualizations

```python
results = pipeline.process_json_to_visualizations(
    json_path="data.json",
    dynasty_map=dynasty_map,
    title="Family Tree",
    formats=['svg', 'png', 'pdf']
)
```

### Batch Processing

```python
results = pipeline.batch_process(
    input_files=['tree1.ged', 'tree2.ged', 'tree3.json'],
    dynasty_maps=[map1, map2, map3],
    titles=['Tree 1', 'Tree 2', 'Tree 3'],
    formats=['svg', 'png']
)
```

## Web Integration

### Topola Viewer

Topola is an interactive web-based genealogy viewer that works entirely client-side.

```python
# Prepare GEDCOM for Topola
gedcom_path = pipeline.prepare_for_topola_viewer("family_tree.ged")

# Then:
# 1. Open https://pewu.github.io/topola-viewer/
# 2. Upload the GEDCOM file from output/web/
```

### SVG-FTG (SVG Family-Tree Generator)

SVG-FTG generates publication-quality SVG family trees.

```python
# Export GEDCOM for SVG-FTG
gedcom_path = pipeline.export_for_svg_ftg("family_tree.ged")

# Use with: https://parallaxviewpoint.com/SVG-FTG/
```

## Configuration

Configuration is stored in `config/settings.yaml`:

```yaml
visualization:
  genealogy:
    data_dir: "data/processed/genealogy"
    output_dir: "output/visualizations"
    default_formats: ["svg", "png", "pdf", "dot"]
    graphviz_engine: "dot"
    orientation: "TB"
    
    dynasty_colors:
      Rurikid: "#FF6B6B"
      Piast: "#4ECDC4"
      # ... etc
```

## Output Files

The pipeline generates:

- **DOT files**: Graphviz source files for manual editing
- **SVG files**: Scalable vector graphics (best for web/publication)
- **PNG files**: Raster images (good for presentations)
- **PDF files**: Vector format (good for printing)
- **Legend files**: Dynasty color legend (if requested)
- **Web-ready GEDCOM**: Prepared for Topola viewer and SVG-FTG

## Advanced Usage

### Custom Node Styling

Modify `DynastyTreeGenerator.DYNASTY_COLORS` or `NODE_SHAPES`:

```python
from visualization.graphviz_trees import DynastyTreeGenerator

generator = DynastyTreeGenerator()
generator.DYNASTY_COLORS['CustomDynasty'] = '#FF0000'
generator.NODE_SHAPES['custom_role'] = 'hexagon'
```

### Custom Graph Attributes

```python
dot = generator.create_tree(data, dynasty_map, title="Tree")

# Modify graph attributes
dot.graph_attr['bgcolor'] = '#F5F5F5'
dot.graph_attr['fontsize'] = '14'

# Modify node attributes
dot.node_attr['fontname'] = 'Times-Roman'

# Modify edge attributes
dot.edge_attr['color'] = '#333333'
```

## Troubleshooting

### Graphviz Not Found

If you get errors about Graphviz not being found:

```bash
# macOS (Homebrew)
brew install graphviz

# Verify installation
which dot
```

### Import Errors

Make sure you're in the project root and have activated the virtual environment:

```bash
source genealogy_env/bin/activate
cd "/Users/andrzejzak/DNA Project"
python scripts/generate_genealogy_tree.py
```

### Large Trees

For very large trees (100+ individuals):

1. Use `engine='fdp'` or `engine='sfdp'` for better layout
2. Increase `ranksep` and `nodesep` in graph attributes
3. Consider splitting into multiple trees

## Examples

See `scripts/generate_genealogy_tree.py` for a complete working example with Bodzia-style data.

## References

- [Graphviz Documentation](https://graphviz.org/documentation/)
- [Topola Viewer](https://pewu.github.io/topola-viewer/)
- [SVG-FTG](https://parallaxviewpoint.com/SVG-FTG/)
- [GEDCOM Format](https://en.wikipedia.org/wiki/GEDCOM)
