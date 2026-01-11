"""
Genetic Analyzer Visualizer
Create visualizations for comprehensive genetic analysis
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from pathlib import Path
from typing import Dict, List, Optional, Any
import json


class GeneticAnalyzerVisualizer:
    """Create visualizations for genetic analysis results"""
    
    def __init__(self, output_dir: str = "output/visualizations/genetic_analysis"):
        """Initialize visualizer"""
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        sns.set_theme(style="whitegrid")
    
    def plot_g25_coordinates(
        self,
        samples: Dict[str, np.ndarray],
        reference_populations: Optional[Dict[str, np.ndarray]] = None,
        output_path: Optional[str] = None,
        use_pca: bool = True,
        n_components: int = 2
    ) -> str:
        """
        Plot G25 coordinates (2D scatter plot using PCA if use_pca=True).
        
        Args:
            samples: Dictionary mapping sample_id to G25 coordinates
            reference_populations: Optional dictionary mapping pop_name to coordinates
            output_path: Path to save plot
            use_pca: Whether to use PCA for dimensionality reduction
            n_components: Number of PCA components (2 or 3)
            
        Returns:
            Path to saved plot
        """
        from sklearn.decomposition import PCA
        
        if output_path is None:
            output_path = self.output_dir / "g25_coordinates.png"
        
        # Combine samples and references
        all_data = {**samples}
        if reference_populations:
            all_data.update(reference_populations)
        
        # Extract coordinates
        labels = list(all_data.keys())
        coords_matrix = np.array([all_data[label] for label in labels])
        
        # Perform PCA
        pca = PCA(n_components=n_components)
        pca_coords = pca.fit_transform(coords_matrix)
        
        # Separate samples and references
        n_samples = len(samples)
        sample_coords = pca_coords[:n_samples]
        ref_coords = pca_coords[n_samples:] if reference_populations else None
        
        # Create plot
        fig, ax = plt.subplots(figsize=(12, 8))
        
        # Plot reference populations
        if ref_coords is not None:
            ax.scatter(
                ref_coords[:, 0],
                ref_coords[:, 1],
                c='lightgray',
                alpha=0.5,
                s=30,
                label='Reference Populations'
            )
        
        # Plot samples
        sample_labels = list(samples.keys())
        colors = plt.cm.Set3(np.linspace(0, 1, len(sample_labels)))
        
        for i, (label, coords) in enumerate(zip(sample_labels, sample_coords)):
            ax.scatter(
                coords[0],
                coords[1],
                c=[colors[i]],
                s=200,
                label=label,
                edgecolors='black',
                linewidth=2
            )
            ax.annotate(
                label,
                (coords[0], coords[1]),
                xytext=(5, 5),
                textcoords='offset points',
                fontsize=10,
                fontweight='bold'
            )
        
        ax.set_xlabel(f'PC1 ({pca.explained_variance_ratio_[0]:.1%} variance)', fontsize=12)
        ax.set_ylabel(f'PC2 ({pca.explained_variance_ratio_[1]:.1%} variance)', fontsize=12)
        ax.set_title('G25 Coordinates - Principal Component Analysis', fontsize=14, fontweight='bold')
        ax.legend(loc='best')
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        return str(output_path)
    
    def plot_admixture_breakdown(
        self,
        samples: Dict[str, Dict[str, Any]],
        component_type: str = 'ancient',
        output_path: Optional[str] = None
    ) -> str:
        """
        Plot admixture bar chart.
        
        Args:
            samples: Dictionary mapping sample_id to admixture profile
            component_type: 'ancient' or 'modern'
            output_path: Path to save plot
            
        Returns:
            Path to saved plot
        """
        if output_path is None:
            output_path = self.output_dir / f"admixture_{component_type}.png"
        
        # Prepare data
        data = []
        for sample_id, profile in samples.items():
            admixture = profile.get('admixture', {})
            components = admixture.get(component_type, {})
            for component, percentage in components.items():
                data.append({
                    'Sample': sample_id,
                    'Component': component,
                    'Percentage': percentage
                })
        
        if not data:
            raise ValueError(f"No {component_type} admixture data found")
        
        df = pd.DataFrame(data)
        
        # Create plot
        fig, ax = plt.subplots(figsize=(14, 8))
        
        # Pivot for grouped bar chart
        pivot_df = df.pivot(index='Component', columns='Sample', values='Percentage')
        pivot_df = pivot_df.sort_values(by=pivot_df.columns[0], ascending=False)
        
        pivot_df.plot(kind='bar', ax=ax, width=0.8)
        
        ax.set_xlabel('Component', fontsize=12)
        ax.set_ylabel('Percentage (%)', fontsize=12)
        ax.set_title(f'{component_type.capitalize()} Admixture Breakdown', fontsize=14, fontweight='bold')
        ax.legend(title='Sample', loc='best')
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
        ax.grid(True, alpha=0.3, axis='y')
        
        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        return str(output_path)
    
    def plot_population_distances(
        self,
        sample_id: str,
        distances: List[Dict[str, Any]],
        top_n: int = 15,
        output_path: Optional[str] = None
    ) -> str:
        """
        Plot population distances as horizontal bar chart.
        
        Args:
            sample_id: Sample identifier
            distances: List of population distance dictionaries
            top_n: Number of top populations to show
            output_path: Path to save plot
            
        Returns:
            Path to saved plot
        """
        if output_path is None:
            output_path = self.output_dir / f"population_distances_{sample_id}.png"
        
        # Get top N populations
        top_distances = distances[:top_n]
        
        # Prepare data
        populations = [d['population'] for d in top_distances]
        dist_values = [d['distance'] for d in top_distances]
        
        # Create plot
        fig, ax = plt.subplots(figsize=(12, 10))
        
        y_pos = np.arange(len(populations))
        bars = ax.barh(y_pos, dist_values, color=plt.cm.viridis(np.linspace(0, 1, len(populations))))
        
        ax.set_yticks(y_pos)
        ax.set_yticklabels(populations)
        ax.set_xlabel('Genetic Distance', fontsize=12)
        ax.set_ylabel('Population', fontsize=12)
        ax.set_title(f'Closest Ancient Populations - {sample_id}', fontsize=14, fontweight='bold')
        ax.invert_yaxis()  # Closest at top
        ax.grid(True, alpha=0.3, axis='x')
        
        # Add value labels
        for i, (bar, dist) in enumerate(zip(bars, dist_values)):
            ax.text(dist, i, f' {dist:.4f}', va='center', fontsize=9)
        
        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        return str(output_path)
    
    def plot_pca_results(
        self,
        pca_data: Dict[str, Any],
        samples: List[str],
        output_path: Optional[str] = None
    ) -> str:
        """
        Plot PCA results.
        
        Args:
            pca_data: Dictionary with PCA results from PCAAnalyzer
            samples: List of sample IDs
            output_path: Path to save plot
            
        Returns:
            Path to saved plot
        """
        if output_path is None:
            output_path = self.output_dir / "pca_results.png"
        
        pca_coords = pca_data.get('pca_coordinates', {})
        
        fig, ax = plt.subplots(figsize=(10, 8))
        
        colors = plt.cm.Set3(np.linspace(0, 1, len(samples)))
        
        for i, sid in enumerate(samples):
            if sid in pca_coords:
                coords = pca_coords[sid]
                ax.scatter(
                    coords[0],
                    coords[1],
                    c=[colors[i]],
                    s=200,
                    label=sid,
                    edgecolors='black',
                    linewidth=2
                )
                ax.annotate(
                    sid,
                    (coords[0], coords[1]),
                    xytext=(5, 5),
                    textcoords='offset points',
                    fontsize=10,
                    fontweight='bold'
                )
        
        explained_var = pca_data.get('explained_variance_ratio', [])
        ax.set_xlabel(f'PC1 ({explained_var[0]:.1%} variance)' if explained_var else 'PC1', fontsize=12)
        ax.set_ylabel(f'PC2 ({explained_var[1]:.1%} variance)' if len(explained_var) > 1 else 'PC2', fontsize=12)
        ax.set_title('PCA Results - Genetic Relationships', fontsize=14, fontweight='bold')
        ax.legend(loc='best')
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        return str(output_path)
    
    def plot_comparison_matrix(
        self,
        samples: Dict[str, Dict[str, Any]],
        output_path: Optional[str] = None
    ) -> str:
        """
        Plot comparison heatmap showing genetic distances between samples.
        
        Args:
            samples: Dictionary mapping sample_id to profile with G25 coordinates
            output_path: Path to save plot
            
        Returns:
            Path to saved plot
        """
        if output_path is None:
            output_path = self.output_dir / "comparison_matrix.png"
        
        # Extract G25 coordinates
        sample_ids = list(samples.keys())
        coords_dict = {}
        for sid in sample_ids:
            if 'g25_coordinates' in samples[sid]:
                coords_dict[sid] = np.array(samples[sid]['g25_coordinates'])
        
        if len(coords_dict) < 2:
            raise ValueError("Need at least 2 samples with G25 coordinates")
        
        # Calculate distance matrix
        import sys
        from pathlib import Path
        project_root = Path(__file__).parent.parent.parent
        sys.path.insert(0, str(project_root / "src"))
        from ancient_dna.g25_analyzer import G25Analyzer
        g25_analyzer = G25Analyzer()
        for sid, coords in coords_dict.items():
            g25_analyzer.load_coordinates(sid, coords)
        
        comparison = g25_analyzer.compare_samples(list(coords_dict.keys()))
        distance_matrix = comparison['distance_matrix']
        
        # Create heatmap
        fig, ax = plt.subplots(figsize=(10, 8))
        
        im = ax.imshow(distance_matrix, cmap='YlOrRd', aspect='auto')
        
        # Set ticks
        ax.set_xticks(np.arange(len(sample_ids)))
        ax.set_yticks(np.arange(len(sample_ids)))
        ax.set_xticklabels(sample_ids)
        ax.set_yticklabels(sample_ids)
        
        # Add text annotations
        for i in range(len(sample_ids)):
            for j in range(len(sample_ids)):
                text = ax.text(j, i, f'{distance_matrix[i][j]:.4f}',
                             ha="center", va="center", color="black", fontsize=9)
        
        ax.set_title('Genetic Distance Matrix', fontsize=14, fontweight='bold')
        plt.colorbar(im, ax=ax, label='Genetic Distance')
        
        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        return str(output_path)
    
    def create_interactive_dashboard(
        self,
        profiles: Dict[str, Dict[str, Any]],
        output_path: Optional[str] = None
    ) -> str:
        """
        Create interactive HTML dashboard combining all visualizations.
        
        Args:
            profiles: Dictionary mapping sample_id to comprehensive profile
            output_path: Path to save HTML file
            
        Returns:
            Path to saved HTML file
        """
        if output_path is None:
            output_path = self.output_dir / "genetic_analysis_dashboard.html"
        
        # Create subplots
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('G25 Coordinates (PCA)', 'Admixture Comparison', 
                          'Population Distances', 'Genetic Distance Matrix'),
            specs=[[{"type": "scatter"}, {"type": "bar"}],
                   [{"type": "bar"}, {"type": "heatmap"}]]
        )
        
        # 1. G25 Coordinates (PCA)
        sample_ids = list(profiles.keys())
        g25_coords = {}
        for sid in sample_ids:
            if 'g25_coordinates' in profiles[sid]:
                g25_coords[sid] = np.array(profiles[sid]['g25_coordinates'])
        
        if g25_coords:
            from sklearn.decomposition import PCA
            g25_sample_ids = list(g25_coords.keys())
            coords_matrix = np.array([g25_coords[sid] for sid in g25_sample_ids])
            pca = PCA(n_components=2)
            pca_coords = pca.fit_transform(coords_matrix)
            
            for i, sid in enumerate(g25_sample_ids):
                fig.add_trace(
                    go.Scatter(
                        x=[pca_coords[i, 0]],
                        y=[pca_coords[i, 1]],
                        mode='markers+text',
                        name=sid,
                        text=[sid],
                        textposition="top center",
                        marker=dict(size=15)
                    ),
                    row=1, col=1
                )
        
        # 2. Admixture Comparison
        admixture_data = []
        for sid in sample_ids:
            if 'admixture' in profiles[sid]:
                admixture = profiles[sid]['admixture']
                ancient = admixture.get('ancient', {})
                for component, pct in ancient.items():
                    admixture_data.append({
                        'Sample': sid,
                        'Component': component,
                        'Percentage': pct
                    })
        
        if admixture_data:
            df_admix = pd.DataFrame(admixture_data)
            for sid in df_admix['Sample'].unique():
                sample_data = df_admix[df_admix['Sample'] == sid]
                fig.add_trace(
                    go.Bar(
                        x=sample_data['Component'],
                        y=sample_data['Percentage'],
                        name=sid
                    ),
                    row=1, col=2
                )
        
        # 3. Population Distances (for first sample)
        if sample_ids and 'population_distances' in profiles.get(sample_ids[0], {}):
            distances = profiles[sample_ids[0]]['population_distances'][:10]
            populations = [d['population'] for d in distances]
            dist_values = [d['distance'] for d in distances]
            
            fig.add_trace(
                go.Bar(
                    x=dist_values,
                    y=populations,
                    orientation='h',
                    name=sample_ids[0]
                ),
                row=2, col=1
            )
        
        # 4. Distance Matrix
        if len(g25_coords) >= 2:
            import sys
            from pathlib import Path
            project_root = Path(__file__).parent.parent.parent
            sys.path.insert(0, str(project_root / "src"))
            from ancient_dna.g25_analyzer import G25Analyzer
            g25_analyzer = G25Analyzer()
            for sid, coords in g25_coords.items():
                g25_analyzer.load_coordinates(sid, coords)
            comparison = g25_analyzer.compare_samples(list(g25_coords.keys()))
            distance_matrix = comparison['distance_matrix']
            
            fig.add_trace(
                go.Heatmap(
                    z=distance_matrix,
                    x=sample_ids,
                    y=sample_ids,
                    colorscale='YlOrRd',
                    showscale=True
                ),
                row=2, col=2
            )
        
        # Update layout
        fig.update_layout(
            height=1000,
            title_text="Comprehensive Genetic Analysis Dashboard",
            showlegend=True
        )
        
        # Save
        fig.write_html(str(output_path))
        
        return str(output_path)
