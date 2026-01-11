#!/usr/bin/env python3
"""
Genealogical DNA Analysis Pipeline
"""
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from y_dna.haplogroup_parser import parse_isogg_tree
from y_dna.snp_analyzer import analyze_snps
from y_dna.tmrca_calculator import calculate_tmrca
from genealogical.gedcom_parser import parse_family_tree
from visualization.phylogenetic_trees import generate_haplogroup_tree
from database.queries import store_results


def main():
    print("🧬 Starting genealogical DNA analysis pipeline...")
    
    # Step 1: Parse Y-DNA data
    print("\n1. Parsing Y-DNA haplogroup data...")
    isogg_tree_path = 'data/reference/isogg_y_tree.csv'
    if os.path.exists(isogg_tree_path):
        y_dna_tree = parse_isogg_tree(isogg_tree_path)
        print(f"   ✓ Loaded {len(y_dna_tree)} haplogroup entries")
    else:
        print(f"   ⚠ Warning: {isogg_tree_path} not found. Download from ISOGG.")
        y_dna_tree = None
    
    # Step 2: Analyze SNPs
    print("\n2. Analyzing SNP data...")
    snp_data_path = 'data/raw/y_dna_results/snp_data.vcf'
    if os.path.exists(snp_data_path):
        snp_results = analyze_snps(snp_data_path)
        print(f"   ✓ Analyzed {len(snp_results)} SNPs")
    else:
        print(f"   ⚠ Warning: {snp_data_path} not found. Add your VCF file.")
        snp_results = []
    
    # Step 3: Calculate TMRCA
    print("\n3. Calculating TMRCA for family branches...")
    y_str_path = 'data/processed/y_str_haplotypes.csv'
    if os.path.exists(y_str_path):
        tmrca_data = calculate_tmrca(
            your_haplogroup='I-Y45113',
            cousin_haplogroups=['I-Y224059', 'I-Y45233'],
            y_str_profiles=y_str_path
        )
        print("   ✓ TMRCA calculation complete")
    else:
        print(f"   ⚠ Warning: {y_str_path} not found. Add your Y-STR data.")
        tmrca_data = {}
    
    # Step 4: Parse genealogical records
    print("\n4. Parsing family tree...")
    gedcom_path = 'data/raw/genealogical/family_tree.ged'
    if os.path.exists(gedcom_path):
        family_tree = parse_family_tree(gedcom_path)
        print("   ✓ Family tree parsed")
    else:
        print(f"   ⚠ Warning: {gedcom_path} not found. Add your GEDCOM file.")
        family_tree = {}
    
    # Step 5: Generate visualizations
    print("\n5. Generating visualizations...")
    if y_dna_tree is not None and not y_dna_tree.empty:
        try:
            generate_haplogroup_tree(
                y_dna_tree,
                output='output/visualizations/haplogroup_tree.png'
            )
            print("   ✓ Haplogroup tree generated")
        except Exception as e:
            print(f"   ⚠ Warning: Could not generate tree: {e}")
    else:
        print("   ⚠ Skipping visualization (no tree data)")
    
    # Step 6: Store in database
    print("\n6. Storing results in database...")
    try:
        store_results(y_dna_tree, snp_results, tmrca_data, family_tree)
        print("   ✓ Results stored")
    except Exception as e:
        print(f"   ⚠ Warning: Could not store results: {e}")
    
    print("\n✅ Pipeline complete! Results saved to output/")


if __name__ == "__main__":
    main()
