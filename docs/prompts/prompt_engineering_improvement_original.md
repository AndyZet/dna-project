# PROMPT ENGINEERING ANALYSIS & IMPROVEMENT STRATEGY

## Executive Summary

Your original prompt **lacks critical specifications** for document structure, audience, and hypothesis-validation framework. The revised prompt below transforms it from a generic review request into a **falsifiable research proposal format** aligned with academic standards (Nature, PNAS, *Journal of Archaeological Science*) while optimizing for readability and cognitive load.

**Key improvements**: (1) Explicit IMRaD-inspired structure, (2) Hypothesis specification with falsifiability criteria, (3) Readability metrics and design standards, (4) Audience specification, (5) Actionable quality gates.

---

## ORIGINAL PROMPT
```
"Analyse and review attached. Suggest enhancements. Document should be 
readable, consistent, easy to read, easy to internalise, in line with 
most recent academic papers, it should present hypothesis to be verified"
```

---

## ANALYSIS OF LIMITATIONS

### 1. Vague Scope
- **"Analyse and review attached"** → What aspects? (structure, content, methods, claims?)
- **"Suggest enhancements"** → To what goal? (accuracy, clarity, novelty?)
- No clarity on which "recent academic papers" serve as models

### 2. Undefined Standards
- **"Readable, consistent, easy to read"** → These are subjective and overlapping
- **"Easy to internalise"** → Cognitive load target unspecified (target audience?)
- **"In line with most recent academic papers"** → Which discipline, journal, methodological tradition?

### 3. Weak Hypothesis Requirement
- **"Present hypothesis to be verified"** → No mention of:
  - Falsifiability criteria
  - How hypotheses connect to data/evidence
  - Testability roadmap
  - Expected outcomes or null scenarios

### 4. Missing Context
- No statement of document purpose (internal working document? journal submission? public communication?)
- No audience profile (peer academics? funding agencies? genealogy community? general public?)
- No constraints (word count, format, visualization requirements?)
- No timeline for implementation

---

## REVISED COMPREHENSIVE PROMPT

### TIER 1: PURPOSE & AUDIENCE (Add this first)

```
PURPOSE:
Transform your "Bodzia Complete Tree Documentation" into a publication-ready 
scholarly report suitable for peer-reviewed academic journals in either:
  • Medieval archaeology and genetics (Nature, *PNAS*, *Journal of Archaeological Science*)
  • Genetic genealogy (American Journal of Human Genetics)
  • Early medieval history (*Early Medieval Europe*, *Speculum*)

AUDIENCE TIER SYSTEM (structure document for all, but optimize for Tier 1):
  
  Tier 1 [PRIMARY]: Peer-reviewing academics in:
    - Medieval archaeology (depositional site analysis, stratigraphy, grave goods)
    - Ancient DNA (admixture modeling, G25 methodology, haplogroup phylogeny)
    - Genetic genealogy (kinship inference, mutation rates, TMRCA estimation)
    
  Tier 2 [SECONDARY]: Historians of Early Medieval Europe familiar with:
    - Rus' ethnogenesis and Piast state formation (950–1050 CE)
    - Viking Age settlement archaeology
    - Cross-cultural elite networks in Central Europe
    
  Tier 3 [TERTIARY]: Educated general audience interested in:
    - Medieval royal genealogy
    - Forensic genetics applications
    - Digital humanities (genealogical data visualization)

OPTIMIZATION: Structure main narrative for Tier 1 rigor; use sidebars/boxes 
for Tier 2 historical context; provide glossary/appendix for Tier 3.
```

### TIER 2: DOCUMENT STRUCTURE (Specify format)

```
ARCHITECTURE:
Adopt modified IMRaD structure (Introduction–Methods–Results–Arguments–Discussion) 
merged with genealogical report standards:

1. EXECUTIVE SUMMARY (250–300 words)
   - One-sentence thesis statement
   - Why Bodzia matters (archaeological significance)
   - Key genetic finding (3–4 bullet points)
   - Testable hypotheses (list 2–3 numbered)
   - Expected journal impact

2. INTRODUCTION (800–1000 words)
   2.1 The Bodzia Problem
       - Why a 10th–11th century elite cemetery in Poland is a rare genetic resource
       - Historical context: Rus'-Polish-Scandinavian contact zone (950–1020 CE)
       - Current state of Viking Age genetics (cite 3–5 recent genome papers)
       - Gap: How do elite males like "Sviatopolk I" fit into broader population history?
   
   2.2 This Study's Questions
       - Main hypothesis (stated as falsifiable proposition)
       - Secondary hypotheses (branching logic: if H1 true, predict H2)
       - Null hypothesis (what would falsify your claims?)
       - Experimental design (how you test each hypothesis)

3. DATA & METHODS (800–1200 words)
   3.1 Sampling & Provenance
       - Each individual (VK155, VK157, VK154, VK156) with burial context, dating
       - Why these 4 samples chosen from larger cemetery?
       - Taphonomy & preservation quality
       - Commingling risk assessment
   
   3.2 Laboratory Methods
       - DNA extraction & library prep (ancient DNA handling; damage profile; mtDNA vs autosomal)
       - Sequencing approach (shotgun vs capture; coverage; reference build)
       - Contamination screening (endogenous content %, contaminant assignment)
       - Reporting: How many SNPs genotyped? Pseudo-haploid vs diploid calls?
   
   3.3 Analytical Framework
       - G25 coordinates: justification, reference populations, distance metrics
       - Admixture modeling: software, reference set, model fit statistics
       - Kinship inference: methods, confidence intervals, relationship categories
       - PCA & population affinities: methodology, interpretation thresholds
       - Why MTA matches useful (and their limitations)

4. RESULTS (1000–1500 words)
   4.1 Pairwise Genetic Distances
       - Table: all pairs (VK155 ↔ VK157, VK155 ↔ VK154, etc.)
       - Interpretation: which pairs fall into "close", "moderate", "distant" categories?
       - How do within-site distances compare to expected kinship thresholds?
   
   4.2 Admixture & Ancestry
       - Table: VK155, VK157, VK154, VK156 admixture proportions (Yamnaya, Neolithic, WHG)
       - Visual: stacked bar chart or ternary plot
       - Key observation: are all 4 samples homogeneous (cohesive elite) or heterogeneous (diverse recruits)?
   
   4.3 Population Affinities
       - PCA: plot showing Bodzia samples in context of reference populations
       - Closest ancient neighbors: Gotland (Scandinavian?), Gnezdovo (Rus'?), Medieval Germany?
       - Interpretation: does clustering match archaeological / historical expectations?
   
   4.4 Y-DNA & mtDNA Haplogroups
       - VK157 Y-DNA I1-S2077 + mtDNA H1c: what is downstream phylogeny? Rare or common lineage?
       - VK156 Y-DNA R1a-SUR51: geographic & temporal distribution in medieval Europe?
       - VK155 + VK154 mtDNA H1c: evidence for family clustering? (or common in elite females?)
   
   4.5 Family Structure from Genetic Data
       - VK154 ↔ VK156 distance (0.0281): consistent with 1st? 2nd? degree kinship?
       - VK155 ↔ VK157 distance (0.0417): mother-son? Cousins? Unrelated but same social network?
       - Joint interpretation with archaeological context (burial proximity, grave goods, bone analysis)

5. ARGUMENTS (800–1000 words)
   5.1 What Bodzia Tells Us About Elite Networks
       - Central thesis: Bodzia is a "window" into Scandinavian-Rus'-Polish cross-cultural elite formation
       - Evidence: (a) genetic homogeneity → cohesive social group; (b) Gotland/Gnezdovo affinities → connected to major networks
   
   5.2 Testing the Hypotheses
       - H1: "Sviatopolk I (VK157) is genetically connected to Rus' populations" → supported by Gnezdovo affinity?
       - H2: "Bodzia represents a 'frontier elite' (not random mixed group)" → supported by genetic clustering?
       - H3: "I-Y45113 ancestors participated in early medieval elite networks" → falsifiable by comparison to Ciepłe?
   
   5.3 Alternative Interpretations & Limitations
       - What would falsify your main claims?
       - Limitations: (low-coverage aDNA, commingling risk, limited sample size, reliance on modern reference populations)
       - How robust are your conclusions? (sensitivity analysis, error bars, confidence levels)

6. DISCUSSION (1000–1200 words)
   6.1 Synthesis: Bodzia in Broader Context
       - How does this work fit into existing literature on Viking Age genetics, Rus' ethnogenesis?
       - Novel contributions: (e.g., first genome-wide kinship within a single elite cemetery + genealogical tree validation?)
   
   6.2 Comparative Sites & Future Work
       - Ciepłe (Danish elite, ~150 km away, contemporary): how will new Y-DNA data test or refine hypotheses?
       - Winchester Cathedral: potential for testing Gorm dynasty connections (pending aDNA release)
       - Roadmap: what next samples, methods, or analyses are needed?
   
   6.3 Broader Implications
       - What does Bodzia tell us about power consolidation in early medieval Central Europe?
       - Gender roles in elite migration networks (matrilineal vs patrilineal pathways)?
       - Scale & timing: how many elite networks existed? How interconnected were they?

7. CONCLUSIONS (300–400 words)
   - Restate main findings concisely (3–4 sentences)
   - Connect back to original research questions
   - State what is proven, what is probable, what remains uncertain
   - Implications for future research

8. REFERENCES (comprehensive, hyperlinked)
   - Academic papers (alphabetical, full citations)
   - Data sources (G25, MTA, FamilyTreeDNA URLs)
   - Methodology papers (PCA, admixture, kinship inference)
   - Minimize self-citations unless necessary

9. APPENDICES (optional but recommended)
   - A. Glossary (G25, TMRCA, nMonte, MTA, etc.)
   - B. Detailed Population Tables (all closest neighbors for each sample)
   - C. Phylogenetic Trees (Y-DNA and mtDNA, downstream SNPs)
   - D. Sensitivity Analysis (results with different reference populations, distance thresholds)
   - E. Complete Genealogical Data (CSV/JSON export of 79 individuals + DNA assignments)
```

### TIER 3: QUALITY STANDARDS (Specify metrics)

```
READABILITY STANDARDS:
✓ Gunning Fog Index: 13–15 (appropriate for peer-reviewed academic audience)
✓ Average sentence length: 15–18 words (mix short + complex sentences)
✓ Passive voice: <25% (favor active "We found..." over "It was found that...")
✓ Jargon density: define every specialized term first mention
✓ Visual hierarchy: use H1 (title) → H2 (major sections) → H3 (subsections) → H4 (definitions)

CONSISTENCY STANDARDS:
✓ Terminology: lock sample IDs (VK157, not "Sviatopolk I" alone; use "Sviatopolk I (VK157)" on first mention)
✓ Units: all distances in same metric (e.g., Euclidean G25 distance, 0–0.1 scale)
✓ Dates: use "950–1020 CE" format consistently (not "950-1020 AD" or "10th–11th century")
✓ Abbreviations: expand on first mention (e.g., "My True Ancestry (MTA)")
✓ Formatting: tables have consistent caption style, color coding explained in figure legends

STRUCTURE CHECKLIST (for each section):
✓ Opening sentence = topic sentence (reader knows section purpose)
✓ First paragraph(s) = context (why this matters)
✓ Middle paragraphs = evidence (data, references, logic)
✓ Final paragraph = conclusion (what does it mean?)
✓ Every figure/table: numbered, captioned, referenced in text ("see Figure 2")
✓ Every table: <5 columns if possible (more → rotate to appendix or separate visualization)

HYPOTHESIS SPECIFICATION (for each claim):
✓ Null hypothesis (H0): explicitly stated
✓ Alternative hypothesis (Ha): prediction + how to test
✓ Evidence threshold: what counts as "support"? (p < 0.05? genetic distance < 0.03? shared rare SNP?)
✓ Falsifiability: what data would disprove the claim?
✓ Confidence: statement of certainty (proven, probable, plausible, speculative)
```

### TIER 4: HYPOTHESIS PRESENTATION (Add subsection to methods)

```
TESTABLE HYPOTHESES FRAMEWORK:

H1: "Bodzia represents a genetically cohesive elite social group"
    Null hypothesis (H0): Bodzia individuals are genetically unrelated (random assemblage)
    Test: G25 pairwise distances + admixture homogeneity
    Evidence threshold: Mean distance VK1-VK4 < 0.045; admixture CV < 5%
    Expected result: Support (all pairs 0.0281–0.0425) ✓ PROVISIONAL SUPPORT
    Falsification scenario: If genetic distances > 0.10, supports H0 (not a cohesive group)

H2: "Sviatopolk I (VK157) belongs to Rus' elite networks (not Scandinavian mercenaries)"
    Null hypothesis (H0): VK157 clusters with Viking Age Gotland or Danish populations only
    Test: Population affinity ranking; G25 distance to Gnezdovo < distance to Gotland?
    Evidence threshold: Gnezdovo distance ≤ 0.0443; historical plausibility (documented Rus' connections)
    Expected result: VK157 closest to Sandomierz (0.0321), then Gotland (0.0333), Gnezdovo (0.0443)
    Interpretation: **Moderate support** — closer to other Polish sites than expected, supporting Rus' hypothesis
    Falsification scenario: If VK157 clusters with Gotland/Uppsala (distance < 0.02), supports pure Scandinavian model

H3: "I-Y45113 haplogroup ancestors participated in Early Medieval elite networks"
    Null hypothesis (H0): I-Y45113 lineage is modern formation unrelated to Bodzia elite
    Test: Haplogroup assignment (does VK157 carry I1-S2077, a likely I-Y45113 parent?); spatial clustering (Bodzia–Płock–Ciepłe triangle)
    Evidence threshold: (a) VK157 Y-DNA = I1-derived; (b) TMRCA ~975 CE (matches Bodzia horizon); (c) Ciepłe Y-DNA ≠ I1-S2077 (rules out single-founder model)
    Expected result: **PARTIAL SUPPORT** — VK157 is I1-S2077 ✓; TMRCA ~975 CE ✓; Ciepłe Y-DNA not yet published (pending Q1-Q2 2026)
    Falsification scenario: If Ciepłe warriors all carry R1a1 or unrelated haplogroups, suggests I-Y45113 lineage is localized to Bodzia/Rus' context only

H4: "Bodzia and Ciepłe represent dual wings of an Early Medieval Scandinavian-Polish elite network"
    Null hypothesis (H0): Bodzia and Ciepłe are independent, unconnected burial sites
    Test: Genetic distance (Bodzia individual ↔ Ciepľe individual); Y-DNA haplogroup matching; admixture profile similarity
    Evidence threshold: Bodzia ↔ Ciepłe pairwise distance 0.02–0.05 (same range as Bodzia internal distances); shared haplogroup subclades; admixture profile correlation > 0.9
    Expected result: **TESTABLE 2026** — awaiting Ciepłe Y-DNA publication
    Falsification scenario: If Bodzia ↔ Ciepłe distances > 0.10, suggests genetically distinct populations (H0 supported)

CONFIDENCE LEVELS (for all conclusions):
    ✓ PROVEN: Strong statistical support + multiple independent lines of evidence + peer review completed
    ◐ PROBABLE: Supported by data but limited sample size or single method; needs validation
    ◑ PLAUSIBLE: Consistent with data but not definitive; alternative explanations exist
    ◒ SPECULATIVE: Suggested by data but requires future work to confirm; low confidence
    
APPLY THIS FRAMEWORK to each major claim in your document.
```

### TIER 5: VISUALIZATION & DESIGN (Specify standards)

```
FIGURES (create or redesign):
✓ Figure 1: Bodzia cemetery map with burial locations of VK155, VK157, VK154, VK156 (archaeological context)
✓ Figure 2: G25 PCA plot with Bodzia samples + reference populations (label closest neighbors)
✓ Figure 3: Admixture stacked bar chart (Yamnaya, Neolithic, WHG) for all 4 samples + 3 comparative populations
✓ Figure 4: Genetic distance heatmap (all pairwise combinations, color-coded by relationship category)
✓ Figure 5: Population distance ranking (top 15 populations for each of VK155, VK157, VK154, VK156)
✓ Figure 6: Y-DNA and mtDNA phylogenetic trees (showing downstream positions of I1-S2077, H1c, R1a-SUR51, J1c2c2a)

DESIGN STANDARDS:
✓ Color-blind safe palette (use colorblind-friendly tools like ColorOracle to validate)
✓ Figure resolution: ≥300 DPI (for print publication)
✓ Legend placement: caption below figure (not overlaid on plot area)
✓ Axes labeled: units, scale, reference populations named
✓ Uncertainty: error bars, confidence intervals, or sample size noted
✓ Reproducibility: if data public, include GitHub/Zenodo link

TABLES:
✓ Table 1: Sample metadata (ID, burial code, date, estimated age, sex, preservation)
✓ Table 2: Haplogroup assignments (Y-DNA, mtDNA, confidence levels, reference sources)
✓ Table 3: Pairwise genetic distances (VK1–VK2, VK1–VK3, etc.)
✓ Table 4: Admixture components (%) with 95% CI
✓ Table 5: Top 10 population affinities per sample
```

### TIER 6: IMPLEMENTATION CHECKLIST

```
BEFORE SUBMISSION:
□ Read entire document aloud (catch awkward phrasing)
□ Check consistency: sample IDs, units, date formats, terminology (search & replace for errors)
□ Verify all figures referenced in text ("see Figure 2...")
□ Check all citations: do they point to existing, accessible sources?
□ Count words per section (does it match target word count?)
□ Test Gunning Fog Index (paste prose into hemingwayapp.com or similar)
□ Have a peer (non-author) read Introduction + Discussion only (can they understand your argument without Methods?)

READABILITY EDITS:
□ Replace "it was found that" → "we found" (minimize passive voice)
□ Replace "it is possible that" → state likelihood (unlikely/plausible/probable)
□ Replace long sentences (>25 words) with two shorter ones
□ Remove redundant phrases (e.g., "unique and novel" → pick one)
□ Use footnotes for tangential details (keep main text focused)

HYPOTHESIS CLARITY:
□ Highlight (in color) each hypothesis statement in the text
□ Check: can a reader state your null hypothesis without reading your preferred outcome?
□ Check: is falsification possible? (if always true under any outcome, it's not testable)
□ Check: are confidence levels consistent? (don't say "proven" for a plausible finding)
```

### TIER 7: JOURNAL TARGET (Select one, align style)

```
OPTION A: Nature / PNAS (multidisciplinary science)
    ✓ Word limit: 3000–4500 + figures/tables
    ✓ Audience: geneticists, archaeologists, historians
    ✓ Style: hypothesis-driven, quantitative, emphasize novelty
    ✓ Expected emphasis: Genome-wide admixture, population structure, cross-site implications
    ✓ Recommendation: Start with Executive Summary + Introduction (why it matters globally?), compress Methods to 1 page

OPTION B: Journal of Archaeological Science (specialized)
    ✓ Word limit: 5000–8000 + figures
    ✓ Audience: archaeologists + geneticists interested in method integration
    ✓ Style: methods-heavy, taphonomy-conscious, depositional context
    ✓ Expected emphasis: Stratigraphic context, sample preservation, laboratory protocols, comparison to other elite cemeteries
    ✓ Recommendation: Expand Methods section; include detailed taphonomy + commingling risk assessment

OPTION C: American Journal of Human Genetics (genetics-focused)
    ✓ Word limit: 4000–6000
    ✓ Audience: population geneticists, genetic epidemiologists
    ✓ Style: quantitative genetics, statistical rigor, modern populations + ancient comparison
    ✓ Expected emphasis: Haplogroup phylogeny, admixture model fit statistics, kinship inference confidence
    ✓ Recommendation: Expand Results section with statistical tests (p-values, confidence intervals, model comparisons)

OPTION D: Early Medieval Europe (history journal)
    ✓ Word limit: 5000–8000
    ✓ Audience: medieval historians, occasional archaeologist readers
    ✓ Style: narrative + evidence, emphasize historical context over method detail
    ✓ Expected emphasis: What does Bodzia elite tell us about 10th–11th century state formation, Rus'-Polish relations, trade networks?
    ✓ Recommendation: Expand Arguments + Discussion; move Methods detail to appendix; add more genealogical tree context

RECOMMENDATION: Submit to **Journal of Archaeological Science** first (best fit for integrated approach: genealogy + genetics + archaeology). Prepare secondary submission to **American Journal of Human Genetics** (emphasize haplogroup phylogeny + population structure).
```

---

## REVISED PROMPT (CONDENSED FINAL VERSION)

```
TASK: Transform "Bodzia Complete Tree Documentation" into a publication-ready 
peer-reviewed academic manuscript.

TARGET AUDIENCE: Medieval archaeologists and genetic genealogists (primary); 
historians of Early Medieval Europe (secondary); educated public (tertiary via 
sidebars/glossary).

STRUCTURE: Modified IMRaD (Introduction–Methods–Results–Arguments–Discussion–
Conclusions) with genealogical rigor.

WORD TARGETS:
  • Executive Summary: 250–300 words
  • Introduction: 800–1000 words
  • Methods: 800–1200 words
  • Results: 1000–1500 words
  • Arguments: 800–1000 words
  • Discussion: 1000–1200 words
  • Total: ~5000–7000 words (target *Journal of Archaeological Science*)

QUALITY STANDARDS:
  ✓ Gunning Fog Index: 13–15
  ✓ Passive voice: <25%
  ✓ Terminology: consistent from first mention (VK157 = "Sviatopolk I (VK157)" on first use)
  ✓ Dates: uniform format (950–1020 CE)
  ✓ All figures numbered + captioned + referenced in text

HYPOTHESIS REQUIREMENTS:
  • State 3–4 falsifiable hypotheses (Null hypothesis H0 + Alternative Ha for each)
  • For each hypothesis: (a) how tested, (b) evidence threshold, (c) falsification scenario
  • Confidence levels: PROVEN / PROBABLE / PLAUSIBLE / SPECULATIVE (use consistently)
  • Roadmap: what future work falsifies or confirms each hypothesis?

VISUALIZATION:
  • Create 6 figures (Bodzia map, G25 PCA, admixture bar chart, genetic distance heatmap, 
    population ranking, Y-DNA/mtDNA trees)
  • Create 5 tables (sample metadata, haplogroups, distances, admixture, population affinities)
  • All figures ≥300 DPI, color-blind safe palette

SPECIFIC GAPS TO ADDRESS IN YOUR CURRENT DOCUMENT:
  1. No explicit null hypotheses → ADD "If H0 is true, we expect X; we observe Y"
  2. No falsification criteria → ADD "This finding is falsified by..."
  3. Vague confidence language → REPLACE "suggests" with PROVEN / PROBABLE / PLAUSIBLE
  4. No Discussion of alternative interpretations → ADD "Alternative explanation 1: ..., 
     ruled out by ..."
  5. Limited genealogical justification → EXPAND: why is the genealogical tree (79 individuals, 
     9 dynasties) necessary context? How does it validate genetic findings?
  6. Ciepłe framed as future work, not current evidence → REFRAME as "Comparative site context; 
     predictions testable Q1-Q2 2026"
  7. Methods section scattered across document → CONSOLIDATE all analytical procedures into 
     one coherent Methods section
  8. No sensitivity analysis → ADD: "Results robust to X? Tested by Y..."

BEFORE FINAL SUBMISSION:
  ✓ Print entire document, read aloud to check flow
  ✓ Use Hemingway app to identify passive constructions & complex sentences
  ✓ Verify all 79 individuals are properly contextualized (why them? why 9 dynasties?)
  ✓ Check that every major claim is traceable to a figure/table or citation
  ✓ Ask a peer: can you state the main hypothesis in one sentence?
```

---

## SUMMARY OF IMPROVEMENTS

| Aspect | Original | Revised |
|--------|----------|---------|
| **Purpose** | Vague | Clear: publication-ready, IMRaD structure, specific journal target |
| **Audience** | Unspecified | Three tiers with optimization strategy |
| **Structure** | Implicit | Explicit 9-section outline with word targets |
| **Hypotheses** | Weak | 4 falsifiable hypotheses with H0/Ha, test methods, confidence levels |
| **Quality Metrics** | Subjective | Gunning Fog Index 13–15, passive voice <25%, consistency rules |
| **Visualizations** | Mentioned | Specified 6 figures + 5 tables with design standards |
| **Limitations** | Not addressed | Explicit section with alternative interpretations & falsification scenarios |
| **Roadmap** | Missing | Ciepłe integration plan + testable predictions (2026) |

---

## NEXT STEPS

1. **Week 1**: Restructure document using the 9-section IMRaD outline (keep existing content, reorganize)
2. **Week 2**: Add explicit hypotheses section (H0/Ha/test method/falsification for each)
3. **Week 3**: Create 6 figures + 5 tables following design standards
4. **Week 4**: Rewrite for Gunning Fog 13–15; check passive voice <25%
5. **Week 5**: Peer review (non-author reads Intro + Discussion; can they summarize your argument?)
6. **Week 6**: Final edits + consistency check (terminology, dates, units)
7. **Submit to**: *Journal of Archaeological Science* (primary target)

---

## REFERENCE EXAMPLES (Model Your Document After)

**Excellent IMRaD + Hypothesis Model**:
- Margaryan et al. (2020). "Population genomics of the Viking world." *Nature*, 585, 390–396.
- Zhur, K. "The Rurikids: Genetic Portrait..." (focuses on haplogroup phylogeny + hypothesis testing)
- Kushniarevich et al. (2015). "Genetic Heritage of Balto-Slavic Populations." *PLOS ONE*, synthesis of aDNA + modern data

**Excellent Genealogy + Genetics Integration**:
- Medieval elite burials papers in *Journal of Archaeological Science* (search: "elite burial genetic analysis")
- DNA + genealogy focus: *American Journal of Human Genetics* special issues on historical genetics

---

**Created**: 2026-01-11 | **Status**: Ready for Implementation
