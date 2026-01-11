"""
Generate phylogenetic tree visualizations
"""
from typing import Optional
from Bio import Phylo
import matplotlib.pyplot as plt


def generate_haplogroup_tree(
    tree_data,
    output: str = 'output/visualizations/haplogroup_tree.png'
) -> None:
    """
    Generate Y-DNA haplogroup tree visualization.
    
    Args:
        tree_data: Tree data (Newick format or Phylo object)
        output: Output file path
    """
    try:
        # Parse tree if string
        if isinstance(tree_data, str):
            trees = Phylo.parse(tree_data, "newick")
            tree = next(trees)
        else:
            tree = tree_data
        
        # Create visualization
        fig, ax = plt.subplots(figsize=(12, 8))
        Phylo.draw(tree, axes=ax)
        plt.title('Y-DNA Haplogroup Tree')
        plt.savefig(output, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"Haplogroup tree saved to {output}")
        
    except Exception as e:
        print(f"Error generating haplogroup tree: {e}")


def draw_ascii_tree(tree_path: str) -> None:
    """
    Draw ASCII representation of phylogenetic tree.
    
    Args:
        tree_path: Path to Newick tree file
    """
    try:
        trees = Phylo.parse(tree_path, "newick")
        for tree in trees:
            Phylo.draw_ascii(tree)
    except Exception as e:
        print(f"Error drawing ASCII tree: {e}")
