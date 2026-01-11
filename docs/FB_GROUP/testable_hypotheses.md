# Testable Hypotheses: Bodzia ↔ Winchester Cathedral ↔ Piast Dynasty DNA Networks

**Prepared**: January 11, 2026  
**Purpose**: Enumerate verifiable genetic hypotheses that emerge when integrating three elite datasets  
**Status**: Pre-publication research framework

---

## Executive Summary: Three-Site Genetic Bridge

When **Bodzia cemetery** (Poland, 950-1020 CE), **Winchester Cathedral** (England, 7th-12th centuries), and **Piast Dynasty aDNA** (Prof. Figlerowicz, 2023+) are analyzed together, they create a testable framework for understanding **transnational Early Medieval elite networks**.

**Key insight**: These three sites span **Scandinavia ↔ Poland ↔ England** and represent the highest-status burial contexts of their regions and periods. If they share genetic markers, this would provide **strong evidence** for cross-cultural elite mobility and marriage alliances. If they do NOT share markers, this would refine our understanding of **regional fragmentation** despite documented political contacts.

---

## PART 1: BODZIA-SPECIFIC HYPOTHESES (Testable NOW)

### **Hypothesis B1: Maternal Kinship – VK157 mtDNA**
**Current status**: ❌ NOT YET EXTRACTED  
**Data source**: PRJEB37976, run ERR4059571 (VK157.final.bam)  
**Test method**: Extract mtDNA from BAM → call consensus → assign haplogroup (Haplogrep)

**Statement**: 
> VK157 (Światopełk I, male) shares mtDNA haplogroup **H1c** with VK155 ("Wiedźma," female) and VK154 ("Księżniczka," female), indicating **maternal lineage kinship** within the Bodzia elite.

**Current evidence**:
- VK155 mtDNA: **H1c**[242]
- VK154 mtDNA: **H1c**[242]
- VK157 mtDNA: **UNKNOWN** ← Critical gap

**Expected outcomes**:
| Result | Interpretation |
|--------|-----------------|
| **VK157 = H1c** | ✅ SUPPORTS maternal kinship; all three share local Polish maternal lineage |
| **VK157 ≠ H1c** (e.g., T2, J1c2c2a, U5) | ❌ REFUTES maternal kinship; VK157 from different maternal line (possibly Rus'/Byzantine) |

**Why it matters**: If true, strengthens hypothesis that Bodzia elite formed a **kin-based clan** rather than a random burial assemblage. If false, suggests VK157 married into the group (typical patrilocal marriage—elite male brought foreign bride or vice versa).

**Cross-check**: Prof. Figlerowicz (2023) showed mtDNA was **locally continuous** in Poland across the first millennium. If VK157 ≠ H1c, compare his mtDNA to Figlerowicz's Piast women to determine if it's Rus'/Byzantine or other origin.

---

### **Hypothesis B2: Patrilineal Continuity – VK157 Y-DNA Refinement**
**Current status**: ⚠️ PARTIALLY KNOWN (I1-S2077 documented, but downstream SNPs not fully called)  
**Data source**: PRJEB37976, run ERR4059571 (VK157.final.bam)  
**Test method**: Refine Y-DNA SNP calling → compare to YFull/FTDNA trees → assess TMRCA

**Statement**:
> VK157 Y-DNA **I1-S2077** traces to a **single founder ~900-950 CE** or earlier, consistent with either (a) **Wielbark culture legacy** (I1 present in Poland since I-V centuries CE) or (b) **fresh Scandinavian immigration** into Rus'-Polish elite networks.

**Current evidence**:
- VK157 Y-DNA: **I1-S2077** (Scandinavian/Germanic)[242]
- Wielbark culture (I-V CE): Dominated by **I1** (Prof. Figlerowicz 2023)
- Rurikid elite: Typically **N1a**, but could absorb conquered I1 lineages

**Expected outcomes**:
| Result | Interpretation |
|--------|-----------------|
| **I1-S2077 TMRCA ~200-400 CE** | ✅ Suggests Wielbark culture origin; I1 embedded in Polish population for 600 years |
| **I1-S2077 TMRCA ~900-950 CE** | ✅ Suggests Rurikid-era elite formation; contemporaneous with Bodzia |
| **I1-S2077 clusters with Gotland/Denmark aDNA** | ✅ Suggests ongoing Scandinavian connections |
| **I1-S2077 clusters with modern Polish R1a males** | ⚠️ Questions "pure Scandinavian" narrative; may indicate assimilation |

**Why it matters**: Determines whether Bodzia was a **Scandinavian-led enclave** or a **locally-rooted elite that absorbed Germanic elements over centuries**. Directly tests Figlerowicz's model of local genetic continuity.

---

### **Hypothesis B3: Kinship Coefficient – Bodzia as Kin-Group**
**Current status**: ⚠️ PARTIALLY KNOWN (G25 distance 0.0417, shared DNA 114.79 cM documented)  
**Data source**: PRJEB37976, all 4 samples  
**Test method**: KING kinship analysis on filtered autosomal SNPs

**Statement**:
> VK155 and VK157 are **3rd-4th degree relatives** (kinship coefficient 0.044–0.088), consistent with **cousins** in a cohesive elite burial community, not unrelated individuals.

**Current evidence**:
- G25 distance: **0.0417** (moderate)[242]
- Shared autosomal DNA: **114.79 cM** (consistent with 3rd-4th degree)[242]
- Both show affinities to Gotland, Medieval Germany, Gnezdovo

**Expected outcomes**:
| Kinship range | Relationship | Implication |
|---------------|--------------|-------------|
| **> 0.177** | 1st degree (half-sib, grandparent-grandchild) | Bodzia is immediate family unit |
| **0.088–0.177** | 2nd degree (aunt/uncle) | Bodzia is close nuclear family |
| **0.044–0.088** | 3rd degree (cousins) | ✅ EXPECTED—cohesive elite clan |
| **< 0.044** | 4th+ degree or unrelated | Suggests random burial assemblage |

**Why it matters**: Establishes whether Bodzia functioned as **dynastic burial ground** (kin-based) or **elite warrior cemetery** (non-kin group). Controls for alternative explanations.

---

### **Hypothesis B4: Chromosome X IBD – Maternal Ancestry Connection**
**Current status**: ❌ NOT YET ANALYZED  
**Data source**: PRJEB37976, all 4 samples  
**Test method**: Extract chrX → call SNPs → run IBD detection (plink)

**Statement**:
> VK155 (female, XX) and VK157 (male, XY) share **X chromosome segments** (PI_HAT > 0.1), indicating they inherit from **closely related mothers**, consistent with maternal cousinship or sibling relationship.

**Logic**: 
- VK157 inherits single X from his mother
- VK155 inherits one X from her father, one from her mother
- If VK155's mother is related to VK157's mother → shared X segments

**Expected outcomes**:
| Result | Interpretation |
|--------|-----------------|
| **PI_HAT > 0.1 on chrX** | ✅ Suggests maternal kinship (mothers related) |
| **PI_HAT 0.05–0.1 on chrX** | ⚠️ Suggests distant maternal relation |
| **PI_HAT < 0.05 on chrX** | ❌ Suggests NO maternal kinship; VK157 married into group |

**Why it matters**: Tests whether Bodzia elite was **kin-based through maternal lines** or assembled through **patrilocal marriage patterns**. Complement to mtDNA analysis (B1).

---

## PART 2: WINCHESTER CATHEDRAL HYPOTHESES (Testable Q3–Q4 2026)

### **Hypothesis W1: Queen Emma mtDNA Confirmation**
**Current status**: ⏳ In progress (DNA extracted, results expected Q3–Q4 2026)  
**Data source**: Winchester Cathedral Mortuary Chests Project (Prof. Robson Brown, University of Bristol)  
**Test method**: Extract mtDNA from female skeleton → assign haplogroup → compare to known relatives (e.g., Sweyn Estridsson in Roskilde)

**Statement**:
> Female skeletal remains in Winchester Cathedral identified as **Queen Emma of Normandy** (b. ~980s, d. 1052) are confirmed via **mtDNA matching to known maternal relatives**, establishing definitive genealogy.

**Background**: Winchester Cathedral project (2012–2027) has reassembled **23 partial skeletons** from **6 mortuary chests**. One mature female is osteologically consistent with Queen Emma, but genetic confirmation is pending.

**Expected outcomes**:
| Result | Confidence |
|--------|-----------|
| **mtDNA matches Sweyn Estridsson** (Emma's brother's son, Roskilde) | 🔴 DEFINITIVE |
| **mtDNA matches Normandy ducal lineage** | 🟡 STRONG |
| **mtDNA does NOT match known relatives** | ❌ REFUTES Emma identity |

**Why it matters**: Opens pathway for **Bodzia ↔ Winchester comparison**. If Emma is confirmed, we can trace her descendants' connections to Polish nobility and compare to Bodzia genetics.

**Key reference**: [327] mentions Danish King Sven Estridsson (son of Emma's sister) with DNA already extracted from Roskilde Cathedral—this provides perfect comparison point.

---

### **Hypothesis W2: King Cnut Y-DNA**
**Current status**: ⏳ In progress (results expected Q3–Q4 2026)  
**Data source**: Winchester Cathedral mortuary chests  
**Test method**: Extract Y-DNA from male skeleton → assign haplogroup → compare to Danish royal ancestry

**Statement**:
> Male skeletal remains in Winchester Cathedral identified as **King Cnut the Great** (r. 1017–1035) carry **Y-DNA consistent with Danish/Scandinavian patriline** (expected **N1a** or **I1**), confirming his genealogical identity.

**Background**: Cnut was the **Danish conqueror** of England (1017–1035), son of Sweyn Forkbeard. If his remains are identified in Winchester Cathedral, his Y-DNA can anchor a comparative framework for other Danish-lineage elites.

**Expected outcomes**:
| Result | Interpretation |
|--------|-----------------|
| **Y-DNA = N1a** (typical Rurikid/Danish) | ✅ CONFIRMS Cnut identity |
| **Y-DNA = I1** (Scandinavian alternative) | ✅ CONFIRMS Cnut identity |
| **Y-DNA = R1a** (Slavic) | ❌ REFUTES Cnut; suggests Polish/Rus' individual |
| **Y-DNA = other** | ❌ REFUTES Cnut |

**Why it matters**: Creates **Y-DNA benchmark** for Danish elite. If Bodzia VK157 (I1-S2077) clusters with Cnut's lineage, this would support **shared Scandinavian elite network**.

---

### **Hypothesis W3: Juvenile Royal Children – Unknown Identity**
**Current status**: ⏳ In progress (results expected Q3–Q4 2026)  
**Data source**: Winchester Cathedral (two boys, aged 10–15, died 1050–1150 CE)  
**Test method**: Extract mtDNA + Y-DNA → build maternal + paternal trees → match to historical records

**Statement**:
> Two juvenile skeletons in Winchester Cathedral (boys, 10–15 years, 1050–1150 CE) are **identified via mtDNA and Y-DNA to specific royal individuals** (e.g., sons of Edward the Confessor, Harold Godwinson, or other late Anglo-Saxon/Norman royals), filling historical gaps.

**Background**: Winchester project found **two boys not recorded in mortuary chest inventories**. "Almost certainly of royal blood" but identity unknown. mtDNA/Y-DNA analysis can reveal who they were.

**Expected outcomes**:
| Result | Significance |
|--------|-------------|
| **mtDNA/Y-DNA match to documented royal pedigree** | ✅ Identifies specific individuals |
| **mtDNA suggests Scandinavian maternal line** | 🟡 May connect to Bodzia network |
| **Y-DNA = R1a (Slavic)** | 🟡 May indicate diplomatic marriage child (Poland/Rus' parent) |
| **Cannot match to any known pedigree** | ⚠️ Suggests illegitimate or unrecorded royal children |

**Why it matters**: May reveal **unexpected family connections** linking Winchester to Bodzia or Rus'. Even "unidentified" results constrain historical narrative.

---

## PART 3: BODZIA ↔ WINCHESTER BRIDGE HYPOTHESES

### **Hypothesis BW1: Elite Feminine Kinship via mtDNA**
**Current status**: ⏳ Awaiting Winchester publication (Q3–Q4 2026)  
**Data source**: Bodzia females (VK155, VK154 = H1c) + Winchester females (esp. Queen Emma)  
**Test method**: Compare mtDNA haplogroups; if same, assess downstream SNP match

**Statement**:
> VK155 and VK154 (Bodzia H1c mtDNA) **share mtDNA haplogroup with Winchester Cathedral females** (esp. Queen Emma), indicating **transnational feminine kinship networks** and matrilineal marriage exchange between Polish and English elites.

**Logic**: Elite women in Early Medieval Europe were often exchanged in marriage between dynasties. If Bodzia women carry the same mtDNA haplogroup as Winchester women, this suggests **maternal lineage connections across the Baltic and North Sea**.

**Expected outcomes**:
| Result | Strength of Evidence |
|--------|---------------------|
| **Both Bodzia + Emma = H1c + same downstream SNPs** | 🔴 **STRONG**—likely maternal kinship |
| **Both Bodzia + Emma = H1c (but different downstream SNPs)** | 🟡 **MODERATE**—suggests distant maternal relation |
| **Bodzia = H1c, Emma = T2** (different haplogroups) | ⚠️ **WEAK**—no direct maternal kinship |
| **Bodzia = H1c, Emma cannot be identified** | ❌ Hypothesis not testable |

**Why it matters**: Tests whether **female-mediated elite networks** connected Poland and England. Compatible with documented historical marriages (e.g., between Polish and Norman/English nobility).

**Caveat**: H1c is widespread in medieval Europe, so same haplogroup is necessary but not sufficient for kinship. **Downstream SNP matching** is critical.

---

### **Hypothesis BW2: Elite Masculine Patriline via Y-DNA**
**Current status**: ⏳ Awaiting Winchester publication (Q3–Q4 2026)  
**Data source**: Bodzia males (VK157 I1-S2077, VK156 R1a-SUR51) + Winchester males (Cnut, others)  
**Test method**: Extract/compare Y-DNA → build phylogenetic trees → assess TMRCA

**Statement**:
> VK157 **I1-S2077** or VK156 **R1a-SUR51** **clusters with Winchester Cathedral male Y-DNA lineages** (esp. Cnut or Danish-lineage kings), indicating **shared patriline** within transnational Scandinavian/Polish elite networks.

**Logic**: If Bodzia and Winchester elites were part of the same **warrior networks** or **royal lineages**, they should share Y-DNA derived from common ancestors. Scandinavian I1 lineages were mobile across the Baltic; Polish R1a lineages might cluster with Rus' or Scandinavian-influenced elites.

**Expected outcomes**:
| Result | Interpretation |
|--------|-----------------|
| **Bodzia I1 + Winchester Cnut I1 clustering** | ✅ Suggests shared Scandinavian patriline |
| **Bodzia R1a + Winchester R1a clustering** | ✅ Suggests shared Polish/Slavic patriline |
| **No Y-DNA clustering** | ⚠️ Suggests separate elite male networks |

**Why it matters**: Tests whether **male-mediated elite networks** (warrior bands, royal retinues, trading expeditions) connected Polish and English elites across centuries.

---

## PART 4: PIAST DYNASTY DNA HYPOTHESES (Testable Q4 2026–Q2 2027)

### **Hypothesis P1: Genetic Continuity Model Validation**
**Current status**: ⏳ Figlerowicz data in preparation (estimated publication Q4 2026–Q2 2027)  
**Data source**: Prof. Marek Figlerowicz (Institute of Bioorganic Chemistry, PAN) — Piast dynasty aDNA  
**Test method**: Extract Y-DNA from documented Piast individuals → compare to model (60–70% R1a, 20–30% I1)

**Statement**:
> When Prof. Figlerowicz publishes full Piast dynasty aDNA, documented Piast males will show **60–70% R1a + 20–30% I1 Y-DNA**, confirming **genetic continuity from Iron Age** through Medieval period without major post-500 CE migration.

**Background**: Prof. Figlerowicz's 2023 *Genome Biology* paper demonstrated:
- Wielbark culture (I–V CE): **70–80% I1** Y-DNA (Germanic)
- By IV–V centuries: I1 was **gradually replaced** by R1a
- Model: **No additional migration needed** after 500 CE to explain Piast genetics

**Expected outcomes**:
| Result | Confidence |
|--------|-----------|
| **Piast Y-DNA = 60–70% R1a + 20–30% I1** | 🔴 **CONFIRMS** continuity model |
| **Piast Y-DNA = 40–60% I1 (higher than expected)** | 🟡 **QUESTIONS** whether I1 was truly minority by X century |
| **Piast Y-DNA ≠ predicted composition** | ❌ **REFUTES** continuity model |

**Why it matters**: 
- If true: **Bodzia individuals (I1 + R1a) are typical of Piast elite**, not anomalous. Weakens hypothesis that Bodzia was "foreign" immigrant group.
- If false: Bodzia may represent **special recruitment** (foreign retinue, hired warriors, diplomat's court).

---

### **Hypothesis P2: Bodzia Genealogical Placement**
**Current status**: ⏳ Awaiting Figlerowicz publication + G25 data  
**Data source**: Figlerowicz Piast individuals + your genealogical tree (79 individuals)  
**Test method**: Compare Bodzia G25 coordinates to Figlerowicz individuals → assess genetic distance → match to genealogical position

**Statement**:
> When Figlerowicz publishes Piast genetic profiles, **Bodzia individuals can be genealogically placed** by comparing G25 distances to documented Piast members. Expected genetic distance should match predicted kinship (e.g., parents closer than cousins).

**Logic**: 
- If VK155 is predicted to be **cousin of Bolesław I**, genetic distance should be ~0.04–0.05.
- If VK157 is predicted to be **son of Polish prince**, genetic distance should be ~0.01–0.02.
- Mismatch between predicted kinship and genetic distance = genealogy needs revision.

**Expected outcomes**:
| Result | Interpretation |
|--------|-----------------|
| **Genetic distance matches predicted kinship** | ✅ Genealogy CONFIRMED |
| **Genetic distance > predicted (more distant)** | ⚠️ Genealogy needs revision; relationship more distant |
| **Genetic distance < predicted (closer)** | ⚠️ Genealogy needs revision; relationship closer |
| **No clear match to any Piast individual** | ❌ Bodzia members may be non-dynastic elites |

**Why it matters**: **Elevates genealogical tree from exploratory hypothesis to empirically grounded model**. Identifies specific Bodzia individuals within Piast dynasty structure.

---

### **Hypothesis P3: Rus'-Polish Genetic Contact**
**Current status**: ⏳ Partially testable now (Gretzinger 2025 + Zhur 2023 data available); Figlerowicz cross-comparison Q4 2026+  
**Data source**: Piast males (Figlerowicz) + Rurikid males (Zhur 2023, Gretzinger 2025)  
**Test method**: Compare Y-DNA haplogroups + mtDNA between Piast + Rurikid datasets

**Statement**:
> **Piast elite females** (mtDNA) **share haplogroups with Rurikid elite females**, indicating **matrilineal exchange** between Polish and Rus' dynasties via documented historical marriages.

**Background**: Historical sources document marriages between Piast and Rurikid families (e.g., Bolesław I's alliances with Rus' princes). If these marriages left genetic traces, mtDNA should cluster.

**Expected outcomes**:
| Result | Interpretation |
|--------|-----------------|
| **Piast females mtDNA clusters with Rurikid females mtDNA** | ✅ **Genetic confirmation** of marital exchange |
| **No mtDNA clustering** | ⚠️ Marriages occurred but left no detectable genetic signature |

**Why it matters**: 
- If true: Validates historical marriage records with genetic evidence.
- If Bodzia females' mtDNA matches Rurikid females: **Direct evidence** that Bodzia women were **daughters of Rus' princes**.

---

## PART 5: COMPARATIVE SITE HYPOTHESIS – CIEPŁE

### **Hypothesis C1: Ciepłe as Regional Network Node**
**Current status**: ⏳ DNA results pending publication (Q1–Q2 2026)  
**Data source**: Ciepłe cemetery (Pomerania, Danish-influenced site)  
**Test method**: Obtain Ciepłe Y-DNA + G25 coordinates → compare to Bodzia

**Statement**:
> **Ciepłe cemetery** (Danish-Pomeranian elite, 950–1020 CE, ~60–150 km from Bodzia) contains **I1-derived Y-DNA lineages clustering with Bodzia VK157 I1-S2077**, indicating **shared Scandinavian-associated elite networks** across Polish territories.

**Background**: Ciepłe is contemporary with Bodzia but in Danish sphere of influence. If both sites contain I1 lineages, this would suggest **coordinated Scandinavian elite presence** across region.

**Expected outcomes**:
| Result | Implication |
|--------|------------|
| **Ciepłe I1 clusters with Bodzia I1-S2077** | ✅ **Regional network confirmed** |
| **Ciepłe contains R1a dominant (no I1)** | ⚠️ Suggests **local Polish elite**, not Scandinavian |
| **Ciepłe + Bodzia G25 identical affinities** | ✅ **Genetic population unity** |

**Why it matters**: Tests whether elite networks were **regional (triangle: Bodzia ↔ Ciepłe ↔ Scandinavia)** or **isolated sites**.

---

## PART 6: CRITICAL DATA GAPS & TIMELINE

| Gap | Status | Criticality | Timeline |
|-----|--------|-------------|----------|
| **VK157 mtDNA extraction** | ❌ Not done | 🔴 CRITICAL | 1–2 days |
| **VK157 Y-DNA SNP refinement** | ⚠️ Partial | 🔴 CRITICAL | 1–2 days |
| **Bodzia kinship analysis** | ⚠️ Partial | 🔴 CRITICAL | 2–3 days |
| **Bodzia chrX IBD** | ❌ Not done | 🟡 HIGH | 2–3 days |
| **Winchester Cathedral DNA** | ⏳ In progress | 🟡 MEDIUM | Q3–Q4 2026 |
| **Ciepłe cemetery DNA** | ⏳ Pending | 🟡 MEDIUM | Q1–Q2 2026 |
| **Figlerowicz Piast aDNA** | ⏳ In preparation | 🔴 CRITICAL | Q4 2026–Q2 2027 |

---

## PART 7: DECISION TREE – WHAT RESULTS MEAN

### **If B1 = TRUE (VK157 mtDNA = H1c)**
- ✅ All three Bodzia females share maternal lineage
- Bodzia = **kin-based elite clan** (maternal line confirmed)
- Consistent with **local Polish H1c** (widespread in medieval Poland)

### **If B1 = FALSE (VK157 mtDNA ≠ H1c)**
- ❌ VK157 has different maternal origin (Rus', Byzantine, Scandinavian)
- Bodzia = **mixed-composition elite** (patrilocal marriage)
- Suggests VK157 married into group or was adopted

### **If B3 = TRUE (Kinship 0.044–0.088)**
- ✅ Bodzia functions as **kin-based burial community**
- **Supports genealogical models** (Piast dynasty connection)

### **If B3 = FALSE (Kinship < 0.044)**
- ❌ VK155 ↔ VK157 are **unrelated or very distant**
- Bodzia = **warrior retinue or trading post** (non-kin group)
- **Genealogical hypotheses weakened**

### **If BW1+BW2 = TRUE (Winchester mtDNA + Y-DNA match)**
- ✅✅ **Transnational elite network CONFIRMED**
- Bodzia ↔ Winchester genetic kinship established
- **Three-site network integrates successfully**

### **If BW1+BW2 = FALSE (No Winchester matching)**
- ❌❌ **Bodzia and Winchester are geographically isolated** genetically
- Political contacts without genetic exchange
- **Regional fragmentation despite cultural similarity**

### **If P1 = TRUE (Piast genetics match model)**
- ✅ **Prof. Figlerowicz continuity model VALIDATED**
- Bodzia individuals = **typical Piast composition**
- No anomalous "foreign" populations at Bodzia

### **If P1 = FALSE (Piast genetics differ from model)**
- ❌ **Figlerowicz model needs revision**
- Bodzia individuals = **unusual elite composition**
- Suggests Bodzia = **special military/diplomatic site**

---

## SUMMARY: CRITICAL EXPERIMENTS (PRIORITY ORDER)

### **🔴 Do immediately (1–2 weeks):**
1. Extract VK157 mtDNA → haplogroup assignment
2. Refine VK157 Y-DNA SNPs
3. Run KING kinship (Bodzia 4-way)
4. Extract chrX IBD segments

### **🟡 Monitor and integrate (Q1–Q2 2026):**
5. Obtain Ciepłe DNA publication
6. Download Gretzinger Gródek coordinates

### **🟡 Integrate when available (Q3–Q4 2026):**
7. Obtain Winchester Cathedral DNA results
8. Compare Bodzia ↔ Winchester

### **🔴 Await and validate (Q4 2026–Q2 2027):**
9. Obtain Figlerowicz Piast aDNA
10. Match Bodzia individuals to Piast genealogy

---

## CONCLUSION

These **15+ testable hypotheses** can **definitively resolve** whether Bodzia represents:
- **(A) Kin-based Polish/Piast elite** (locally rooted, Figlerowicz continuity model)
- **(B) Foreign Scandinavian retinue** (immigrant warrior band)
- **(C) Transnational elite hub** (connected to Winchester, Rus', Scandinavia)
- **(D) Mixed-composition cemetery** (multiple recruitment sources)

**The answers emerge from systematic genetic analysis + comparison to three independent elite datasets.**

