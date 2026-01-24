#!/bin/bash
# Convert BAM file to GedMatch-compatible 23andMe format
# Usage: bash convert_bam_to_gedmatch.sh input.bam [output_prefix]

set -e

# Configuration
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
REF_GENOME="$PROJECT_DIR/data/reference/genomes/human_g1k_v37.fasta"
DBSNP="$PROJECT_DIR/data/reference/dbsnp/All_20180423.vcf.gz"
OUTPUT_DIR="$PROJECT_DIR/output/gedmatch"

# Input validation
if [ -z "$1" ]; then
    echo "Usage: $0 <input.bam> [output_prefix]"
    echo ""
    echo "Example:"
    echo "  $0 data/raw/bam/VK157.bam VK157"
    exit 1
fi

INPUT_BAM="$1"
OUTPUT_PREFIX="${2:-$(basename "$INPUT_BAM" .bam)}"

# Verify input file exists
if [ ! -f "$INPUT_BAM" ]; then
    echo "ERROR: Input BAM file not found: $INPUT_BAM"
    exit 1
fi

# Verify reference files exist
if [ ! -f "$REF_GENOME" ]; then
    echo "ERROR: Reference genome not found: $REF_GENOME"
    echo "Run: bash scripts/setup_bam_conversion.sh first"
    exit 1
fi

if [ ! -f "$DBSNP" ]; then
    echo "ERROR: dbSNP file not found: $DBSNP"
    echo "Run: bash scripts/setup_bam_conversion.sh first"
    exit 1
fi

echo "=========================================="
echo "BAM → GedMatch Conversion"
echo "=========================================="
echo "Input:  $INPUT_BAM"
echo "Output: $OUTPUT_DIR/${OUTPUT_PREFIX}_23andme.txt"
echo "=========================================="

mkdir -p "$OUTPUT_DIR"
TEMP_DIR="$OUTPUT_DIR/temp_${OUTPUT_PREFIX}"
mkdir -p "$TEMP_DIR"

# Check if BAM is indexed
if [ ! -f "${INPUT_BAM}.bai" ] && [ ! -f "${INPUT_BAM%.bam}.bai" ]; then
    echo "[0/6] Indexing BAM file..."
    samtools index "$INPUT_BAM"
fi

# Step 1: Check BAM header for reference genome build
echo "[1/6] Checking BAM alignment build..."
BAM_BUILD=$(samtools view -H "$INPUT_BAM" | grep -E "^@SQ.*SN:" | head -1)
echo "      Header: $BAM_BUILD"

# Step 2: Variant calling (autosomal chromosomes only)
echo "[2/6] Variant calling (autosomal chr 1-22)..."
echo "      This may take 30-90 minutes for WGS data..."

bcftools mpileup -Ou -f "$REF_GENOME" \
    -r 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22 \
    --max-depth 250 \
    --min-MQ 20 \
    "$INPUT_BAM" 2>/dev/null | \
bcftools call -mv -Ob -o "$TEMP_DIR/raw.bcf" 2>/dev/null

# Step 3: Quality filtering
echo "[3/6] Quality filtering (QUAL >= 20)..."
bcftools view "$TEMP_DIR/raw.bcf" -O z -o "$TEMP_DIR/variants.vcf.gz"
bcftools index "$TEMP_DIR/variants.vcf.gz"
bcftools filter -i 'QUAL>=20' "$TEMP_DIR/variants.vcf.gz" \
    -O z -o "$TEMP_DIR/filtered.vcf.gz"

# Step 4: Normalize variants
echo "[4/6] Normalizing variants..."
bcftools norm -f "$REF_GENOME" "$TEMP_DIR/filtered.vcf.gz" \
    -O z -o "$TEMP_DIR/normalized.vcf.gz" 2>/dev/null
bcftools index "$TEMP_DIR/normalized.vcf.gz"

# Step 4b: Rename chromosomes to match dbSNP format (1 -> chr1)
echo "      Renaming chromosomes to match dbSNP format..."
cat > "$TEMP_DIR/chr_rename.txt" << 'CHRMAP'
1 chr1
2 chr2
3 chr3
4 chr4
5 chr5
6 chr6
7 chr7
8 chr8
9 chr9
10 chr10
11 chr11
12 chr12
13 chr13
14 chr14
15 chr15
16 chr16
17 chr17
18 chr18
19 chr19
20 chr20
21 chr21
22 chr22
CHRMAP
bcftools annotate --rename-chrs "$TEMP_DIR/chr_rename.txt" \
    "$TEMP_DIR/normalized.vcf.gz" -O z -o "$TEMP_DIR/normalized_chr.vcf.gz" 2>/dev/null
bcftools index "$TEMP_DIR/normalized_chr.vcf.gz"

# Step 5: Annotate with rsids
echo "[5/6] Annotating with rsids from dbSNP..."
bcftools annotate -a "$DBSNP" -c ID \
    "$TEMP_DIR/normalized_chr.vcf.gz" \
    -O z -o "$TEMP_DIR/annotated.vcf.gz" 2>/dev/null
bcftools index "$TEMP_DIR/annotated.vcf.gz"

# Count annotation rate
TOTAL=$(bcftools view -H "$TEMP_DIR/annotated.vcf.gz" | wc -l)
ANNOTATED=$(bcftools view -H "$TEMP_DIR/annotated.vcf.gz" | awk '$3 != "."' | wc -l)
RATE=$(echo "scale=1; $ANNOTATED * 100 / $TOTAL" | bc)
echo "      Annotation rate: $RATE% ($ANNOTATED / $TOTAL variants)"

# Step 6: Convert to 23andMe format
echo "[6/6] Converting to 23andMe format..."

# Filter to only SNPs with rsids, then convert with plink
bcftools view -i 'ID!="." && strlen(REF)==1 && strlen(ALT)==1' \
    "$TEMP_DIR/annotated.vcf.gz" -O z -o "$TEMP_DIR/snps_only.vcf.gz"

# Rename chromosomes back to numeric format for plink
echo "      Converting chr-prefixed back to numeric..."
cat > "$TEMP_DIR/chr_rename_back.txt" << 'CHRMAP'
chr1 1
chr2 2
chr3 3
chr4 4
chr5 5
chr6 6
chr7 7
chr8 8
chr9 9
chr10 10
chr11 11
chr12 12
chr13 13
chr14 14
chr15 15
chr16 16
chr17 17
chr18 18
chr19 19
chr20 20
chr21 21
chr22 22
CHRMAP
bcftools annotate --rename-chrs "$TEMP_DIR/chr_rename_back.txt" \
    "$TEMP_DIR/snps_only.vcf.gz" -O z -o "$TEMP_DIR/snps_numeric.vcf.gz" 2>/dev/null

plink --vcf "$TEMP_DIR/snps_numeric.vcf.gz" \
    --recode 23 \
    --chr 1-22 \
    --out "$TEMP_DIR/plink_output" 2>/dev/null

# Add proper header and rename
echo "# rsid	chromosome	position	genotype" > "$OUTPUT_DIR/${OUTPUT_PREFIX}_23andme.txt"
tail -n +2 "$TEMP_DIR/plink_output.txt" >> "$OUTPUT_DIR/${OUTPUT_PREFIX}_23andme.txt"

# Final statistics
SNP_COUNT=$(tail -n +2 "$OUTPUT_DIR/${OUTPUT_PREFIX}_23andme.txt" | wc -l | tr -d ' ')

echo ""
echo "=========================================="
echo "Conversion Complete!"
echo "=========================================="
echo "Output file: $OUTPUT_DIR/${OUTPUT_PREFIX}_23andme.txt"
echo "SNP count:   $SNP_COUNT"
echo ""

if [ "$SNP_COUNT" -lt 200000 ]; then
    echo "⚠️  WARNING: SNP count < 200,000"
    echo "   GedMatch may reject files with too few SNPs."
    echo "   This often indicates low-coverage sequencing data."
else
    echo "✓ SNP count looks good for GedMatch upload"
fi

echo ""
echo "To upload to GedMatch:"
echo "  1. Go to https://www.gedmatch.com"
echo "  2. Log in → DNA Upload"
echo "  3. Select '23andMe' format"
echo "  4. Upload: $OUTPUT_DIR/${OUTPUT_PREFIX}_23andme.txt"
echo "=========================================="

# Cleanup temp files (optional - comment out to keep for debugging)
# rm -rf "$TEMP_DIR"
echo ""
echo "Temp files retained at: $TEMP_DIR"
echo "(Delete manually when done: rm -rf $TEMP_DIR)"
