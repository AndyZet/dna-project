# G25 Coordinates

Global25 (G25) principal component coordinates for genetic affinity analysis.

## Files

| File | Description |
|------|-------------|
| `g25_scaled_coordinates.csv` | Scaled coordinates for population comparisons |
| `g25_raw_coordinates.csv` | Raw (unscaled) PCA values |

## Samples

| Sample ID | Type | Description | Source |
|-----------|------|-------------|--------|
| andrzej_zak | Modern | User-provided coordinates | User submission (2026-01-23) |
| VK155 | Ancient | Bodzia cemetery female, VK157 maternal relative | Krzewińska et al. 2018 |
| VK156 | Ancient | Bodzia cemetery individual | Krzewińska et al. 2018 |
| VK157 | Ancient | Bodzia cemetery elite male, proposed Sviatopolk I | Krzewińska et al. 2018 |
| VK159 | Ancient | Kievan Rus' sample | Krzewińska et al. 2018 |
| VK160 | Ancient | Kievan Rus' sample | Krzewińska et al. 2018 |

## Distance Analysis (2026-01-23)

### Distances from andrzej_zak (sorted by proximity)

| Comparison | Euclidean Distance | Interpretation |
|------------|-------------------|----------------|
| andrzej_zak ↔ VK159 | 0.0326 | Close (Kievan Rus') |
| andrzej_zak ↔ VK156 | 0.0353 | Close (Bodzia) |
| andrzej_zak ↔ VK160 | 0.0399 | Close (Kievan Rus') |
| andrzej_zak ↔ VK155 | 0.0461 | Moderate |
| andrzej_zak ↔ VK157 | 0.0547 | Moderate |

### Kievan Rus' vs Bodzia elite (VK157)

| Comparison | Euclidean Distance |
|------------|-------------------|
| VK160 ↔ VK157 | 0.0382 |
| VK159 ↔ VK157 | 0.0608 |
| VK159 ↔ VK160 | 0.0463 |

### Key Finding

andrzej_zak shows closest affinity to Kievan Rus' samples (VK159, VK160), suggesting stronger genetic pull toward Eastern Slavic medieval populations than the Bodzia cemetery cluster. VK160 is notably closer to VK157 than VK159 is, suggesting VK160 may have had more Scandinavian admixture.

## Data Quality Tier

**Exploratory ⚠️** — G25 coordinates are useful for population affinity comparisons and hypothesis generation, but should not be used for definitive phylogenetic claims.

## References

- Krzewińska, M. et al. (2018). Genomic and strontium isotope variation reveal immigration patterns in a Viking Age town. *Current Biology*, 28(17), 2730-2738.
