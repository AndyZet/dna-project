"""
Admixture Analysis Module
Parse and analyze admixture percentages from Explore Your DNA and other sources
"""
from typing import Dict, List, Optional, Any
import json
from pathlib import Path


class AdmixtureAnalyzer:
    """Analyze admixture components (ancient and modern)"""
    
    def __init__(self):
        """Initialize admixture analyzer"""
        self.admixture_data = {}  # sample_id -> admixture profile
    
    def parse_admixture_data(
        self,
        sample_id: str,
        source_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Extract admixture percentages from source data.
        
        Expected structure:
        {
            'ancient': {
                'Yamnaya_RUS_Samara': 48.1,
                'TUR_Barcin_N': 27.9,
                'WHG': 21.9,
                ...
            },
            'modern': {
                'Europe': 96.0,
                'Northwestern European': 39.0,
                'English': 28.2,
                ...
            }
        }
        
        Args:
            sample_id: Sample identifier
            source_data: Dictionary with admixture data
            
        Returns:
            Structured admixture profile
        """
        profile = {
            'sample_id': sample_id,
            'ancient': source_data.get('ancient', {}),
            'modern': source_data.get('modern', {}),
            'total_ancient': sum(source_data.get('ancient', {}).values()),
            'total_modern': sum(source_data.get('modern', {}).values())
        }
        
        self.admixture_data[sample_id] = profile
        return profile
    
    def compare_admixture_profiles(
        self,
        sample_ids: List[str]
    ) -> Dict[str, Any]:
        """
        Compare admixture profiles between samples.
        
        Args:
            sample_ids: List of sample IDs to compare
            
        Returns:
            Dictionary with comparison results
        """
        # Check all samples exist
        missing = [sid for sid in sample_ids if sid not in self.admixture_data]
        if missing:
            raise ValueError(f"Samples not found: {missing}")
        
        if len(sample_ids) < 2:
            raise ValueError("Need at least 2 samples to compare")
        
        # Extract all component names
        all_ancient_components = set()
        all_modern_components = set()
        
        for sid in sample_ids:
            profile = self.admixture_data[sid]
            all_ancient_components.update(profile['ancient'].keys())
            all_modern_components.update(profile['modern'].keys())
        
        # Compare ancient components
        ancient_comparison = {}
        for component in all_ancient_components:
            values = {}
            for sid in sample_ids:
                values[sid] = self.admixture_data[sid]['ancient'].get(component, 0.0)
            ancient_comparison[component] = values
        
        # Compare modern components
        modern_comparison = {}
        for component in all_modern_components:
            values = {}
            for sid in sample_ids:
                values[sid] = self.admixture_data[sid]['modern'].get(component, 0.0)
            modern_comparison[component] = values
        
        # Calculate differences
        differences = {}
        if len(sample_ids) == 2:
            sid1, sid2 = sample_ids[0], sample_ids[1]
            
            # Ancient differences
            for component in all_ancient_components:
                val1 = self.admixture_data[sid1]['ancient'].get(component, 0.0)
                val2 = self.admixture_data[sid2]['ancient'].get(component, 0.0)
                diff = abs(val1 - val2)
                if diff > 0.1:  # Only include significant differences
                    differences[f'ancient_{component}'] = {
                        sid1: val1,
                        sid2: val2,
                        'difference': diff
                    }
            
            # Modern differences
            for component in all_modern_components:
                val1 = self.admixture_data[sid1]['modern'].get(component, 0.0)
                val2 = self.admixture_data[sid2]['modern'].get(component, 0.0)
                diff = abs(val1 - val2)
                if diff > 0.1:  # Only include significant differences
                    differences[f'modern_{component}'] = {
                        sid1: val1,
                        sid2: val2,
                        'difference': diff
                    }
        
        return {
            'sample_ids': sample_ids,
            'ancient_comparison': ancient_comparison,
            'modern_comparison': modern_comparison,
            'differences': differences
        }
    
    def calculate_admixture_statistics(
        self,
        sample_ids: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Calculate aggregate statistics across samples.
        
        Args:
            sample_ids: List of sample IDs (None = all samples)
            
        Returns:
            Dictionary with statistics
        """
        if sample_ids is None:
            sample_ids = list(self.admixture_data.keys())
        
        if not sample_ids:
            return {}
        
        # Collect all components
        all_ancient = {}
        all_modern = {}
        
        for sid in sample_ids:
            profile = self.admixture_data[sid]
            
            for component, value in profile['ancient'].items():
                if component not in all_ancient:
                    all_ancient[component] = []
                all_ancient[component].append(value)
            
            for component, value in profile['modern'].items():
                if component not in all_modern:
                    all_modern[component] = []
                all_modern[component].append(value)
        
        # Calculate statistics
        ancient_stats = {}
        for component, values in all_ancient.items():
            ancient_stats[component] = {
                'mean': sum(values) / len(values),
                'min': min(values),
                'max': max(values),
                'std': (sum((x - sum(values)/len(values))**2 for x in values) / len(values))**0.5 if len(values) > 1 else 0.0
            }
        
        modern_stats = {}
        for component, values in all_modern.items():
            modern_stats[component] = {
                'mean': sum(values) / len(values),
                'min': min(values),
                'max': max(values),
                'std': (sum((x - sum(values)/len(values))**2 for x in values) / len(values))**0.5 if len(values) > 1 else 0.0
            }
        
        return {
            'sample_count': len(sample_ids),
            'ancient_statistics': ancient_stats,
            'modern_statistics': modern_stats
        }
    
    def identify_shared_components(
        self,
        sample_ids: List[str],
        threshold: float = 1.0
    ) -> Dict[str, List[str]]:
        """
        Find common ancestry components across samples.
        
        Args:
            sample_ids: List of sample IDs
            threshold: Minimum percentage to consider a component present
            
        Returns:
            Dictionary with shared components by category
        """
        if len(sample_ids) < 2:
            return {'ancient': [], 'modern': []}
        
        # Find components present in all samples
        shared_ancient = []
        shared_modern = []
        
        # Get components from first sample
        first_profile = self.admixture_data[sample_ids[0]]
        
        # Check ancient components
        for component in first_profile['ancient'].keys():
            if first_profile['ancient'][component] >= threshold:
                # Check if present in all other samples
                present_in_all = True
                for sid in sample_ids[1:]:
                    if sid not in self.admixture_data:
                        present_in_all = False
                        break
                    value = self.admixture_data[sid]['ancient'].get(component, 0.0)
                    if value < threshold:
                        present_in_all = False
                        break
                
                if present_in_all:
                    shared_ancient.append(component)
        
        # Check modern components
        for component in first_profile['modern'].keys():
            if first_profile['modern'][component] >= threshold:
                # Check if present in all other samples
                present_in_all = True
                for sid in sample_ids[1:]:
                    if sid not in self.admixture_data:
                        present_in_all = False
                        break
                    value = self.admixture_data[sid]['modern'].get(component, 0.0)
                    if value < threshold:
                        present_in_all = False
                        break
                
                if present_in_all:
                    shared_modern.append(component)
        
        return {
            'ancient': shared_ancient,
            'modern': shared_modern
        }
    
    def get_profile(self, sample_id: str) -> Optional[Dict[str, Any]]:
        """Get admixture profile for a sample"""
        return self.admixture_data.get(sample_id)
    
    def export_profiles(self, output_path: str):
        """Export all profiles to JSON"""
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(self.admixture_data, f, indent=2)
