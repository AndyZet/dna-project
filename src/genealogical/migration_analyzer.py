"""
Analyze family migration patterns
"""
import pandas as pd
from typing import Dict, List
import geopandas as gpd


def analyze_migrations(
    genealogical_data: pd.DataFrame,
    location_column: str = 'location'
) -> Dict:
    """
    Analyze migration patterns from genealogical data.
    
    Args:
        genealogical_data: DataFrame with genealogical records
        location_column: Column name containing location data
        
    Returns:
        Dictionary with migration analysis results
    """
    results = {
        'migration_routes': [],
        'geographic_distribution': {},
        'timeline': []
    }
    
    try:
        if location_column in genealogical_data.columns:
            # Analyze location changes over time
            locations = genealogical_data[location_column].value_counts()
            results['geographic_distribution'] = locations.to_dict()
            
            print("Analyzing migration patterns...")
        
    except Exception as e:
        print(f"Error analyzing migrations: {e}")
    
    return results


def create_migration_map(
    genealogical_data: pd.DataFrame,
    output_path: str = 'output/visualizations/migration_map.html'
) -> None:
    """
    Create interactive map of migration routes.
    
    Args:
        genealogical_data: DataFrame with location and date data
        output_path: Path to save HTML map
    """
    try:
        import folium
        
        # Create base map
        m = folium.Map(location=[52.0, 20.0], zoom_start=6)
        
        # Add markers for locations
        if 'latitude' in genealogical_data.columns and 'longitude' in genealogical_data.columns:
            for idx, row in genealogical_data.iterrows():
                folium.Marker(
                    [row['latitude'], row['longitude']],
                    popup=row.get('location', 'Unknown')
                ).add_to(m)
        
        m.save(output_path)
        print(f"Migration map saved to {output_path}")
        
    except Exception as e:
        print(f"Error creating migration map: {e}")
