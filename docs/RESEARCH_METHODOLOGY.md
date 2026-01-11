# Research Methodology

## Overview

This document outlines the methodology for genealogical DNA analysis in this workspace.

## Data Sources

### Y-DNA Data
- **Source:** FamilyTreeDNA Big Y-700
- **Format:** VCF files, Y-STR haplotypes
- **Storage:** `data/raw/y_dna_results/`

### Autosomal DNA
- **Source:** 23andMe, MyTrueAncestry, etc.
- **Format:** CSV, JSON
- **Storage:** `data/raw/autosomal/`

### Genealogical Records
- **Source:** Parish records, census data, family trees
- **Format:** GEDCOM, CSV
- **Storage:** `data/raw/genealogical/`

## Analysis Workflow

### Phase 1: Data Collection
1. Gather all DNA test results
2. Collect genealogical records
3. Download reference data (ISOGG tree, ancient DNA samples)

### Phase 2: Data Processing
1. Parse and normalize DNA data
2. Parse genealogical records
3. Validate data quality

### Phase 3: Analysis
1. Y-DNA haplogroup assignment
2. SNP analysis
3. TMRCA calculations
4. Ancient DNA matching
5. Admixture analysis

### Phase 4: Validation
1. Cross-reference DNA with genealogical records
2. Validate family tree relationships
3. Verify hypotheses

### Phase 5: Reporting
1. Generate visualizations
2. Create reports
3. Document findings

## Quality Control

- **Data Validation:** Check for missing values, outliers
- **Cross-Validation:** Compare multiple data sources
- **Statistical Significance:** Use appropriate statistical tests
- **Documentation:** Document all assumptions and methods

## Tools and Methods

### Y-DNA Analysis
- ISOGG tree for haplogroup assignment
- Y-STR mutation rates for TMRCA
- SNP analysis for subclade determination

### Ancient DNA Matching
- Genetic distance calculations
- Population structure analysis
- Admixture modeling

### Genealogical Analysis
- GEDCOM parsing and validation
- Relationship verification
- Migration pattern analysis

## References

- ISOGG Y-DNA Tree: https://isogg.org/tree/
- YFull Y-DNA Tree: https://www.yfull.com/
- FamilyTreeDNA: https://www.familytreedna.com/
