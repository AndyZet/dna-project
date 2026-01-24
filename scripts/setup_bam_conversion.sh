#!/bin/bash
# Setup script for BAM to GedMatch conversion
# Run this ONCE to install dependencies and download reference data

set -e

echo "=========================================="
echo "BAM → GedMatch Conversion Setup"
echo "=========================================="

# Check for Homebrew
if ! command -v brew &> /dev/null; then
    echo "ERROR: Homebrew not found. Install from https://brew.sh"
    exit 1
fi

# Install plink if missing
if ! command -v plink &> /dev/null; then
    echo "[1/4] Installing plink..."
    brew install plink
else
    echo "[1/4] plink already installed ✓"
fi

# Create reference data directory
REF_DIR="$(dirname "$0")/../data/reference/genomes"
mkdir -p "$REF_DIR"
cd "$REF_DIR"

# Download GRCh37 reference genome (if not present)
if [ ! -f "GRCh37.fa" ] && [ ! -f "human_g1k_v37.fasta" ]; then
    echo "[2/4] Downloading GRCh37 reference genome (~3GB)..."
    echo "      This may take 10-30 minutes depending on connection..."

    # Use 1000 Genomes version (widely compatible)
    wget -c ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/human_g1k_v37.fasta.gz
    echo "      Decompressing..."
    gunzip human_g1k_v37.fasta.gz

    # Create samtools index
    echo "      Indexing reference..."
    samtools faidx human_g1k_v37.fasta
else
    echo "[2/4] Reference genome already present ✓"
fi

# Download dbSNP for rsid annotation (if not present)
DBSNP_DIR="$(dirname "$0")/../data/reference/dbsnp"
mkdir -p "$DBSNP_DIR"
cd "$DBSNP_DIR"

if [ ! -f "All_20180423.vcf.gz" ]; then
    echo "[3/4] Downloading dbSNP b151 (~10GB compressed)..."
    echo "      This may take 30-60 minutes..."

    wget -c ftp://ftp.ncbi.nih.gov/snp/organisms/human_9606_b151_GRCh37p13/VCF/GATK/All_20180423.vcf.gz
    wget -c ftp://ftp.ncbi.nih.gov/snp/organisms/human_9606_b151_GRCh37p13/VCF/GATK/All_20180423.vcf.gz.tbi
else
    echo "[3/4] dbSNP already present ✓"
fi

# Create output directory
OUTPUT_DIR="$(dirname "$0")/../output/gedmatch"
mkdir -p "$OUTPUT_DIR"

echo "[4/4] Setup complete!"
echo ""
echo "=========================================="
echo "Next steps:"
echo "=========================================="
echo "1. Download your BAM files from Google Drive to:"
echo "   $(dirname "$0")/../data/raw/bam/"
echo ""
echo "2. Run the conversion:"
echo "   bash scripts/convert_bam_to_gedmatch.sh data/raw/bam/your_file.bam"
echo ""
echo "Reference files location:"
echo "  - Genome: $REF_DIR/"
echo "  - dbSNP:  $DBSNP_DIR/"
echo "=========================================="
