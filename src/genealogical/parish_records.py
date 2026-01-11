"""
Handle parish records data
"""
import pandas as pd
from typing import Dict, List, Optional


def load_parish_records(records_path: str) -> pd.DataFrame:
    """
    Load parish records from CSV or other format.
    
    Args:
        records_path: Path to parish records file
        
    Returns:
        DataFrame with parish records
    """
    try:
        df = pd.read_csv(records_path)
        return df
    except FileNotFoundError:
        print(f"Warning: {records_path} not found.")
        return pd.DataFrame()
    except Exception as e:
        print(f"Error loading parish records: {e}")
        return pd.DataFrame()


def search_parish_records(
    df: pd.DataFrame,
    name: Optional[str] = None,
    location: Optional[str] = None,
    date_range: Optional[tuple] = None
) -> pd.DataFrame:
    """
    Search parish records by criteria.
    
    Args:
        df: DataFrame with parish records
        name: Name to search for
        location: Location to filter by
        date_range: Tuple of (start_date, end_date)
        
    Returns:
        Filtered DataFrame
    """
    filtered = df.copy()
    
    if name:
        filtered = filtered[filtered['name'].str.contains(name, case=False, na=False)]
    
    if location:
        filtered = filtered[filtered['location'].str.contains(location, case=False, na=False)]
    
    if date_range:
        start_date, end_date = date_range
        if 'date' in filtered.columns:
            filtered = filtered[
                (filtered['date'] >= start_date) & 
                (filtered['date'] <= end_date)
            ]
    
    return filtered
