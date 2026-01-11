# API Usage Guide

## Y-DNA Analysis

### Haplogroup Parser

```python
from src.y_dna.haplogroup_parser import parse_isogg_tree, find_haplogroup

# Parse ISOGG tree
tree = parse_isogg_tree('data/reference/isogg_y_tree.csv')

# Find specific haplogroup
haplogroup = find_haplogroup(tree, 'I-Y45113')
```

### SNP Analyzer

```python
from src.y_dna.snp_analyzer import analyze_snps, filter_by_haplogroup

# Analyze VCF file
snps = analyze_snps('data/raw/y_dna_results/snp_data.vcf')

# Filter by haplogroup
filtered = filter_by_haplogroup('data/raw/y_dna_results/snp_data.vcf', 'I-Y45113')
```

### TMRCA Calculator

```python
from src.y_dna.tmrca_calculator import calculate_tmrca

# Calculate TMRCA
results = calculate_tmrca(
    your_haplogroup='I-Y45113',
    cousin_haplogroups=['I-Y224059', 'I-Y45233'],
    y_str_profiles='data/processed/y_str_haplotypes.csv'
)
```

## Ancient DNA Analysis

### Bodzia Matcher

```python
from src.ancient_dna.bodzia_matcher import match_bodzia_samples

matches = match_bodzia_samples(
    your_dna='data/raw/autosomal/mytrueancestry_results.json',
    bodzia_samples='data/reference/bodzia_samples.csv'
)
```

### Kievan Rus' Analysis

```python
from src.ancient_dna.kievan_rus_analysis import analyze_kievan_rus_connections

results = analyze_kievan_rus_connections(
    your_dna='data/raw/autosomal/your_dna.csv',
    kievan_rus_data='data/reference/kievan_rus_ancient_dna.csv'
)
```

## Genealogical Data

### GEDCOM Parser

```python
from src.genealogical.gedcom_parser import parse_family_tree

tree = parse_family_tree('data/raw/genealogical/family_tree.ged')
```

### Parish Records

```python
from src.genealogical.parish_records import load_parish_records, search_parish_records

# Load records
records = load_parish_records('data/raw/genealogical/parish_records/records.csv')

# Search
filtered = search_parish_records(
    records,
    name='Radzimowski',
    location='Sucha',
    date_range=('1800', '1900')
)
```

## Visualization

### Phylogenetic Trees

```python
from src.visualization.phylogenetic_trees import generate_haplogroup_tree

generate_haplogroup_tree(
    tree_data,
    output='output/visualizations/haplogroup_tree.png'
)
```

### Migration Maps

```python
from src.visualization.migration_maps import create_migration_map

locations = [
    {'lat': 52.7, 'lon': 18.9, 'name': 'Bodzia', 'date': '1000 AD'},
    {'lat': 51.5, 'lon': 20.4, 'name': 'Sucha', 'date': '1800'}
]

create_migration_map(
    locations,
    center=(52.0, 20.0),
    output_path='output/visualizations/migration_map.html'
)
```

## Database

### Models

```python
from src.database.models import YDNAResult, Individual, create_database

# Create database
engine = create_database()

# Use models
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

result = YDNAResult(
    individual_id='AR001',
    haplogroup='I-Y45113',
    snp_count=500
)
session.add(result)
session.commit()
```

### Queries

```python
from src.database.queries import get_y_dna_results

results = get_y_dna_results(session, haplogroup='I-Y45113')
```
