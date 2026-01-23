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

## Distance Analysis (2026-01-23)

### Distances from andrzej_zak (sorted by proximity)

| Comparison | Euclidean Distance | Interpretation |
|------------|-------------------|----------------|
| andrzej_zak ↔ VK159 | 0.0326 | Close (Kievan Rus') |
| andrzej_zak ↔ VK156 | 0.0353 | Close (Bodzia) |
| andrzej_zak ↔ VK155 | 0.0461 | Moderate |
| andrzej_zak ↔ VK157 | 0.0547 | Moderate |

### Ancient sample internal distances

| Comparison | Euclidean Distance |
|------------|-------------------|
| VK155 ↔ VK157 | 0.0417 |
| VK156 ↔ VK159 | 0.0418 |
| VK155 ↔ VK156 | 0.0420 |
| VK156 ↔ VK157 | 0.0425 |
| VK155 ↔ VK159 | 0.0549 |
| VK157 ↔ VK159 | 0.0608 |

### Key Finding

andrzej_zak shows closest affinity to VK159 (Kievan Rus'), suggesting stronger genetic pull toward Eastern Slavic medieval populations than the Bodzia cemetery cluster. VK157 shows the greatest distance from VK159, consistent with VK157's stronger Scandinavian ancestry component.

## Data Quality Tier

**Exploratory ⚠️** — G25 coordinates are useful for population affinity comparisons and hypothesis generation, but should not be used for definitive phylogenetic claims.

## References

- Krzewińska, M. et al. (2018). Genomic and strontium isotope variation reveal immigration patterns in a Viking Age town. *Current Biology*, 28(17), 2730-2738.
