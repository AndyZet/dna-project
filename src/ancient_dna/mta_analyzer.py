"""
Analyzer for MTA match data - statistical analysis and comparisons
"""
from typing import Dict, List, Any, Optional
from collections import Counter, defaultdict
import statistics


class MTAAnalyzer:
    """Analyze MTA match data and compare samples"""
    
    def __init__(self):
        """Initialize analyzer"""
        pass
    
    def analyze_sample(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze a single sample's match data.
        
        Args:
            data: Parsed MTA data from MTAParser
            
        Returns:
            Dictionary with analysis results
        """
        top_matches = data.get('top_matches', [])
        deep_dive = data.get('deep_dive_results', [])
        
        # Genetic distance statistics
        distances = [m['genetic_distance'] for m in top_matches]
        
        # Era distribution
        eras = [m.get('era') for m in top_matches if m.get('era')]
        era_counts = Counter(eras)
        
        # Region distribution
        all_regions = []
        for m in top_matches:
            all_regions.extend(m.get('regions', []))
        region_counts = Counter(all_regions)
        
        # Time period analysis
        years = []
        for m in top_matches:
            date_info = m.get('date', {})
            if date_info.get('year'):
                years.append(date_info['year'])
        
        # Deep Dive statistics
        deep_dive_stats = {}
        if deep_dive:
            total_cm = sum(d.get('total_cm', 0) for d in deep_dive)
            avg_cm = total_cm / len(deep_dive) if deep_dive else 0
            avg_chains = statistics.mean([d.get('num_snp_chains', 0) for d in deep_dive]) if deep_dive else 0
            
            deep_dive_stats = {
                'total_matches': len(deep_dive),
                'total_cm': total_cm,
                'avg_cm_per_match': avg_cm,
                'avg_snp_chains': avg_chains,
                'largest_match_cm': max([d.get('total_cm', 0) for d in deep_dive]) if deep_dive else 0
            }
        
        return {
            'sample_id': data.get('kit_info', {}).get('sample_id'),
            'total_top_matches': len(top_matches),
            'genetic_distance_stats': {
                'min': min(distances) if distances else None,
                'max': max(distances) if distances else None,
                'mean': statistics.mean(distances) if distances else None,
                'median': statistics.median(distances) if distances else None,
                'stdev': statistics.stdev(distances) if len(distances) > 1 else None
            },
            'era_distribution': dict(era_counts),
            'region_distribution': dict(region_counts),
            'time_period_stats': {
                'earliest_year': min(years) if years else None,
                'latest_year': max(years) if years else None,
                'avg_year': statistics.mean(years) if years else None
            },
            'deep_dive_stats': deep_dive_stats,
            'top_10_matches': top_matches[:10] if len(top_matches) >= 10 else top_matches
        }
    
    def compare_samples(
        self,
        vk155_data: Dict[str, Any],
        vk157_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Compare VK155 and VK157 match data.
        
        Args:
            vk155_data: Parsed VK155 data
            vk157_data: Parsed VK157 data
            
        Returns:
            Dictionary with comparison results
        """
        vk155_matches = {m['sample_id']: m for m in vk155_data.get('top_matches', [])}
        vk157_matches = {m['sample_id']: m for m in vk157_data.get('top_matches', [])}
        
        # Find common matches
        common_ids = set(vk155_matches.keys()) & set(vk157_matches.keys())
        common_matches = []
        for sample_id in common_ids:
            vk155_match = vk155_matches[sample_id]
            vk157_match = vk157_matches[sample_id]
            common_matches.append({
                'sample_id': sample_id,
                'description': vk155_match.get('description', ''),
                'vk155_distance': vk155_match.get('genetic_distance'),
                'vk157_distance': vk157_match.get('genetic_distance'),
                'distance_diff': abs(vk155_match.get('genetic_distance', 0) - 
                                    vk157_match.get('genetic_distance', 0)),
                'vk155_rank': vk155_match.get('rank'),
                'vk157_rank': vk157_match.get('rank')
            })
        
        # Sort by average distance
        common_matches.sort(key=lambda x: (x['vk155_distance'] + x['vk157_distance']) / 2)
        
        # Find unique matches
        vk155_unique = set(vk155_matches.keys()) - set(vk157_matches.keys())
        vk157_unique = set(vk157_matches.keys()) - set(vk155_matches.keys())
        
        # Bodzia site connections
        bodzia_samples = ['VK153', 'VK154', 'VK155', 'VK156', 'VK157']
        bodzia_matches_vk155 = {sid: vk155_matches[sid] for sid in bodzia_samples if sid in vk155_matches}
        bodzia_matches_vk157 = {sid: vk157_matches[sid] for sid in bodzia_samples if sid in vk157_matches}
        
        return {
            'common_matches_count': len(common_matches),
            'vk155_unique_count': len(vk155_unique),
            'vk157_unique_count': len(vk157_unique),
            'common_matches': common_matches[:50],  # Top 50 common matches
            'vk155_unique_samples': [vk155_matches[sid]['sample_id'] for sid in list(vk155_unique)[:20]],
            'vk157_unique_samples': [vk157_matches[sid]['sample_id'] for sid in list(vk157_unique)[:20]],
            'bodzia_connections': {
                'vk155': {sid: {
                    'distance': vk155_matches[sid].get('genetic_distance'),
                    'rank': vk155_matches[sid].get('rank')
                } for sid in bodzia_matches_vk155.keys()},
                'vk157': {sid: {
                    'distance': vk157_matches[sid].get('genetic_distance'),
                    'rank': vk157_matches[sid].get('rank')
                } for sid in bodzia_matches_vk157.keys()}
            },
            'distance_correlation': self._calculate_distance_correlation(common_matches)
        }
    
    def _calculate_distance_correlation(self, common_matches: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Calculate correlation between VK155 and VK157 distances for common matches"""
        if len(common_matches) < 2:
            return {'correlation': None, 'note': 'Insufficient data'}
        
        vk155_distances = [m['vk155_distance'] for m in common_matches]
        vk157_distances = [m['vk157_distance'] for m in common_matches]
        
        # Simple correlation calculation
        try:
            import statistics
            mean_vk155 = statistics.mean(vk155_distances)
            mean_vk157 = statistics.mean(vk157_distances)
            
            numerator = sum((vk155_distances[i] - mean_vk155) * (vk157_distances[i] - mean_vk157) 
                          for i in range(len(common_matches)))
            denom_vk155 = sum((d - mean_vk155) ** 2 for d in vk155_distances)
            denom_vk157 = sum((d - mean_vk157) ** 2 for d in vk157_distances)
            
            if denom_vk155 > 0 and denom_vk157 > 0:
                correlation = numerator / ((denom_vk155 * denom_vk157) ** 0.5)
            else:
                correlation = None
            
            return {
                'correlation': correlation,
                'avg_distance_diff': statistics.mean([m['distance_diff'] for m in common_matches]),
                'max_distance_diff': max([m['distance_diff'] for m in common_matches])
            }
        except Exception as e:
            return {'correlation': None, 'error': str(e)}
    
    def identify_patterns(self, vk155_analysis: Dict[str, Any], vk157_analysis: Dict[str, Any]) -> Dict[str, Any]:
        """
        Identify patterns across both samples.
        
        Args:
            vk155_analysis: Analysis results for VK155
            vk157_analysis: Analysis results for VK157
            
        Returns:
            Dictionary with identified patterns
        """
        patterns = {
            'strongest_connections': {
                'vk155': vk155_analysis.get('top_10_matches', [])[:5],
                'vk157': vk157_analysis.get('top_10_matches', [])[:5]
            },
            'dominant_eras': {
                'vk155': self._get_top_items(vk155_analysis.get('era_distribution', {}), 3),
                'vk157': self._get_top_items(vk157_analysis.get('era_distribution', {}), 3)
            },
            'dominant_regions': {
                'vk155': self._get_top_items(vk155_analysis.get('region_distribution', {}), 5),
                'vk157': self._get_top_items(vk157_analysis.get('region_distribution', {}), 5)
            },
            'time_period_focus': {
                'vk155': vk155_analysis.get('time_period_stats', {}),
                'vk157': vk157_analysis.get('time_period_stats', {})
            }
        }
        
        return patterns
    
    def _get_top_items(self, counter_dict: Dict[str, int], n: int) -> List[tuple]:
        """Get top N items from a counter dictionary"""
        sorted_items = sorted(counter_dict.items(), key=lambda x: x[1], reverse=True)
        return sorted_items[:n]
