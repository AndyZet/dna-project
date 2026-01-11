"""
Match DNA to Bodzia ancient DNA samples
"""
import pandas as pd
import json
from typing import Dict, List, Optional


def match_bodzia_samples(
    your_dna: str,
    bodzia_samples: str
) -> List[Dict]:
    """
    Match your DNA to Bodzia ancient DNA samples.
    
    Args:
        your_dna: Path to your DNA results (JSON or CSV)
        bodzia_samples: Path to Bodzia samples CSV
        
    Returns:
        List of match results
    """
    matches = []
    
    try:
        # Load your DNA data
        if your_dna.endswith('.json'):
            with open(your_dna, 'r') as f:
                your_data = json.load(f)
        else:
            your_data = pd.read_csv(your_dna)
        
        # Load Bodzia samples
        bodzia_df = pd.read_csv(bodzia_samples)
        
        # Perform matching analysis
        print(f"Matching to {len(bodzia_df)} Bodzia samples")
        
        # Placeholder for actual matching logic
        # This would compare SNP profiles, calculate genetic distances, etc.
        
    except FileNotFoundError as e:
        print(f"Warning: File not found - {e}")
    except Exception as e:
        print(f"Error matching Bodzia samples: {e}")
    
    return matches
