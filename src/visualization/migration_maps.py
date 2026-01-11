"""
Create geographic migration maps
"""
import folium
from typing import List, Dict, Tuple, Optional


def create_migration_map(
    locations: List[Dict],
    center: Tuple[float, float] = (52.0, 20.0),
    output_path: str = 'output/visualizations/migration_map.html'
) -> None:
    """
    Create interactive map of migration routes.
    
    Args:
        locations: List of dictionaries with 'lat', 'lon', 'name', 'date'
        center: Center coordinates (lat, lon)
        output_path: Path to save HTML map
    """
    try:
        m = folium.Map(location=center, zoom_start=6)
        
        for loc in locations:
            popup_text = f"{loc.get('name', 'Unknown')}"
            if 'date' in loc:
                popup_text += f"<br>{loc['date']}"
            
            folium.Marker(
                [loc['lat'], loc['lon']],
                popup=popup_text
            ).add_to(m)
        
        m.save(output_path)
        print(f"Migration map saved to {output_path}")
        
    except Exception as e:
        print(f"Error creating migration map: {e}")
