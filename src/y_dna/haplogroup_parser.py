"""
Parse ISOGG Y-DNA haplogroup tree
"""
import pandas as pd
from typing import Dict, List, Optional


def parse_isogg_tree(filepath: str) -> pd.DataFrame:
    """
    Parse ISOGG Y-DNA tree CSV file.
    
    Args:
        filepath: Path to ISOGG Y_Tree_list.csv
        
    Returns:
        DataFrame with haplogroup information
    """
    try:
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        print(f"Warning: {filepath} not found. Please download from ISOGG.")
        return pd.DataFrame()


def find_haplogroup(df: pd.DataFrame, haplogroup: str) -> Optional[pd.Series]:
    """
    Find specific haplogroup in ISOGG tree.
    
    Args:
        df: ISOGG tree DataFrame
        haplogroup: Haplogroup identifier (e.g., 'I-Y45113')
        
    Returns:
        Series with haplogroup data or None
    """
    if df.empty:
        return None
    
    matches = df[df['Haplogroup'] == haplogroup]
    if not matches.empty:
        return matches.iloc[0]
    return None
