"""
Comprehensive Genetic Profile Generator
Integrate all genetic data sources into unified profiles
"""
from typing import Dict, List, Optional, Any
import json
from pathlib import Path
import numpy as np

from .g25_analyzer import G25Analyzer
from .admixture_analyzer import AdmixtureAnalyzer
from .population_distance_analyzer import PopulationDistanceAnalyzer
from .pca_analyzer import PCAAnalyzer


class GeneticProfileGenerator:
    """Generate comprehensive genetic profiles integrating all data sources"""
    
    def __init__(self):
        """Initialize profile generator"""
        self.g25_analyzer = G25Analyzer()
        self.admixture_analyzer = AdmixtureAnalyzer()
        self.distance_analyzer = PopulationDistanceAnalyzer()
        self.pca_analyzer = PCAAnalyzer()
        self.profiles = {}
    
    def generate_profile(
        self,
        sample_id: str,
        g25_coords: Optional[np.ndarray] = None,
        g25_file: Optional[str] = None,
        admixture_data: Optional[Dict[str, Any]] = None,
        population_distances: Optional[List[Dict[str, Any]]] = None,
        haplogroups: Optional[Dict[str, str]] = None,
        mta_data: Optional[Dict[str, Any]] = None,
        metadata: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Create comprehensive genetic profile for a sample.
        
        Args:
            sample_id: Sample identifier
            g25_coords: G25 coordinates as numpy array (or use g25_file)
            g25_file: Path to G25 coordinate file
            admixture_data: Dictionary with ancient/modern admixture percentages
            population_distances: List of population distance dictionaries
            haplogroups: Dictionary with 'Y-DNA' and/or 'mtDNA' keys
            mta_data: MTA match analysis data
            metadata: Additional metadata (date, location, sex, etc.)
            
        Returns:
            Comprehensive genetic profile dictionary
        """
        profile = {
            'sample_id': sample_id,
            'metadata': metadata or {}
        }
        
        # Load G25 coordinates
        if g25_coords is not None:
            self.g25_analyzer.load_coordinates(sample_id, g25_coords)
            profile['g25_coordinates'] = g25_coords.tolist()
        elif g25_file:
            coords_dict = self.g25_analyzer.parse_g25_file(g25_file)
            if sample_id in coords_dict:
                profile['g25_coordinates'] = coords_dict[sample_id].tolist()
        
        # Parse admixture data
        if admixture_data:
            admixture_profile = self.admixture_analyzer.parse_admixture_data(
                sample_id, admixture_data
            )
            profile['admixture'] = admixture_profile
        
        # Parse population distances
        if population_distances:
            distances = self.distance_analyzer.parse_population_distances(
                sample_id, population_distances
            )
            profile['population_distances'] = distances
            profile['closest_populations'] = distances[:10] if len(distances) >= 10 else distances
        
        # Add haplogroups
        if haplogroups:
            profile['haplogroups'] = haplogroups
        
        # Add MTA data
        if mta_data:
            profile['mta_analysis'] = mta_data
        
        # Store profile
        self.profiles[sample_id] = profile
        return profile
    
    def compare_profiles(
        self,
        sample_ids: List[str]
    ) -> Dict[str, Any]:
        """
        Compare genetic profiles across samples.
        
        Args:
            sample_ids: List of sample IDs to compare
            
        Returns:
            Dictionary with comparison results
        """
        # Check all profiles exist
        missing = [sid for sid in sample_ids if sid not in self.profiles]
        if missing:
            raise ValueError(f"Profiles not found: {missing}")
        
        comparison = {
            'sample_ids': sample_ids,
            'g25_comparison': None,
            'admixture_comparison': None,
            'common_populations': None
        }
        
        # Compare G25 coordinates
        g25_coords = {}
        for sid in sample_ids:
            if 'g25_coordinates' in self.profiles[sid]:
                coords = np.array(self.profiles[sid]['g25_coordinates'])
                self.g25_analyzer.load_coordinates(sid, coords)
                g25_coords[sid] = coords
        
        if len(g25_coords) >= 2:
            comparison['g25_comparison'] = self.g25_analyzer.compare_samples(list(g25_coords.keys()))
        
        # Compare admixture
        admixture_samples = [sid for sid in sample_ids if 'admixture' in self.profiles[sid]]
        if len(admixture_samples) >= 2:
            comparison['admixture_comparison'] = self.admixture_analyzer.compare_admixture_profiles(admixture_samples)
        
        # Find common populations
        distance_samples = [sid for sid in sample_ids if 'population_distances' in self.profiles[sid]]
        if len(distance_samples) >= 2:
            all_distances = {}
            for sid in distance_samples:
                distances = self.profiles[sid]['population_distances']
                self.distance_analyzer.parse_population_distances(sid, distances)
            
            comparison['common_populations'] = self.distance_analyzer.find_common_populations(distance_samples)
        
        return comparison
    
    def identify_relationships(
        self,
        profiles: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Identify genetic relationships between profiles.
        
        Args:
            profiles: List of sample IDs (None = all profiles)
            
        Returns:
            Dictionary with relationship analysis
        """
        if profiles is None:
            profiles = list(self.profiles.keys())
        
        if len(profiles) < 2:
            return {'relationships': []}
        
        relationships = []
        
        # Calculate pairwise G25 distances
        g25_coords = {}
        for sid in profiles:
            if 'g25_coordinates' in self.profiles[sid]:
                g25_coords[sid] = np.array(self.profiles[sid]['g25_coordinates'])
        
        if len(g25_coords) >= 2:
            for i, sid1 in enumerate(g25_coords.keys()):
                for sid2 in list(g25_coords.keys())[i+1:]:
                    distance = self.g25_analyzer.calculate_distance(
                        g25_coords[sid1],
                        g25_coords[sid2]
                    )
                    relationships.append({
                        'sample1': sid1,
                        'sample2': sid2,
                        'g25_distance': distance,
                        'relationship_type': self._classify_relationship(distance)
                    })
        
        # Sort by distance
        relationships.sort(key=lambda x: x.get('g25_distance', float('inf')))
        
        return {
            'relationships': relationships,
            'closest_pair': relationships[0] if relationships else None
        }
    
    def _classify_relationship(self, distance: float) -> str:
        """Classify relationship based on G25 distance"""
        if distance < 0.01:
            return 'Very Close (possible close relatives)'
        elif distance < 0.02:
            return 'Close (likely related)'
        elif distance < 0.05:
            return 'Moderate (possibly related)'
        elif distance < 0.10:
            return 'Distant (shared ancestry)'
        else:
            return 'Unrelated (different populations)'
    
    def export_profile(
        self,
        sample_id: str,
        output_format: str = 'json',
        output_path: Optional[str] = None
    ) -> str:
        """
        Export profile in specified format.
        
        Args:
            sample_id: Sample identifier
            output_format: 'json' or 'dict'
            output_path: Path to save file (for JSON format)
            
        Returns:
            Exported data (as string for JSON, dict for dict format)
        """
        if sample_id not in self.profiles:
            raise ValueError(f"Profile not found: {sample_id}")
        
        profile = self.profiles[sample_id]
        
        if output_format == 'json':
            if output_path is None:
                output_path = f"genetic_profile_{sample_id}.json"
            
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(profile, f, indent=2, default=str)
            
            return output_path
        elif output_format == 'dict':
            return profile
        else:
            raise ValueError(f"Unsupported output format: {output_format}")
    
    def get_profile(self, sample_id: str) -> Optional[Dict[str, Any]]:
        """Get profile for a sample"""
        return self.profiles.get(sample_id)
    
    def export_all_profiles(self, output_path: str):
        """Export all profiles to JSON"""
        export_data = {}
        for sid, profile in self.profiles.items():
            # Convert numpy arrays to lists for JSON serialization
            export_profile = json.loads(json.dumps(profile, default=str))
            export_data[sid] = export_profile
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, indent=2, default=str)
