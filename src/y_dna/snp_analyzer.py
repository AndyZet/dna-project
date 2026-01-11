"""
Analyze SNP data from VCF files
"""
import pysam
from typing import List, Dict, Optional


def analyze_snps(vcf_path: str) -> List[Dict]:
    """
    Analyze SNP data from VCF file.
    
    Args:
        vcf_path: Path to VCF file
        
    Returns:
        List of SNP records
    """
    results = []
    try:
        vcf_file = pysam.VariantFile(vcf_path)
        for record in vcf_file:
            results.append({
                'chrom': record.chrom,
                'pos': record.pos,
                'ref': record.ref,
                'alt': record.alleles,
                'id': record.id
            })
    except FileNotFoundError:
        print(f"Warning: {vcf_path} not found.")
    except Exception as e:
        print(f"Error reading VCF file: {e}")
    
    return results


def filter_by_haplogroup(vcf_path: str, haplogroup: str) -> List[Dict]:
    """
    Filter SNPs by haplogroup.
    
    Args:
        vcf_path: Path to VCF file
        haplogroup: Haplogroup identifier
        
    Returns:
        Filtered SNP records
    """
    results = []
    try:
        vcf_file = pysam.VariantFile(vcf_path)
        for record in vcf_file:
            info = record.info
            if 'HAPLOGROUP' in info:
                if haplogroup in info['HAPLOGROUP']:
                    results.append({
                        'chrom': record.chrom,
                        'pos': record.pos,
                        'ref': record.ref,
                        'alt': record.alleles
                    })
    except Exception as e:
        print(f"Error filtering VCF: {e}")
    
    return results
