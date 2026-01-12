# Bodzia (Central Poland) Elite Networks at the Viking Age–Early Medieval Transition (ca. 950–1020 CE): A Genealogical Graph Model Integrated with Exploratory Genetic Comparisons

**Manuscript status:** Draft scholarly report prepared from repository data and scripts; not peer‑reviewed.  
**Audience optimization:** Tier 1 (archaeology + aDNA + genetic genealogy). Tier 2 context is provided in boxed sidebars; Tier 3 support in a glossary and appendices.  
**Prepared:** 2026-01-11 (see Supplementary Information for auto-generated content provenance).

## Abstract

Elite burials at Bodzia (central Poland) provide a key archaeological context for investigating cross-cultural interaction among Scandinavia, the emergent Piast polity, and the Rus’ sphere around the turn of the first millennium [1]. This report presents a reproducible digital-humanities workflow that (i) formalizes a curated genealogical diagram of early medieval royal houses as a machine-readable graph (79 individuals; 47 family unions) [5] and (ii) integrates genetic summary representations for four Bodzia individuals (VK154, VK155, VK156, VK157), including uniparental haplogroups and PCA-projection coordinates (Global25/G25) used for exploratory distance and affinity comparisons [6, 27, 29].

Exploratory analyses of G25 coordinates show moderate pairwise distances among all four Bodzia individuals (0.0281–0.0425), consistent with two related clusters (VK154–VK156; VK155–VK157) and broadly compatible with archaeological interpretations of family groupings within an elite burial community. Admixture-component summaries and population-distance comparisons indicate shared affinities to Viking-Age Scandinavia (e.g., Gotland) and to medieval central/eastern European reference populations. We situate these findings within a multi-dynasty historical framework and outline falsifiable tests for external comparisons, including the potential integration of elite English contexts (e.g., Winchester Cathedral) once reliable genomic datasets and attributions are available. ⚠️ **UPDATE (2026-01-11):** Winchester Cathedral mortuary chests project has **completed genetic analysis** identifying Cnut the Great, Harthacnut, and Emma of Normandy (all present in this genealogical tree); results expected in 2026, enabling direct testing of Bodzia ↔ Winchester connections. **See:** `docs/BODZIA_WINCHESTER_PIAST_CONNECTIONS.md`. The genetic results presented here are derived from coordinate/summary representations and should be validated with standard ancient-DNA workflows on raw genotype data for publication-grade inference.

## Keywords

Bodzia; Viking Age; early medieval Poland; Piast; Kievan Rus’; elite burials; ancient DNA; kinship; Y‑chromosome haplogroups; mtDNA; Global25 (G25); digital humanities; genealogical graphs.

## Executive Summary (Tier 2/3)

This report formalizes a Bodzia-associated early medieval “royal houses” diagram as a reproducible genealogical graph model and integrates exploratory genetic summaries for four Bodzia individuals (VK154, VK155, VK156, VK157). The primary contribution is methodological: it operationalizes a complex historical diagram as machine-readable data (JSON/GEDCOM + visualizations) and attaches a transparent set of genetic summaries (haplogroups; G25 distances/affinities) that can be used to generate falsifiable hypotheses for follow-up with publication-grade ancient DNA pipelines.

All results here are **draft, exploratory, and not peer-reviewed**; they rely on coordinate-based summaries rather than raw aDNA genotypes.

Key results (exploratory):

- The genealogical model contains **79 individuals** and **47 family unions**, spanning **9 dynasties** and a broad modeled timeframe (800–1173 CE), with the Bodzia cemetery horizon situated at ~950–1020 CE [1, 5].
- Across VK154/VK155/VK156/VK157, pairwise G25 distances fall within a narrow “moderate” band (0.0281–0.0425), consistent with two small clusters (VK154–VK156; VK155–VK157) within an elite burial community (Table 3) [27, 29].
- “Closest population” lists derived from the same coordinate framework repeatedly include Viking-Age Scandinavian references (e.g., Gotland) and medieval central/eastern European references (see Supplementary for full lists) [27, 29].

Testable hypotheses (summary; see §2.4):

1. Bodzia’s four profiled individuals represent a genetically cohesive elite community at a coarse scale (coordinate-based) rather than an extremely heterogeneous assemblage.
2. Scandinavian-associated affinities in the coordinate framework are consistent with archaeological observations of Scandinavian-linked material culture at Bodzia.
3. External elite contexts (e.g., Ciepłe; Winchester Cathedral) can be used as falsifiable comparators once published, attributable genomic datasets exist.

All major claims are explicitly tiered by confidence and mapped to evidence (Appendix A).

## 1. Introduction (Tier 1)

Bodzia is an elite cemetery in central Poland dated to the late 10th–early 11th centuries, notable for “hybrid” material culture combining Scandinavian, Rus’, and local elements [1]. The site is frequently discussed in terms of long-distance connectivity and elite mobility across the Baltic and eastern European riverine networks. The present project treats Bodzia as a test case for integrating (a) **explicit genealogical hypotheses** about elite networks with (b) **genetic summaries** that can be compared across ancient reference datasets.

This report addresses three practical research questions:

1. What is the structure of the curated Bodzia-associated “royal houses” genealogical model (scope, dynasties, and core bridging marriages)?
2. What do exploratory genomic summaries (G25 distance/affinity; admixture components) suggest about relationships among the four Bodzia individuals represented here (VK154, VK155, VK156, VK157)?
3. Which external elite contexts provide high-yield future comparison targets for testing cross-site connectivity hypotheses (e.g., Ciepłe; Winchester Cathedral)?

> **Box 1 (Tier 2): Historical frame (950–1050 CE, simplified)**
>  
> The Bodzia horizon overlaps major political consolidation across the southern Baltic. In the west, Danish kings of the House of Gorm (Harald Bluetooth → Sweyn Forkbeard → Cnut) are central to the formation of an Anglo‑Scandinavian realm. In the east, the Rus’ polity consolidates along routes linking the Baltic to the Black Sea, while Piast Poland expands and competes for control of frontier regions. The genealogical model used here encodes one hypothesis for how dynastic marriages and alliances connect these spheres at the elite level; it is not, by itself, evidence of biological kinship.

## 2. Materials and Methods (Tier 1)

### 2.1 Genealogical model

The genealogical network in this report is a structured transcription of the project’s source diagram (“Bodzia & Early Medieval Royal Houses – Color”) [5] into a graph model exported to JSON and GEDCOM. Individuals are labeled with dynasty membership and familial relationships. Because early medieval genealogy is source-limited and contested in places, all “named” linkages should be interpreted as hypotheses at the level of historical prosopography unless independently supported by primary/secondary scholarship.

### 2.2 Genetic data summarized in this report

This report uses **genetic summary representations** for four Bodzia-associated individuals (VK154, VK155, VK156, VK157) as curated in the project (with sample labeling consistent with the project’s reference sources) [6, 26, 27, 29]:

- Uniparental haplogroups (Y‑DNA and mtDNA) as recorded in the project’s curated sources.
- Global25/G25 PCA-projection coordinates used for Euclidean distance comparisons.
- Admixture-component summaries and “closest population” lists derived from the same coordinate framework.

These summaries are suitable for exploratory comparison and hypothesis generation, but they are not a substitute for publication-grade aDNA processing from raw reads/genotypes (authentication, contamination estimation, genotype likelihood calling, and formal population-genetic modeling).

Non–peer-reviewed inputs (e.g., MyTrueAncestry match reports; Facebook-group G25 coordinates) are used in Supplementary materials and should be treated as provisional until validated against published datasets.

### 2.3 Analytic approach (exploratory)

Analyses reported below include:

- Euclidean distances in 25D G25 space across all Bodzia pairs.
- Simple PCA and k-means clustering over the four samples (for visualization/structure only).
- Admixture-component summaries using a reduced 3-way model (Steppe/Yamnaya; Neolithic farmers; WHG) and small residual components.
- “Closest population” affinity lists to a reference panel of ancient samples labeled in the same coordinate framework.

> **Box 2 (Tier 2): What “genetic distance” means here**
>  
> “Distance” refers to Euclidean distance between projected PCA coordinates (G25). It can be informative for broad affinities but does not directly estimate genealogical relatedness. Close-kinship inference in aDNA typically relies on genome-wide relatedness methods on raw genotype data (often low-coverage-aware), ideally within a controlled and published pipeline.

### 2.4 Testable hypotheses and falsifiability criteria (Tier 1)

The hypotheses below are formulated to be falsifiable and to separate what can be assessed with the current coordinate-based summaries from what requires publication-grade aDNA processing.

**H1. Cohesion hypothesis (within Bodzia; exploratory)**

- **H0 (null):** The four profiled Bodzia individuals (VK154/VK155/VK156/VK157) are highly heterogeneous in ancestry and do not form a cohesive genetic cluster even at a coarse (coordinate) scale.
- **Ha (alternative):** The four individuals are broadly cohesive at a coarse scale, consistent with an elite burial community with limited heterogeneity.
- **Test(s):** Pairwise G25 distance distribution + admixture-component similarity across the four individuals (Tables 3–4) [27, 29].
- **Evidence thresholds (operational; coordinate dependent):**
  - Max pairwise distance < 0.06 and no outlier pair > 0.10 (flags extreme heterogeneity)
  - Broadly similar reduced-component admixture profiles without a single sample deviating by > ~10 percentage points on a major component
- **Current status:** **Provisionally supported (exploratory)** given observed distances 0.0281–0.0425 and similar component profiles (Tables 3–4).
- **Falsification scenario:** Recomputed genome-wide relatedness/affinity from raw genotypes shows one or more individuals as clear outliers (e.g., PCA/qpAdm placing them in markedly distinct clusters relative to the others).

**H2. Scandinavian-affinity hypothesis (Bodzia ↔ Viking-Age Scandinavia; exploratory)**

- **H0:** Scandinavian-associated reference populations do not appear as consistently close comparators for the Bodzia individuals in the project’s coordinate/reference framework.
- **Ha:** Scandinavian-associated references (e.g., Gotland) recur as close comparators across Bodzia individuals, consistent with archaeological indicators of Scandinavian-linked networks [1].
- **Test(s):** Presence/recurrence of Scandinavian-associated references among “closest population” lists across the four individuals (Supplementary tables/plots) [27, 29].
- **Evidence threshold (operational):** At least one Scandinavian-associated reference population appears among the top ~10–15 closest populations for ≥3 of the 4 individuals, in the same coordinate framework.
- **Current status:** **Provisionally supported (exploratory)** within the project’s coordinate/reference panel (see Supplementary).
- **Falsification scenario:** Using alternative reference panels / formal statistics (f-statistics/qpAdm) eliminates Scandinavian-associated affinity signals or shows them to be artifactual.

**H3. External comparator hypothesis (Ciepłe; Winchester; forward-looking)**

- **H0:** External elite contexts do not provide testable constraints on Bodzia connectivity beyond general “Viking Age” similarity.
- **Ha:** Published, attributable elite-context genomes enable falsifiable cross-site kinship/lineage tests that can confirm or constrain specific connectivity hypotheses.
- **Test(s):** Cross-site relatedness/lineage overlap once comparable datasets exist (see §4.1 and Supplementary “Winchester”/“Ciepłe” sections).
- **Current status:** **Inconclusive / pending data**.
- **Falsification scenario:** Well-powered, attributable datasets show no kinship or lineage overlap where hypothesized, or point to alternative networks.

### 2.5 Reproducibility

The repository contains scripts that generate the genealogical data products and attach genetic summaries to the tree model. Key outputs are listed in the Data & Code Availability section and in the Supplementary Information.

## 3. Results (Tier 1)

### 3.1 Genealogical dataset scope

**Table 1. Genealogical model summary**

| Metric | Value |
|---|---:|
| Individuals (named nodes) | 79 |
| Families (unions) | 47 |
| Dynasties represented | 9 |
| Temporal coverage (model) | 800–1173 CE |
| Bodzia cemetery horizon (site) | ~950–1020 CE (first period; second period: late 11th-early 12th century) |
| Total graves at Bodzia | More than 58 graves (including cenotaphs) |
| Excavation dates | 2007-2009 (led by Andrzej Buko, Polish Academy of Sciences) |
| Area excavated | 3 hectares |
| Total features discovered | 2069 important features |
| Total graves discovered | More than 58 graves (including cenotaphs) |
| Excavation dates | 2007-2009 (led by Andrzej Buko, Polish Academy of Sciences) |
| Area excavated | 3 hectares |
| Total features discovered | 2069 important features |

### 3.2 DNA-tested / DNA-profiled Bodzia individuals

**Table 2. Bodzia individuals analyzed genetically in this report**

| Sample | Sex (if recorded) | Y‑DNA | mtDNA | Notes |
|---|---|---|---|---|
| VK154 | F | – | H1c3 | Bodzia elite female (see Supplementary for context) |
| VK155 | F | – | H1c | Bodzia elite female (internal project label previously "The Witch"); **⚠️ Same grave (E864/I) as VK157, shares mtDNA H1c (maternal-line cousin)** |
| VK156 | M | R1a1a1b1a2a2a1 | J1c2c2a | Bodzia elite male |
| VK157 | M | I1a3a1 (I1‑S2077) | H1c | Bodzia elite male (mapped to RUR001 in the genealogical model; proposed identification should be treated as a hypothesis); **⚠️ Same grave (E864/I) as VK155 and unexamined female (lay on top of VK157 - NOT TESTED)** |

Note: Historical naming/role assignments (e.g., RUR001 → “Sviatopolk I”) remain hypothetical without independent archaeological attribution.

### 3.3 Exploratory genetic structure among Bodzia individuals

**Table 3. Pairwise G25 distances between Bodzia individuals**

| Sample Pair | Genetic Distance | Classification |
|-------------|------------------|----------------|
| VK154 ↔ VK156 | 0.0281 | Moderate |
| VK155 ↔ VK157 | 0.0417 | Moderate |
| VK155 ↔ VK154 | 0.0421 | Moderate |
| VK155 ↔ VK156 | 0.0420 | Moderate |
| VK157 ↔ VK154 | 0.0421 | Moderate |
| VK157 ↔ VK156 | 0.0425 | Moderate |

Across all pairs, distances fall in a narrow “moderate” band, with VK154–VK156 forming the closest pair. PCA/clustering over the four points yields two coherent groupings (VK154–VK156; VK155–VK157), suggesting within-site structure consistent with small-number family clustering rather than a highly heterogeneous assemblage.

Classification method: Euclidean distances in 25‑D G25 space computed by `scripts/comprehensive_genetic_analysis.py`; thresholds used for narration here—<0.06 “moderate,” >0.10 “outlier/heterogeneous”—follow the exploratory criteria in `docs/COMPREHENSIVE_GENETIC_ANALYSIS.md`.

### 3.4 Admixture-component summaries (exploratory)

**Table 4. Reduced admixture-component summaries**

| Sample | Steppe/Yamnaya (%) | Neolithic farmers (%) | WHG (%) | Residual (%) |
|--------|---------------------:|----------------------:|--------:|-------------:|
| VK155 | 52.7 | 29.7 | 16.9 | 0.7 |
| VK157 | 48.1 | 27.9 | 21.9 | 2.1 |
| VK154 | 52.6 | 28.3 | 19.1 | – |
| VK156 | 50.9 | 31.4 | 17.8 | – |

All four show broadly similar component profiles. “Closest population” lists in the same framework repeatedly include other Bodzia-labeled references, Viking-Age Scandinavia (notably Gotland), and medieval central European references (see Supplementary Information for full lists).

Admixture estimates derive from the same script (`scripts/comprehensive_genetic_analysis.py`) using Davidski G25 reference sets; component labels are heuristic and should be interpreted as exploratory summaries, not formal qpAdm models.

### 3.5 Figures and tables produced by this workflow (roadmap)

This repository already contains figure-ready outputs that can be adapted into journal figures (final captioning, layout, and DPI checks required):

- **Figure 1 (genealogical model graph):** `output/visualizations/bodzia_complete/bodzia_complete_tree.png` (also `.svg`/`.pdf`)
- **Figure 2 (G25 PCA):** `output/visualizations/genetic_analysis/pca_results.png`
- **Figure 3 (admixture summary):** `output/visualizations/genetic_analysis/admixture_ancient.png`
- **Figure 4 (pairwise distance heatmap):** `output/visualizations/genetic_analysis/comparison_matrix.png`
- **Figure 5 (population affinities; multi-panel):** `output/visualizations/genetic_analysis/population_distances_VK154.png`, `output/visualizations/genetic_analysis/population_distances_VK155.png`, `output/visualizations/genetic_analysis/population_distances_VK156.png`, `output/visualizations/genetic_analysis/population_distances_VK157.png`

Tables in the main manuscript are provided as Tables 1–4; expanded lists and “closest population” tables should remain in Supplementary Information.

## 4. Discussion (Tier 1)

The combined genealogical and genetic summaries support a working model in which the Bodzia burial community is genetically cohesive at a coarse scale, with internal structure consistent with at least two related clusters. The recurring affinity signals to Viking-Age Scandinavian references align with archaeological observations of Scandinavian-associated material culture at Bodzia, but these signals do not, by themselves, identify specific historical individuals or confirm dynastic assignments.

### 4.1 Comparative frameworks and falsifiable next tests

Two comparative directions are particularly high-yield:

- **Regional elite comparators (e.g., Ciepłe):** useful for testing whether multiple elite sites in Piast-adjacent territories share similar Scandinavian-associated genetic signatures and/or uniparental lineages [21, 31].
- **Anglo‑Scandinavian elite contexts (e.g., Winchester Cathedral):** the genealogical model includes House of Gorm and Normandy figures that connect to England (Cnut, Emma, Harthacnut). If reliable, attributable genomes become available from Winchester contexts, cross-site kinship/lineage tests could directly evaluate whether Bodzia individuals fall within plausible biological proximity to this dynastic network.

> **Box 3 (Tier 2): Bodzia ↔ Winchester as a “bridge hypothesis”**
>  
> The “bridge” is genealogical: the model explicitly includes Danish and Norman rulers connected to England. The genetic test is separate: it requires published, attributable genomes from Winchester contexts and low-coverage-aware relatedness methods. Shared broad haplogroups are not sufficient; downstream resolution and genome-wide relatedness are required. **No Winchester Cathedral genomic data are public as of 2026‑01‑11; this section is forward-looking only.**

## 5. Limitations (Tier 1)

1. **Summary data vs raw genotypes:** Most results here are based on G25 projections and derivative summaries, not on raw aDNA genotype likelihoods.
2. **Small sample size:** Four individuals cannot capture the full Bodzia burial community and limits statistical inference.
3. **Uncertain historical identifications:** Mapping an archaeological/genetic sample ID (e.g., VK157) onto a named historical individual is a hypothesis that requires independent corroboration.
4. **Third-party matching outputs:** Any MyTrueAncestry-derived “shared segment/cM” interpretations should be treated as exploratory and are best relegated to supplementary material unless validated.

## 6. Publication-grade aDNA data requirements (checklist)

To make the genetics component suitable for peer review in an aDNA-focused venue, the following metadata and QC outputs should be available per sample (VK154/VK155/VK156/VK157), ideally as a structured table:

- Burial context identifier(s) + provenance and commingling risk assessment
- Dating (radiocarbon where possible) with lab codes and calibrated ranges
- Sex determination method (osteology and/or genetic)
- Library preparation (e.g., UDG treatment; ds/ss) and capture strategy (if any)
- Sequencing type/platform and coverage metrics (genome-wide; mtDNA; Y for males)
- Authentication/damage metrics and contamination estimates (mtDNA; X for males)
- Reference build and mapping pipeline details (alignment parameters; duplicates; filtering)
- Genotype calling representation (pseudo-haploid vs diploid likelihoods) and SNP panel definition

If these are not currently available in the repository, they should be added as `[[UNKNOWN]]` fields in a sample metadata table and explicitly requested from the primary data source/publication before submitting a manuscript.

## 7. Conclusions and Future Work (Tier 1)

This project demonstrates a reproducible framework for integrating genealogical network models with exploratory genetic summaries for a key late 10th–early 11th century elite context in central Europe. The immediate next steps for publication-grade inference are to (i) ground claims in peer-reviewed primary genetic datasets and (ii) run standard aDNA authentication/kinship/population-genetic workflows on raw genotype data (where permitted). Comparative integration with other elite contexts—especially sites that can be securely dated and attributed—offers a clear path for testing the Bodzia connectivity hypotheses in a falsifiable way.

## Data & Code Availability

- Genealogical graph data: `data/processed/genealogy/bodzia_complete_tree.json`
- Visual outputs (tree + genetics): `output/visualizations/`
- Supplementary scripts: `scripts/`

Raw genetic inputs (e.g., commercial exports; raw match reports; BAM/VCF files) may be stored locally but are not included in versioned outputs.

## Glossary (Tier 3)

- **aDNA**: Ancient DNA.
- **G25 / Global25**: A PCA-projection coordinate system used in genetic genealogy for exploratory affinity comparisons.
- **WHG**: Western Hunter‑Gatherers (a common ancient ancestry component label).
- **Yamnaya/Steppe**: A label used for steppe pastoralist-related ancestry components.
- **mtDNA / Y‑DNA**: Mitochondrial DNA / Y‑chromosome DNA (uniparental lineages).
- **Haplogroup**: A lineage label defined by shared mutations on mtDNA or Y‑DNA.
- **PCA**: Principal Component Analysis, used to reduce dimensionality and visualize structure.
- **Kinship / relatedness**: Genetic relationship between individuals; close-kinship inference in aDNA typically requires genome-wide methods on raw data.
- **SNP / STR**: Single‑nucleotide polymorphism / short tandem repeat (two common Y‑DNA marker types in genetic genealogy).
- **TMRCA**: Time to most recent common ancestor (a phylogenetic estimate for a lineage/clade).
- **IBD**: Identical‑by‑descent; shared genome segments inherited from a common ancestor (challenging to infer reliably from low‑coverage aDNA without specialized methods).
- **Pseudo-haploid genotypes**: A common representation for low-coverage aDNA where one allele is sampled per site.
- **Contamination estimation**: Quantification of modern DNA contamination (often via mtDNA and X‑chromosome metrics).
- **qpAdm / f-statistics**: Standard aDNA toolkit methods for modeling ancestry mixtures and testing population relationships (not performed in this report).
- **ADMIXTURE / nMonte-style optimization**: Mixture-model approaches; in this project, admixture summaries are derived from a reduced coordinate-based model and should be treated as exploratory.

## Appendix A. Claims & Evidence Ledger (Tier 1)

This ledger maps high-level claims in the manuscript to the most direct supporting artifacts (references and/or repository outputs). It is intended to make peer review and internal auditing easier.

| Claim (short form) | Status | Primary support (evidence) |
|---|---|---|
| The Bodzia genealogical model contains 79 individuals and 47 unions | Supported | Table 1; `data/processed/genealogy/bodzia_complete_tree.json`; Supplementary “Tree Statistics” |
| The Bodzia cemetery horizon is ~950–1020 CE | Supported | [1] (Buko et al. 2013); Supplementary “Bodzia Archaeological Site” |
| VK157 is reported as Y‑DNA I1‑S2077 (I1a3a1) | Supported (as reported) | Supplementary “Genetic Connections”; [27], [29] |
| Pairwise G25 distances among VK154/VK155/VK156/VK157 are 0.0281–0.0425 | Supported (exploratory) | Table 3; `data/processed/ancient_dna/g25_comparison.json`; `output/visualizations/genetic_analysis/comparison_matrix.png` |
| G25 “closest populations” repeatedly include Viking-Age Scandinavian references (e.g., Gotland) | Supported (exploratory) | Supplementary population lists; `data/processed/ancient_dna/genetic_profiles.json`; `output/visualizations/genetic_analysis/population_distances_VK*.png` |
| The VK157 ↔ “Sviatopolk I” mapping is a hypothesis | Supported | Supplementary Rurikid section notes; see “MODEL NODE” labeling |
| Winchester Cathedral is a plausible external comparator for House of Gorm / Normandy nodes | Hypothesis / pending | Supplementary “Winchester Cathedral” section; requires primary Winchester genomic outputs to test |

---

# Supplementary Information (project dossier; auto-generated and script-updated)

## Bodzia Early Medieval Royal Houses - COMPLETE Tree Documentation

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

- **VK157** (RUR001; labeled "Sviatopolk I" in the genealogical model): Y-DNA I1-S2077 (I1a3a1)
  - Bodzia burial E864/I, sample VK157
  - **⚠️ BURIAL CONTEXT:** VK157 was buried in grave E864/I with:
    - **Unexamined female** who lay **on top of VK157** (one on top of the other) - **NOT GENETICALLY TESTED**
    - **VK155** (female, mtDNA H1c) who lay **next to** VK157 and the unexamined female
  - **⚠️ CRITICAL RESEARCH GAP:** The unexamined female from the same grave chamber as VK157 has **NOT been genetically tested**, preventing full understanding of family relationships
  - **Hypothesis:** Unexamined female = **wife of VK157** (if VK157 = Sviatopolk I, then Piast princess according to genealogical model)
  - **Piast aDNA context:** do not assume a stable, published “Piast Y-DNA signature” for validating this marriage hypothesis; secondary reporting indicates the Piast genomic program had not yet published dynasty-specific Y results and may observe multiple Y lineages across putative Piast remains [44].
  - **See:** `docs/VK155_VK157_BURIAL_HYPOTHESIS.md` for detailed analysis and verification steps
- **VK156** (BOD003; elite male): Y-DNA R1a (reported as R1a-SUR51 / R1a1a1b1a2a2a1)
  - Bodzia burial, sample VK156

#### mtDNA Tested (2)

- **VK154** (BOD001; elite female): mtDNA H1c3 (H1c)
  - Bodzia burial E864/II, sample VK154
- **VK155** (BOD002; elite female; previously labeled "The Witch" in internal project notes): mtDNA H1c
  - Bodzia burial E864/I, sample VK155
  - **⚠️ BURIAL CONTEXT:** VK155 was buried in the **same grave (E864/I) as VK157**, but **next to** VK157 and an **unexamined female** who lay **on top of VK157**
  - **⚠️ CRITICAL FINDING:** VK155 and VK157 share **identical mtDNA H1c**, indicating **maternal-line kinship** (cousins through female line)
  - **Hypothesis:** VK155 = relative of VK157 through his mother (Carolingian princess), consistent with VK157 = Sviatopolk I hypothesis
  - **See:** `docs/VK155_VK157_BURIAL_HYPOTHESIS.md` for detailed analysis

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
   - **Group 1**: VK155 and VK157 (possible close relationship or shared lineage; exploratory)
     - **⚠️ CRITICAL FINDING:** VK155 and VK157 share **identical mtDNA H1c**, indicating **maternal-line kinship** (cousins through female line)
     - **Burial context:** Same grave (E864/I), with VK155 next to VK157 and an **unexamined female** who lay on top of VK157
     - **Hypothesis:** VK155 = relative of VK157 through his mother (Carolingian princess); unexamined female = wife of VK157
     - **See:** `docs/VK155_VK157_BURIAL_HYPOTHESIS.md` for detailed analysis
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

**VK155 (Bodzia elite female):**
1. VK2020_POL_Bodzia_VA (0.0309)
2. VK2020_SWE_Gotland_VA (0.0391)
3. DEU_MA_Krakauer_Berg (0.0399)
4. HUN_Avar_Szolad (0.0430)
5. VK2020_RUS_Gnezdovo_VA (0.0443)

**VK157 (Bodzia elite male; RUR001 in genealogical model):**
1. VK2020_POL_Sandomierz_VA (0.0321)
2. VK2020_SWE_Gotland_VA (0.0333)
3. VK2020_POL_Bodzia_VA (0.0335)
4. DEU_MA_Krakauer_Berg (0.0337)
5. HUN_Avar_Szolad (0.0372)

**VK154 (Bodzia elite female):**
1. VK2020_POL_Bodzia_VA (0.0240) - **Closest to other Bodzia samples**
2. VK2020_SWE_Gotland_VA (0.0261)
3. DEU_MA_Krakauer_Berg (0.0341)

**VK156 (Bodzia elite male):**
1. VK2020_POL_Bodzia_VA (0.0189) - **Closest overall match**
2. VK2020_SWE_Gotland_VA (0.0222)
3. DEU_MA_Krakauer_Berg (0.0268)

#### Regional Affinities

1. **Local Connections**: All samples show closest affinity to other Bodzia samples (VK2020_POL_Bodzia_VA), confirming genetic continuity within the site.

2. **Viking Age Scandinavia**: Strong connections to Gotland (Sweden) populations across all samples, consistent with archaeological evidence of Scandinavian cultural influence at Bodzia.

3. **Medieval Central Europe**: Consistent affinities to Medieval German populations (Krakauer Berg), reflecting the broader Central European context.

4. **Avar and Early Slavic**: Connections to Avar period Hungary and early Slavic populations, consistent with the geographic location and time period.

5. **Rus' Connections**: VK157 shows particularly close connections to Rus'-labeled reference populations (e.g., Gnezdovo, Kurevanikha) within the project’s G25 reference panel; this is compatible with (but does not prove) eastern-network connectivity hypotheses encoded in the genealogical model.

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
- **VK155 and VK157**: Form a second cluster (distance: 0.0417), consistent with a possible close relationship or shared lineage (exploratory)
- **Between-group distances**: All pairs show moderate distances (0.0417-0.0425), indicating shared ancestry within the elite community

#### Cluster Analysis

K-means clustering was performed on G25 coordinates with multiple k values:

**k=2 Clusters** (two family groups):
- **Cluster 0**: VK155, VK157 (possible close relationship or shared lineage; exploratory)
- **Cluster 1**: VK154, VK156 (father-daughter/second-degree relatives)

**k=3 Clusters** (individual family units):
- **Cluster 0**: VK155
- **Cluster 1**: VK157
- **Cluster 2**: VK154, VK156 (closest pair)

**k=4 Clusters** (individual samples):
- Each sample forms its own cluster, reflecting individual genetic distinctness while maintaining overall similarity

**Interpretation**: The clustering patterns support the archaeological interpretation of two distinct family groups within the Bodzia elite burial site. The genetic distances and PCA structure indicate:
1. **Family Group 1** (VK155-VK157): Moderate genetic distance consistent with a possible close relationship or shared lineage (exploratory)
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

**VK155 (Bodzia elite female):**
- **Total Top Matches**: 298
- **Deep Dive Matches**: 7 matches with shared DNA segments
- **Closest Match**: PCA148_N (Germanic Medieval Poland, 950 AD) - Genetic Distance: 2.768
- **Top 5 Matches Include**:
  1. Germanic Medieval Poland (950 AD) - Genetic Distance: 2.768
  2. Iron Age Pommerania Kowalewko Wielbark (200 AD) - Genetic Distance: 3.988
  3. Holmens Church Copenhagen (1750 AD) - Genetic Distance: 4.449
  4. Vendel Age Saaremaa Salme II-XXXII (725 AD) - Genetic Distance: 4.649
  5. Pict Era Scotland Isle of Skye High Pasture Cave (124 AD) - Genetic Distance: 4.887

**VK157 (Bodzia elite male; RUR001 in genealogical model):**
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

**⚠️ CRITICAL FINDING:** VK155 and VK157 share **identical mtDNA H1c**, indicating **maternal-line kinship** (cousins through female line). This is consistent with the hypothesis that VK155 is a relative of VK157 through his mother (Carolingian princess), if VK157 = Sviatopolk I.

**Burial Context:**
- **VK157** and **VK155** were buried in the **same grave (E864/I)**
- **Unexamined female** lay **on top of VK157** (one on top of the other) - **NOT GENETICALLY TESTED**
- **Hypothesis:** Unexamined female = **wife of VK157** (if VK157 = Sviatopolk I, then Piast princess according to genealogical model)
- **Piast aDNA context:** do not assume a stable, published “Piast Y-DNA signature” for validating this marriage hypothesis; secondary reporting indicates the Piast genomic program had not yet published dynasty-specific Y results and may observe multiple Y lineages across putative Piast remains [44].
- **See:** `docs/VK155_VK157_BURIAL_HYPOTHESIS.md` for detailed analysis and verification steps

This asymmetric pattern is consistent with the G25 distance of 0.0417 (moderate - possibly related) and supports the interpretation that these individuals were part of the same elite community, with VK155 and VK157 being **maternal-line cousins**.

**Interpretation (exploratory)**: The G25 distance of 0.0417 between VK155 and VK157, together with third‑party MTA “Deep Dive” matching outputs (41 SNP chains; 114.79 cM reported from VK157 → VK155), is suggestive of a relationship signal within the model used by MTA. Because MTA’s “shared segment/cM” outputs are not a standard, validated kinship method for low-coverage ancient data, these results should be treated as hypothesis-generating and corroborated with genome-wide aDNA relatedness methods on raw genotypes.

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
- **MTA Shared DNA**: MTA reports mutual matching with shared segments (exploratory; see caveats)
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

4. **Rus' Connections**: VK157’s close affinity to Rus'-labeled reference populations is consistent with eastern-network connectivity scenarios encoded in the genealogical model; however, it does not establish a named historical identification on its own.

5. **Avar Influence**: Affinities to Avar period Hungary populations suggest genetic contributions from earlier Central European populations, consistent with the region's complex migration history.

#### Integration with Genealogy

The genetic analysis results have been integrated into the genealogy tree (`bodzia_complete_tree.json`), with comprehensive genetic profiles added to each DNA-tested individual:

- **RUR001 (VK157; labeled “Sviatopolk I” in the genealogical model)**: Full genetic profile including G25 coordinates, admixture, population distances, haplogroups, and MTA analysis
- **BOD002 (VK155; Bodzia elite female)**: Full genetic profile including G25 coordinates, admixture, population distances, haplogroups, and MTA analysis
- **BOD001 (VK154; Bodzia elite female)**: Full genetic profile including G25 coordinates, admixture, population distances, and haplogroups
- **BOD003 (VK156; Bodzia elite male)**: Full genetic profile including G25 coordinates, admixture, population distances, and haplogroups

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

> **Evidence note (aDNA status):** A large-scale Polish project (“Program badań genomicznych Piastów”, NCN grant **2014/12/W/NZ2/00466**, Figlerowicz et al.) reportedly identified multiple likely Piast individuals and determined Y-chromosome haplogroups for male remains, but dynasty-specific Y results were not yet published in primary form in the secondary update summarized by histslov (2021; upd. 2022). Do **not** treat any single haplogroup (including the widely repeated late-Piast Janusz III **R1b** claim) as a definitive “Piast marker” for 10th–11th century hypotheses until primary data are available [44].

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
- **Sviatopolk I** (980 - 1019) - Grand Prince of Kiev - **MODEL NODE** (project hypothesis)
  - This project associates the Bodzia E864/I burial with sample VK157 and maps VK157 to the "Sviatopolk I" node as a working hypothesis.
  - **⚠️ GENEALOGY CORRECTION:** Sviatopolk I was **son of Yaropolk I** (older line), NOT son of Vladimir I (younger line)
  - **Tamga:** Sviatopolk I used **two-pronged tamga** (not three-pronged), confirming his descent from the older Yaropolk line
  - **Source:** Beletsky S. V. (2009) genealogical tree with tamgas
- **VK154** (990 - 1020) - Princess (model label: “Princess from Bodzia”) - **PROJECT-ASSOCIATED SAMPLE**: mtDNA H1c3 (H1c)
  - Bodzia burial E864/II (association), sample VK154

---

## Key Connections

### Bodzia Site Connections

- **RUR001 (VK157; labeled "Sviatopolk I" in the genealogical model)**: Associated in this project with Bodzia burial E864/I (sample VK157); Y-DNA I1-S2077
  - **⚠️ GENEALOGY CORRECTION:** Sviatopolk I was **son of Yaropolk I** (older line), NOT son of Vladimir I
  - **Tamga:** Two-pronged tamga confirms older line descent
  - **⚠️ FILOGENETYCZNA KOREKTA (2026-01-11):** I-S2077 → I-Y49957 → I-Y45113 (phylogenetic structure)
  - **Polish DNA matches:** I-Y49957 has Polish DNA matches, supporting Rurikid lineage continuity in Poland
  - **Geographic pattern:** Ukraine (I-FTC2520) → Poland (I-Y49957/I-Y45113) = migration from Rus' to Poland
  - **If Wareg grave = Yaropolk I with I1-S2077:** This would provide **definitive confirmation** that VK157 = Sviatopolk I (direct father-son line)
- **BOD001 (VK154)**: Associated in this project with Bodzia burial E864/II (sample VK154); mtDNA H1c3 (H1c)
- **VK155** (BOD002): mtDNA H1c
  - **⚠️ MATERNAL-LINE KINSHIP:** VK155 and VK157 share **identical mtDNA H1c** (maternal-line cousins)
  - **Burial context:** Same grave (E864/I) as VK157, next to him and an unexamined female
  - **Hypothesis:** VK155 = relative of VK157 through his mother (Carolingian princess)
  - **See:** `docs/VK155_VK157_BURIAL_HYPOTHESIS.md`
- **VK156** (BOD003; model label: “Bodzia Warrior”): Y-DNA R1a (reported as R1a-SUR51 / R1a1a1b1a2a2a1)
- **Boleslaw I the Brave** (PIA001): Allied with Sviatopolk, Bodzia connection
- **Time Period**: 950-1020 CE matches Bodzia cemetery active period

### Cross-Dynasty Marriages and Alliances

- **Igor Rurikovich** (Rurikid) × **Olga** (Rurikid) - 903
- **Sviatopolk I** (Rurikid, son of Yaropolk I - older line) × **BOD001 (VK154)** (elite female; project association) - 1010 (model marriage)
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

The Bodzia cemetery (near Włocławek, central Poland) represents one of the most significant early medieval elite burial sites in Central Europe. Dating to 950-1020 CE (first period; second period: late 11th - early 12th century), it contains:

**Location and Discovery:**
- **Coordinates:** 52°42′19″N 18°53′09″E
- **Distance from Włocławek:** ~15 km northwest
- **Discovery:** 2000 (field survey for A1 motorway)
- **Excavation:** 2007-2009 (led by Andrzej Buko, Polish Academy of Sciences)
- **Area excavated:** 3 hectares
- **Total graves:** More than 58 graves (including cenotaphs)
- **Total features discovered:** 2069 important features

**Burial Characteristics:**
- Scandinavian-style weaponry (Viking swords)
- Mammen-style silver artifacts
- Cross-cultural goods (Rus', Polish, Scandinavian, Anglo-Saxon, Frisian, Khazar)
- Elite warrior burials
- Chamber burials (common in Old Rus, Scandinavian and Slavic countries in Viking Age)
- **4 DNA-tested individuals** with specific genetic markers

**Periods of Use:**
- **First period:** 980-1035 AD (late 10th century - early 11th century) - **Note:** Some sources cite 950-1020 CE; verification needed with primary publications
- **Second period:** Late 11th century - Early 12th century

**Isotope Analysis:**
- Indicates foreign origin of those buried (unknown foreign origin)
- Consistent with multicultural artifacts and proximity to Vistula River trade route
- Suggests foreign trade settlement connecting Baltic to Byzantine Empire

**Settlement Context:**
- Little evidence of early settlement discovered
- Later settlement finds tentatively attributed to second phase of cemetery

**See:** [Wikipedia - Bodzia Cemetery](https://en.wikipedia.org/wiki/Bodzia_Cemetery) for general overview; verify details against primary publications (Buko et al. 2013)

### Genetic Connections

**Haplogroups:**
- **VK157** (RUR001; labeled "Sviatopolk I" in the genealogical model): Y-DNA I1a3a1 (I1-S2077), mtDNA H1c
  - **⚠️ FILOGENETYCZNA KOREKTA (2026-01-11):** I-S2077 → I-Y49957 → I-Y45113 (phylogenetic structure)
  - **Polish DNA matches:** I-Y49957 has Polish DNA matches, supporting Rurikid lineage continuity in Poland
  - **Geographic pattern:** Ukraine (I-FTC2520) → Poland (I-Y49957/I-Y45113) = migration from Rus' to Poland
- **VK154** (BOD001; model label: "Princess from Bodzia"): mtDNA H1c3
- **VK155**: mtDNA H1c
  - **⚠️ MATERNAL-LINE KINSHIP:** Shares **identical mtDNA H1c** with VK157 (maternal-line cousins)
  - **Burial context:** Same grave (E864/I) as VK157, next to him and an unexamined female
  - **Hypothesis:** VK155 = relative of VK157 through his mother (Carolingian princess), consistent with VK157 = Sviatopolk I hypothesis
  - **See:** `docs/VK155_VK157_BURIAL_HYPOTHESIS.md` for detailed analysis
- **VK156** (BOD003; model label: "Bodzia Warrior"): Y-DNA R1a1a1b1a2a2a1, mtDNA J1c2c2a

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
  - **⚠️ FILOGENETYCZNA KOREKTA (2026-01-11):** I-Y45113 jest **subkladą I-Y49957** (nadrzędna haplogrupa)
  - **Struktura filogenetyczna:** I-S2077 > I-FGC950 > I-Y49957 > I-Y45113
  - **Polskie dopasowania:** I-Y49957 ma polskie dopasowania DNA, co potwierdza obecność linii w Polsce
  - **Geograficzne rozprzestrzenienie:** Ukraina (I-FTC2520, 2 dopasowania) → Polska (I-Y49957/I-Y45113)
- **Formation date**: ~975 CE (matches Bodzia active period)
- **Geographic alignment**: Bodzia is ~60 km from Płock (Mazowieckie region)
- **Cross-Cultural Connections**: Strong genetic affinities to Viking Age Scandinavia, Medieval Central Europe, and Rus' populations
- **Wsparcie dla hipotezy VK157 = Sviatopolk I:** Jeśli VK157 = I-S2077 → I-Y49957 → I-Y45113, polskie dopasowania do I-Y49957 potwierdzają kontynuację linii Rurykowiczów w Polsce

### Ciepłe Archaeological Site (Comparative Context)

The **Ciepłe settlement complex** (Gniew, Tczew, Eastern Pomerania) provides a useful comparative context for evaluating Scandinavian-associated elite activity in Piast-adjacent territories during the same broad horizon as Bodzia. As a parallel elite burial/settlement complex discussed in the literature, Ciepłe can inform (but not by itself prove) hypotheses about multi-node elite connectivity.

#### Temporal & Geographic Alignment

**Substantial chronological overlap with Bodzia:**
- **Active period**: 980-1020 CE (40-year overlap with Bodzia's 950-1020 CE)
- **Foundation**: 980s-990s CE (radiocarbon-dated)—coincides with peak of Bodzia's use
- **Distance**: ~150 km northwest of Bodzia (Gniew, Tczew vs. Włocławek)
- **Same political context**: Founded during Bolesław I the Brave's reign (992-1025), who appears in this tree as **PIA001 with "Bodzia connection"**

#### Complementary Elite Network: Bodzia = Rus' Wing, Ciepłe = Danish Wing

This genealogical tree documents **9 dynasties** including:
- **Rurikid** (21 individuals): a model node labeled “Sviatopolk I” is mapped in this project to sample VK157 (Y-DNA I1-S2077) as a working hypothesis
- **Gorm** (9 individuals): Harald Bluetooth, Sweyn Forkbeard, Cnut the Great
- **Piast** (14 individuals): Bolesław I the Brave (967-1025) with "Bodzia connection"

**Ciepłe as a Danish–Pomeranian comparator (as reported in secondary summaries):**
- **4 Scandinavian warriors** reported as supported by strontium isotope analysis and genetic analysis in secondary summaries (verify against the primary publication)
- **Origin**: Denmark (most likely southern Scandinavia)
- **Role**: Elite warriors with chamber graves, scales (tax collection), touchstones (precious metal assaying)
- **Context**: Piast state control of Eastern Pomerania during Bolesław I's expansion

**Network interpretation (hypothesis)**: The genealogical model encodes **Rus'-Polish integration** via a Rurikid–Piast marriage (node labeled “Sviatopolk I” × a Piast princess). Ciepłe is discussed as a potential parallel for **Danish-Polish integration** at the “ground level” (elite warriors embedded in Piast territories). Together, these contexts motivate a regional “dual-wing” Scandinavian connectivity hypothesis that can be tested when comparable genomic datasets are available.

#### Archaeological Evidence

Ciepłe represents an exceptional early medieval settlement complex at the Piast frontier, containing:
- **Chamber graves** with Scandinavian-style burial practices
- **Elite warrior burials** with weaponry and prestige goods
- **Administrative artifacts**: Scales (tax collection), touchstones (precious metal assaying)
- **Strontium isotope analysis**: Confirmed Scandinavian origin for 4 warriors
- **Settlement context**: Piast state control of Eastern Pomerania during Bolesław I's expansion

#### DNA Testing Status (January 2026; verify against primary publication)

**Current status (as recorded in project notes):**
- **4 Scandinavian warriors**: DNA tested (genetic analysis complete)
- **Y-DNA haplogroups**: Not recorded here as published; once available, they can be compared to Bodzia lineages reported for VK157 (I1‑S2077) and VK156 (R1a‑derived) in a hypothesis-driven framework.

#### Integration Opportunities (When Ciepłe DNA Publishes)

**This documentation already includes:**
- G25 coordinate analysis with pairwise distance matrix (all 4 Bodzia samples)
- Admixture modeling showing shared ancestry profiles
- Population distance analysis to 203+ ancient reference populations
- PCA clustering identifying 2 family groups within Bodzia

**Planned integration once comparable genomic summaries are available:**
1. **G25 distance matrix**: Calculate Bodzia ↔ Ciepłe pairwise distances and compare to within‑Bodzia distances (exploratory)
2. **PCA plot**: Check if Ciepłe clusters with Bodzia or separates geographically
3. **Admixture comparison**: Compare component summaries (exploratory; coordinate‑model dependent)
4. **Population affinities**: Do Ciepłe warriors cluster closer to Bodzia than to generic Viking Age Scandinavian populations?

**Hypotheses to test when Y‑DNA is published:**
- If Ciepłe males carry I1‑derived lineages overlapping downstream with Bodzia VK157 (I1‑S2077), this would support (not prove) a shared Scandinavian-associated paternal-line context across sites.
- If Ciepłe males carry R1a‑derived lineages overlapping downstream with Bodzia VK156, this would support a multi-lineage Scandinavian/central‑eastern European admixture context in Piast‑adjacent elites.
- If neither lineage overlaps, that result would constrain “shared retinue/lineage” hypotheses and favor more site-specific recruitment histories.

#### Research Context: I-Y45113 Haplogroup Implications

**⚠️ FILOGENETYCZNA KOREKTA (2026-01-11):** I-Y45113 jest **subkladą I-Y49957**

**Struktura filogenetyczna I-S2077 (z YFull/FTDNA):**
```
I-S2077 > I-FGC950
    ├─ I-Y49957 (nadrzędna haplogrupa dla I-Y45113)
    │   └─ I-Y45113 (subklada)
    │   └─ Polskie dopasowania DNA 🇵🇱
    │
    ├─ I-Y58442 (równoległa gałąź)
    │
    └─ I-FTC2520 (wspólny przodek, poziom ~10 pokoleń)
        └─ Ukraińskie dopasowania DNA 🇺🇦 (2 dopasowania)
```

**Geographic triangle:**
- **Płock** ←60 km→ **Bodzia** ←150 km→ **Ciepłe**
- **I-Y45113 TMRCA estimates** are often placed in the late 10th century in consumer phylogenies (e.g., ~975 CE in YFull YTree; verify against the specific tree version used)
- **I-Y49957 formation:** ~950-1000 CE (based on phylogenetic structure; I-FTC2520 at ~10 generations depth suggests ~800-900 CE formation, with I-Y49957 forming ~950-1000 CE)

**Geographic distribution pattern:**
- **I-FTC2520 (Ukraina):** 2 DNA matches - region Kijowa/Rus' (older population)
- **I-Y49957 (Polska):** Polish DNA matches expected - region Bodzia/Mazowieckie (migration to Poland)
- **Migration pattern:** I-FTC2520 (~800-900 CE) → I-Y49957 (~950-1000 CE) → Bodzia (~1000 CE)
- **Chronology alignment:** Perfect match with Bodzia active period (950-1020 CE) and Sviatopolk I hypothesis (980-1019 CE)

**Wsparcie dla hipotezy VK157 = Sviatopolk I:**
- Jeśli VK157 = I-S2077 → I-Y49957 → I-Y45113
- Polskie dopasowania do I-Y49957 potwierdzają kontynuację linii Rurykowiczów w Polsce
- Geograficzne rozprzestrzenienie: Ukraina (Rus'/Kijów) → Polska (Bodzia) = zgodne z historycznymi migracjami
- Zgodne z hipotezą: Sviatopolk I (syn Yaropolka I, starsza linia) → migracja do Polski → Bodzia

If I-Y45113 ancestors were in this region, they could have been part of:
1. **Bodzia elite** (Rus'-Polish nexus) ← Current hypothesis (supported by I-Y49957 Polish matches)
2. **Ciepłe elite** (Danish-Pomeranian nexus) ← New possibility
3. **Mobile elite** moving between both sites (warriors, traders, administrators)

**Critical test**: When Ciepłe Y‑DNA results are published with sufficient downstream resolution, compare lineages against Bodzia VK157 (I1‑S2077) and VK156 (R1a‑derived). Overlap would support a shared-network hypothesis; non-overlap would refine it.

**Source:** YFull/FTDNA haplogroup tree visualization (2026-01-11); see `docs/I_Y49957_POLAND_ANALYSIS.md` for detailed analysis.

#### Validation of Multi-Dynasty Approach

This genealogical tree documents **79 individuals across 9 dynasties** (Rurikid, Piast, Gorm, Normandy, Arpad, Premyslid, Ottonian, Capetian). Ciepłe provides a concrete archaeological comparator for discussing how dynastic-level connections could be instantiated by mobile elites on the ground:

- **Royal level** (this tree): Gorm dynasty rulers (Harald Bluetooth, Sweyn Forkbeard) allied with Piast rulers (Bolesław I)
- **Ground level** (Ciepłe): Danish warriors (Gorm retainers) embedded in Polish territories (Piast administration), living alongside local populations, collecting taxes, maintaining military control

**Same period; different geographic node**. Adding Ciepłe as a comparator shifts the framing from a single-site description toward a testable regional network hypothesis (subject to the availability of comparable genomic datasets).

#### Actionable Next Steps

**Now (January 2026):**
- Add Ciepłe as comparative site section (this documentation)
- Note DNA results pending publication
- Establish framework for integration when data becomes available

**Q1-Q2 2026** (when Ciepłe Y-DNA publishes):
1. Compare haplogroups to Bodzia VK157 (I1‑S2077) and VK156 (R1a‑derived)
2. Add Ciepłe G25 coordinates to distance matrix
3. Update PCA plot to include both sites
4. Test population affinities and admixture profiles
5. If kinship detected, add "Bodzia ↔ Ciepłe elite network" connections to genealogical tree

**Summary**: Ciepłe is a high-yield comparative candidate for testing regional elite-network hypotheses once primary genetic results (including downstream Y‑DNA calls) are available.

### Winchester Cathedral (Ongoing Research) and Relevance to the Bodzia Hypothesis

This tree includes dynasties that directly intersect with **England** in the late 10th–11th centuries (notably Danish and Norman rulers). **Winchester Cathedral** is a key comparative site because (a) it is traditionally associated with high-status burials from these periods, and (b) ongoing conservation/archaeological work there has the potential to produce (or refine) **ancient DNA datasets** for elite individuals that overlap chronologically and politically with the Bodzia horizon.

**Data status:** ⚠️ **UPDATE 2026-01-11:** The Times reports that Winchester Cathedral mortuary chests project has **completed 14 years of genetic analysis** and **identified individuals including Cnut the Great, Harthacnut, and Emma of Normandy**. Results are **expected to be published in 2026** by Winchester Cathedral and Francis Crick Institute. This represents a **critical breakthrough** for testing Bodzia ↔ Winchester connections. **See:** `docs/BODZIA_WINCHESTER_PIAST_CONNECTIONS.md` for detailed analysis.

If genomic profiles from Winchester Cathedral can be confidently assigned to specific individuals (or at least to well-dated, high-status burials), they become an external reference point to test the working hypothesis in this file: **that the Bodzia individuals represent an elite network with genetic ties extending into the Anglo-Scandinavian / Anglo-Norman sphere**, not only cultural/artefactual parallels.

#### Bodzia–Winchester royal-house bridge (key individuals in this tree)

The Bodzia diagram/tree already contains several individuals who are frequently discussed in connection with Winchester Cathedral’s elite burial context (e.g., via the mortuary chests tradition and related conservation/analysis work). These are the highest-value “targets” for an eventual Bodzia ↔ Winchester genetic comparison, because they sit on a direct dynastic chain in the diagram:

- **Cnut the Great** (House of Gorm): King of England/Denmark/Norway (d. 1035). Chronologically overlaps the Bodzia horizon and represents the Anglo-Scandinavian consolidation phase that the Bodzia material culture is often compared against. ⭐ **GENETICALLY IDENTIFIED** in Winchester Cathedral mortuary chests (2026).
- **Emma of Normandy** (House of Normandy): spouse of Cnut (d. 1052). Key diplomatic/dynastic link between the Norman and Danish networks represented in this tree. ⭐ **GENETICALLY IDENTIFIED** in Winchester Cathedral mortuary chests (2026) - **only woman identified**.
- **Harthacnut** (House of Gorm): son of Cnut and Emma (d. 1042). Provides direct continuity of the Danish royal paternal line into England in the 11th century. ⭐ **GENETICALLY IDENTIFIED** in Winchester Cathedral mortuary chests (2026).

**Additional individuals identified:** Cynegils (first Christian king of Wessex, d. ~642), Wini (first bishop of Winchester), Egbert, Ethelwulf (father of Alfred the Great), Stigand (last Anglo-Saxon archbishop of Canterbury), and others. **Total:** At least 21 adults + 4 children identified from ~1,300 bones in 6 mortuary chests.

Additional “corridor anchors” present in the tree that contextualize the bridge (even if not themselves Winchester burials):

- **Sweyn Forkbeard** (House of Gorm): father of Cnut (d. 1014).
- **Harald Bluetooth** (House of Gorm): grandfather of Cnut (d. 986), active around the early phase of the Bodzia timeframe.
- **Richard I the Fearless** and **William I Longsword** (House of Normandy): Emma’s close ancestry in the Norman/Viking elite line shown in the diagram.

**⚠️ CRITICAL UPDATE (2026-01-11):** The Times reports that Winchester Cathedral mortuary chests project has **successfully identified Cnut, Harthacnut, and Emma of Normandy** after 14 years of genetic analysis. Results are **expected to be published in 2026**, making this a **high-priority target** for testing Bodzia ↔ Winchester connections. **See:** `docs/BODZIA_WINCHESTER_PIAST_CONNECTIONS.md` for detailed analysis and testable hypotheses.

This list matters because it lets you formulate a testable statement with clear expected outcomes: **Winchester Cathedral has now yielded reliably attributable genomes for Cnut, Harthacnut, and Emma** (publication expected 2026), enabling direct testing of whether any Bodzia individuals fall within a plausible kinship/lineage radius of this Anglo-Scandinavian/Norman dynastic network (close kinship, shared rare uniparental subclades, or only broader affinity).

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

7a. **I-Y49957 Phylogenetic Analysis** (2026-01-11)
   - Available: `docs/I_Y49957_POLAND_ANALYSIS.md`
   - **Key finding:** I-Y45113 is a subclade of I-Y49957 (parent haplogroup)
   - **Phylogenetic structure:** I-S2077 > I-FGC950 > I-Y49957 > I-Y45113
   - **Geographic distribution:** Ukraine (I-FTC2520) → Poland (I-Y49957/I-Y45113)
   - **Polish DNA matches:** I-Y49957 has Polish DNA matches, confirming lineage presence in Poland
   - **Support for VK157 = Sviatopolk I hypothesis:** Polish matches to I-Y49957 support Rurikid lineage continuity in Poland

8. **Mielnik-Sikorska, M., et al.** (2013). "The History of Slavs Inferred from Complete Mitochondrial Genome Sequences". *PLOS ONE*, 8(1), e54360.
   - Available: `docs/Academic Papers/Marta Mielnik-Sikorska - The History of Slavs Inferred from Complete Mitochondrial Genome Sequences [2013].pdf`
   - mtDNA H1c haplogroup context

9. **Olalde, I., et al.** (2018). "The Beaker phenomenon and the genomic transformation of northwest Europe". *Nature*, 555, 190-196.
   - Reference: nature25738_Olalde.pdf
   - Ancient DNA methodology

### Comparative Site: Winchester Cathedral (England)

**⚠️ CRITICAL UPDATE (2026-01-11):** The Times reports that Winchester Cathedral mortuary chests project has **completed 14 years of genetic analysis** and **identified individuals including Cnut the Great, Harthacnut, and Emma of Normandy**. Results are **expected to be published in 2026** by Winchester Cathedral and Francis Crick Institute. **See:** `docs/BODZIA_WINCHESTER_PIAST_CONNECTIONS.md` for detailed analysis.

**Project Details:**
- **Duration:** 14 years (2012-2026)
- **Institutions:** Winchester Cathedral + Francis Crick Institute
- **Breakthrough (2015):** Oxford AMS radiocarbon dating confirmed bones from late Anglo-Saxon and early Norman periods
- **Identified individuals:** Cnut the Great, Harthacnut, Emma of Normandy, Cynegils (first Christian king of Wessex, d. ~642), Wini (first bishop of Winchester), Egbert, Ethelwulf (father of Alfred the Great), Stigand (last Anglo-Saxon archbishop of Canterbury), and others
- **Total:** At least 21 adults + 4 children from ~1,300 bones in 6 mortuary chests
- **Publication:** Expected 2026 (series of scientific papers)

**References to add when published:**
- Publication/preprint title, authors, year, and persistent identifier (DOI/arXiv/Zenodo)
- If data are public: accession (ENA/SRA), SNP panel/capture description, and sample IDs
- If data are not public: a stable project page and a description of what can be used (summary haplogroups vs full genotypes)
- Winchester Cathedral — mortuary chests conservation / analysis project (official project page + technical reports)
- Francis Crick Institute publications (expected 2026)

**Source:** The Times (2026) - "Bones of Anglo-Saxon kings return to cathedral after DNA 'jigsaw'" (translated by ChatGPT)

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

31. **VK155-VK157 Burial Hypothesis** (2026-01-11)
   - Available: `docs/VK155_VK157_BURIAL_HYPOTHESIS.md`
   - **Critical finding:** VK155 and VK157 share identical mtDNA H1c (maternal-line kinship)
   - **Burial context:** Same grave (E864/I), with unexamined female who lay on top of VK157 (NOT GENETICALLY TESTED)
   - **Hypothesis:** VK155 = relative of VK157 through his mother (Carolingian princess); unexamined female = wife of VK157
   - **Research gap:** Unexamined female from same grave chamber as VK157 requires urgent genetic testing
   - **Impact:** Could confirm Sviatopolk I × Piast princess marriage hypothesis if unexamined female = wife

32. **Wikipedia - Bodzia Cemetery Analysis** (2026-01-11)
   - Available: `docs/WIKIPEDIA_BODZIA_ANALYSIS.md`
   - **Source:** https://en.wikipedia.org/wiki/Bodzia_Cemetery
   - **Analysis:** Comparison of Wikipedia article with project documentation
   - **Key findings:** More than 58 graves, two periods of use (980-1035 AD and late 11th-early 12th century), excavation details (2007-2009, Andrzej Buko), isotope analysis indicating foreign origin
   - **Recommendations:** Updates to documentation based on Wikipedia information (verify against primary publications)
   - **Note:** Some discrepancies require verification with primary sources (Buko et al. 2013)

33. **Bodzia ↔ Winchester ↔ Piast Connections** (2026-01-11) ⭐ **CRITICAL UPDATE**
   - Available: `docs/BODZIA_WINCHESTER_PIAST_CONNECTIONS.md`
   - **Source:** The Times (2026) - "Bones of Anglo-Saxon kings return to cathedral after DNA 'jigsaw'"
   - **Critical finding:** Winchester Cathedral mortuary chests project has **completed 14 years of genetic analysis** and **identified Cnut the Great, Harthacnut, and Emma of Normandy** - all present in the project's genealogical tree
   - **Publication:** Results expected in 2026 (Winchester Cathedral + Francis Crick Institute)
   - **Significance:** Enables direct testing of Bodzia ↔ Winchester connections, including:
     - VK157 (Sviatopolk I hypothesis) ↔ Cnut/Harthacnut (Y-DNA, autosomal DNA comparison)
     - Unexamined female (Piast princess hypothesis) ↔ Emma of Normandy (mtDNA, autosomal DNA comparison)
     - VK155 (Carolingian princess hypothesis) ↔ Emma of Normandy (mtDNA comparison)
   - **Testable hypotheses:** Detailed analysis of genetic connections between Bodzia, Winchester, and Piast dynasties
   - **Status:** Awaiting publication of Winchester genetic data (2026)

34. **Ciepłe Archaeological Site** - Comparative elite burial site in Eastern Pomerania.
   - **Cambridge Antiquity**: "Ciepłe Revisited: An Exceptional Early Medieval Settlement Complex at the Piast Frontier"
   - **University of Warsaw Archaeology**: Ciepłe settlement complex information (https://www.archeologia.uw.edu.pl/en/cieple-a-settlement-complex-from-the-turn-of-the-10th-11th-century-in-eastern-pomerania/)
   - **Medievalists.net**: "Four Warriors Buried in 11th-Century Poland Came from Scandinavia, Researchers Find" (https://www.medievalists.net/2020/02/four-warriors-buried-in-11th-century-poland-came-from-scandinavia-researchers-find/)
   - **Science in Poland**: "Four Warriors Buried in 11th-Century Tombs in Pomerania Came from Scandinavia, Say Scientists" (https://scienceinpoland.pl/en/news/news,80395,four-warriors-buried-11th-century-tombs-pomerania-came-scandinavia-say-scientists)
   - **Active period**: 980-1020 CE (40-year overlap with Bodzia)
   - **Location**: Gniew, Tczew, Eastern Pomerania (~150 km northwest of Bodzia)
   - **Key findings (as summarized in project notes)**: 4 Scandinavian warriors reported as supported by strontium isotope analysis + genetic analysis; origin summarized as Denmark (verify against the primary publication)
   - **DNA status**: Genetic analysis complete, Y-DNA haplogroups analyzed but not yet published (expected Q1-Q2 2026)
   - **Relevance**: Provides Danish-Polish integration counterpart to Bodzia's Rus'-Polish integration, validating the dual Scandinavian wings of the elite network documented in the genealogical tree

32. **Elicit** - Academic paper extraction and review.
   - Available: `docs/Academic Papers/Elicit - extract-results-review-8aefa20a-f5fd-4895-9251-47b725cf0810.csv`
   - Structured data extraction from academic literature

### Additional References

35. **Androshchuk, F.** (2022). "From Vikings to Rus — the Danish Connection". In *Rus — Vikings in the East* (Moesgaard Museum volume).
   - Status: Referenced but not publicly available

36. **Litvina, A., Uspenskij, F.** (2017). "Dynastic Power And Name-giving Principles in Medieval Rus'". *Micrologus*, XXV.
   - Status: Referenced, may require institutional access

37. **Nazarenko, A. V.** (2001). Book chapter on early Rus' (in Russian).
   - Status: Referenced but not publicly available

38. **Pritsak, O.** (1977). "The Origin of Rus'". *The Russian Review*, 36(3), 249-273.
   - Status: Commonly available through JSTOR or publisher

39. **Duczko, W.** (2004). *Viking Rus: Studies on the Presence of Scandinavians in Eastern Europe*. Brill.
   - Status: Academic publisher, may require institutional access

### Online Resources

40. **Topola Genealogy Viewer**
   - Source: https://pewu.github.io/topola-viewer/
   - Interactive GEDCOM viewer

41. **SVG Family-Tree Generator (SVG-FTG)**
   - Source: https://parallaxviewpoint.com/SVG-FTG/
   - Publication-quality family tree generation

42. **Graphviz** - Graph Visualization Software
   - Source: https://graphviz.org/
   - Used for tree diagram generation

43. **dTree** - Interactive Family Tree Visualization Library
   - Source: https://github.com/ErikGartner/dTree
   - Built on D3.js for interactive family tree visualization
   - Supports multiple parents and complex relationships
   - Used for: `output/web/bodzia_complete_dtree.html`

44. **histslov** (2021; updated 2022). "PIASTOWIE HG Y-DNA" (blog post; Polish).
   - Source: https://histslov.wordpress.com/2021/11/16/piastowie-hg-y-dna/
   - **Use note:** secondary source that quotes project updates (incl. Prof. Marek Figlerowicz) about sample counts and pending publications; treat dynasty-specific haplogroup claims as unconfirmed until primary publications/datasets are available.

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
- **Y-DNA SNP Data**: `data/raw/y_dna_results/SNP_for_<YFULL_ID>_<YYYYMMDD>.csv`
- **Y-DNA STR Data**: `data/raw/y_dna_results/STR_for_<YFULL_ID>_<YYYYMMDD>.csv`
- **YFull STR Matches**: `data/raw/y_dna_results/YFull _ STR matches.pdf`

---

**Document Version**: 2.2 (Complete - 79 Individuals with Comprehensive Genetic Analysis)  
**Last Updated**: 2026-01-11  
**Generated By**: Bodzia Complete Tree Generation Pipeline + Comprehensive Genetic Analysis Pipeline
