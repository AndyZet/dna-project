"""
Visualization module for MTA match data
"""
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path
from typing import Dict, List, Any, Optional
import json


class MTAVisualizer:
    """Generate visualizations for MTA match data"""
    
    def __init__(self, output_dir: str = "output/visualizations/mta"):
        """
        Initialize visualizer.
        
        Args:
            output_dir: Directory to save visualizations
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Set style
        sns.set_style("whitegrid")
        plt.rcParams['figure.figsize'] = (12, 8)
        plt.rcParams['font.size'] = 10
    
    def plot_genetic_distance_distribution(
        self,
        vk155_distances: List[float],
        vk157_distances: List[float],
        output_filename: str = "genetic_distance_distribution.png"
    ):
        """Plot genetic distance distribution for both samples"""
        fig, axes = plt.subplots(1, 2, figsize=(14, 6))
        
        # VK155
        axes[0].hist(vk155_distances, bins=50, alpha=0.7, color='#4ECDC4', edgecolor='black')
        axes[0].set_title('VK155 (Elite Woman) - Genetic Distance Distribution', fontsize=12, fontweight='bold')
        axes[0].set_xlabel('Genetic Distance', fontsize=10)
        axes[0].set_ylabel('Frequency', fontsize=10)
        axes[0].axvline(np.mean(vk155_distances), color='red', linestyle='--', 
                       label=f'Mean: {np.mean(vk155_distances):.2f}')
        axes[0].legend()
        axes[0].grid(True, alpha=0.3)
        
        # VK157
        axes[1].hist(vk157_distances, bins=50, alpha=0.7, color='#FF6B6B', edgecolor='black')
        axes[1].set_title('VK157 (Elite Warrior) - Genetic Distance Distribution', fontsize=12, fontweight='bold')
        axes[1].set_xlabel('Genetic Distance', fontsize=10)
        axes[1].set_ylabel('Frequency', fontsize=10)
        axes[1].axvline(np.mean(vk157_distances), color='red', linestyle='--', 
                       label=f'Mean: {np.mean(vk157_distances):.2f}')
        axes[1].legend()
        axes[1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        output_path = self.output_dir / output_filename
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
        return str(output_path)
    
    def plot_era_distribution(
        self,
        vk155_eras: Dict[str, int],
        vk157_eras: Dict[str, int],
        output_filename: str = "era_distribution.png"
    ):
        """Plot era distribution comparison"""
        fig, axes = plt.subplots(1, 2, figsize=(14, 6))
        
        # VK155
        if vk155_eras:
            eras_155 = list(vk155_eras.keys())
            counts_155 = list(vk155_eras.values())
            axes[0].barh(eras_155, counts_155, color='#4ECDC4', edgecolor='black')
            axes[0].set_title('VK155 - Era Distribution', fontsize=12, fontweight='bold')
            axes[0].set_xlabel('Number of Matches', fontsize=10)
            axes[0].invert_yaxis()
            axes[0].grid(True, alpha=0.3, axis='x')
        
        # VK157
        if vk157_eras:
            eras_157 = list(vk157_eras.keys())
            counts_157 = list(vk157_eras.values())
            axes[1].barh(eras_157, counts_157, color='#FF6B6B', edgecolor='black')
            axes[1].set_title('VK157 - Era Distribution', fontsize=12, fontweight='bold')
            axes[1].set_xlabel('Number of Matches', fontsize=10)
            axes[1].invert_yaxis()
            axes[1].grid(True, alpha=0.3, axis='x')
        
        plt.tight_layout()
        output_path = self.output_dir / output_filename
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
        return str(output_path)
    
    def plot_region_distribution(
        self,
        vk155_regions: Dict[str, int],
        vk157_regions: Dict[str, int],
        output_filename: str = "region_distribution.png"
    ):
        """Plot geographic region distribution"""
        fig, axes = plt.subplots(1, 2, figsize=(16, 8))
        
        # VK155
        if vk155_regions:
            regions_155 = list(vk155_regions.keys())[:15]  # Top 15
            counts_155 = [vk155_regions[r] for r in regions_155]
            axes[0].barh(regions_155, counts_155, color='#4ECDC4', edgecolor='black')
            axes[0].set_title('VK155 - Top Geographic Regions', fontsize=12, fontweight='bold')
            axes[0].set_xlabel('Number of Matches', fontsize=10)
            axes[0].invert_yaxis()
            axes[0].grid(True, alpha=0.3, axis='x')
        
        # VK157
        if vk157_regions:
            regions_157 = list(vk157_regions.keys())[:15]  # Top 15
            counts_157 = [vk157_regions[r] for r in regions_157]
            axes[1].barh(regions_157, counts_157, color='#FF6B6B', edgecolor='black')
            axes[1].set_title('VK157 - Top Geographic Regions', fontsize=12, fontweight='bold')
            axes[1].set_xlabel('Number of Matches', fontsize=10)
            axes[1].invert_yaxis()
            axes[1].grid(True, alpha=0.3, axis='x')
        
        plt.tight_layout()
        output_path = self.output_dir / output_filename
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
        return str(output_path)
    
    def plot_time_period_distribution(
        self,
        vk155_years: List[float],
        vk157_years: List[float],
        output_filename: str = "time_period_distribution.png"
    ):
        """Plot time period distribution"""
        fig, axes = plt.subplots(2, 1, figsize=(14, 10))
        
        # VK155
        axes[0].hist(vk155_years, bins=50, alpha=0.7, color='#4ECDC4', edgecolor='black')
        axes[0].set_title('VK155 - Time Period Distribution', fontsize=12, fontweight='bold')
        axes[0].set_xlabel('Year (BC/AD)', fontsize=10)
        axes[0].set_ylabel('Frequency', fontsize=10)
        axes[0].axvline(0, color='black', linestyle='-', linewidth=1, alpha=0.5, label='AD/BC boundary')
        axes[0].legend()
        axes[0].grid(True, alpha=0.3)
        
        # VK157
        axes[1].hist(vk157_years, bins=50, alpha=0.7, color='#FF6B6B', edgecolor='black')
        axes[1].set_title('VK157 - Time Period Distribution', fontsize=12, fontweight='bold')
        axes[1].set_xlabel('Year (BC/AD)', fontsize=10)
        axes[1].set_ylabel('Frequency', fontsize=10)
        axes[1].axvline(0, color='black', linestyle='-', linewidth=1, alpha=0.5, label='AD/BC boundary')
        axes[1].legend()
        axes[1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        output_path = self.output_dir / output_filename
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
        return str(output_path)
    
    def plot_comparison_scatter(
        self,
        common_matches: List[Dict[str, Any]],
        output_filename: str = "distance_comparison_scatter.png"
    ):
        """Plot scatter plot comparing VK155 vs VK157 distances for common matches"""
        if not common_matches:
            return None
        
        vk155_distances = [m['vk155_distance'] for m in common_matches]
        vk157_distances = [m['vk157_distance'] for m in common_matches]
        
        plt.figure(figsize=(10, 10))
        plt.scatter(vk155_distances, vk157_distances, alpha=0.6, s=50, color='#95E1D3', edgecolors='black')
        
        # Add diagonal line
        max_dist = max(max(vk155_distances), max(vk157_distances))
        plt.plot([0, max_dist], [0, max_dist], 'r--', alpha=0.5, label='Perfect correlation')
        
        plt.xlabel('VK155 Genetic Distance', fontsize=12, fontweight='bold')
        plt.ylabel('VK157 Genetic Distance', fontsize=12, fontweight='bold')
        plt.title('VK155 vs VK157 Genetic Distances (Common Matches)', fontsize=14, fontweight='bold')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        output_path = self.output_dir / output_filename
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
        return str(output_path)
    
    def plot_top_matches_comparison(
        self,
        vk155_top: List[Dict[str, Any]],
        vk157_top: List[Dict[str, Any]],
        output_filename: str = "top_matches_comparison.png"
    ):
        """Plot comparison of top matches"""
        fig, axes = plt.subplots(1, 2, figsize=(16, 10))
        
        # VK155 top 20
        if vk155_top:
            top20_155 = vk155_top[:20]
            distances_155 = [m['genetic_distance'] for m in top20_155]
            labels_155 = [f"{m['rank']}. {m['sample_id']}" for m in top20_155]
            
            axes[0].barh(range(len(labels_155)), distances_155, color='#4ECDC4', edgecolor='black')
            axes[0].set_yticks(range(len(labels_155)))
            axes[0].set_yticklabels(labels_155, fontsize=8)
            axes[0].set_xlabel('Genetic Distance', fontsize=10)
            axes[0].set_title('VK155 - Top 20 Matches', fontsize=12, fontweight='bold')
            axes[0].invert_yaxis()
            axes[0].grid(True, alpha=0.3, axis='x')
        
        # VK157 top 20
        if vk157_top:
            top20_157 = vk157_top[:20]
            distances_157 = [m['genetic_distance'] for m in top20_157]
            labels_157 = [f"{m['rank']}. {m['sample_id']}" for m in top20_157]
            
            axes[1].barh(range(len(labels_157)), distances_157, color='#FF6B6B', edgecolor='black')
            axes[1].set_yticks(range(len(labels_157)))
            axes[1].set_yticklabels(labels_157, fontsize=8)
            axes[1].set_xlabel('Genetic Distance', fontsize=10)
            axes[1].set_title('VK157 - Top 20 Matches', fontsize=12, fontweight='bold')
            axes[1].invert_yaxis()
            axes[1].grid(True, alpha=0.3, axis='x')
        
        plt.tight_layout()
        output_path = self.output_dir / output_filename
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
        return str(output_path)
