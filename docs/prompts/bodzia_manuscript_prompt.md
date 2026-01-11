# Bodzia manuscript “master prompt” (publication-ready rewrite)

This file is a **copy-and-revision** of `/Users/andrzejzak/Downloads/prompt_engineering_improvement.md`, adapted to this repository’s current structure and constraints (privacy, evidence/hypothesis separation, and ancient-DNA reporting expectations).

## How to use

1. Provide the assistant the target document path: `docs/BODZIA_COMPLETE_TREE_DOCUMENTATION.md`.
2. Tell it which journal style you want (default: *Journal of Archaeological Science*).
3. Provide any missing primary citations or datasets (especially for Winchester/Ciepłe claims).

## Master prompt (copy/paste)

```text
TASK
Transform `docs/BODZIA_COMPLETE_TREE_DOCUMENTATION.md` into a publication-ready scholarly report suitable for peer-reviewed venues in:
- Medieval archaeology + genetics (e.g., Nature/PNAS/JAS-style rigor)
- Genetic genealogy / population genetics
- Early medieval history (with genetics methods in supplements)

AUDIENCE TIER SYSTEM
Structure for all, but optimize for Tier 1:
Tier 1 (PRIMARY): peer-reviewing academics (archaeology + aDNA + genetic genealogy)
Tier 2 (SECONDARY): early medieval historians (Rus’/Piast/Viking networks)
Tier 3 (TERTIARY): educated general readers (via glossary + appendices)

NON-NEGOTIABLE CONSTRAINTS (EVIDENCE & SAFETY)
1) No invented data:
   - Use only values already present in the repo or explicitly provided in the prompt.
   - If a value is missing, write `[[TBD]]` or `[[UNKNOWN]]` and add it to a “Data required” checklist.
2) Evidence vs hypothesis separation:
   - Clearly label (a) observed data, (b) interpretation, (c) hypothesis, (d) speculation.
   - Any proposed identification of an archaeological sample with a named historical person MUST be labeled as a hypothesis and not written as fact.
3) Citation discipline:
   - Every non-trivial factual claim must either (a) cite a Reference entry, or (b) cite a local data artifact (file path) as the source.
   - If you cannot cite it, downgrade the claim and mark `[[CITATION NEEDED]]`.
4) Privacy:
   - Do not include personal genetic identifiers (e.g., YFull kit IDs, match IDs, detailed SNP lists) in the main manuscript.
   - If needed, keep personal genetic details in a clearly marked LOCAL/PRIVATE appendix and use placeholders like `<YFULL_ID>`.
5) Don’t overclaim:
   - Treat Global25/G25 distances, admixture summaries, and third‑party matching outputs (e.g., MTA) as exploratory unless validated against standard aDNA pipelines.

TARGET JOURNAL & LENGTH
Default target: Journal of Archaeological Science (integrated archaeology + genetics).
Target length: ~5,000–7,000 words (excluding references and supplementary).

REQUIRED MANUSCRIPT ARCHITECTURE (IMRaD+)
0. Title
1. Abstract (200–300 words)
2. Keywords (8–15)
3. Introduction (problem framing, why Bodzia matters, research questions)
4. Materials and Methods
   - 4.1 Archaeological context (site, chronology, burials, key uncertainties)
   - 4.2 Samples and metadata (VK154/VK155/VK156/VK157; what is known vs unknown)
   - 4.3 Genetic data and analytic methods (what was done in this repo)
   - 4.4 Reproducibility (scripts and file outputs)
5. Results (tables/figures first, narrative second)
6. Discussion (interpretation + alternatives + falsification scenarios)
7. Limitations (explicitly, with impact on conclusions)
8. Conclusions (what is supported, what is plausible, what is open)
9. Data & Code Availability (repo paths + constraints)
10. References (numbered; include local files when applicable)
11. Supplementary Information / Appendices

DOCUMENT HYGIENE RULES
- Terminology lock:
  - Use sample IDs consistently (VK157, not just “Sviatopolk”).
  - First mention format: `VK157 (RUR001; model label “Sviatopolk I”)`.
- Dates: use CE (e.g., 950–1020 CE).
- Avoid loaded labels (e.g., “witch”); use neutral terms (“elite female burial”).
- Do not remove the existing “Supplementary Information” dossier; keep long lists there.

ANCIENT DNA MINIMUM REPORTING CHECKLIST (ADD A TABLE)
Create a table listing for each sample (VK154/VK155/VK156/VK157):
- Archaeological context / burial ID
- Estimated date range + dating method (radiocarbon? stratigraphy?) [[UNKNOWN if missing]]
- Sex assignment method (osteology/genetics) [[UNKNOWN if missing]]
- Library prep method (UDG? ds/ss?) [[UNKNOWN]]
- Sequencing (shotgun/capture; platform) [[UNKNOWN]]
- Coverage (genome-wide; Y/mt) [[UNKNOWN]]
- Damage patterns/authentication [[UNKNOWN]]
- Contamination estimates (mtDNA, X for males) [[UNKNOWN]]
- Reference build and mapping pipeline [[UNKNOWN]]
If the repo doesn’t contain these, list what’s needed to obtain them.

HYPOTHESIS FRAMEWORK (REQUIRED)
State 3–5 falsifiable hypotheses. For each:
- H0 (null)
- Ha (alternative)
- Test(s) using available or explicitly proposed data
- Evidence threshold(s) (numeric where possible; otherwise defined qualitative gates)
- Falsification scenario(s)
- Current status: SUPPORTED / PARTIALLY SUPPORTED / INCONCLUSIVE / NOT SUPPORTED

REQUIRED FIGURES/TABLES (IF DATA EXISTS; OTHERWISE MARK `[[TBD]]`)
Tables:
- Sample metadata table (with unknowns flagged)
- Haplogroups table (Y/mt)
- Pairwise distance table (G25)
- Admixture component summary table
- Population affinity summary (top N closest references)
Figures (only if the repo already has them; otherwise write the caption as `[[TBD]]`):
- Map/overview (site + comparative sites)
- PCA plot (G25)
- Admixture bar chart
- Distance heatmap

QUALITY STANDARDS (PRACTICAL)
- Passive voice <25% (prefer active voice where appropriate).
- Topic sentences: each subsection starts with a 1-sentence “what/why” anchor.
- Every table/figure is explicitly referenced in the text.
- Every major claim is traceable to either a citation or a repo artifact path.

DELIVERABLES
1) Update `docs/BODZIA_COMPLETE_TREE_DOCUMENTATION.md` in place, producing:
   - A clean Tier-1 manuscript front section, and
   - A clearly separated Supplementary/Appendix section for long-form project outputs.
2) Add a “Claims & Evidence Ledger” appendix:
   - 10–20 key claims, each mapped to (a) reference number(s) and/or (b) repo file paths.
3) Add a “Data required for publication-grade aDNA inference” checklist.

SCOPING NOTE
Do not browse the internet unless explicitly instructed. Use only repo content and the citations already present in the References section, and mark gaps for the user to fill.
```

