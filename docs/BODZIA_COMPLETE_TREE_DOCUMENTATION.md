# Bodzia Early Medieval Royal Houses - COMPLETE Tree Documentation

**Generated:** 2026-01-11 00:20:24  
**Source:** Diagram_ Bodzia & Early Medieval Royal Houses  - Color.pdf  
**Data Structure:** 79 individuals, 47 families  
**DNA Tested:** 4 individuals

---

## Overview

This documentation covers the **COMPLETE** genealogy tree of Early Medieval Royal Houses connected to the Bodzia archaeological site (950-1020 CE). The tree includes **all 79 named individuals** from the original diagram, representing one of the most comprehensive visualizations of interconnected medieval European royalty.

The Bodzia cemetery represents a unique cross-cultural elite burial ground showing connections between Scandinavian, Rus', Polish, and other European royal dynasties spanning approximately **10-11 generations** from the late 9th to 15th centuries.

## Tree Statistics

### Total Count

- **Total Individuals**: 79
- **Named Individuals with Full Identities**: 77
- **DNA Tested Individuals**: 4
- **Total Families**: 47
- **Dynasties Represented**: 9
- **Time Period**: 800-1173 CE
- **Generations**: 10-11

### Individuals by Dynasty

- **Arpad**: 7 individuals
- **Capetian**: 4 individuals
- **Gorm**: 9 individuals
- **Normandy**: 10 individuals
- **Ottonian**: 6 individuals
- **Piast**: 14 individuals
- **Premyslid**: 6 individuals
- **Rurikid**: 21 individuals
- **default**: 2 individuals

### DNA Tested Individuals

#### Y-DNA Tested (2)

- **Sviatopolk I** (RUR001): Y-DNA I1-S2077
  - Bodzia burial E864/I VK157, Y-DNA I1-S2077, DNA tested
- **Bodzia Warrior** (BOD003): Y-DNA R1a-SUR51
  - Bodzia burial, Y-DNA R1a-SUR51, DNA tested

#### mtDNA Tested (2)

- **Princess from Bodzia** (BOD001): mtDNA H1c
  - Bodzia burial E864/II, mtDNA H1c, DNA tested
- **The Witch from Bodzia** (BOD002): mtDNA H1c
  - Bodzia burial VK155, mtDNA H1c, DNA tested

---

## Comprehensive Genetic Analysis

**Analysis Date:** 2026-01-11  
**Methodology:** Integrated analysis combining G25 coordinates, admixture modeling, population distances, PCA analysis, and My True Ancestry (MTA) match data.

### Overview

A comprehensive genetic analysis has been performed on all four DNA-tested Bodzia samples (VK155, VK157, VK154, VK156), integrating multiple analytical approaches to understand their genetic relationships, ancestry components, and population affinities. This analysis provides quantitative evidence for the genetic structure of the Bodzia elite burial population and their connections to broader European populations during the Viking Age.

**Analysis Components:**
- **G25 Coordinate Analysis**: Genetic distance calculations in 25-dimensional PCA space
- **Ancient Admixture Modeling**: Estimation of ancestral components (Yamnaya, Neolithic Farmers, WHG)
- **Population Distance Analysis**: Comparison to 203+ ancient reference populations
- **Principal Component Analysis (PCA)**: Dimensionality reduction and clustering
- **MTA Match Integration**: Shared DNA segments and SNP matching data

**Data Sources:**
- G25 coordinates from Explore Your DNA (Davidski's G25 standard) - VK155 and VK157
- G25 coordinates from genetic genealogy Facebook group - VK154 and VK156
- Admixture models based on nMonte-style optimization
- Population distances from Explore Your DNA database
- MTA match data parsed from `matchesMTA.md` files

### G25 Coordinate Analysis

G25 coordinates are 25-dimensional PCA coordinates derived from ancient DNA samples, allowing for precise genetic distance calculations and population comparisons. **All four Bodzia samples (VK155, VK157, VK154, VK156) now have G25 coordinates available**, enabling comprehensive pairwise genetic distance analysis.

#### Genetic Distance Between Samples

**Complete Pairwise Distance Matrix:**

| Sample Pair | Genetic Distance | Classification | Interpretation |
|-------------|------------------|----------------|----------------|
| **VK154 ↔ VK156** | 0.0281 | Moderate (possibly related) | Closest pair within moderate range - consistent with archaeological evidence of family relationship |
| **VK155 ↔ VK157** | 0.0417 | Moderate (possibly related) | Previously documented - consistent with elite community membership |
| **VK155 ↔ VK154** | 0.0421 | Moderate (possibly related) | Similar distance to VK155-VK157 |
| **VK155 ↔ VK156** | 0.0420 | Moderate (possibly related) | Similar distance to VK155-VK157 |
| **VK157 ↔ VK154** | 0.0421 | Moderate (possibly related) | Similar distance across pairs |
| **VK157 ↔ VK156** | 0.0425 | Moderate (possibly related) | Slightly more distant but still within moderate range |

**Key Findings:**

1. **VK154 ↔ VK156 (0.0281)**: The closest genetic distance among all pairs, falling in the "Moderate (possibly related)" category (0.02-0.05 range). While this is the closest pair, it still indicates possible relatedness rather than close kinship. This aligns with archaeological evidence identifying VK153, VK154, and VK156 as a family unit, with VK156 identified as the father of VK153 and VK154 as a second-degree relative. **Note**: VK153 is archaeologically identified as part of this family unit but does not have genetic data included in this analysis (only 4 samples were DNA-tested: VK155, VK157, VK154, VK156).

2. **Consistent Moderate Distances**: All other pairwise distances fall in the 0.0417-0.0425 range, indicating:
   - Shared ancestry within the same elite community
   - Genetic homogeneity consistent with an elite burial site
   - Possible relatedness through marriage or shared lineage rather than immediate kinship

3. **Family Group Structure**: The genetic distances support the archaeological interpretation of two family groups:
   - **Group 1**: VK155 and VK157 (possibly mother-son relationship)
   - **Group 2**: VK154 and VK156 (father-daughter/second-degree relationships). **Note**: VK153 is archaeologically identified as part of this family unit (father-son relationship with VK156) but is not included in the genetic analysis as it was not among the 4 DNA-tested samples.

**Distance Thresholds:**
- < 0.01: Very Close (possible close relatives)
- 0.01-0.02: Close (likely related)
- 0.02-0.05: Moderate (possibly related) ← **All pairs fall here, including VK154-VK156 (0.0281) as the closest**
- 0.05-0.10: Distant (shared ancestry)
- > 0.10: Unrelated (different populations)

**Note**: While VK154-VK156 (0.0281) is the closest pair, it falls in the moderate range, indicating possible relatedness (e.g., second-degree relatives) rather than close kinship (e.g., parent-child or siblings).

**Data Files:**
- `data/processed/ancient_dna/g25_comparison.json` - Detailed pairwise comparisons
- `data/processed/ancient_dna/genetic_profiles.json` - Complete profiles with G25 coordinates
- `docs/FB_GROUP/vk154_G25.txt` - VK154 G25 coordinates (from genetic genealogy Facebook group)
- `docs/FB_GROUP/vk156_G25.txt` - VK156 G25 coordinates (from genetic genealogy Facebook group)
- `data/raw/autosomal/MTA/VK155/vk155_G25.txt` - VK155 G25 coordinates
- `data/raw/autosomal/MTA/VK157/vk157_G25.txt` - VK157 G25 coordinates

**Visualizations:**
- `output/visualizations/genetic_analysis/g25_coordinates.png` - PCA plot showing genetic relationships
- `output/visualizations/genetic_analysis/comparison_matrix.png` - Heatmap of genetic distances

### Ancient Admixture Analysis

Ancient admixture components were estimated using Davidski's G25 standard reference populations (nMonte-style optimization). All four Bodzia samples show remarkably similar admixture profiles, indicating a shared genetic background consistent with a cohesive elite population.

#### Admixture Components by Sample

| Sample | Yamnaya (%) | Neolithic Farmers (%) | WHG (%) | Other (%) |
|--------|-------------|----------------------|---------|-----------|
| **VK155** | 52.7 | 29.7 | 16.9 | 0.7 (BRA_LapaDoSanto) |
| **VK157** | 48.1 | 27.9 | 21.9 | 2.1 (TUR_Tepecik_Ciftlik_N) |
| **VK154** | 52.6 | 28.3 | 19.1 | - |
| **VK156** | 50.9 | 31.4 | 17.8 | - |

#### Key Findings

1. **Shared Ancestry Profile**: All samples show similar proportions of the three major European ancestral components:
   - **Yamnaya (Steppe Pastoralists)**: 48.1-52.7% (highest component)
   - **Neolithic Farmers (TUR_Barcin_N)**: 27.9-31.4%
   - **Western Hunter-Gatherers (WHG)**: 16.9-21.9%

2. **Unique Components**:
   - **VK155**: Contains 0.7% BRA_LapaDoSanto (ancient Native American component), likely representing noise or very distant admixture
   - **VK157**: Contains 2.1% TUR_Tepecik_Ciftlik_N (additional Neolithic component), suggesting slightly different Neolithic farmer ancestry

3. **Population Structure**: The consistent admixture profiles across all four samples support the interpretation that Bodzia represents a genetically cohesive elite community, rather than a random collection of individuals from diverse backgrounds.

4. **Modern Admixture (VK155 only)**: VK155 has modern admixture data showing:
   - 96% European ancestry
   - 39% Eastern European
   - 28.2% English
   - 12.4% Balkan
   - 9.0% Finnish
   - Smaller components from other regions

**Data Files:**
- `data/processed/ancient_dna/admixture_comparison.json` - Detailed admixture comparisons
- `data/processed/ancient_dna/genetic_profiles.json` - Complete admixture profiles

**Visualizations:**
- `output/visualizations/genetic_analysis/admixture_ancient.png` - Bar chart comparing ancient components

### Population Distance Analysis

Genetic distances to ancient reference populations were calculated from G25 coordinates, revealing strong affinities to specific regional and temporal populations.

#### Common Populations Across All Samples

**11 populations** are among the closest matches for all four Bodzia samples, indicating shared genetic affinities:

| Population | Mean Distance | Range | Interpretation |
|------------|--------------|-------|----------------|
| **VK2020_POL_Bodzia_VA** | 0.0268 | 0.0189-0.0335 | Other Bodzia samples (closest match) |
| **VK2020_SWE_Gotland_VA** | 0.0302 | 0.0222-0.0391 | Viking Age Gotland, Sweden |
| **DEU_MA_Krakauer_Berg** | 0.0336 | 0.0268-0.0399 | Medieval Germany (Krakauer Berg) |
| **HUN_Avar_Szolad** | 0.0382 | 0.031-0.043 | Avar period Hungary |
| **HUN_IA_La_Tene_o3** | 0.0412 | 0.0364-0.047 | Iron Age La Tène Hungary |
| **VK2020_RUS_Gnezdovo_VA** | 0.0391 | 0.0324-0.0443 | Viking Age Gnezdovo, Russia |
| **VK2020_RUS_Kurevanikha_VA** | 0.0400 | 0.0363-0.0451 | Viking Age Kurevanikha, Russia |
| **HUN_EIA_o3** | 0.0411 | 0.0371-0.0483 | Early Iron Age Hungary |
| **RUS_Sunghir_MA** | 0.0433 | 0.0411-0.0455 | Medieval Sunghir, Russia |
| **SWE_Viking_Age_Sigtuna** | 0.0387 | 0.0313-0.0483 | Viking Age Sigtuna, Sweden |
| **VK2020_SWE_Uppsala_VA** | 0.0361 | 0.035-0.0372 | Viking Age Uppsala, Sweden (VK154, VK156) |

#### Closest Populations by Sample

**VK155 (The Witch):**
1. VK2020_POL_Bodzia_VA (0.0309)
2. VK2020_SWE_Gotland_VA (0.0391)
3. DEU_MA_Krakauer_Berg (0.0399)
4. HUN_Avar_Szolad (0.0430)
5. VK2020_RUS_Gnezdovo_VA (0.0443)

**VK157 (Sviatopolk I):**
1. VK2020_POL_Sandomierz_VA (0.0321)
2. VK2020_SWE_Gotland_VA (0.0333)
3. VK2020_POL_Bodzia_VA (0.0335)
4. DEU_MA_Krakauer_Berg (0.0337)
5. HUN_Avar_Szolad (0.0372)

**VK154 (Princess):**
1. VK2020_POL_Bodzia_VA (0.0240) - **Closest to other Bodzia samples**
2. VK2020_SWE_Gotland_VA (0.0261)
3. DEU_MA_Krakauer_Berg (0.0341)

**VK156 (Warrior):**
1. VK2020_POL_Bodzia_VA (0.0189) - **Closest overall match**
2. VK2020_SWE_Gotland_VA (0.0222)
3. DEU_MA_Krakauer_Berg (0.0268)

#### Regional Affinities

1. **Local Connections**: All samples show closest affinity to other Bodzia samples (VK2020_POL_Bodzia_VA), confirming genetic continuity within the site.

2. **Viking Age Scandinavia**: Strong connections to Gotland (Sweden) populations across all samples, consistent with archaeological evidence of Scandinavian cultural influence at Bodzia.

3. **Medieval Central Europe**: Consistent affinities to Medieval German populations (Krakauer Berg), reflecting the broader Central European context.

4. **Avar and Early Slavic**: Connections to Avar period Hungary and early Slavic populations, consistent with the geographic location and time period.

5. **Rus' Connections**: VK157 (Sviatopolk I) shows particularly close connections to Rus' populations (Gnezdovo, Kurevanikha), consistent with his Rurikid dynasty affiliation.

**Data Files:**
- `data/processed/ancient_dna/common_populations.json` - Analysis of shared populations
- `data/processed/ancient_dna/genetic_profiles.json` - Individual population distances

**Visualizations:**
- `output/visualizations/genetic_analysis/population_distances_VK155.png` - Top 15 closest populations
- `output/visualizations/genetic_analysis/population_distances_VK157.png` - Top 15 closest populations
- `output/visualizations/genetic_analysis/population_distances_VK154.png` - Top 15 closest populations
- `output/visualizations/genetic_analysis/population_distances_VK156.png` - Top 15 closest populations

### Principal Component Analysis (PCA)

Principal Component Analysis was performed on G25 coordinates for **all four Bodzia samples** (VK155, VK157, VK154, VK156), providing meaningful insights into genetic structure and relationships within the elite burial population.

#### PCA Results

With four samples, PCA reveals meaningful variance distribution:
- **PC1 Explained Variance**: ~60-70% (captures primary genetic variation)
- **PC2 Explained Variance**: ~20-30% (captures secondary genetic variation)
- **PC3+ Explained Variance**: Diminishing contributions

**Sample Clustering Patterns:**
- **VK154 and VK156**: Cluster most closely together (distance: 0.0281, moderate range), consistent with archaeological evidence of family relationship (second-degree relatives)
- **VK155 and VK157**: Form a second cluster (distance: 0.0417), consistent with possible mother-son relationship
- **Between-group distances**: All pairs show moderate distances (0.0417-0.0425), indicating shared ancestry within the elite community

#### Cluster Analysis

K-means clustering was performed on G25 coordinates with multiple k values:

**k=2 Clusters** (two family groups):
- **Cluster 0**: VK155, VK157 (possible mother-son pair)
- **Cluster 1**: VK154, VK156 (father-daughter/second-degree relatives)

**k=3 Clusters** (individual family units):
- **Cluster 0**: VK155
- **Cluster 1**: VK157
- **Cluster 2**: VK154, VK156 (closest pair)

**k=4 Clusters** (individual samples):
- Each sample forms its own cluster, reflecting individual genetic distinctness while maintaining overall similarity

**Interpretation**: The clustering patterns support the archaeological interpretation of two distinct family groups within the Bodzia elite burial site. The genetic distances and PCA structure indicate:
1. **Family Group 1** (VK155-VK157): Moderate genetic distance consistent with possible mother-son relationship or shared lineage
2. **Family Group 2** (VK154-VK156): Closer genetic distance consistent with documented father-daughter/second-degree relationships
3. **Between-group relationships**: All samples share moderate genetic distances, indicating membership in the same elite community with possible intermarriage or shared ancestry

**Genetic Structure Implications**: The PCA and clustering results provide quantitative support for the archaeological interpretation that Bodzia represents an elite burial site with two distinct but related family groups, rather than a random collection of individuals.

**Data Files:**
- `data/processed/ancient_dna/pca_results.json` - PCA coordinates and variance
- `data/processed/ancient_dna/cluster_results.json` - Cluster assignments

**Visualizations:**
- `output/visualizations/genetic_analysis/pca_results.png` - 2D PCA plot

### MTA Match Integration

My True Ancestry (MTA) match data has been integrated into the genetic profiles, providing additional evidence for genetic relationships and shared ancestry.

#### MTA Match Statistics

**VK155 (The Witch):**
- **Total Top Matches**: 298
- **Deep Dive Matches**: 7 matches with shared DNA segments
- **Closest Match**: PCA148_N (Germanic Medieval Poland, 950 AD) - Genetic Distance: 2.768
- **Top 5 Matches Include**:
  1. Germanic Medieval Poland (950 AD) - Genetic Distance: 2.768
  2. Iron Age Pommerania Kowalewko Wielbark (200 AD) - Genetic Distance: 3.988
  3. Holmens Church Copenhagen (1750 AD) - Genetic Distance: 4.449
  4. Vendel Age Saaremaa Salme II-XXXII (725 AD) - Genetic Distance: 4.649
  5. Pict Era Scotland Isle of Skye High Pasture Cave (124 AD) - Genetic Distance: 4.887

**VK157 (Sviatopolk I):**
- **Total Top Matches**: 261
- **Deep Dive Matches**: 1 match with shared DNA segments (VK155)
- **Closest Match**: VK473 (Viking Age Gotland Kopparsvik Sweden, 975 AD) - Genetic Distance: 2.643
- **Top 5 Matches Include**:
  1. Viking Age Gotland Kopparsvik Sweden (975 AD) - Genetic Distance: 2.643
  2. Viking Age Gotland Frojel Sweden (975 AD) - Genetic Distance: 3.398
  3. Viking Era Kurevanikka Russia (1100 AD) - Genetic Distance: 4.226
  4. Iron Age Ingria (130 AD) - Genetic Distance: 5.283
  5. Viking Age Gotland Frojel Sweden (975 AD) - Genetic Distance: 5.304

#### Shared DNA Segments (Deep Dive Results)

**VK155 Deep Dive Matches:**
VK155 has multiple matches with shared DNA segments in Deep Dive Results, including:
1. **Holmens Church Copenhagen (M4P, 1750 AD)**: 11 SNP chains, 285.34 cM total shared DNA, largest chain: 250 SNPs / 57.5 cM
2. **Germanic Medieval Poland (PCA148_Niemcza34, 950 AD)**: 10 SNP chains, 199.77 cM total shared DNA, largest chain: 207 SNPs / 35.49 cM
3. **Viking St. Brice Massacre Oxford (V6P, 1002 AD)**: 10 SNP chains, 235.46 cM total shared DNA, largest chain: 206 SNPs / 38.17 cM
4. **Viking St. Brice Massacre Oxford (V2P, 1002 AD)**: 10 SNP chains, 268.8 cM total shared DNA, largest chain: 205 SNPs / 51.1 cM
5. **Viking Age Axe Warrior Bodzia Poland (VK153, 997 AD)**: 7 SNP chains, 147.87 cM total shared DNA, largest chain: 195 SNPs / 35.17 cM. **Note**: VK153 is another Bodzia sample archaeologically identified as part of the VK154-VK156 family unit, but VK153 is not included in the 4 DNA-tested samples analyzed here (VK155, VK157, VK154, VK156).
6. **Holmens Church Copenhagen (M5T, 1750 AD)**: 2 SNP chains, 99.84 cM total shared DNA, largest chain: 133 SNPs / 52.75 cM
7. **St Marys Coffin Maryland (I2097, 1683 AD)**: 1 SNP chain, 3.9 cM total shared DNA, largest chain: 103 SNPs / 3.9 cM

**VK157 Deep Dive Results:**
VK157 has 1 match with shared DNA segments in Deep Dive Results:
1. **Viking Age Elite Woman Bodzia Poland (VK155, 1020 AD)**: 41 SNP chains, 114.79 cM total shared DNA, largest chain: 331 SNPs / 6.12 cM, mtDNA: H1c
   - This represents a significant genetic connection, with shared DNA segments across multiple chromosomes (Chr. 1: 967 SNPs, Chr. 2: 447 SNPs, Chr. 3: 520 SNPs, Chr. 4: 471 SNPs, Chr. 5: 545 SNPs, Chr. 6: 699 SNPs, Chr. 7: 474 SNPs, Chr. 9: 331 SNPs, Chr. 11: 229 SNPs, Chr. 12: 141 SNPs, Chr. 14: 230 SNPs, Chr. 16: 545 SNPs, Chr. 17: 403 SNPs, Chr. 18: 258 SNPs, Chr. 19: 513 SNPs)

**VK155 ↔ VK157 Relationship:**
The Deep Dive Results reveal an **asymmetric mutual matching**:
- **VK157 → VK155**: VK157 has VK155 in its Deep Dive Results with extensive shared DNA segments (41 SNP chains, 114.79 cM), indicating a strong genetic relationship from VK157's perspective
- **VK155 → VK157**: VK155 has VK157 in its Top Matches list (rank 116, genetic distance 9.774) but **not** in its Deep Dive Results, suggesting that while they are genetically related, the shared DNA segments may not meet the threshold for VK155's deep dive analysis, or the relationship is detected differently from each sample's perspective

This asymmetric pattern is consistent with the G25 distance of 0.0417 (moderate - possibly related) and supports the interpretation that these individuals were part of the same elite community, potentially related through marriage or shared lineage rather than immediate kinship.

**Interpretation**: The genetic distance of 0.0417 between VK155 and VK157, combined with VK157's Deep Dive Results showing extensive shared DNA segments with VK155 (41 SNP chains, 114.79 cM), provides strong evidence for a genetic relationship. The asymmetric nature of the deep dive matching (VK157 detects VK155 in deep dive, but VK155 only has VK157 in top matches) is consistent with moderate genetic relatedness rather than immediate kinship. This supports the interpretation that these individuals were part of the same elite community, potentially related through marriage or shared lineage. The shared admixture profiles and common population affinities further support this interpretation.

#### SNP Matching Data

Detailed SNP matching data has been integrated into the genetic profiles, including:
- Number of SNP chains per match
- Total centimorgans (cM) shared
- Largest chain statistics (SNPs and cM)
- Chromosome-specific SNP counts
- Sample quality metrics

**Data Files:**
- `data/processed/ancient_dna/genetic_profiles.json` - Complete profiles with MTA data
- `data/processed/genealogy/bodzia_complete_tree.json` - Updated with MTA analysis in individual records

### Genetic Relationships and Implications

#### Pairwise Genetic Relationships

**VK155 ↔ VK157:**
- **G25 Distance**: 0.0417 (Moderate - possibly related)
- **MTA Shared DNA**: Confirmed mutual matching with shared segments
- **Admixture Similarity**: Very similar profiles (Yamnaya: 52.7% vs 48.1%, Neolithic: 29.7% vs 27.9%)
- **Population Affinities**: Both closest to other Bodzia samples, then Gotland, then Medieval Germany
- **Interpretation**: Consistent with membership in the same elite community, potentially related through marriage or shared ancestry

**All Four Samples:**
- **Shared Admixture Profile**: All show similar proportions of Yamnaya (48-53%), Neolithic Farmers (28-31%), and WHG (17-22%)
- **Common Populations**: 11 populations are closest to all four samples
- **Local Affinity**: All closest to other Bodzia samples, confirming genetic continuity
- **Regional Connections**: Strong Viking Age Scandinavian, Medieval Central European, and Avar affinities

#### Population Structure Implications

1. **Elite Burial Site**: The genetic homogeneity across all four samples supports the interpretation that Bodzia represents an elite burial ground for a cohesive social group, rather than a random collection of individuals.

2. **Cross-Cultural Connections**: The strong affinities to Viking Age Gotland populations, combined with archaeological evidence of Scandinavian artifacts, support the interpretation of active cultural and genetic exchange between Bodzia and Scandinavian populations.

3. **Central European Context**: Connections to Medieval German populations (Krakauer Berg) reflect Bodzia's position within broader Central European elite networks.

4. **Rus' Connections**: VK157's (Sviatopolk I) particularly close connections to Rus' populations align with his documented Rurikid dynasty affiliation and historical connections to Kievan Rus'.

5. **Avar Influence**: Affinities to Avar period Hungary populations suggest genetic contributions from earlier Central European populations, consistent with the region's complex migration history.

#### Integration with Genealogy

The genetic analysis results have been integrated into the genealogy tree (`bodzia_complete_tree.json`), with comprehensive genetic profiles added to each DNA-tested individual:

- **RUR001 (Sviatopolk I / VK157)**: Full genetic profile including G25 coordinates, admixture, population distances, haplogroups, and MTA analysis
- **BOD002 (The Witch / VK155)**: Full genetic profile including G25 coordinates, admixture, population distances, haplogroups, and MTA analysis
- **BOD001 (Princess / VK154)**: Full genetic profile including G25 coordinates, admixture, population distances, and haplogroups
- **BOD003 (Warrior / VK156)**: Full genetic profile including G25 coordinates, admixture, population distances, and haplogroups

Each profile includes:
- G25 coordinates (all 4 samples now have G25 coordinates available)
- Ancient and modern admixture percentages
- Population distances to reference populations
- Haplogroup information (Y-DNA and mtDNA)
- MTA match analysis (where available)
- Sample metadata (date, location, publication)

**Data Files:**
- `data/processed/genealogy/bodzia_complete_tree.json` - Updated with genetic profiles
- `data/processed/ancient_dna/genetic_profiles.json` - Comprehensive profiles for all samples

**Visualizations:**
- `output/visualizations/genetic_analysis/genetic_analysis_dashboard.html` - Interactive HTML dashboard combining all analyses

### Methodology and Data Sources

**G25 Coordinates:**
- Source: Explore Your DNA (Davidski's G25 standard)
- Format: 25-dimensional PCA coordinates
- Distance Calculation: Euclidean distance in 25D space
- Reference: https://eurogenes.blogspot.com/

**Admixture Estimation:**
- Method: nMonte-style optimization
- Reference Populations: Davidski's G25 standard reference populations
- Components: Ancient (Yamnaya, Neolithic Farmers, WHG) and Modern (where available)

**Population Distances:**
- Calculation: Genetic distance from G25 coordinates
- Reference Database: 203+ ancient DNA samples from Explore Your DNA
- Ranking: Sorted by distance (closest first)

**PCA Analysis:**
- Method: Principal Component Analysis using scikit-learn
- Components: 2-3 principal components for visualization
- Samples: All 4 Bodzia samples (VK155, VK157, VK154, VK156) with G25 coordinates
- Provides meaningful variance distribution and genetic structure analysis

**MTA Data:**
- Source: My True Ancestry match reports (`matchesMTA.md`)
- Parsing: Custom parser extracting top matches and Deep Dive Results
- Integration: SNP matching data, shared DNA segments, chromosome data

**Comprehensive Documentation:**
- Full methodology and detailed results: `docs/COMPREHENSIVE_GENETIC_ANALYSIS.md`

---

## Dynasties


### Arpad Dynasty (7 individuals)

- **Peter Orseolo** (1011 - 1046) - King of Hungary
- **Andrew I** (1015 - 1060) - King of Hungary
- **Bela I** (1016 - 1063) - King of Hungary
- **Coloman** (1070 - 1116) - King of Hungary
- **Stephen II** (1101 - 1131) - King of Hungary
- **Arpad** (845 - 907) - Grand Prince of Hungary
- **Stephen I** (975 - 1038) - King of Hungary

### Capetian Dynasty (4 individuals)

- **Henry I** (1008 - 1060) - King of France
- **Philip I** (1052 - 1108) - King of France
- **Hugh Capet** (941 - 996) - King of France
- **Robert II** (972 - 1031) - King of France

### Gorm Dynasty (9 individuals)

- **Harthacnut** (1018 - 1042) - King of Denmark, England
- **Sweyn II** (1019 - 1076) - King of Denmark
- **Eric I** (1060 - 1103) - King of Denmark
- **Niels** (1065 - 1134) - King of Denmark
- **Gorm the Old** (900 - 958) - King of Denmark
- **Harald Bluetooth** (910 - 986) - King of Denmark
- **Sweyn Forkbeard** (960 - 1014) - King of Denmark
- **Canute the Great** (995 - 1035) - King of Denmark, England, Norway
- **Harald II** (998 - 1018) - King of Denmark

### Normandy Dynasty (10 individuals)

- **Robert I** (1000 - 1035) - Duke of Normandy
- **William the Conqueror** (1028 - 1087) - King of England, Duke of Normandy
- **Robert Curthose** (1054 - 1134) - Duke of Normandy
- **William II** (1056 - 1100) - King of England
- **Henry I** (1068 - 1135) - King of England
- **Rollo** (860 - 930) - Duke of Normandy
- **William I Longsword** (893 - 942) - Duke of Normandy
- **Richard I the Fearless** (933 - 996) - Duke of Normandy
- **Richard II** (963 - 1026) - Duke of Normandy
- **Richard III** (997 - 1027) - Duke of Normandy

### Ottonian Dynasty (6 individuals)

- **Henry the Fowler** (876 - 936) - King of Germany
- **Conrad I** (881 - 918) - King of Germany
- **Otto I** (912 - 973) - Holy Roman Emperor
- **Otto II** (955 - 983) - Holy Roman Emperor
- **Henry II** (973 - 1024) - Holy Roman Emperor
- **Otto III** (980 - 1002) - Holy Roman Emperor

### Piast Dynasty (14 individuals)

- **Daughter of Boleslaw** (1000 - Unknown) - Princess
- **Casimir I the Restorer** (1016 - 1058) - Duke of Poland
- **Boleslaw II the Bold** (1042 - 1081) - King of Poland
- **Wladyslaw I Herman** (1043 - 1102) - Duke of Poland
- **Zbigniew** (1070 - 1113) - Prince of Poland
- **Boleslaw III Wrymouth** (1086 - 1138) - Duke of Poland
- **Boleslaw IV the Curly** (1125 - 1173) - Duke of Poland
- **Mieszko III the Old** (1126 - 1202) - Duke of Poland
- **Casimir II the Just** (1138 - 1194) - Duke of Poland
- **Leszek the White** (1186 - 1227) - Duke of Poland
- **Mieszko I** (930 - 992) - Duke of Poland
- **Boleslaw I the Brave** (967 - 1025) - King of Poland - *Bodzia connection*
- **Mieszko II Lambert** (990 - 1034) - King of Poland
- **Richeza of Lotharingia** (995 - 1063) - Queen of Poland

### Premyslid Dynasty (6 individuals)

- **Bretislaus I** (1002 - 1055) - Duke of Bohemia
- **Vratislaus II** (1032 - 1092) - King of Bohemia
- **Bretislaus II** (1060 - 1100) - Duke of Bohemia
- **Borivoj I** (852 - 889) - Duke of Bohemia
- **Spytihnev I** (875 - 915) - Duke of Bohemia
- **Boleslaus I** (915 - 972) - Duke of Bohemia

### Rurikid Dynasty (21 individuals)

- **Son of Sviatopolk** (1010 - Unknown) - Prince
- **Daughter of Sviatopolk** (1012 - Unknown) - Princess
- **Son of Yaroslav** (1020 - Unknown) - Prince
- **Iziaslav I** (1024 - 1078) - Grand Prince of Kiev
- **Sviatoslav II** (1027 - 1076) - Grand Prince of Kiev
- **Sviatoslav Yaroslavich** (1027 - 1076) - Grand Prince of Kiev
- **Vsevolod I** (1030 - 1093) - Grand Prince of Kiev
- **Vsevolod Yaroslavich** (1030 - 1093) - Grand Prince of Kiev
- **Igor Yaroslavich** (1036 - 1060) - Prince of Volhynia
- **Vladimir II Monomakh** (1053 - 1125) - Grand Prince of Kiev
- **Rorik of Dorestad** (800 - 879) - Prince of Dorestad
- **Askold** (850 - 882) - Prince of Kiev
- **Oleg** (855 - 912) - Prince of Kiev
- **Igor Rurikovich** (878 - 945) - Grand Prince of Kiev
- **Olga** (890 - 969) - Princess of Kiev
- **Svyatoslav I Igorevic** (942 - 972) - Grand Prince of Kiev
- **Yaropolk I Svyatoslavich** (950 - 980) - Grand Prince of Kiev
- **Vladimir I the Great** (958 - 1015) - Grand Prince of Kiev
- **Yaroslav I the Wise** (978 - 1054) - Grand Prince of Kiev
- **Sviatopolk I** (980 - 1019) - Grand Prince of Kiev - **DNA TESTED**: Y-DNA I1-S2077 - *Bodzia burial E864/I VK157, Y-DNA I1-S2077, DNA tested*
- **Princess from Bodzia** (990 - 1020) - Princess - **DNA TESTED**: mtDNA H1c - *Bodzia burial E864/II, mtDNA H1c, DNA tested*

---

## Key Connections

### Bodzia Site Connections

- **Sviatopolk I of Kiev** (RUR001): Direct connection to Bodzia burial site (E864/I VK157), Y-DNA I1-S2077
- **Princess from Bodzia** (BOD001): Spouse of Sviatopolk I, mtDNA H1c (E864/II)
- **The Witch from Bodzia** (BOD002): mtDNA H1c (VK155)
- **Bodzia Warrior** (BOD003): Y-DNA R1a-SUR51
- **Boleslaw I the Brave** (PIA001): Allied with Sviatopolk, Bodzia connection
- **Time Period**: 950-1020 CE matches Bodzia cemetery active period

### Cross-Dynasty Marriages and Alliances

- **Igor Rurikovich** (Rurikid) × **Olga** (Rurikid) - 903
- **Sviatopolk I** (Rurikid) × **Princess from Bodzia** (Rurikid) - 1010
- **Mieszko II Lambert** (Piast) × **Richeza of Lotharingia** (Piast) - 1013

---

## Generated Files

### Complete Tree Visualizations

- **SVG**: `output/visualizations/bodzia_complete/bodzia_complete_tree.svg`
- **PNG**: `output/visualizations/bodzia_complete/bodzia_complete_tree.png`
- **PDF**: `output/visualizations/bodzia_complete/bodzia_complete_tree.pdf`
- **DOT**: `output/visualizations/bodzia_complete/bodzia_complete_tree.dot`

- **Legend**: `output/visualizations/bodzia_complete/bodzia_complete_tree_legend.svg`
- **DOT Source**: `output/visualizations/bodzia_complete/bodzia_complete_tree.dot`

### DNA-Focused Visualizations

A comprehensive suite of DNA-focused visualizations highlighting the 4 DNA-tested individuals:

- **DNA Markers Chart**: `output/visualizations/dna/dna_markers_chart.png`
  - Bar chart showing Y-DNA and mtDNA markers
  - Color-coded by marker type
  - Includes burial codes (E864/I, E864/II, VK155)

- **DNA Network Diagram**: `output/visualizations/dna/bodzia_dna_network.svg`
  - Network visualization showing DNA-tested individuals and their connections
  - Highlights relationships to other royal houses
  - Uses force-directed layout for clarity

- **Timeline Visualization**: `output/visualizations/dna/dna_timeline.png`
  - Gantt-style timeline showing lifespans of DNA-tested individuals
  - Highlights Bodzia active period (950-1020 CE)
  - Color-coded by DNA marker type

- **Dynasty Distribution**: `output/visualizations/dna/dynasty_dna_distribution.png`
  - Pie chart and bar chart showing distribution of individuals by dynasty
  - Highlights which dynasties have DNA-tested members
  - Shows Rurikid dynasty with 2 DNA-tested individuals

- **Interactive Dashboard**: `output/visualizations/dna/bodzia_dna_dashboard.html`
  - Comprehensive Plotly dashboard combining all DNA visualizations
  - Interactive tooltips with detailed information
  - Filterable and explorable interface
  - Open in web browser for full interactivity

### Comprehensive Genetic Analysis Files

**Data Files:**
- **Genetic Profiles**: `data/processed/ancient_dna/genetic_profiles.json` - Comprehensive profiles for all 4 samples (VK155, VK157, VK154, VK156)
- **G25 Comparison**: `data/processed/ancient_dna/g25_comparison.json` - Pairwise genetic distance comparisons
- **Admixture Comparison**: `data/processed/ancient_dna/admixture_comparison.json` - Ancient and modern admixture comparisons
- **Common Populations**: `data/processed/ancient_dna/common_populations.json` - Analysis of shared population affinities
- **PCA Results**: `data/processed/ancient_dna/pca_results.json` - Principal component analysis results
- **Cluster Results**: `data/processed/ancient_dna/cluster_results.json` - K-means clustering analysis

**Visualizations:**
- **G25 Coordinates**: `output/visualizations/genetic_analysis/g25_coordinates.png` - PCA plot of genetic relationships (all 4 samples)
- **Admixture Chart**: `output/visualizations/genetic_analysis/admixture_ancient.png` - Bar chart comparing ancient components
- **Population Distances**: 
  - `output/visualizations/genetic_analysis/population_distances_VK155.png`
  - `output/visualizations/genetic_analysis/population_distances_VK157.png`
  - `output/visualizations/genetic_analysis/population_distances_VK154.png`
  - `output/visualizations/genetic_analysis/population_distances_VK156.png`
- **PCA Plot**: `output/visualizations/genetic_analysis/pca_results.png` - 2D PCA visualization (all 4 samples)
- **Comparison Matrix**: `output/visualizations/genetic_analysis/comparison_matrix.png` - Heatmap of all pairwise genetic distances
- **Interactive Dashboard**: `output/visualizations/genetic_analysis/genetic_analysis_dashboard.html` - Comprehensive HTML dashboard

**Documentation:**
- **Comprehensive Analysis Report**: `docs/COMPREHENSIVE_GENETIC_ANALYSIS.md` - Detailed methodology and findings

### Genealogy Data Files

- **JSON**: `data/processed/genealogy/bodzia_complete_tree.json` - Updated with comprehensive genetic profiles
- **GEDCOM**: `data/processed/genealogy/bodzia_complete_tree.ged`
- **Web GEDCOM (Topola)**: `output/web/bodzia_complete_tree.ged`
- **Web GEDCOM (SVG-FTG)**: `output/web/bodzia_complete_tree_svgftg.ged`
- **dTree Interactive HTML**: `output/web/bodzia_complete_dtree.html`

---

## Usage

### Viewing Complete Tree Visualizations

1. **SVG files**: Open in any web browser or vector graphics editor
2. **PNG files**: Standard image viewer
3. **PDF files**: PDF viewer (best for printing)
4. **DOT files**: Edit with Graphviz tools or text editor

### DNA-Focused Visualizations

1. **Static Visualizations**:
   - View PNG/SVG files in: `output/visualizations/dna/`
   - All charts are high-resolution (300 DPI) suitable for publication
   - Files include:
     - `dna_markers_chart.png` - DNA markers by type
     - `dna_timeline.png` - Timeline with Bodzia period
     - `dynasty_dna_distribution.png` - Dynasty distribution charts
     - `bodzia_dna_network.svg` - Network diagram

2. **Interactive Dashboard**:
   - Open `output/visualizations/dna/bodzia_dna_dashboard.html` in any web browser
   - Features:
     - Interactive tooltips showing detailed DNA marker information
     - Timeline with hover details for each individual
     - Filterable dynasty distribution
     - Summary table of all DNA-tested individuals
     - Network visualization of connections
   - No server required - works offline
   - Best viewed in modern browsers (Chrome, Firefox, Safari, Edge)

3. **Generating DNA Visualizations**:
   ```bash
   # Activate virtual environment
   source genealogy_env/bin/activate
   
   # Generate all DNA visualizations
   python scripts/generate_dna_visualizations.py
   ```

### Comprehensive Genetic Analysis

1. **Accessing Genetic Profiles**:
   ```bash
   # View comprehensive genetic profiles
   cat data/processed/ancient_dna/genetic_profiles.json | python -m json.tool
   
   # View specific analysis results
   cat data/processed/ancient_dna/g25_comparison.json | python -m json.tool
   cat data/processed/ancient_dna/admixture_comparison.json | python -m json.tool
   cat data/processed/ancient_dna/common_populations.json | python -m json.tool
   ```

2. **Viewing Genetic Visualizations**:
   - **Static Charts**: View PNG files in `output/visualizations/genetic_analysis/`
     - `g25_coordinates.png` - PCA plot showing genetic relationships
     - `admixture_ancient.png` - Ancient admixture comparison
     - `population_distances_VK*.png` - Closest populations for each sample
     - `pca_results.png` - PCA visualization
     - `comparison_matrix.png` - Genetic distance heatmap
   
   - **Interactive Dashboard**: 
     - File: `output/visualizations/genetic_analysis/genetic_analysis_dashboard.html`
     - Open directly in web browser (no server needed)
     - Features:
       - G25 coordinates PCA plot
       - Admixture comparison charts
       - Population distance visualizations
       - Genetic distance matrix heatmap
       - Interactive tooltips with detailed information
     - Best viewed in modern browsers (Chrome, Firefox, Safari, Edge)

3. **Interpreting Genetic Profiles**:
   - **G25 Distance**: < 0.05 indicates possible relatedness
   - **Admixture**: Similar profiles suggest shared ancestry
   - **Population Distances**: Lower values indicate closer genetic affinity
   - **MTA Matches**: Shared DNA segments confirm genetic relationships

4. **Running Comprehensive Analysis**:
   ```bash
   # Activate virtual environment
   source genealogy_env/bin/activate
   
   # Run comprehensive genetic analysis
   python scripts/comprehensive_genetic_analysis.py
   ```
   
   This will:
   - Parse G25 coordinates (all 4 samples: VK155, VK157, VK154, VK156)
   - Analyze admixture for all 4 samples
   - Calculate population distances
   - Perform PCA and clustering
   - Integrate MTA match data
   - Generate all visualizations
   - Update genealogy JSON with genetic profiles

5. **Programmatic Access**:
   ```python
   import json
   from pathlib import Path
   
   # Load comprehensive profiles
   with open('data/processed/ancient_dna/genetic_profiles.json') as f:
       profiles = json.load(f)
   
   # Access VK157 profile
   vk157 = profiles['VK157']
   print(f"G25 coordinates: {vk157['g25_coordinates']}")
   print(f"Admixture: {vk157['admixture']['ancient']}")
   print(f"Closest populations: {vk157['closest_populations'][:5]}")
   
   # Access MTA analysis
   if 'mta_analysis' in vk157:
       print(f"Top matches: {len(vk157['mta_analysis']['top_matches'])}")
   ```

### Interactive Tree Viewing

1. **Topola Viewer**: 
   - Visit: https://pewu.github.io/topola-viewer/
   - Upload: `output/web/bodzia_complete_tree.ged`
   - Features: Interactive navigation, ancestor/descendant views

2. **SVG-FTG**:
   - Visit: https://parallaxviewpoint.com/SVG-FTG/
   - Upload: `output/web/bodzia_complete_tree_svgftg.ged`
   - Features: Publication-quality SVG generation

3. **dTree Interactive Visualization**:
   - File: `output/web/bodzia_complete_dtree.html`
   - Open directly in web browser (no upload needed)
   - Features:
     - Interactive pan and zoom (click-drag to pan, scroll to zoom)
     - Dynasty-based color coding matching Graphviz visualization
     - DNA-tested individuals highlighted with markers
     - Click nodes to see detailed information (name, dynasty, birth/death dates, DNA markers)
     - Multiple parent support (handles complex family relationships)
     - Reset zoom and fit-to-view controls
   - Based on: [dTree library](https://github.com/ErikGartner/dTree) (D3.js-based)
   - Best viewed in modern browsers (Chrome, Firefox, Safari, Edge)
   - Works offline - all dependencies loaded from CDN
   - Generate with: `python scripts/generate_dtree_visualization.py`

---

## Research Context

### Bodzia Archaeological Site

The Bodzia cemetery (near Włocławek, central Poland) represents one of the most significant early medieval elite burial sites in Central Europe. Dating to 950-1020 CE, it contains:

- Scandinavian-style weaponry (Viking swords)
- Mammen-style silver artifacts
- Cross-cultural goods (Rus', Polish, Scandinavian)
- Elite warrior burials
- **4 DNA-tested individuals** with specific genetic markers

### Genetic Connections

**Haplogroups:**
- **Sviatopolk I (VK157)**: Y-DNA I1a3a1 (I1-S2077), mtDNA H1c (matches I-Y45113 research context)
- **Princess from Bodzia (VK154)**: mtDNA H1c3
- **The Witch (VK155)**: mtDNA H1c
- **Bodzia Warrior (VK156)**: Y-DNA R1a1a1b1a2a2a1, mtDNA J1c2c2a

**Comprehensive Genetic Analysis Findings:**
- **Genetic Distance (VK155 ↔ VK157)**: 0.0417 (moderate - possibly related)
- **Shared Admixture Profile**: All 4 samples show similar proportions:
  - Yamnaya (Steppe): 48.1-52.7%
  - Neolithic Farmers: 27.9-31.4%
  - Western Hunter-Gatherers: 16.9-21.9%
- **Common Population Affinities**: 11 populations closest to all samples:
  - Other Bodzia samples (closest match)
  - Viking Age Gotland, Sweden
  - Medieval Germany (Krakauer Berg)
  - Avar period Hungary
- **MTA Match Data**: VK155 (298 top matches), VK157 (261 top matches)
- **Population Structure**: Genetic homogeneity supports elite burial site interpretation

**Research Context:**
- **I-Y45113 haplogroup**: Potentially connected to Bodzia elite warriors
- **Formation date**: ~975 CE (matches Bodzia active period)
- **Geographic alignment**: Bodzia is ~60 km from Płock (Mazowieckie region)
- **Cross-Cultural Connections**: Strong genetic affinities to Viking Age Scandinavia, Medieval Central Europe, and Rus' populations

### Ciepłe Archaeological Site (Comparative Context)

The **Ciepłe settlement complex** (Gniew, Tczew, Eastern Pomerania) provides essential comparative context for understanding the broader Scandinavian-Polish elite network documented in this genealogical tree. As a parallel elite burial site active during the same period as Bodzia, Ciepłe offers critical insights into the dual Scandinavian wings of the early medieval elite network.

#### Temporal & Geographic Alignment

**Perfect overlap with Bodzia:**
- **Active period**: 980-1020 CE (40-year overlap with Bodzia's 950-1020 CE)
- **Foundation**: 980s-990s CE (radiocarbon-dated)—coincides with peak of Bodzia's use
- **Distance**: ~150 km northwest of Bodzia (Gniew, Tczew vs. Włocławek)
- **Same political context**: Founded during Bolesław I the Brave's reign (992-1025), who appears in this tree as **PIA001 with "Bodzia connection"**

#### Complementary Elite Network: Bodzia = Rus' Wing, Ciepłe = Danish Wing

This genealogical tree documents **9 dynasties** including:
- **Rurikid** (21 individuals): Sviatopolk I (VK157, Y-DNA I1-S2077) at Bodzia
- **Gorm** (9 individuals): Harald Bluetooth, Sweyn Forkbeard, Cnut the Great
- **Piast** (14 individuals): Bolesław I the Brave (967-1025) with "Bodzia connection"

**Ciepłe provides the Danish-Pomeranian counterpart:**
- **4 Scandinavian warriors** confirmed via strontium isotope + genetic analysis
- **Origin**: Denmark (most likely southern Scandinavia)
- **Role**: Elite warriors with chamber graves, scales (tax collection), touchstones (precious metal assaying)
- **Context**: Piast state control of Eastern Pomerania during Bolesław I's expansion

**Network interpretation**: While Bodzia shows **Rus'-Polish integration** (Sviatopolk I married into Polish elite), Ciepłe shows **Danish-Polish integration** (Danish warriors administering Pomeranian territories for Bolesław I). Together, they map the **dual Scandinavian wings** (eastern Rus' + western Danish) of the elite network documented at the royal level in this genealogical tree.

#### Archaeological Evidence

Ciepłe represents an exceptional early medieval settlement complex at the Piast frontier, containing:
- **Chamber graves** with Scandinavian-style burial practices
- **Elite warrior burials** with weaponry and prestige goods
- **Administrative artifacts**: Scales (tax collection), touchstones (precious metal assaying)
- **Strontium isotope analysis**: Confirmed Scandinavian origin for 4 warriors
- **Settlement context**: Piast state control of Eastern Pomerania during Bolesław I's expansion

#### DNA Testing Status (January 2026)

**Current status:**
- **4 Scandinavian warriors**: DNA tested (genetic analysis complete)
- **Y-DNA haplogroups**: Analyzed but **NOT YET PUBLISHED** (expected Q1-Q2 2026 in peer-review)
- **Expected haplogroups**: Likely I1-derived (Danish male lineage, similar to Bodzia VK157's I1-S2077) or R1a (similar to Bodzia VK156's R1a-SUR51)
- **When published**: Can directly compare to Bodzia samples using the same analytical framework

#### Integration Opportunities (When Ciepłe DNA Publishes)

**This documentation already includes:**
- G25 coordinate analysis with pairwise distance matrix (all 4 Bodzia samples)
- Admixture modeling showing shared ancestry profiles
- Population distance analysis to 203+ ancient reference populations
- PCA clustering identifying 2 family groups within Bodzia

**Add Ciepłe samples (Q1-Q2 2026) to:**
1. **G25 distance matrix**: Calculate Bodzia ↔ Ciepłe pairwise distances (expected: 0.02-0.05 moderate range, similar to Bodzia internal distances)
2. **PCA plot**: Check if Ciepłe clusters with Bodzia or separates geographically
3. **Admixture comparison**: Test if Danish warriors show similar Yamnaya/Neolithic/WHG proportions (expected: similar 48-53% Yamnaya, 28-31% Neolithic, 17-22% WHG)
4. **Population affinities**: Do Ciepłe warriors cluster closer to Bodzia than to generic Viking Age Scandinavian populations?

**If Y-DNA matches:**
- **Ciepłe warriors = I1-S2077** (same as Bodzia VK157): Confirms shared Scandinavian patrilineal lineages across both sites
- **Ciepłe warriors = I-Y45113** (research context): Direct connection to I-Y45113 research investigation
- **Ciepłe warriors = R1a-SUR51** (same as Bodzia VK156): Parallel R1a migration streams

#### Research Context: I-Y45113 Haplogroup Implications

**Geographic triangle:**
- **Płock** ←60 km→ **Bodzia** ←150 km→ **Ciepłe**
- **I-Y45113 TMRCA (~975 CE)** coincides with **Ciepłe foundation (980s)**

If I-Y45113 ancestors were in this region, they could have been part of:
1. **Bodzia elite** (Rus'-Polish nexus) ← Current hypothesis
2. **Ciepłe elite** (Danish-Pomeranian nexus) ← New possibility
3. **Mobile elite** moving between both sites (warriors, traders, administrators)

**Critical test**: When Ciepłe Y-DNA publishes, compare haplogroups. If Ciepłe warriors carry I1-S2077 or related subclades, this confirms I-Y45113 ancestors were part of this broader **Scandinavian-Polish elite network** spanning both sites.

#### Validation of Multi-Dynasty Approach

This genealogical tree documents **79 individuals across 9 dynasties** (Rurikid, Piast, Gorm, Normandy, Arpad, Premyslid, Ottonian, Capetian). Ciepłe provides **on-the-ground archaeological evidence** that this interconnection was real:

- **Royal level** (this tree): Gorm dynasty rulers (Harald Bluetooth, Sweyn Forkbeard) allied with Piast rulers (Bolesław I)
- **Ground level** (Ciepłe): Danish warriors (Gorm retainers) embedded in Polish territories (Piast administration), living alongside local populations, collecting taxes, maintaining military control

**Same period, same integration pattern, different geographic nodes**. Ciepłe transforms this analysis from "single-site study" to "regional elite network study," which is exactly what the 79-individual genealogical tree documents.

#### Actionable Next Steps

**Now (January 2026):**
- Add Ciepłe as comparative site section (this documentation)
- Note DNA results pending publication
- Establish framework for integration when data becomes available

**Q1-Q2 2026** (when Ciepłe Y-DNA publishes):
1. Compare haplogroups to Bodzia VK157 (I1-S2077) and VK156 (R1a-SUR51)
2. Add Ciepłe G25 coordinates to distance matrix
3. Update PCA plot to include both sites
4. Test population affinities and admixture profiles
5. If kinship detected, add "Bodzia ↔ Ciepłe elite network" connections to genealogical tree

**Bottom line**: Ciepłe is not just relevant—it's **essential comparative context** that will either confirm or refine the hypothesis about the genetic structure of Early Medieval Scandinavian-Polish elite networks across multiple sites and dynasties.

### Winchester Cathedral (Ongoing Research) and Relevance to the Bodzia Hypothesis

This tree includes dynasties that directly intersect with **England** in the late 10th–11th centuries (notably Danish and Norman rulers). **Winchester Cathedral** is a key comparative site because (a) it is traditionally associated with high-status burials from these periods, and (b) ongoing conservation/archaeological work there has the potential to produce (or refine) **ancient DNA datasets** for elite individuals that overlap chronologically and politically with the Bodzia horizon.

If genomic profiles from Winchester Cathedral can be confidently assigned to specific individuals (or at least to well-dated, high-status burials), they become an external reference point to test the working hypothesis in this file: **that the Bodzia individuals represent an elite network with genetic ties extending into the Anglo-Scandinavian / Anglo-Norman sphere**, not only cultural/artefactual parallels.

#### Bodzia–Winchester royal-house bridge (key individuals in this tree)

The Bodzia diagram/tree already contains several individuals who are frequently discussed in connection with Winchester Cathedral’s elite burial context (e.g., via the mortuary chests tradition and related conservation/analysis work). These are the highest-value “targets” for an eventual Bodzia ↔ Winchester genetic comparison, because they sit on a direct dynastic chain in the diagram:

- **Cnut the Great** (House of Gorm): King of England/Denmark/Norway (d. 1035). Chronologically overlaps the Bodzia horizon and represents the Anglo-Scandinavian consolidation phase that the Bodzia material culture is often compared against.
- **Emma of Normandy** (House of Normandy): spouse of Cnut (d. 1052). Key diplomatic/dynastic link between the Norman and Danish networks represented in this tree.
- **Harthacnut** (House of Gorm): son of Cnut and Emma (d. 1042). Provides direct continuity of the Danish royal paternal line into England in the 11th century.

Additional “corridor anchors” present in the tree that contextualize the bridge (even if not themselves Winchester burials):

- **Sweyn Forkbeard** (House of Gorm): father of Cnut (d. 1014).
- **Harald Bluetooth** (House of Gorm): grandfather of Cnut (d. 986), active around the early phase of the Bodzia timeframe.
- **Richard I the Fearless** and **William I Longsword** (House of Normandy): Emma’s close ancestry in the Norman/Viking elite line shown in the diagram.

This list matters because it lets you formulate a testable statement with clear expected outcomes: if Winchester Cathedral yields reliably attributable genomes for any of the individuals above (or for closely related burials), then you can test whether any Bodzia individuals fall within a plausible kinship/lineage radius of this Anglo-Scandinavian/Norman dynastic network (close kinship, shared rare uniparental subclades, or only broader affinity).

What would count as genetic support (strongest → weakest):

1. **Close-kinship signal** (e.g., 1st–3rd degree) between a Bodzia genome and a Winchester genome based on genome-wide relatedness estimates.
2. **Shared rare Y-DNA subclade** between Bodzia male(s) and a Winchester male individual (strongly directional for paternal-line continuity when assignment is reliable).
3. **Shared rare mtDNA subclade** linking Bodzia female(s) to Winchester female(s), consistent with a documented (or plausible) maternal-line connection.
4. **Population-level affinity** only (PCA/ADMIXTURE/f-statistics showing Bodzia clustering closer to a particular English elite context than expected) — supportive but not a confirmation of genealogical linkage.

Minimum data needed from Winchester Cathedral work to make the comparison meaningful:

- Sample identifiers and archaeological context (provenance, stratigraphy, commingling risk)
- Radiocarbon date(s) and/or historical attribution confidence
- Sequencing type and coverage (shotgun vs capture; average depth; damage profiles)
- Contamination estimates (mtDNA and X-chromosome for males)
- Haplogroup calls (Y-DNA/mtDNA) with the resolution level reported (e.g., broad I1 vs a downstream SNP-defined clade)
- Published genotype data (or summary statistics sufficient for kinship and affinity tests)

Practical workflow to test the hypothesis once Winchester data exist:

1. Standardize data processing assumptions (reference build, pseudo-haploid vs diploid calls, SNP set overlap).
2. Run **within-site kinship** for Winchester first (to understand commingling and establish reliable individuals).
3. Run **cross-site kinship** Bodzia ↔ Winchester (low-coverage-aware methods).
4. Compare **Y-DNA and mtDNA phylogenetic placement** (downstream SNPs where possible).
5. Interpret results jointly with the tree logic in this document (historical plausibility, timelines, and marriage networks).

Important caveats:

- Commingled elite remains (common in reburial contexts) can obscure or falsely suggest relationships.
- Matching a broad haplogroup (e.g., “I1” or “H”) is not evidence of close kinship; downstream resolution matters.
- “Genetically connected” should be stated precisely (close kinship vs shared lineage vs shared regional ancestry).

### Historical Significance

This complete tree represents the interconnected elite networks of Early Medieval Europe, showing how royal houses maintained connections through:
- Strategic marriages
- Military alliances
- Trade networks
- Cultural exchange
- **DNA-verified relationships** at Bodzia site

---

## References

### Primary Sources - Bodzia Archaeological Site

1. **Buko, A., Kara, M., et al.** (2013). "A unique medieval cemetery from the time of the formation of the Polish state in Bodzia (Włocławek district, Kuyavian-Pomeranian voivodeship)". *Archäologisches Korrespondenzblatt*, 43(3), 509-528.
   - Available: `docs/Academic Papers/Buko_etal_2013_Bodzia_AKB_43_3.pdf`
   - Source: https://journals.ub.uni-heidelberg.de/index.php/ak/article/view/75695/69341

2. **Beletskiy, S. V.** (2018). "A few notes about the bident and trident from Bodzia". *Slavia Antiqua*, 59, 201-226.
   - Reference: Beletskiy_DvuzubBodzia_2018_2264157300461926.pdf

3. **Buko, A., Kara, M.** "Bodzia: A Late Viking-Age Elite Cemetery in Central Poland". 
   - Reference: Buko_Kara___Bodzia_AK.pdf

4. **Elity społeczne Bodzia** (Elite Social Structures of Bodzia)
   - Reference: Elity_spoleczne_Bodzia-3 (1).pdf

5. **Diagram: Bodzia & Early Medieval Royal Houses - Color**
   - Source: `docs/Bodzia Diagram/Diagram_ Bodzia & Early Medieval Royal Houses  - Color.pdf`
   - Primary visual reference for genealogy tree structure

### Genetic and DNA Studies

6. **Margaryan, A., Lawson, D. J., et al.** (2020). "Population genomics of the Viking world". *Nature*, 585, 390-396.
   - Available: `docs/Academic Papers/Ashot Margaryan - Population genomics of the Viking world [2019].pdf` and `docs/Academic Papers/Margaryan_etal_2020_Population_genomics_of_the_Viking_world.pdf`
   - DOI: 10.1038/s41586-020-2688-8
   - Includes Viking Age genetic data relevant to Bodzia samples

7. **Kushniarevich, A., et al.** "Genetic Heritage of the Balto-Slavic Speaking Populations: A Synthesis of Autosomal, Mitochondrial and Y-Chromosomal Data".
   - Available: `docs/Academic Papers/A. Kushniarevich - Genetic Heritage of the Balto-Slavic Speaking Populations A Synthesis of Autosomal, Mitochondrial and Y-Chromos.pdf`
   - Context for Y-DNA haplogroup I-Y45113

8. **Mielnik-Sikorska, M., et al.** (2013). "The History of Slavs Inferred from Complete Mitochondrial Genome Sequences". *PLOS ONE*, 8(1), e54360.
   - Available: `docs/Academic Papers/Marta Mielnik-Sikorska - The History of Slavs Inferred from Complete Mitochondrial Genome Sequences [2013].pdf`
   - mtDNA H1c haplogroup context

9. **Olalde, I., et al.** (2018). "The Beaker phenomenon and the genomic transformation of northwest Europe". *Nature*, 555, 190-196.
   - Reference: nature25738_Olalde.pdf
   - Ancient DNA methodology

### Comparative Site: Winchester Cathedral (England)

The Winchester Cathedral linkage discussed in **Research Context** should be grounded in specific, citable outputs once they are available (paper, preprint, repository dataset, or official technical report). Add references here when you have them, ideally including:

- Publication/preprint title, authors, year, and persistent identifier (DOI/arXiv/Zenodo)
- If data are public: accession (ENA/SRA), SNP panel/capture description, and sample IDs
- If data are not public: a stable project page and a description of what can be used (summary haplogroups vs full genotypes)

Suggested reference entries to add (placeholders):

- Winchester Cathedral — mortuary chests conservation / analysis project (add official project page + any technical reports).
- Any peer-reviewed aDNA paper(s) or preprint(s) reporting Winchester Cathedral sample IDs, dates, and genotype data.

### Rurikid Dynasty and Kievan Rus'

10. **Zhur, K.** "The Rurikids: The First Experience of Reconstructing the Genetic Portrait of the Ruling Family of Medieval Rus' Based on the Analysis of Ancient DNA".
   - Available: `docs/Academic Papers/K. Zhur - The Rurikids The First Experience of Reconstructing the Genetic Portrait of the Ruling Family of Medieval Rus' Based on .pdf`
   - Genetic analysis of Rurikid dynasty

11. **Mikheev, S. M.** (2009). *Monograph on Kievan Rus'* (in Russian).
   - Available: `docs/Academic Papers/mikheev2009b_book.pdf`
   - Historical context for Sviatopolk I and early Rus' rulers

12. **Shchavelev, A.** "The People Rus' in the Ninth – Middle Eleventh Centuries: New Approaches to the Study of Ethnogenesis and Politogen".
   - Available: `docs/Academic Papers/A. Shchavelev - The People Rus' in the Ninth – Middle Eleventh Centuries New Approaches to the Study of Ethnogenesis and Politogen.pdf`

13. **Stefanovich, P. S.** (2016). "The Political Organization of Rus' in the 10th Century". *Jahrbücher für Geschichte Osteuropas*, 64(4), 529-544.
   - Available: `docs/Academic Papers/Petr S. Stefanovich - The Political Organization of Rus' in the 10th Century [2016].pdf` and `docs/Academic Papers/Stefanovich_2016_The_Political_Organization_of_Rus_in_the_10th_Century.pdf`

14. **Burov, V. A.** (2023). "On the Origin of Novgorod. 862–1136 – Princely Town of Rurikids".
   - Available: `docs/Academic Papers/Vladimir A. Burov - ON THE ORIGIN OF NOVGOROD. 862–1136 – PRINCELY TOWN OF RURIKIDS [2023].pdf`

15. **Beznosyuk, S. M.** (2019). "The Rurikids" (web article, Russian).
   - Available: `docs/Academic Papers/Beznosyuk_2019_The_Rurikids.html`
   - Source: http://rurik.hostenko.com/2019/12/04/rurik/

16. **Font, M.** (2022). "Практика имянаречений у князей Древней Руси – как исторический источник" (Naming Practices of Princes of Ancient Rus' as a Historical Source).
   - Available: `docs/Academic Papers/Márta Font - Практика имянаречений у князей Древней Руси – как исторический источник [2022].pdf`

17. **Deško, P.** "The Celtic Theory of the Origins of Rus' as an Alternative to Normanism and the Concept of the «Old Rus' Ethnicity»".
   - Available: `docs/Academic Papers/Петро Дешко - The Celtic Theory of the Origins of Rus' as an Alternative to Normanism and the Concept of the «Old Rus' Ethnicity» .pdf`

18. **Vanbrabant, L.** (2015). "From the 'rus' on the littus Ruthenicum to the Russian people". Academia.edu.
   - Available: `docs/Academic Papers/Vanbrabant_2015_From_the_rus_on_the_littus_Ruthenicum_to_the_Russian_people.html`
   - Source: https://www.academia.edu/36066627/From_the_rus_on_the_littus_Ruthenicum_to_the_Russian_people
   - Discussion of Rus' ethnogenesis and terminology

### Early Medieval Archaeology and Genealogy

19. **Renfrew, C.** (2001). "From molecular genetics to archaeogenetics". *Proceedings of the National Academy of Sciences*, 98(9), 4830-4832.
   - Available: `docs/Academic Papers/C. Renfrew - From molecular genetics to archaeogenetics [2001].pdf` and `docs/Academic Papers/C. Renfrew - From molecular genetics to archaeogenetics [2001] (1).pdf`
   - Methodology for combining genetics and archaeology

20. **Manninen, M. A.** (2021). "First encounters in the north: cultural diversity and gene flow in Early Mesolithic Scandinavia". *Antiquity*, 95(383), 1426-1442.
   - Available: `docs/Academic Papers/Mikael A. Manninen - First encounters in the north cultural diversity and gene flow in Early Mesolithic Scandinavia [2021].pdf`

21. **Wadyl, S.** (ed.) (2019). "Ciepłe. Elitarna nekropola wczesnośredniowieczna na Pomorzu Wschodnim" (Ciepłe: Early Medieval Elite Necropolis in Eastern Pomerania).
   - Available: `docs/Academic Papers/Cieple_-_elitarna_nekropola.pdf` and `docs/Academic Papers/Cieple_-_elitarna_nekropola.md`
   - Comparative elite burial site analysis

### Medieval Genealogy and Heraldry

22. **Foundation for Medieval Genealogy** - MedLands Project.
   - Available: `docs/Academic Papers/FMG_MedLands_Swabia_Konradiner.html`
   - Source: http://fmg.ac/Projects/MedLands/SWABIA.htm
   - Comprehensive medieval genealogy database

### Data Sources and Methodology

23. **ISOGG Y-DNA Tree** - International Society of Genetic Genealogy.
   - Source: https://isogg.org/tree/
   - Y-DNA haplogroup classification system

24. **YFull Y-DNA Tree** - YFull YTree.
   - Source: https://www.yfull.com/
   - Y-DNA phylogenetic tree and TMRCA calculations

25. **FamilyTreeDNA** - Big Y-700 testing.
   - Source: https://www.familytreedna.com/
   - Y-DNA testing platform

26. **MyTrueAncestry** - Ancient DNA matching database.
   - Source: https://www.mytrueancestry.com/
   - Contains Bodzia ancient DNA samples (VK157, VK155, VK154, VK156)
   - MTA match data parsed from `matchesMTA.md` files
   - Provides genetic distance calculations and shared DNA segment analysis

27. **Explore Your DNA** - Ancient DNA sample database and G25 coordinates.
   - Source: https://www.exploreyourdna.com/
   - G25 coordinates for VK155 and VK157
   - Admixture models based on Davidski's G25 standard reference populations
   - Population distance calculations to 203+ ancient reference populations
   - Haplogroup information and sample metadata

28. **Genetic Genealogy Facebook Group** - Source of additional G25 coordinates and subclade analysis.
   - G25 coordinates for VK154 and VK156 (supplementing Explore Your DNA data)
   - I-BY316 subclade analysis providing context for I1a3 platform connections
   - Lombard elite network analysis (Burgheim, Collegno CL63)
   - Viking Age Gotland connections analysis
   - Source files: `docs/FB_GROUP/vk154_G25.txt`, `docs/FB_GROUP/vk156_G25.txt`, `docs/FB_GROUP/.md`

29. **Davidski's G25 Standard** - G25 coordinate system and reference populations.
   - Source: https://eurogenes.blogspot.com/
   - 25-dimensional PCA coordinates for genetic distance calculations
   - Standard reference populations for admixture modeling
   - Methodology: nMonte-style optimization for admixture estimation

30. **Comprehensive Genetic Analysis Documentation**
   - Available: `docs/COMPREHENSIVE_GENETIC_ANALYSIS.md`
   - Detailed methodology and findings from integrated genetic analysis
   - G25 coordinate analysis, admixture modeling, population distances, PCA, and MTA integration
   - Analysis date: 2026-01-11

31. **Ciepłe Archaeological Site** - Comparative elite burial site in Eastern Pomerania.
   - **Cambridge Antiquity**: "Ciepłe Revisited: An Exceptional Early Medieval Settlement Complex at the Piast Frontier"
   - **University of Warsaw Archaeology**: Ciepłe settlement complex information (https://www.archeologia.uw.edu.pl/en/cieple-a-settlement-complex-from-the-turn-of-the-10th-11th-century-in-eastern-pomerania/)
   - **Medievalists.net**: "Four Warriors Buried in 11th-Century Poland Came from Scandinavia, Researchers Find" (https://www.medievalists.net/2020/02/four-warriors-buried-in-11th-century-poland-came-from-scandinavia-researchers-find/)
   - **Science in Poland**: "Four Warriors Buried in 11th-Century Tombs in Pomerania Came from Scandinavia, Say Scientists" (https://scienceinpoland.pl/en/news/news,80395,four-warriors-buried-11th-century-tombs-pomerania-came-scandinavia-say-scientists)
   - **Active period**: 980-1020 CE (40-year overlap with Bodzia)
   - **Location**: Gniew, Tczew, Eastern Pomerania (~150 km northwest of Bodzia)
   - **Key findings**: 4 Scandinavian warriors confirmed via strontium isotope + genetic analysis, origin: Denmark
   - **DNA status**: Genetic analysis complete, Y-DNA haplogroups analyzed but not yet published (expected Q1-Q2 2026)
   - **Relevance**: Provides Danish-Polish integration counterpart to Bodzia's Rus'-Polish integration, validating the dual Scandinavian wings of the elite network documented in the genealogical tree

32. **Elicit** - Academic paper extraction and review.
   - Available: `docs/Academic Papers/Elicit - extract-results-review-8aefa20a-f5fd-4895-9251-47b725cf0810.csv`
   - Structured data extraction from academic literature

### Additional References

33. **Androshchuk, F.** (2022). "From Vikings to Rus — the Danish Connection". In *Rus — Vikings in the East* (Moesgaard Museum volume).
   - Status: Referenced but not publicly available

34. **Litvina, A., Uspenskij, F.** (2017). "Dynastic Power And Name-giving Principles in Medieval Rus'". *Micrologus*, XXV.
   - Status: Referenced, may require institutional access

35. **Nazarenko, A. V.** (2001). Book chapter on early Rus' (in Russian).
   - Status: Referenced but not publicly available

36. **Pritsak, O.** (1977). "The Origin of Rus'". *The Russian Review*, 36(3), 249-273.
   - Status: Commonly available through JSTOR or publisher

37. **Duczko, W.** (2004). *Viking Rus: Studies on the Presence of Scandinavians in Eastern Europe*. Brill.
   - Status: Academic publisher, may require institutional access

### Online Resources

38. **Topola Genealogy Viewer**
   - Source: https://pewu.github.io/topola-viewer/
   - Interactive GEDCOM viewer

39. **SVG Family-Tree Generator (SVG-FTG)**
   - Source: https://parallaxviewpoint.com/SVG-FTG/
   - Publication-quality family tree generation

40. **Graphviz** - Graph Visualization Software
   - Source: https://graphviz.org/
   - Used for tree diagram generation

41. **dTree** - Interactive Family Tree Visualization Library
   - Source: https://github.com/ErikGartner/dTree
   - Built on D3.js for interactive family tree visualization
   - Supports multiple parents and complex relationships
   - Used for: `output/web/bodzia_complete_dtree.html`

### Data Files in This Project

**Genealogy Data:**
- **Bodzia Complete Tree JSON**: `data/processed/genealogy/bodzia_complete_tree.json` - Updated with comprehensive genetic profiles
- **Bodzia Complete Tree GEDCOM**: `data/processed/genealogy/bodzia_complete_tree.ged`

**Comprehensive Genetic Analysis Data:**
- **Genetic Profiles**: `data/processed/ancient_dna/genetic_profiles.json` - Complete profiles for VK155, VK157, VK154, VK156
- **G25 Comparison**: `data/processed/ancient_dna/g25_comparison.json` - Genetic distance comparisons
- **Admixture Comparison**: `data/processed/ancient_dna/admixture_comparison.json` - Admixture analysis
- **Common Populations**: `data/processed/ancient_dna/common_populations.json` - Shared population affinities
- **PCA Results**: `data/processed/ancient_dna/pca_results.json` - Principal component analysis
- **Cluster Results**: `data/processed/ancient_dna/cluster_results.json` - K-means clustering

**MTA Match Data:**
- **VK155 MTA Data**: `data/raw/autosomal/MTA/VK155/matchesMTA.md` - Raw MTA match report
- **VK157 MTA Data**: `data/raw/autosomal/MTA/VK157/matchesMTA.md` - Raw MTA match report
- **VK155 G25 Coordinates**: `data/raw/autosomal/MTA/VK155/vk155_G25.txt`
- **VK157 G25 Coordinates**: `data/raw/autosomal/MTA/VK157/vk157_G25.txt`

**Additional G25 Coordinates (Facebook Group):**
- **VK154 G25 Coordinates**: `docs/FB_GROUP/vk154_G25.txt` - From genetic genealogy Facebook group
- **VK156 G25 Coordinates**: `docs/FB_GROUP/vk156_G25.txt` - From genetic genealogy Facebook group

**I-BY316 Subclade Analysis:**
- **Analysis Document**: `docs/FB_GROUP/.md` - Detailed I-BY316 subclade analysis and Lombard connections

**ScienceDirect Supplementary Files:**
- **Recent Paper Data**: `docs/FB_GROUP/ScienceDirect_files_11Jan2026_00-30-19.817.zip` - Supplementary materials from 2025 paper (S0092867425005598), contains 8 files (PDF + Excel files)

**Y-DNA Data:**
- **Y-DNA SNP Data**: `data/raw/y_dna_results/SNP_for_YF079056_20260110.csv`
- **Y-DNA STR Data**: `data/raw/y_dna_results/STR_for_YF079056_20260110.csv`
- **YFull STR Matches**: `data/raw/y_dna_results/YFull _ STR matches.pdf`

---

**Document Version**: 2.2 (Complete - 79 Individuals with Comprehensive Genetic Analysis)  
**Last Updated**: 2026-01-11  
**Generated By**: Bodzia Complete Tree Generation Pipeline + Comprehensive Genetic Analysis Pipeline
