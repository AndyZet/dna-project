"""
Population Distance Analyzer
Parse and analyze genetic distances to ancient reference populations
"""
from typing import Dict, List, Optional, Any
import json
from pathlib import Path


class PopulationDistanceAnalyzer:
    """Analyze genetic distances to ancient reference populations"""
    
    def __init__(self):
        """Initialize population distance analyzer"""
        self.distances = {}  # sample_id -> list of population distances
    
    def parse_population_distances(
        self,
        sample_id: str,
        distances_data: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """
        Extract population distance data.
        
        Expected format:
        [
            {'population': 'VK2020_POL_Sandomierz_VA', 'distance': 0.0321},
            {'population': 'VK2020_SWE_Gotland_VA', 'distance': 0.0333},
            ...
        ]
        
        Args:
            sample_id: Sample identifier
            distances_data: List of dictionaries with population and distance
            
        Returns:
            Sorted list of population distances
        """
        # Validate and sort by distance
        validated_distances = []
        for entry in distances_data:
            if 'population' in entry and 'distance' in entry:
                try:
                    distance = float(entry['distance'])
                    validated_distances.append({
                        'population': entry['population'],
                        'distance': distance
                    })
                except (ValueError, TypeError):
                    continue
        
        # Sort by distance (closest first)
        validated_distances.sort(key=lambda x: x['distance'])
        
        self.distances[sample_id] = validated_distances
        return validated_distances
    
    def rank_populations_by_distance(
        self,
        sample_id: str,
        top_n: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        """
        Get populations ranked by genetic distance for a sample.
        
        Args:
            sample_id: Sample identifier
            top_n: Number of top populations to return (None = all)
            
        Returns:
            List of population distances, sorted by distance
        """
        if sample_id not in self.distances:
            raise ValueError(f"Sample {sample_id} not found in distances")
        
        distances = self.distances[sample_id]
        if top_n is None:
            return distances
        return distances[:top_n]
    
    def find_common_populations(
        self,
        sample_ids: List[str],
        top_n: int = 10
    ) -> Dict[str, Any]:
        """
        Find populations that are close to multiple samples.
        
        Args:
            sample_ids: List of sample IDs
            top_n: Number of top populations to consider per sample
            
        Returns:
            Dictionary with common populations and their distances
        """
        if len(sample_ids) < 2:
            raise ValueError("Need at least 2 samples to find common populations")
        
        # Get top N populations for each sample
        sample_top_populations = {}
        for sid in sample_ids:
            if sid not in self.distances:
                continue
            top_pops = self.rank_populations_by_distance(sid, top_n=top_n)
            sample_top_populations[sid] = {pop['population']: pop['distance'] for pop in top_pops}
        
        # Find populations present in multiple samples
        population_counts = {}
        population_distances = {}
        
        for sid, pops in sample_top_populations.items():
            for pop_name, distance in pops.items():
                if pop_name not in population_counts:
                    population_counts[pop_name] = 0
                    population_distances[pop_name] = {}
                population_counts[pop_name] += 1
                population_distances[pop_name][sid] = distance
        
        # Filter to populations present in at least 2 samples
        common_populations = {}
        for pop_name, count in population_counts.items():
            if count >= 2:
                common_populations[pop_name] = {
                    'sample_count': count,
                    'distances': population_distances[pop_name],
                    'mean_distance': sum(population_distances[pop_name].values()) / count,
                    'min_distance': min(population_distances[pop_name].values()),
                    'max_distance': max(population_distances[pop_name].values())
                }
        
        # Sort by mean distance
        sorted_common = sorted(
            common_populations.items(),
            key=lambda x: x[1]['mean_distance']
        )
        
        return {
            'common_populations': dict(sorted_common),
            'total_common': len(common_populations)
        }
    
    def calculate_group_averages(
        self,
        sample_id: str,
        population_groups: Dict[str, List[str]]
    ) -> Dict[str, float]:
        """
        Calculate average distances to population groups.
        
        Args:
            sample_id: Sample identifier
            population_groups: Dictionary mapping group names to lists of population names
                e.g., {'Viking Age': ['VK2020_SWE_Gotland_VA', ...], ...}
            
        Returns:
            Dictionary with average distances per group
        """
        if sample_id not in self.distances:
            raise ValueError(f"Sample {sample_id} not found in distances")
        
        sample_distances = {pop['population']: pop['distance'] for pop in self.distances[sample_id]}
        
        group_averages = {}
        
        for group_name, population_list in population_groups.items():
            group_distances = []
            for pop_name in population_list:
                if pop_name in sample_distances:
                    group_distances.append(sample_distances[pop_name])
            
            if group_distances:
                group_averages[group_name] = sum(group_distances) / len(group_distances)
            else:
                group_averages[group_name] = None
        
        return group_averages
    
    def create_distance_matrix(
        self,
        sample_ids: List[str],
        reference_populations: List[str]
    ) -> Dict[str, Any]:
        """
        Create distance matrix for samples vs reference populations.
        
        Args:
            sample_ids: List of sample IDs
            reference_populations: List of reference population names
            
        Returns:
            Dictionary with distance matrix and metadata
        """
        matrix = []
        
        for sid in sample_ids:
            if sid not in self.distances:
                row = [None] * len(reference_populations)
            else:
                sample_distances = {pop['population']: pop['distance'] for pop in self.distances[sid]}
                row = [sample_distances.get(pop, None) for pop in reference_populations]
            matrix.append(row)
        
        return {
            'sample_ids': sample_ids,
            'reference_populations': reference_populations,
            'distance_matrix': matrix
        }
    
    def get_distances(self, sample_id: str) -> Optional[List[Dict[str, Any]]]:
        """Get all population distances for a sample"""
        return self.distances.get(sample_id)
    
    def export_distances(self, output_path: str):
        """Export all distances to JSON"""
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(self.distances, f, indent=2)
