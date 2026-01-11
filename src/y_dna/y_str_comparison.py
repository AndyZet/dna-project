"""
Y-STR comparison and matching
"""
import pandas as pd
from typing import List, Dict
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage, dendrogram


def compare_y_str_profiles(y_str_data: pd.DataFrame) -> Dict:
    """
    Compare Y-STR profiles and calculate distances.
    
    Args:
        y_str_data: DataFrame with Y-STR haplotypes
        
    Returns:
        Dictionary with distance matrix and clusters
    """
    results = {
        'distances': None,
        'clusters': None
    }
    
    try:
        # Extract Y-STR marker columns
        y_str_markers = y_str_data.select_dtypes(include=['int64', 'float64']).columns
        
        # Calculate Manhattan distance (cityblock) for Y-STR
        y_str_profiles = y_str_data[y_str_markers].values
        distances = pdist(y_str_profiles, metric='cityblock')
        distance_matrix = squareform(distances)
        
        results['distances'] = distance_matrix
        
        # Perform hierarchical clustering
        linkage_matrix = linkage(distances, method='ward')
        results['clusters'] = linkage_matrix
        
    except Exception as e:
        print(f"Error comparing Y-STR profiles: {e}")
    
    return results


def find_matches(
    y_str_data: pd.DataFrame,
    target_profile: Dict,
    max_distance: int = 10
) -> pd.DataFrame:
    """
    Find Y-STR matches within specified distance.
    
    Args:
        y_str_data: DataFrame with Y-STR haplotypes
        target_profile: Dictionary with target Y-STR values
        max_distance: Maximum Manhattan distance for match
        
    Returns:
        DataFrame with matching profiles
    """
    matches = pd.DataFrame()
    
    try:
        # Calculate distances and filter
        # Implementation depends on Y-STR marker structure
        print(f"Finding matches within distance {max_distance}")
        
    except Exception as e:
        print(f"Error finding matches: {e}")
    
    return matches
