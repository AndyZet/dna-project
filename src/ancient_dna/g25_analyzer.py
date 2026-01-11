"""
G25 Coordinate Parser and Analyzer
Parse G25 coordinate files and perform genetic distance calculations
"""
import csv
import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any
import numpy as np


class G25Analyzer:
    """Parse and analyze G25 coordinates for genetic distance calculations"""
    
    def __init__(self):
        """Initialize G25 analyzer"""
        self.coordinates = {}  # sample_id -> numpy array of 25 coordinates
        self.reference_populations = {}  # population_name -> numpy array
    
    def parse_g25_file(self, file_path: str) -> Dict[str, np.ndarray]:
        """
        Parse G25 coordinate file.
        
        Format: sample_id,coord1,coord2,...,coord25
        
        Args:
            file_path: Path to G25 coordinate file
            
        Returns:
            Dictionary mapping sample_id to numpy array of coordinates
        """
        file_path = Path(file_path)
        if not file_path.exists():
            raise FileNotFoundError(f"G25 file not found: {file_path}")
        
        coords_dict = {}
        
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if not row or len(row) < 26:  # Need sample_id + 25 coordinates
                    continue
                
                sample_id = row[0].strip()
                try:
                    coords = np.array([float(x) for x in row[1:26]], dtype=np.float64)
                    if len(coords) == 25:
                        coords_dict[sample_id] = coords
                        self.coordinates[sample_id] = coords
                except (ValueError, IndexError) as e:
                    print(f"Warning: Could not parse coordinates for {sample_id}: {e}")
                    continue
        
        return coords_dict
    
    def load_coordinates(self, sample_id: str, coordinates: np.ndarray):
        """
        Load coordinates for a sample directly.
        
        Args:
            sample_id: Sample identifier
            coordinates: numpy array of 25 G25 coordinates
        """
        if len(coordinates) != 25:
            raise ValueError(f"G25 coordinates must have 25 dimensions, got {len(coordinates)}")
        self.coordinates[sample_id] = np.array(coordinates, dtype=np.float64)
    
    def calculate_distance(self, coords1: np.ndarray, coords2: np.ndarray) -> float:
        """
        Calculate Euclidean distance between two G25 coordinate vectors.
        
        Args:
            coords1: First coordinate vector (25 dimensions)
            coords2: Second coordinate vector (25 dimensions)
            
        Returns:
            Euclidean distance
        """
        if len(coords1) != 25 or len(coords2) != 25:
            raise ValueError("Both coordinate vectors must have 25 dimensions")
        
        return float(np.linalg.norm(coords1 - coords2))
    
    def compare_samples(self, sample_ids: List[str]) -> Dict[str, Any]:
        """
        Compare multiple samples pairwise.
        
        Args:
            sample_ids: List of sample IDs to compare
            
        Returns:
            Dictionary with pairwise distances and statistics
        """
        # Check all samples exist
        missing = [sid for sid in sample_ids if sid not in self.coordinates]
        if missing:
            raise ValueError(f"Samples not found: {missing}")
        
        if len(sample_ids) < 2:
            raise ValueError("Need at least 2 samples to compare")
        
        # Calculate pairwise distances
        distances = {}
        distance_matrix = []
        
        for i, sid1 in enumerate(sample_ids):
            row = []
            for j, sid2 in enumerate(sample_ids):
                if i == j:
                    distance = 0.0
                else:
                    distance = self.calculate_distance(
                        self.coordinates[sid1],
                        self.coordinates[sid2]
                    )
                row.append(distance)
                if i < j:  # Only store upper triangle to avoid duplicates
                    distances[f"{sid1}_vs_{sid2}"] = distance
            distance_matrix.append(row)
        
        # Calculate statistics
        pairwise_distances = [d for d in distances.values()]
        
        results = {
            'sample_ids': sample_ids,
            'pairwise_distances': distances,
            'distance_matrix': distance_matrix,
            'statistics': {
                'min_distance': float(np.min(pairwise_distances)) if pairwise_distances else None,
                'max_distance': float(np.max(pairwise_distances)) if pairwise_distances else None,
                'mean_distance': float(np.mean(pairwise_distances)) if pairwise_distances else None,
                'median_distance': float(np.median(pairwise_distances)) if pairwise_distances else None,
                'std_distance': float(np.std(pairwise_distances)) if pairwise_distances else None
            }
        }
        
        return results
    
    def find_closest_references(
        self,
        sample_id: str,
        reference_data: Dict[str, np.ndarray],
        top_n: int = 10
    ) -> List[Dict[str, Any]]:
        """
        Find closest reference populations for a sample.
        
        Args:
            sample_id: Sample ID to analyze
            reference_data: Dictionary mapping population names to G25 coordinates
            top_n: Number of closest populations to return
            
        Returns:
            List of dictionaries with population name and distance, sorted by distance
        """
        if sample_id not in self.coordinates:
            raise ValueError(f"Sample {sample_id} not found in coordinates")
        
        sample_coords = self.coordinates[sample_id]
        distances = []
        
        for pop_name, pop_coords in reference_data.items():
            try:
                distance = self.calculate_distance(sample_coords, pop_coords)
                distances.append({
                    'population': pop_name,
                    'distance': distance
                })
            except Exception as e:
                print(f"Warning: Could not calculate distance to {pop_name}: {e}")
                continue
        
        # Sort by distance and return top N
        distances.sort(key=lambda x: x['distance'])
        return distances[:top_n]
    
    def get_coordinates(self, sample_id: str) -> Optional[np.ndarray]:
        """
        Get coordinates for a sample.
        
        Args:
            sample_id: Sample identifier
            
        Returns:
            numpy array of coordinates or None if not found
        """
        return self.coordinates.get(sample_id)
    
    def get_all_samples(self) -> List[str]:
        """Get list of all loaded sample IDs"""
        return list(self.coordinates.keys())
    
    def export_coordinates(self, output_path: str):
        """
        Export all coordinates to JSON file.
        
        Args:
            output_path: Path to save JSON file
        """
        export_data = {
            sample_id: coords.tolist()
            for sample_id, coords in self.coordinates.items()
        }
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, indent=2)
    
    def load_reference_population(self, population_name: str, coordinates: np.ndarray):
        """
        Load reference population coordinates.
        
        Args:
            population_name: Name of the reference population
            coordinates: numpy array of 25 G25 coordinates
        """
        if len(coordinates) != 25:
            raise ValueError(f"G25 coordinates must have 25 dimensions, got {len(coordinates)}")
        self.reference_populations[population_name] = np.array(coordinates, dtype=np.float64)
