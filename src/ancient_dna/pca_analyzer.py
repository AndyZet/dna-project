"""
PCA Analysis Module
Perform Principal Component Analysis on G25 coordinates
"""
from typing import Dict, List, Optional, Any, Tuple
import numpy as np
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import json
from pathlib import Path


class PCAAnalyzer:
    """Perform PCA analysis on genetic coordinates"""
    
    def __init__(self):
        """Initialize PCA analyzer"""
        self.pca_model = None
        self.pca_results = {}
        self.clusters = {}
    
    def perform_pca(
        self,
        samples_coords: Dict[str, np.ndarray],
        n_components: int = 2
    ) -> Dict[str, Any]:
        """
        Perform PCA on sample coordinates.
        
        Args:
            samples_coords: Dictionary mapping sample_id to coordinate array
            n_components: Number of principal components to extract
            
        Returns:
            Dictionary with PCA results
        """
        if len(samples_coords) < 2:
            raise ValueError("Need at least 2 samples for PCA")
        
        # Extract sample IDs and coordinate arrays
        sample_ids = list(samples_coords.keys())
        coords_matrix = np.array([samples_coords[sid] for sid in sample_ids])
        
        # Check dimensions
        if coords_matrix.shape[1] != 25:
            raise ValueError(f"Expected 25-dimensional G25 coordinates, got {coords_matrix.shape[1]}")
        
        # Perform PCA
        pca = PCA(n_components=n_components)
        pca_coords = pca.fit_transform(coords_matrix)
        
        # Store model
        self.pca_model = pca
        
        # Create results dictionary
        results = {
            'sample_ids': sample_ids,
            'pca_coordinates': {
                sid: pca_coords[i].tolist()
                for i, sid in enumerate(sample_ids)
            },
            'explained_variance_ratio': pca.explained_variance_ratio_.tolist(),
            'explained_variance': pca.explained_variance_.tolist(),
            'components': pca.components_.tolist(),
            'mean': pca.mean_.tolist(),
            'n_components': n_components
        }
        
        self.pca_results[f'n_components_{n_components}'] = results
        return results
    
    def project_samples(
        self,
        samples_coords: Dict[str, np.ndarray],
        pca_model: Optional[PCA] = None
    ) -> Dict[str, np.ndarray]:
        """
        Project samples onto PCA space using existing model.
        
        Args:
            samples_coords: Dictionary mapping sample_id to coordinate array
            pca_model: Pre-fitted PCA model (uses self.pca_model if None)
            
        Returns:
            Dictionary mapping sample_id to PCA coordinates
        """
        if pca_model is None:
            if self.pca_model is None:
                raise ValueError("No PCA model available. Run perform_pca() first.")
            pca_model = self.pca_model
        
        projected = {}
        for sid, coords in samples_coords.items():
            if len(coords) != 25:
                raise ValueError(f"Expected 25-dimensional coordinates for {sid}")
            projected_coords = pca_model.transform(coords.reshape(1, -1))
            projected[sid] = projected_coords[0]
        
        return projected
    
    def identify_clusters(
        self,
        samples_coords: Dict[str, np.ndarray],
        n_clusters: int = 2
    ) -> Dict[str, Any]:
        """
        Identify genetic clusters using K-means clustering.
        
        Args:
            samples_coords: Dictionary mapping sample_id to coordinate array
            n_clusters: Number of clusters to identify
            
        Returns:
            Dictionary with cluster assignments
        """
        if len(samples_coords) < n_clusters:
            raise ValueError(f"Need at least {n_clusters} samples for {n_clusters} clusters")
        
        # Extract coordinates
        sample_ids = list(samples_coords.keys())
        coords_matrix = np.array([samples_coords[sid] for sid in sample_ids])
        
        # Perform K-means clustering
        kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
        cluster_labels = kmeans.fit_predict(coords_matrix)
        
        # Organize results by cluster
        clusters = {}
        for i, sid in enumerate(sample_ids):
            cluster_id = int(cluster_labels[i])
            if cluster_id not in clusters:
                clusters[cluster_id] = []
            clusters[cluster_id].append(sid)
        
        results = {
            'n_clusters': n_clusters,
            'cluster_assignments': {
                sid: int(cluster_labels[i])
                for i, sid in enumerate(sample_ids)
            },
            'clusters': clusters,
            'cluster_centers': kmeans.cluster_centers_.tolist(),
            'inertia': float(kmeans.inertia_)
        }
        
        self.clusters[f'n_clusters_{n_clusters}'] = results
        return results
    
    def compare_with_references(
        self,
        samples_coords: Dict[str, np.ndarray],
        reference_coords: Dict[str, np.ndarray],
        n_components: int = 2
    ) -> Dict[str, Any]:
        """
        Compare samples with reference populations using PCA.
        
        Args:
            samples_coords: Dictionary mapping sample_id to coordinate array
            reference_coords: Dictionary mapping population_name to coordinate array
            n_components: Number of PCA components
            
        Returns:
            Dictionary with combined PCA results
        """
        # Combine samples and references
        all_coords = {**samples_coords, **reference_coords}
        
        # Perform PCA on combined dataset
        sample_ids = list(samples_coords.keys())
        ref_names = list(reference_coords.keys())
        all_names = sample_ids + ref_names
        
        coords_matrix = np.array([all_coords[name] for name in all_names])
        
        pca = PCA(n_components=n_components)
        pca_coords = pca.fit_transform(coords_matrix)
        
        # Separate sample and reference coordinates
        n_samples = len(sample_ids)
        sample_pca = {
            sid: pca_coords[i].tolist()
            for i, sid in enumerate(sample_ids)
        }
        reference_pca = {
            ref_name: pca_coords[n_samples + i].tolist()
            for i, ref_name in enumerate(ref_names)
        }
        
        return {
            'sample_ids': sample_ids,
            'reference_populations': ref_names,
            'sample_pca_coordinates': sample_pca,
            'reference_pca_coordinates': reference_pca,
            'explained_variance_ratio': pca.explained_variance_ratio_.tolist(),
            'n_components': n_components
        }
    
    def get_pca_results(self, n_components: int = 2) -> Optional[Dict[str, Any]]:
        """Get stored PCA results"""
        key = f'n_components_{n_components}'
        return self.pca_results.get(key)
    
    def get_clusters(self, n_clusters: int = 2) -> Optional[Dict[str, Any]]:
        """Get stored cluster results"""
        key = f'n_clusters_{n_clusters}'
        return self.clusters.get(key)
    
    def export_results(self, output_path: str):
        """Export PCA and cluster results to JSON"""
        export_data = {
            'pca_results': self.pca_results,
            'clusters': self.clusters
        }
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, indent=2)
