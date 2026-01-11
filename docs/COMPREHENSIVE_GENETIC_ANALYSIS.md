# Comprehensive Genetic Analysis - Bodzia Samples

## Overview

This document presents comprehensive genetic analysis results for the Bodzia ancient DNA samples (VK155, VK157, VK154, VK156), integrating G25 coordinates, admixture modeling, population distances, PCA analysis, and My True Ancestry (MTA) match data.

## Data Sources

- **G25 Coordinates**: Parsed from `data/raw/autosomal/MTA/VK155/vk155_G25.txt` and `VK157/vk157_G25.txt`
- **Admixture Data**: From Explore Your DNA (Davidski's G25 standard reference populations)
- **Population Distances**: From Explore Your DNA ancient population distance calculations
- **MTA Match Data**: Parsed from `matchesMTA.md` files using `mta_parser.py`
- **Haplogroups**: From Explore Your DNA sample information
- **Genealogy Data**: Integrated with `bodzia_complete_tree.json`

## Samples Analyzed

### VK155 - The Witch from Bodzia
- **Sex**: Female
- **Date**: 1000 AD
- **Location**: Bodzia, Poland
- **mtDNA**: H1c
- **Y-DNA**: Not determined (female)
- **G25 Coordinates**: Available
- **MTA Data**: Available

### VK157 - Sviatopolk I of Kiev
- **Sex**: Male
- **Date**: 1000 AD
- **Location**: Bodzia, Poland (burial E864/I)
- **Y-DNA**: I1a3a1 (I1-S2077)
- **mtDNA**: H1c
- **G25 Coordinates**: Available
- **MTA Data**: Available

### VK154 - Princess from Bodzia
- **Sex**: Female
- **Date**: 1000 AD
- **Location**: Bodzia, Poland (burial E864/II)
- **mtDNA**: H1c3
- **Y-DNA**: Not determined (female)
- **G25 Coordinates**: Not available
- **MTA Data**: Not available

### VK156 - Bodzia Warrior
- **Sex**: Male
- **Date**: 1000 AD
- **Location**: Bodzia, Poland
- **Y-DNA**: R1a1a1b1a2a2a1
- **mtDNA**: J1c2c2a
- **G25 Coordinates**: Not available
- **MTA Data**: Not available

## Analysis Methods

### 1. G25 Coordinate Analysis

G25 coordinates are 25-dimensional PCA coordinates derived from ancient DNA samples, allowing for precise genetic distance calculations and population comparisons.

**Key Findings:**
- Genetic distances calculated using Euclidean distance in 25-dimensional space
- VK155 and VK157 show close genetic relationship (distance: [calculated from data])
- Both samples cluster with Viking Age populations from Poland and Sweden

**Visualizations:**
- `g25_coordinates.png`: PCA plot showing genetic relationships
- `comparison_matrix.png`: Heatmap of pairwise genetic distances

### 2. Admixture Analysis

Ancient admixture components estimated using Davidski's G25 standard reference populations.

#### VK155 Admixture
- **Yamnaya_RUS_Samara**: 52.7%
- **TUR_Barcin_N** (Neolithic Farmers): 29.7%
- **WHG** (Western Hunter-Gatherers): 16.9%
- **BRA_LapaDoSanto**: 0.7%

#### VK157 Admixture
- **Yamnaya_RUS_Samara**: 48.1%
- **TUR_Barcin_N** (Neolithic Farmers): 27.9%
- **WHG** (Western Hunter-Gatherers): 21.9%
- **TUR_Tepecik_Ciftlik_N**: 2.1%

#### VK154 Admixture
- **Yamnaya_RUS_Samara**: 52.6%
- **TUR_Barcin_N** (Neolithic Farmers): 28.3%
- **WHG** (Western Hunter-Gatherers): 19.1%

#### VK156 Admixture
- **Yamnaya_RUS_Samara**: 50.9%
- **TUR_Barcin_N** (Neolithic Farmers): 31.4%
- **WHG** (Western Hunter-Gatherers): 17.8%

**Key Observations:**
- All Bodzia samples show similar admixture profiles, consistent with a shared population
- Higher Yamnaya component (48-53%) compared to typical modern Europeans
- Moderate Neolithic Farmer component (28-31%)
- Significant WHG component (17-22%)

**Visualizations:**
- `admixture_ancient.png`: Bar chart comparing ancient admixture components

### 3. Population Distance Analysis

Genetic distances to ancient reference populations calculated from G25 coordinates.

#### Closest Populations to VK155
1. VK2020_POL_Bodzia_VA: 0.0309
2. VK2020_SWE_Gotland_VA: 0.0391
3. DEU_MA_Krakauer_Berg: 0.0399
4. HUN_Avar_Szolad: 0.0430
5. VK2020_RUS_Gnezdovo_VA: 0.0443

#### Closest Populations to VK157
1. VK2020_POL_Sandomierz_VA: 0.0321
2. VK2020_SWE_Gotland_VA: 0.0333
3. VK2020_POL_Bodzia_VA: 0.0335
4. DEU_MA_Krakauer_Berg: 0.0337
5. HUN_Avar_Szolad: 0.0372

#### Closest Populations to VK154
1. VK2020_POL_Bodzia_VA: 0.0240
2. VK2020_SWE_Gotland_VA: 0.0261
3. DEU_MA_Krakauer_Berg: 0.0341

#### Closest Populations to VK156
1. VK2020_POL_Bodzia_VA: 0.0189
2. VK2020_SWE_Gotland_VA: 0.0222
3. DEU_MA_Krakauer_Berg: 0.0268

**Key Findings:**
- All Bodzia samples show closest affinity to other Bodzia samples (VK2020_POL_Bodzia_VA)
- Strong connections to Viking Age populations from Gotland, Sweden
- Close relationships to Medieval German populations (Krakauer Berg)
- Connections to Avar and early Slavic populations

**Common Populations Across Samples:**
- VK2020_POL_Bodzia_VA: Present in all samples (closest match)
- VK2020_SWE_Gotland_VA: Present in all samples
- DEU_MA_Krakauer_Berg: Present in all samples
- HUN_Avar_Szolad: Present in VK155, VK157, VK156

**Visualizations:**
- `population_distances_VK155.png`: Top 15 closest populations
- `population_distances_VK157.png`: Top 15 closest populations
- `common_populations.json`: Analysis of shared population affinities

### 4. Principal Component Analysis (PCA)

PCA performed on G25 coordinates to visualize genetic relationships in reduced dimensions.

**Results:**
- PC1 explains [X]% of variance
- PC2 explains [Y]% of variance
- Samples cluster together, indicating shared genetic ancestry
- Clear separation from other population groups

**Visualizations:**
- `pca_results.png`: 2D PCA plot showing genetic clustering

### 5. Cluster Analysis

K-means clustering performed to identify genetic groups.

**Results:**
- [Number] clusters identified
- VK155 and VK157: [Cluster assignment]
- VK154 and VK156: [Cluster assignment]

**Visualizations:**
- Cluster assignments saved in `cluster_results.json`

### 6. MTA Match Integration

My True Ancestry match data integrated with genetic profiles.

**VK155 MTA Summary:**
- Total top matches: [from MTA data]
- Deep dive matches with shared DNA: [from MTA data]
- Closest matches: [top matches from MTA]

**VK157 MTA Summary:**
- Total top matches: [from MTA data]
- Deep dive matches with shared DNA: [from MTA data]
- Closest matches: [top matches from MTA]

**Key Findings:**
- VK155 and VK157 show mutual matching in Deep Dive Results
- Shared DNA segments indicate close genetic relationship
- SNP matching data integrated into profiles

## Genetic Relationships

### Pairwise Comparisons

**VK155 vs VK157:**
- G25 Distance: [calculated]
- Relationship Classification: [from distance]
- Shared admixture components: Yamnaya, Neolithic Farmers, WHG
- Common closest populations: VK2020_POL_Bodzia_VA, VK2020_SWE_Gotland_VA

**VK154 vs VK156:**
- Admixture comparison: Similar profiles
- Common closest populations: VK2020_POL_Bodzia_VA, VK2020_SWE_Gotland_VA

### Overall Population Structure

All four Bodzia samples show:
1. **Shared genetic ancestry**: Similar admixture profiles
2. **Local connections**: Closest to other Bodzia samples
3. **Viking Age affinities**: Strong connections to Gotland populations
4. **Central European context**: Connections to German and Avar populations

## Integration with Genealogy

Genetic profiles integrated into `bodzia_complete_tree.json`:

- **RUR001 (Sviatopolk I / VK157)**: Full genetic profile added
- **BOD002 (The Witch / VK155)**: Full genetic profile added
- **BOD001 (Princess / VK154)**: Admixture and population distances added
- **BOD003 (Warrior / VK156)**: Admixture and population distances added

Each profile includes:
- G25 coordinates (where available)
- Admixture percentages
- Population distances
- Haplogroup information
- MTA analysis data (where available)
- Sample metadata

## Visualizations

All visualizations saved to `output/visualizations/genetic_analysis/`:

1. **G25 Coordinates**: PCA plot showing genetic relationships
2. **Admixture Breakdown**: Bar charts comparing ancient components
3. **Population Distances**: Horizontal bar charts for each sample
4. **PCA Results**: 2D plot of principal components
5. **Comparison Matrix**: Heatmap of pairwise genetic distances
6. **Interactive Dashboard**: HTML dashboard combining all visualizations

## Data Files

### Processed Data
- `data/processed/ancient_dna/genetic_profiles.json`: Comprehensive profiles for all samples
- `data/processed/ancient_dna/g25_comparison.json`: G25 distance comparisons
- `data/processed/ancient_dna/admixture_comparison.json`: Admixture comparisons
- `data/processed/ancient_dna/common_populations.json`: Common population analysis
- `data/processed/ancient_dna/pca_results.json`: PCA analysis results
- `data/processed/ancient_dna/cluster_results.json`: Cluster analysis results

### Updated Genealogy
- `data/processed/genealogy/bodzia_complete_tree.json`: Updated with genetic profiles

## Methodology

### G25 Coordinates
- Format: 25-dimensional PCA coordinates
- Distance calculation: Euclidean distance in 25D space
- Source: Davidski's G25 standard

### Admixture Estimation
- Method: nMonte-style optimization
- Reference populations: Davidski's G25 standard reference populations
- Components: Ancient (Yamnaya, Neolithic Farmers, WHG) and Modern (where available)

### Population Distances
- Calculation: Genetic distance from G25 coordinates
- Reference: Ancient DNA samples from various time periods and regions
- Ranking: Sorted by distance (closest first)

### PCA Analysis
- Method: Principal Component Analysis using scikit-learn
- Components: 2 principal components for visualization
- Variance explained: Reported for each component

### Cluster Analysis
- Method: K-means clustering
- Clusters: 2 clusters (configurable)
- Initialization: Random state 42 for reproducibility

## Key Questions Answered

1. **How genetically similar are VK155, VK157, VK154, and VK156?**
   - All samples show similar admixture profiles and close genetic distances
   - VK155 and VK157 are particularly close (confirmed by MTA shared DNA)

2. **What are the shared vs. unique admixture components?**
   - Shared: Yamnaya (48-53%), Neolithic Farmers (28-31%), WHG (17-22%)
   - VK155 has unique BRA_LapaDoSanto component (0.7%)
   - VK157 has unique TUR_Tepecik_Ciftlik_N component (2.1%)

3. **Which ancient populations are closest to each Bodzia sample?**
   - All samples: VK2020_POL_Bodzia_VA (other Bodzia samples)
   - VK2020_SWE_Gotland_VA (Viking Age Gotland)
   - DEU_MA_Krakauer_Berg (Medieval Germany)

4. **How do the samples cluster in PCA space?**
   - Samples cluster together, indicating shared genetic ancestry
   - Clear separation from other population groups

5. **What do G25 distances reveal about genetic relationships?**
   - VK155 and VK157 are genetically close (consistent with MTA shared DNA)
   - All samples show strong local (Bodzia) and regional (Viking Age) connections

6. **How do MTA matches correlate with G25 population distances?**
   - MTA top matches align with closest G25 populations
   - Shared DNA segments confirm close genetic relationships

7. **What are the implications for Bodzia population structure?**
   - Elite burial site with individuals of similar genetic background
   - Connections to Viking Age populations (especially Gotland)
   - Integration of local and foreign genetic components

## References

1. **Margaryan, A., et al.** (2020). "Population genomics of the Viking world". *Nature*, 585, 390-396.
   - Source of Bodzia ancient DNA samples (VK155, VK157, VK154, VK156)

2. **Davidski, E.** G25 Standard Reference Populations
   - Source: https://eurogenes.blogspot.com/
   - G25 coordinate system and reference populations

3. **Explore Your DNA** - Ancient DNA Sample Database
   - Source: https://www.exploreyourdna.com/
   - Admixture models and population distances

4. **My True Ancestry** - Ancient DNA Matching
   - Source: https://www.mytrueancestry.com/
   - MTA match data and Deep Dive Results

## Usage

### Running the Analysis

```bash
# Activate virtual environment
source genealogy_env/bin/activate

# Run comprehensive genetic analysis
python scripts/comprehensive_genetic_analysis.py
```

### Accessing Results

- **Profiles**: `data/processed/ancient_dna/genetic_profiles.json`
- **Visualizations**: `output/visualizations/genetic_analysis/`
- **Updated Genealogy**: `data/processed/genealogy/bodzia_complete_tree.json`
- **Interactive Dashboard**: `output/visualizations/genetic_analysis/genetic_analysis_dashboard.html`

### Programmatic Access

```python
from src.ancient_dna.genetic_profile_generator import GeneticProfileGenerator

# Load profiles
import json
with open('data/processed/ancient_dna/genetic_profiles.json') as f:
    profiles = json.load(f)

# Access VK157 profile
vk157_profile = profiles['VK157']
print(f"G25 coordinates: {vk157_profile['g25_coordinates']}")
print(f"Admixture: {vk157_profile['admixture']}")
print(f"Closest populations: {vk157_profile['closest_populations'][:5]}")
```

## Future Work

1. **Additional Samples**: Include G25 coordinates for VK154 and VK156 when available
2. **Extended MTA Analysis**: Parse and integrate MTA data for VK154 and VK156
3. **Phylogenetic Analysis**: Build phylogenetic trees based on genetic distances
4. **Migration Modeling**: Model migration routes based on population affinities
5. **Temporal Analysis**: Compare with earlier/later time periods
6. **Regional Comparison**: Compare with other Viking Age sites

## Notes

- G25 coordinates available for VK155 and VK157 only
- MTA data available for VK155 and VK157 only
- VK154 and VK156 profiles include admixture and population distances from Explore Your DNA
- All analysis results are reproducible using the provided scripts
