# Testable Hypotheses Derived from `BODZIA_COMPLETE_TREE_DOCUMENTATION.md`

**Prepared:** 2026-01-11  
**Purpose:** Consolidate a falsifiable, data-driven hypothesis set derived from `docs/BODZIA_COMPLETE_TREE_DOCUMENTATION.md` into a standalone file suitable for (a) internal project tracking and (b) publication-oriented study planning.  
**Status:** Research framework (pre-publication; many hypotheses depend on data not yet available, e.g., Winchester Cathedral genomes).

> **Important scope note:** The genealogical graph in `docs/BODZIA_COMPLETE_TREE_DOCUMENTATION.md` contains **model nodes** and project associations (e.g., mapping VK157 to a historical label). Hypotheses below separate **(i) what is directly testable from genomic data** from **(ii) what requires historical-source validation**.

---

## 0) Data required to test these hypotheses (Bodzia core set)

The four Bodzia individuals used throughout the project are VK154, VK155, VK156, VK157. ENA provides both FASTQ (raw reads) and BAM (aligned reads) for these samples (study: **PRJEB37976**).

File: `data/reference/ena/PRJEB37976_bodzia_VK154_VK155_VK156_VK157.tsv`

### ENA accessions and direct URLs (Bodzia)

| Sample | ENA sample | ENA experiment | ENA run | FASTQ (ENA FTP) | BAM (ENA FTP) |
|---|---|---|---|---|---|
| VK154 | SAMEA6799930 | ERX4058353 | ERR4059568 | `https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR405/008/ERR4059568/ERR4059568.fastq.gz` | `https://ftp.sra.ebi.ac.uk/vol1/run/ERR405/ERR4059568/VK154.final.bam` |
| VK155 | SAMEA6799931 | ERX4058354 | ERR4059569 | `https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR405/009/ERR4059569/ERR4059569.fastq.gz` | `https://ftp.sra.ebi.ac.uk/vol1/run/ERR405/ERR4059569/VK155.final.bam` |
| VK156 | SAMEA6799932 | ERX4058355 | ERR4059570 | `https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR405/000/ERR4059570/ERR4059570.fastq.gz` | `https://ftp.sra.ebi.ac.uk/vol1/run/ERR405/ERR4059570/VK156.final.bam` |
| VK157 | SAMEA6799933 | ERX4058356 | ERR4059571 | `https://ftp.sra.ebi.ac.uk/vol1/fastq/ERR405/001/ERR4059571/ERR4059571.fastq.gz` | `https://ftp.sra.ebi.ac.uk/vol1/run/ERR405/ERR4059571/VK157.final.bam` |

**Local storage suggestion (repo convention):**
- `data/raw/ancient_dna/bodzia/PRJEB37976/` (and keep `.bam/.bai` ignored by git; see `docs/ANCIENT_BAM_WORKFLOW.md`)

---

## 1) Bodzia-only hypotheses (testable now with ENA data)

### Hypothesis B1 — Uniparental haplogroups (confirmation/refinement from raw data)

**Current status:** Partially known from secondary summaries; requires confirmation from BAM/FASTQ for publication-grade claims.  
**Primary data:** PRJEB37976 (runs above).  
**Test method:** Authenticate aDNA → call mtDNA consensus + Y-SNPs (where applicable) → assign haplogroups.

**Statement:**  
> Haplogroup assignments reported for VK154/VK155/VK156/VK157 in `docs/BODZIA_COMPLETE_TREE_DOCUMENTATION.md` (e.g., VK156 R1a-derived; VK157 I1-S2077; VK154/VK155 H1c-derived mtDNA) are reproducible when haplogroups are re-called from the ENA data using standard aDNA QC and haplogroup pipelines.

**Operational acceptance criteria (Tier 1):**
- aDNA authentication metrics are consistent with ancient origin (damage patterns; fragment length; contamination estimates within acceptable ranges).
- mtDNA: consistent haplogroup assignment across at least two independent approaches (e.g., consensus + Haplogrep vs read-backed variant calls).
- Y-DNA (males): consistent placement on a modern Y tree with explicit SNP support (include a list of supporting/refuting SNPs in a private appendix).

**Falsification scenario:**  
Re-calling indicates different top-level haplogroups (e.g., VK157 not I1-derived; VK154/VK155 not H1c-derived), or contamination/authentication fails such that haplogroup calls are not reliable.

---

### Hypothesis B2 — Within-Bodzia kinship structure (genome-wide relatedness, not G25 proximity)

**Current status:** Exploratory support only (G25 distances; third‑party matching outputs).  
**Primary data:** PRJEB37976 (all four samples).  
**Test method:** Low-coverage-aware relatedness estimation on genome-wide data (e.g., READ, lcMLkin, NgsRelate2-like workflows; use genotype likelihoods or pseudo-haploid calls appropriate to coverage).

**Statement:**  
> The four Bodzia individuals form a **cohesive kin-structured group** at the genome-wide level, with at least one pair showing detectable biological relatedness, consistent with the “two-cluster” exploratory pattern (VK154–VK156; VK155–VK157) reported in the manuscript.

**Expected outcomes (examples):**
- **Support:** One or more pairs show relatedness consistent with ≤4th degree (method-dependent confidence intervals), and the strongest relatedness pairs align with the exploratory “cluster” pattern.
- **Refute:** All pairs are effectively unrelated within method sensitivity (after QC), suggesting social rather than biological clustering.

**Falsification scenario:**  
Genome-wide relatedness shows no detectable kinship among all pairs (after ensuring adequate SNP overlap and QC), or reveals a completely different kinship topology than the exploratory pattern.

---

### Hypothesis B3 — Maternal-line structure (H1c-derived mtDNA does/does not imply close kinship)

**Current status:** VK154/VK155 are reported as H1c-derived; VK157 mtDNA is reported in-project but should be treated as unconfirmed until re-called.  
**Primary data:** PRJEB37976.  
**Test method:** mtDNA consensus and *downstream* subclade resolution (not just “H1c”); compare shared private variants; evaluate contamination.

**Statement:**  
> Any apparent shared mtDNA “H1c” signal among Bodzia individuals either (a) resolves to the **same downstream subclade** with shared private variants (consistent with maternal kinship) or (b) resolves to different downstream branches (consistent with a common but non-informative maternal haplogroup in the region).

**Expected outcomes:**
- **Support (maternal kin):** Identical (or near-identical, within damage/noise) mtDNA consensus profiles and shared downstream variants among at least two individuals.
- **Refute (no close maternal kin):** Different downstream H1c subclades or divergent mtDNA consensus profiles inconsistent with close maternal-line relationship.

---

### Hypothesis B4 — VK157 paternal-line placement and relationship to the project’s modern Y line (phylogenetic)

**Current status:** VK157 is reported as I1-S2077; the project’s modern Y line currently summarizes as I-Y224059 (from local YFull exports).  
**Primary data:** VK157 ENA; local YFull exports (`data/raw/y_dna_results/`).  
**Test method:** Place VK157 on a Y tree using supported SNPs; compare to modern YFull placement; evaluate whether the two lineages converge within plausible time depth for the project’s stated historical hypotheses.

**Statement:**  
> VK157’s Y lineage and the project’s modern Y lineage are either (a) phylogenetically close enough to motivate deeper targeted comparison (shared upstream nodes within a plausible TMRCA window) or (b) clearly distant within haplogroup I, constraining any proposed patrilineal continuity narrative.

**Acceptance criteria:**
- Explicit SNP-supported placement for VK157 and explicit YTree placement for the modern sample.
- TMRCA reasoning clearly separated into “tree-based” vs “genome-wide” evidence; no claims of direct descent without explicit evidence.

**Falsification scenario:**  
Lineages are in clearly non-overlapping branches such that any “direct paternal link” hypothesis becomes implausible without additional intermediary evidence.

---

### Hypothesis B5 — Population affinity (formal statistics vs coordinate summaries)

**Current status:** Exploratory support from G25 “closest populations” and admixture summaries.  
**Primary data:** PRJEB37976 + well-defined reference panels.  
**Test method:** Formal population-genetic statistics from publication-grade genotype calls (PCA on called genotypes; f-statistics; qpAdm/qpGraph as appropriate).

**Statement:**  
> The “Scandinavian-associated affinity” pattern suggested in coordinate space persists when tested using formal statistics on publication-grade genotype calls (within uncertainty limits due to coverage).

**Falsification scenario:**  
Formal statistics do not reproduce the Scandinavian-associated signal, or show it is explainable by alternative sources/structures (e.g., broad North/Central European affinity without a specific Scandinavian component).

---

## 2) External comparator hypotheses (pending data availability)

### Hypothesis BW1 — Bodzia ↔ Winchester (cross-site elite connectivity; requires attributable Winchester genomes)

**Current status:** Pending external genomic datasets and attribution quality.  
**Primary data needed:** Public, attributable genome-wide data from Winchester Cathedral contexts (or close proxies), with dates/coverage/QC sufficient for relatedness and haplogroup assignment.

**Statement:**  
> If Winchester Cathedral yields reliably attributable genomes for 10th–11th century elite individuals connected to the Anglo‑Scandinavian sphere, then Bodzia individuals can be tested for (a) genome-wide relatedness, (b) rare uniparental subclade sharing, or (c) population-level affinity that is unusually close given geography/time.

**Support criteria (strong → weak):**
1. Detectable cross-site biological relatedness (≤4th degree, method-dependent) between a Bodzia individual and a Winchester individual.
2. Shared rare Y-DNA/mtDNA downstream subclades with sufficient resolution to be informative.
3. Population-level affinity patterns that are more consistent with a specific Anglo‑Scandinavian elite context than with generic North/Central European similarity.

**Falsification scenario:**  
High-quality Winchester genomes show no kinship/lineage overlap where hypothesized, or point to alternative networks that better explain Bodzia’s affinities.

---

### Hypothesis BC1 — Bodzia ↔ Ciepłe (regional elite-network test; requires comparable Ciepłe genomes)

**Current status:** Pending external datasets.  
**Primary data needed:** Ciepłe genome-wide data with comparable QC/calling strategy.

**Statement:**  
> Ciepłe provides a regional comparator to test whether multiple Piast-adjacent elite contexts share similar Scandinavian-associated ancestry signals and/or overlapping uniparental lineages with Bodzia.

---

## 3) Historical-source hypotheses (not DNA-only)

### Hypothesis H1 — Historical attribution constraints for “model nodes”

**Statement:**  
> Any mapping between archaeological individuals (VK154–VK157) and named historical persons in the genealogical graph is **consistent with** (not proven by) a minimal set of primary-source constraints (date ranges, political plausibility, geographic plausibility), and remains explicitly labeled as a hypothesis unless independently corroborated.

**Test method:** Source-critical review + chronology constraints; require explicit citations for each inference step.

---

## 4) Tracking table (quick status dashboard)

| Hypothesis | Type | Testability | Primary dependency |
|---|---|---|---|
| B1 | Haplogroups | Now | PRJEB37976 BAM/FASTQ + aDNA QC |
| B2 | Kinship | Now | PRJEB37976 + low-coverage relatedness |
| B3 | mtDNA kinship | Now | PRJEB37976 mtDNA re-calls |
| B4 | Y phylogeny | Now | VK157 Y calls + local YFull exports |
| B5 | Population affinity | Now (with work) | Publication-grade calling + reference panels |
| BW1 | Bodzia↔Winchester | Later | Attributable Winchester genomes |
| BC1 | Bodzia↔Ciepłe | Later | Comparable Ciepłe genomes |
| H1 | Source-critical | Now | Primary historical sources |

---

## Appendix A) Reference templates (how to cite datasets)

When these hypotheses move toward publication, each dataset should be cited with:
- Study accession (ENA/NCBI), run accessions, sample accessions
- Library type and capture/WGS status
- Coverage (mean/median; SNP overlap at 1240k if applicable)
- QC and contamination estimates

For Bodzia ENA accessions, use the table in §0 and keep a copy of the ENA query output in `data/reference/ena/`.

