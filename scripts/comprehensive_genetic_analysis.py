#!/usr/bin/env python3
"""
Comprehensive Genetic Analysis Script
Integrate G25 coordinates, admixture, population distances, PCA, and MTA data
"""
import sys
import json
from pathlib import Path
from typing import Dict, List, Any, Optional
import numpy as np

# Add src to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root / "src"))

from ancient_dna.g25_analyzer import G25Analyzer
from ancient_dna.admixture_analyzer import AdmixtureAnalyzer
from ancient_dna.population_distance_analyzer import PopulationDistanceAnalyzer
from ancient_dna.pca_analyzer import PCAAnalyzer
from ancient_dna.genetic_profile_generator import GeneticProfileGenerator
from ancient_dna.mta_parser import MTAParser
from visualization.genetic_analyzer_visualizer import GeneticAnalyzerVisualizer


# Admixture data from Explore Your DNA (provided by user)
ADMIXTURE_DATA = {
    'VK155': {
        'ancient': {
            'Yamnaya_RUS_Samara': 52.7,
            'TUR_Barcin_N': 29.7,
            'WHG': 16.9,
            'BRA_LapaDoSanto': 0.7
        },
        'modern': {
            'Europe': 96.0,
            'Northwestern European': 39.0,
            'English': 28.2,
            'Finnish': 9.0,
            'Northwestern European': 1.4,
            'Scandinavian': 0.5,
            'Eastern European': 39.0,
            'Balkan': 12.4,
            'Iberian': 5.7,
            'Asia': 4.0,
            'Northern West Asian': 3.0,
            'Cypriot': 2.5,
            'Central Asian, Northern Indian & Pakistani': 1.0,
            'Indian': 1.1
        }
    },
    'VK157': {
        'ancient': {
            'Yamnaya_RUS_Samara': 48.1,
            'TUR_Barcin_N': 27.9,
            'WHG': 21.9,
            'TUR_Tepecik_Ciftlik_N': 2.1
        },
        'modern': {}  # Not provided in user data
    },
    'VK154': {
        'ancient': {
            'Yamnaya_RUS_Samara': 52.6,
            'TUR_Barcin_N': 28.3,
            'WHG': 19.1
        },
        'modern': {}
    },
    'VK156': {
        'ancient': {
            'Yamnaya_RUS_Samara': 50.9,
            'TUR_Barcin_N': 31.4,
            'WHG': 17.8
        },
        'modern': {}
    }
}

# Population distances from Explore Your DNA
POPULATION_DISTANCES = {
    'VK155': [
        {'population': 'VK2020_POL_Bodzia_VA', 'distance': 0.0309},
        {'population': 'VK2020_SWE_Gotland_VA', 'distance': 0.0391},
        {'population': 'DEU_MA_Krakauer_Berg', 'distance': 0.0399},
        {'population': 'HUN_Avar_Szolad', 'distance': 0.0430},
        {'population': 'VK2020_RUS_Gnezdovo_VA', 'distance': 0.0443},
        {'population': 'VK2020_RUS_Kurevanikha_VA', 'distance': 0.0451},
        {'population': 'RUS_Sunghir_MA', 'distance': 0.0455},
        {'population': 'HUN_IA_La_Tene_o3', 'distance': 0.0470},
        {'population': 'SWE_Viking_Age_Sigtuna', 'distance': 0.0483},
        {'population': 'HUN_EIA_o3', 'distance': 0.0483},
        {'population': 'VK2020_UKR_Lutsk_MA', 'distance': 0.0496},
        {'population': 'VK2020_SWE_Uppsala_VA', 'distance': 0.0507},
        {'population': 'CZE_Early_Slav', 'distance': 0.0511},
        {'population': 'KAZ_Golden_Horde_Euro', 'distance': 0.0518},
        {'population': 'VK2020_UKR_Shestovitsa_VA', 'distance': 0.0528}
    ],
    'VK157': [
        {'population': 'VK2020_POL_Sandomierz_VA', 'distance': 0.0321},
        {'population': 'VK2020_SWE_Gotland_VA', 'distance': 0.0333},
        {'population': 'VK2020_POL_Bodzia_VA', 'distance': 0.0335},
        {'population': 'DEU_MA_Krakauer_Berg', 'distance': 0.0337},
        {'population': 'HUN_Avar_Szolad', 'distance': 0.0372},
        {'population': 'HUN_EIA_o3', 'distance': 0.0379},
        {'population': 'VK2020_RUS_Kurevanikha_VA', 'distance': 0.0386},
        {'population': 'HUN_IA_La_Tene_o3', 'distance': 0.0395},
        {'population': 'RUS_Sunghir_MA', 'distance': 0.0411},
        {'population': 'VK2020_POL_Cedynia_VA', 'distance': 0.0430},
        {'population': 'KAZ_Golden_Horde_Euro', 'distance': 0.0458},
        {'population': 'VK2020_UKR_Shestovitsa_VA', 'distance': 0.0478},
        {'population': 'SWE_Viking_Age_Sigtuna', 'distance': 0.0482},
        {'population': 'VK2020_RUS_Gnezdovo_VA', 'distance': 0.0483},
        {'population': 'HUN_MBA_Fuzesabony', 'distance': 0.0491}
    ],
    'VK154': [
        {'population': 'VK2020_POL_Bodzia_VA', 'distance': 0.0240},
        {'population': 'VK2020_SWE_Gotland_VA', 'distance': 0.0261},
        {'population': 'DEU_MA_Krakauer_Berg', 'distance': 0.0341},
        {'population': 'VK2020_RUS_Kurevanikha_VA', 'distance': 0.0363},
        {'population': 'SWE_Viking_Age_Sigtuna', 'distance': 0.0364},
        {'population': 'VK2020_SWE_Uppsala_VA', 'distance': 0.0372},
        {'population': 'VK2020_EST_Saaremaa_EVA', 'distance': 0.0378},
        {'population': 'VK2020_RUS_Gnezdovo_VA', 'distance': 0.0405},
        {'population': 'HUN_Avar_Szolad', 'distance': 0.0415},
        {'population': 'HUN_IA_La_Tene_o3', 'distance': 0.0419}
    ],
    'VK156': [
        {'population': 'VK2020_POL_Bodzia_VA', 'distance': 0.0189},
        {'population': 'VK2020_SWE_Gotland_VA', 'distance': 0.0222},
        {'population': 'DEU_MA_Krakauer_Berg', 'distance': 0.0268},
        {'population': 'HUN_Avar_Szolad', 'distance': 0.0310},
        {'population': 'SWE_Viking_Age_Sigtuna', 'distance': 0.0313},
        {'population': 'VK2020_RUS_Gnezdovo_VA', 'distance': 0.0324},
        {'population': 'VK2020_SWE_Uppsala_VA', 'distance': 0.0350},
        {'population': 'VK2020_RUS_Ladoga_VA', 'distance': 0.0360},
        {'population': 'HUN_IA_La_Tene_o3', 'distance': 0.0364},
        {'population': 'HUN_EIA_o3', 'distance': 0.0371}
    ]
}

# Haplogroup data from Explore Your DNA
HAPLOGROUPS = {
    'VK155': {
        'mtDNA': 'H1c',
        'Y-DNA': None  # Not determined (female)
    },
    'VK157': {
        'Y-DNA': 'I1a3a1',
        'mtDNA': 'H1c'
    },
    'VK154': {
        'mtDNA': 'H1c3',
        'Y-DNA': None  # Not determined (female)
    },
    'VK156': {
        'Y-DNA': 'R1a1a1b1a2a2a1',
        'mtDNA': 'J1c2c2a'
    }
}

# Sample metadata
SAMPLE_METADATA = {
    'VK155': {
        'date': '1000 AD',
        'sex': 'F',
        'country': 'Poland',
        'locality': 'Bodzia (Kuyavian-Pomeranian Province, Wrocław County, Brześć Kujawski)',
        'publication': 'MargaryanNature2020'
    },
    'VK157': {
        'date': '1000 AD',
        'sex': 'M',
        'country': 'Poland',
        'locality': 'Bodzia (Kuyavian-Pomeranian Province, Wrocław County, Brześć Kujawski)',
        'publication': 'MargaryanNature2020'
    },
    'VK154': {
        'date': '1000 AD',
        'sex': 'F',
        'country': 'Poland',
        'locality': 'Bodzia (Kuyavian-Pomeranian Province, Wrocław County, Brześć Kujawski)',
        'publication': 'MargaryanNature2020'
    },
    'VK156': {
        'date': '1000 AD',
        'sex': 'M',
        'country': 'Poland',
        'locality': 'Bodzia (Kuyavian-Pomeranian Province, Wrocław County, Brześć Kujawski)',
        'publication': 'MargaryanNature2020'
    }
}


def main():
    """Main analysis function"""
    print("=" * 80)
    print("COMPREHENSIVE GENETIC ANALYSIS - BODZIA SAMPLES")
    print("=" * 80)
    
    # Output directories
    output_data_dir = project_root / "data/processed/ancient_dna"
    output_data_dir.mkdir(parents=True, exist_ok=True)
    
    # Initialize modules
    print("\n📊 Step 1: Initializing analysis modules...")
    g25_analyzer = G25Analyzer()
    admixture_analyzer = AdmixtureAnalyzer()
    distance_analyzer = PopulationDistanceAnalyzer()
    pca_analyzer = PCAAnalyzer()
    profile_generator = GeneticProfileGenerator()
    visualizer = GeneticAnalyzerVisualizer()
    mta_parser = MTAParser()
    print("   ✓ Modules initialized")
    
    # Step 2: Load G25 coordinates
    print("\n📖 Step 2: Loading G25 coordinates...")
    g25_files = {
        'VK155': project_root / "data/raw/autosomal/MTA/VK155/vk155_G25.txt",
        'VK157': project_root / "data/raw/autosomal/MTA/VK157/vk157_G25.txt"
    }
    
    g25_coords = {}
    for sample_id, file_path in g25_files.items():
        if file_path.exists():
            coords_dict = g25_analyzer.parse_g25_file(str(file_path))
            if sample_id in coords_dict:
                g25_coords[sample_id] = coords_dict[sample_id]
                print(f"   ✓ Loaded G25 coordinates for {sample_id}")
            else:
                print(f"   ⚠ Warning: {sample_id} not found in {file_path}")
        else:
            print(f"   ⚠ Warning: G25 file not found: {file_path}")
    
    # Step 3: Load MTA data
    print("\n📖 Step 3: Loading MTA match data...")
    mta_files = {
        'VK155': project_root / "data/raw/autosomal/MTA/VK155/matchesMTA.md",
        'VK157': project_root / "data/raw/autosomal/MTA/VK157/matchesMTA.md"
    }
    
    mta_data = {}
    for sample_id, file_path in mta_files.items():
        if file_path.exists():
            try:
                parsed = mta_parser.parse_file(str(file_path))
                mta_data[sample_id] = parsed
                print(f"   ✓ Loaded MTA data for {sample_id}: {parsed.get('total_top_matches', 0)} top matches")
            except Exception as e:
                print(f"   ⚠ Warning: Error parsing MTA data for {sample_id}: {e}")
    
    # Step 4: Generate comprehensive profiles
    print("\n🔬 Step 4: Generating comprehensive genetic profiles...")
    profiles = {}
    
    for sample_id in ['VK155', 'VK157', 'VK154', 'VK156']:
        profile = profile_generator.generate_profile(
            sample_id=sample_id,
            g25_coords=g25_coords.get(sample_id),
            admixture_data=ADMIXTURE_DATA.get(sample_id),
            population_distances=POPULATION_DISTANCES.get(sample_id, []),
            haplogroups=HAPLOGROUPS.get(sample_id),
            mta_data=mta_data.get(sample_id),
            metadata=SAMPLE_METADATA.get(sample_id)
        )
        profiles[sample_id] = profile
        print(f"   ✓ Generated profile for {sample_id}")
    
    # Step 5: Perform comparisons
    print("\n🔍 Step 5: Performing genetic comparisons...")
    
    # G25 comparison (for samples with coordinates)
    samples_with_g25 = [sid for sid in profiles.keys() if 'g25_coordinates' in profiles[sid]]
    if len(samples_with_g25) >= 2:
        comparison = profile_generator.compare_profiles(samples_with_g25)
        print(f"   ✓ Compared {len(samples_with_g25)} samples with G25 coordinates")
        
        # Save comparison
        with open(output_data_dir / "g25_comparison.json", 'w', encoding='utf-8') as f:
            json.dump(comparison, f, indent=2, default=str)
    
    # Admixture comparison
    samples_with_admixture = [sid for sid in profiles.keys() if 'admixture' in profiles[sid]]
    if len(samples_with_admixture) >= 2:
        # Parse admixture data into analyzer first
        for sid in samples_with_admixture:
            if 'admixture' in profiles[sid]:
                admixture_data = {
                    'ancient': profiles[sid]['admixture'].get('ancient', {}),
                    'modern': profiles[sid]['admixture'].get('modern', {})
                }
                admixture_analyzer.parse_admixture_data(sid, admixture_data)
        
        admixture_comparison = admixture_analyzer.compare_admixture_profiles(samples_with_admixture)
        print(f"   ✓ Compared admixture for {len(samples_with_admixture)} samples")
        
        # Save comparison
        with open(output_data_dir / "admixture_comparison.json", 'w', encoding='utf-8') as f:
            json.dump(admixture_comparison, f, indent=2, default=str)
    
    # Common populations
    samples_with_distances = [sid for sid in profiles.keys() if 'population_distances' in profiles[sid]]
    if len(samples_with_distances) >= 2:
        for sid in samples_with_distances:
            distances = profiles[sid]['population_distances']
            distance_analyzer.parse_population_distances(sid, distances)
        
        common_pops = distance_analyzer.find_common_populations(samples_with_distances)
        print(f"   ✓ Found {common_pops['total_common']} common populations")
        
        # Save common populations
        with open(output_data_dir / "common_populations.json", 'w', encoding='utf-8') as f:
            json.dump(common_pops, f, indent=2, default=str)
    
    # Step 6: Perform PCA analysis
    print("\n📊 Step 6: Performing PCA analysis...")
    if len(samples_with_g25) >= 2:
        g25_coords_dict = {}
        for sid in samples_with_g25:
            g25_coords_dict[sid] = np.array(profiles[sid]['g25_coordinates'])
        
        pca_results = pca_analyzer.perform_pca(g25_coords_dict, n_components=2)
        print(f"   ✓ PCA explained variance: PC1={pca_results['explained_variance_ratio'][0]:.1%}, PC2={pca_results['explained_variance_ratio'][1]:.1%}")
        
        # Save PCA results
        with open(output_data_dir / "pca_results.json", 'w', encoding='utf-8') as f:
            json.dump(pca_results, f, indent=2, default=str)
        
        # Cluster analysis
        cluster_results = pca_analyzer.identify_clusters(g25_coords_dict, n_clusters=2)
        print(f"   ✓ Identified {cluster_results['n_clusters']} genetic clusters")
        
        # Save cluster results
        with open(output_data_dir / "cluster_results.json", 'w', encoding='utf-8') as f:
            json.dump(cluster_results, f, indent=2, default=str)
    
    # Step 7: Generate visualizations
    print("\n🎨 Step 7: Generating visualizations...")
    visualization_files = []
    
    try:
        # G25 coordinates plot
        if len(samples_with_g25) >= 2:
            g25_coords_dict = {}
            for sid in samples_with_g25:
                g25_coords_dict[sid] = np.array(profiles[sid]['g25_coordinates'])
            
            viz_file = visualizer.plot_g25_coordinates(g25_coords_dict)
            visualization_files.append(viz_file)
            print(f"   ✓ Created: {Path(viz_file).name}")
        
        # Admixture plots
        samples_with_admix = {sid: profiles[sid] for sid in samples_with_admixture}
        if samples_with_admix:
            viz_file = visualizer.plot_admixture_breakdown(samples_with_admix, component_type='ancient')
            visualization_files.append(viz_file)
            print(f"   ✓ Created: {Path(viz_file).name}")
        
        # Population distances plots
        for sid in samples_with_distances:
            distances = profiles[sid]['population_distances']
            viz_file = visualizer.plot_population_distances(sid, distances, top_n=15)
            visualization_files.append(viz_file)
            print(f"   ✓ Created: {Path(viz_file).name}")
        
        # PCA plot
        if len(samples_with_g25) >= 2 and 'pca_results' in locals():
            viz_file = visualizer.plot_pca_results(pca_results, samples_with_g25)
            visualization_files.append(viz_file)
            print(f"   ✓ Created: {Path(viz_file).name}")
        
        # Comparison matrix
        if len(samples_with_g25) >= 2:
            samples_dict = {sid: profiles[sid] for sid in samples_with_g25}
            viz_file = visualizer.plot_comparison_matrix(samples_dict)
            visualization_files.append(viz_file)
            print(f"   ✓ Created: {Path(viz_file).name}")
        
        # Interactive dashboard
        if profiles:
            viz_file = visualizer.create_interactive_dashboard(profiles)
            visualization_files.append(viz_file)
            print(f"   ✓ Created: {Path(viz_file).name}")
        
    except Exception as e:
        print(f"   ⚠ Warning: Error generating visualizations: {e}")
        import traceback
        traceback.print_exc()
    
    # Step 8: Save comprehensive profiles
    print("\n💾 Step 8: Saving comprehensive profiles...")
    profile_generator.export_all_profiles(str(output_data_dir / "genetic_profiles.json"))
    print(f"   ✓ Saved profiles to {output_data_dir / 'genetic_profiles.json'}")
    
    # Step 9: Integrate with genealogy data
    print("\n🔗 Step 9: Integrating with genealogy data...")
    try:
        genealogy_path = project_root / "data/processed/genealogy/bodzia_complete_tree.json"
        
        if genealogy_path.exists():
            with open(genealogy_path, 'r', encoding='utf-8') as f:
                genealogy_data = json.load(f)
            
            individuals = genealogy_data.get('individuals', [])
            updated_count = 0
            
            for ind in individuals:
                # Find matching sample by VK ID in notes
                notes_str = ' '.join(ind.get('notes', []))
                sample_id = None
                
                # Check for VK IDs in notes
                for sid in ['VK155', 'VK157', 'VK154', 'VK156']:
                    if sid in notes_str:
                        sample_id = sid
                        break
                
                # Also check for known mappings
                ind_id = ind.get('id')
                if not sample_id:
                    if ind_id == 'RUR001' and 'VK157' in notes_str:
                        sample_id = 'VK157'
                    elif ind_id == 'BOD002' and 'VK155' in notes_str:
                        sample_id = 'VK155'
                    elif ind_id == 'BOD001' and 'E864/II' in notes_str:
                        sample_id = 'VK154'  # Princess
                    elif ind_id == 'BOD003' and 'Warrior' in ind.get('name', ''):
                        sample_id = 'VK156'  # Warrior (best guess)
                
                if sample_id and sample_id in profiles:
                    # Add genetic profile
                    profile = profiles[sample_id]
                    ind['genetic_profile'] = profile
                    updated_count += 1
                    print(f"   ✓ Updated {ind.get('name', ind_id)} ({sample_id})")
            
            # Save updated genealogy
            with open(genealogy_path, 'w', encoding='utf-8') as f:
                json.dump(genealogy_data, f, indent=2, default=str)
            
            print(f"   ✓ Updated {updated_count} individuals in genealogy tree")
        else:
            print(f"   ⚠ Warning: Genealogy file not found: {genealogy_path}")
    
    except Exception as e:
        print(f"   ⚠ Warning: Error integrating with genealogy: {e}")
        import traceback
        traceback.print_exc()
    
    # Summary
    print("\n" + "=" * 80)
    print("✅ COMPREHENSIVE GENETIC ANALYSIS COMPLETE!")
    print("=" * 80)
    
    print(f"\n📊 Summary:")
    print(f"   • Profiles generated: {len(profiles)}")
    print(f"   • Samples with G25 coordinates: {len(samples_with_g25)}")
    print(f"   • Samples with admixture data: {len(samples_with_admixture)}")
    print(f"   • Samples with population distances: {len(samples_with_distances)}")
    print(f"   • Visualizations created: {len(visualization_files)}")
    
    print(f"\n📁 Output files:")
    print(f"   • Profiles: {output_data_dir / 'genetic_profiles.json'}")
    print(f"   • Visualizations: {visualizer.output_dir}/")
    print(f"   • Updated genealogy: {genealogy_path if genealogy_path.exists() else 'N/A'}")


if __name__ == "__main__":
    main()
