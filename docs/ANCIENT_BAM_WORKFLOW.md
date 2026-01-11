# Ancient DNA BAM workflow (VK155 / VK157)

This repo can store and analyze **ancient sample BAMs** (e.g., Bodzia VK155 and VK157) locally.

## Recommended storage

Create a dedicated folder for large ancient BAMs, for example:

- `data/raw/ancient_dna/bams/`

and place files like:

- `data/raw/ancient_dna/bams/VK155.bam` + `data/raw/ancient_dna/bams/VK155.bam.bai`
- `data/raw/ancient_dna/bams/VK157.bam` + `data/raw/ancient_dna/bams/VK157.bam.bai`

`.bam`/`.bai` are ignored by git.

## What we need before doing cross-site comparisons

To compare VK155/VK157 to other sites (e.g., Winchester), we need:

- The reference build used for alignment (e.g., GRCh37/hg19, GRCh38, or T2T/CHM13)
- BAM index files (`.bai`) for random access and fast QC
- A toolchain for QC/variant calling (at minimum `samtools`; for aDNA, low-coverage-aware calling is typically required)

If you tell me where your BAMs live inside this workspace and what reference build they use, I can add a small QC step and generate a repeatable report (coverage by contig, mapped reads, etc.).

