#!/usr/bin/env python3
"""
Analyze My True Ancestry (MTA) matches for VK155 and VK157
"""
import sys
import json
from pathlib import Path
from datetime import datetime

# Add src to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root / "src"))

from ancient_dna.mta_parser import MTAParser
from ancient_dna.mta_analyzer import MTAAnalyzer
from visualization.mta_visualizer import MTAVisualizer


def main():
    """Main analysis function"""
    print("=" * 80)
    print("MTA MATCHES ANALYSIS - VK155 & VK157")
    print("=" * 80)
    
    # File paths
    vk155_path = project_root / "data/raw/autosomal/MTA/VK155/matchesMTA.md"
    vk157_path = project_root / "data/raw/autosomal/MTA/VK157/matchesMTA.md"
    
    # Output directories
    output_data_dir = project_root / "data/processed/ancient_dna"
    output_data_dir.mkdir(parents=True, exist_ok=True)
    
    # Step 1: Parse files
    print("\n📖 Step 1: Parsing MTA files...")
    parser = MTAParser()
    
    try:
        vk155_data = parser.parse_file(str(vk155_path))
        print(f"   ✓ VK155: {len(vk155_data['top_matches'])} top matches, "
              f"{len(vk155_data['deep_dive_results'])} deep dive results")
    except Exception as e:
        print(f"   ✗ Error parsing VK155: {e}")
        print("   Note: File may be unsaved in editor. Please save the file and try again.")
        return
    
    try:
        vk157_data = parser.parse_file(str(vk157_path))
        print(f"   ✓ VK157: {len(vk157_data['top_matches'])} top matches, "
              f"{len(vk157_data['deep_dive_results'])} deep dive results")
    except Exception as e:
        print(f"   ✗ Error parsing VK157: {e}")
        print("   Note: File may be unsaved in editor. Please save the file and try again.")
        return
    
    # Save parsed data
    print("\n💾 Step 2: Saving parsed data...")
    with open(output_data_dir / "mta_vk155_matches.json", 'w') as f:
        json.dump(vk155_data, f, indent=2, default=str)
    with open(output_data_dir / "mta_vk157_matches.json", 'w') as f:
        json.dump(vk157_data, f, indent=2, default=str)
    print(f"   ✓ Saved parsed data to {output_data_dir}")
    
    # Step 3: Analyze data
    print("\n📊 Step 3: Analyzing match data...")
    analyzer = MTAAnalyzer()
    
    vk155_analysis = analyzer.analyze_sample(vk155_data)
    vk157_analysis = analyzer.analyze_sample(vk157_data)
    comparison = analyzer.compare_samples(vk155_data, vk157_data)
    patterns = analyzer.identify_patterns(vk155_analysis, vk157_analysis)
    
    print(f"   ✓ VK155 analysis complete")
    print(f"   ✓ VK157 analysis complete")
    print(f"   ✓ Comparison complete: {comparison['common_matches_count']} common matches")
    
    # Save analysis results
    comparison_data = {
        'vk155_analysis': vk155_analysis,
        'vk157_analysis': vk157_analysis,
        'comparison': comparison,
        'patterns': patterns,
        'analysis_date': datetime.now().isoformat()
    }
    
    with open(output_data_dir / "mta_comparison.json", 'w') as f:
        json.dump(comparison_data, f, indent=2, default=str)
    print(f"   ✓ Saved analysis results to {output_data_dir / 'mta_comparison.json'}")
    
    # Step 4: Generate visualizations
    print("\n🎨 Step 4: Generating visualizations...")
    visualizer = MTAVisualizer()
    
    # Extract data for visualizations
    vk155_distances = [m['genetic_distance'] for m in vk155_data['top_matches']]
    vk157_distances = [m['genetic_distance'] for m in vk157_data['top_matches']]
    
    vk155_years = [m['date']['year'] for m in vk155_data['top_matches'] 
                   if m['date'].get('year') is not None]
    vk157_years = [m['date']['year'] for m in vk157_data['top_matches'] 
                   if m['date'].get('year') is not None]
    
    visualization_files = []
    
    try:
        # Genetic distance distribution
        viz_file = visualizer.plot_genetic_distance_distribution(
            vk155_distances, vk157_distances
        )
        visualization_files.append(viz_file)
        print(f"   ✓ Created: {Path(viz_file).name}")
        
        # Era distribution
        viz_file = visualizer.plot_era_distribution(
            vk155_analysis.get('era_distribution', {}),
            vk157_analysis.get('era_distribution', {})
        )
        visualization_files.append(viz_file)
        print(f"   ✓ Created: {Path(viz_file).name}")
        
        # Region distribution
        viz_file = visualizer.plot_region_distribution(
            vk155_analysis.get('region_distribution', {}),
            vk157_analysis.get('region_distribution', {})
        )
        visualization_files.append(viz_file)
        print(f"   ✓ Created: {Path(viz_file).name}")
        
        # Time period distribution
        if vk155_years and vk157_years:
            viz_file = visualizer.plot_time_period_distribution(vk155_years, vk157_years)
            visualization_files.append(viz_file)
            print(f"   ✓ Created: {Path(viz_file).name}")
        
        # Comparison scatter
        if comparison.get('common_matches'):
            viz_file = visualizer.plot_comparison_scatter(comparison['common_matches'])
            if viz_file:
                visualization_files.append(viz_file)
                print(f"   ✓ Created: {Path(viz_file).name}")
        
        # Top matches comparison
        viz_file = visualizer.plot_top_matches_comparison(
            vk155_analysis.get('top_10_matches', []),
            vk157_analysis.get('top_10_matches', [])
        )
        visualization_files.append(viz_file)
        print(f"   ✓ Created: {Path(viz_file).name}")
        
    except Exception as e:
        print(f"   ⚠ Warning: Error generating visualizations: {e}")
    
    # Step 5: Integrate with genealogy data
    print("\n🔗 Step 5: Integrating with genealogy data...")
    try:
        integrate_with_genealogy(
            vk155_analysis, vk157_analysis, comparison,
            project_root / "data/processed/genealogy/bodzia_complete_tree.json",
            vk155_data=vk155_data,
            vk157_data=vk157_data
        )
        print("   ✓ Integrated MTA data (including SNP matching) into genealogy tree")
    except Exception as e:
        print(f"   ⚠ Warning: Error integrating with genealogy: {e}")
    
    # Step 6: Update documentation
    print("\n📚 Step 6: Updating documentation...")
    try:
        update_documentation(
            vk155_analysis, vk157_analysis, comparison,
            project_root / "docs/BODZIA_COMPLETE_TREE_DOCUMENTATION.md"
        )
        print("   ✓ Updated BODZIA_COMPLETE_TREE_DOCUMENTATION.md")
    except Exception as e:
        print(f"   ⚠ Warning: Error updating documentation: {e}")
    
    # Step 7: Generate report
    print("\n📝 Step 7: Generating analysis report...")
    report_path = generate_report(
        vk155_analysis, vk157_analysis, comparison, patterns, visualization_files
    )
    print(f"   ✓ Report generated: {report_path}")
    
    # Summary
    print("\n" + "=" * 80)
    print("✅ ANALYSIS COMPLETE!")
    print("=" * 80)
    print(f"\n📊 Summary:")
    print(f"   • VK155 top matches: {len(vk155_data['top_matches'])}")
    print(f"   • VK157 top matches: {len(vk157_data['top_matches'])}")
    print(f"   • Common matches: {comparison['common_matches_count']}")
    print(f"   • Visualizations: {len(visualization_files)}")
    print(f"\n📁 Output files:")
    print(f"   • Data: {output_data_dir}/")
    print(f"   • Visualizations: {visualizer.output_dir}/")
    print(f"   • Report: {report_path}")


def integrate_with_genealogy(
    vk155_analysis: Dict,
    vk157_analysis: Dict,
    comparison: Dict,
    genealogy_path: Path,
    vk155_data: Dict = None,
    vk157_data: Dict = None
):
    """Integrate MTA findings into genealogy JSON file"""
    # Load genealogy data
    with open(genealogy_path, 'r', encoding='utf-8') as f:
        genealogy_data = json.load(f)
    
    # Find VK155 (BOD002 - The Witch) and VK157 (RUR001 - Sviatopolk I)
    individuals = genealogy_data.get('individuals', [])
    
    for ind in individuals:
        # VK157 - Sviatopolk I (RUR001)
        if ind.get('id') == 'RUR001':
            notes_str = ' '.join(ind.get('notes', []))
            if 'VK157' in notes_str:
                # Get Deep Dive Results (SNP matching data) for VK157
                deep_dive_vk157 = []
                if vk157_data:
                    deep_dive_vk157 = vk157_data.get('deep_dive_results', [])
                    # Find VK155 match specifically (they match each other)
                    vk155_match = next((d for d in deep_dive_vk157 if d.get('sample_id') == 'VK155'), None)
                
                mta_data = {
                    'sample_id': 'VK157',
                    'total_matches': vk157_analysis.get('total_top_matches', 0),
                    'genetic_distance_stats': vk157_analysis.get('genetic_distance_stats', {}),
                    'top_5_matches': [
                        {
                            'sample_id': m.get('sample_id'),
                            'description': m.get('description'),
                            'genetic_distance': m.get('genetic_distance'),
                            'date': m.get('date', {}).get('raw')
                        }
                        for m in vk157_analysis.get('top_10_matches', [])[:5]
                    ],
                    'dominant_eras': vk157_analysis.get('era_distribution', {}),
                    'dominant_regions': dict(list(vk157_analysis.get('region_distribution', {}).items())[:5]),
                    'bodzia_connections': comparison.get('bodzia_connections', {}).get('vk157', {})
                }
                
                # Add SNP matching data from Deep Dive Results
                if vk155_match:
                    mta_data['snp_matching'] = {
                        'vk155_match': {
                            'sample_id': vk155_match.get('sample_id'),
                            'num_snp_chains': vk155_match.get('num_snp_chains'),
                            'total_cm': vk155_match.get('total_cm'),
                            'largest_chain_snps': vk155_match.get('largest_chain_snps'),
                            'largest_chain_cm': vk155_match.get('largest_chain_cm'),
                            'chromosomes': vk155_match.get('chromosomes', []),
                            'sample_quality': vk155_match.get('sample_quality')
                        }
                    }
                
                # Add summary of all Deep Dive matches
                if deep_dive_vk157:
                    mta_data['deep_dive_summary'] = {
                        'total_matches_with_shared_dna': len(deep_dive_vk157),
                        'total_cm_shared': sum(d.get('total_cm', 0) for d in deep_dive_vk157),
                        'avg_cm_per_match': sum(d.get('total_cm', 0) for d in deep_dive_vk157) / len(deep_dive_vk157) if deep_dive_vk157 else 0,
                        'top_10_by_cm': sorted(
                            [
                                {
                                    'sample_id': d.get('sample_id'),
                                    'sample_name': d.get('sample_name'),
                                    'total_cm': d.get('total_cm'),
                                    'num_snp_chains': d.get('num_snp_chains'),
                                    'largest_chain_snps': d.get('largest_chain_snps')
                                }
                                for d in deep_dive_vk157
                            ],
                            key=lambda x: x.get('total_cm', 0),
                            reverse=True
                        )[:10]
                    }
                
                ind['mta_analysis'] = mta_data
        
        # VK155 - The Witch (BOD002)
        if ind.get('id') == 'BOD002':
            notes_str = ' '.join(ind.get('notes', []))
            if 'VK155' in notes_str:
                # Get Deep Dive Results (SNP matching data) for VK155
                deep_dive_vk155 = []
                if vk155_data:
                    deep_dive_vk155 = vk155_data.get('deep_dive_results', [])
                    # Find VK157 match specifically (they match each other)
                    vk157_match = next((d for d in deep_dive_vk155 if d.get('sample_id') == 'VK157'), None)
                
                mta_data = {
                    'sample_id': 'VK155',
                    'total_matches': vk155_analysis.get('total_top_matches', 0),
                    'genetic_distance_stats': vk155_analysis.get('genetic_distance_stats', {}),
                    'top_5_matches': [
                        {
                            'sample_id': m.get('sample_id'),
                            'description': m.get('description'),
                            'genetic_distance': m.get('genetic_distance'),
                            'date': m.get('date', {}).get('raw')
                        }
                        for m in vk155_analysis.get('top_10_matches', [])[:5]
                    ],
                    'dominant_eras': vk155_analysis.get('era_distribution', {}),
                    'dominant_regions': dict(list(vk155_analysis.get('region_distribution', {}).items())[:5]),
                    'bodzia_connections': comparison.get('bodzia_connections', {}).get('vk155', {})
                }
                
                # Add SNP matching data from Deep Dive Results
                if vk157_match:
                    mta_data['snp_matching'] = {
                        'vk157_match': {
                            'sample_id': vk157_match.get('sample_id'),
                            'num_snp_chains': vk157_match.get('num_snp_chains'),
                            'total_cm': vk157_match.get('total_cm'),
                            'largest_chain_snps': vk157_match.get('largest_chain_snps'),
                            'largest_chain_cm': vk157_match.get('largest_chain_cm'),
                            'chromosomes': vk157_match.get('chromosomes', []),
                            'sample_quality': vk157_match.get('sample_quality')
                        }
                    }
                
                # Add summary of all Deep Dive matches
                if deep_dive_vk155:
                    mta_data['deep_dive_summary'] = {
                        'total_matches_with_shared_dna': len(deep_dive_vk155),
                        'total_cm_shared': sum(d.get('total_cm', 0) for d in deep_dive_vk155),
                        'avg_cm_per_match': sum(d.get('total_cm', 0) for d in deep_dive_vk155) / len(deep_dive_vk155) if deep_dive_vk155 else 0,
                        'top_10_by_cm': sorted(
                            [
                                {
                                    'sample_id': d.get('sample_id'),
                                    'sample_name': d.get('sample_name'),
                                    'total_cm': d.get('total_cm'),
                                    'num_snp_chains': d.get('num_snp_chains'),
                                    'largest_chain_snps': d.get('largest_chain_snps')
                                }
                                for d in deep_dive_vk155
                            ],
                            key=lambda x: x.get('total_cm', 0),
                            reverse=True
                        )[:10]
                    }
                
                ind['mta_analysis'] = mta_data
    
    # Save updated genealogy data
    with open(genealogy_path, 'w', encoding='utf-8') as f:
        json.dump(genealogy_data, f, indent=2, ensure_ascii=False, default=str)


def update_documentation(
    vk155_analysis: Dict,
    vk157_analysis: Dict,
    comparison: Dict,
    doc_path: Path
):
    """Update BODZIA_COMPLETE_TREE_DOCUMENTATION.md with MTA analysis section"""
    with open(doc_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the References section and add MTA section before it
    mta_section = f"""
---

## My True Ancestry (MTA) Match Analysis

**Analysis Date:** {datetime.now().strftime('%Y-%m-%d')}

### Overview

Comprehensive analysis of My True Ancestry genetic matches for Bodzia DNA samples:
- **VK155** (The Witch from Bodzia, BOD002): {vk155_analysis.get('total_top_matches', 0)} top matches
- **VK157** (Sviatopolk I, RUR001): {vk157_analysis.get('total_top_matches', 0)} top matches
- **Common Matches**: {comparison.get('common_matches_count', 0)} samples appear in both datasets

### Key Findings

#### VK155 (Elite Woman)
- **Average Genetic Distance**: {vk155_analysis.get('genetic_distance_stats', {}).get('mean', 'N/A'):.3f if vk155_analysis.get('genetic_distance_stats', {}).get('mean') else 'N/A'}
- **Strongest Match**: {vk155_analysis.get('top_10_matches', [{}])[0].get('description', 'N/A') if vk155_analysis.get('top_10_matches') else 'N/A'} (Distance: {vk155_analysis.get('top_10_matches', [{}])[0].get('genetic_distance', 'N/A'):.3f if vk155_analysis.get('top_10_matches') else 'N/A'})
- **Dominant Eras**: {', '.join([era for era, _ in list(vk155_analysis.get('era_distribution', {}).items())[:3]]) if vk155_analysis.get('era_distribution') else 'N/A'}
- **Top Regions**: {', '.join([region for region, _ in list(vk155_analysis.get('region_distribution', {}).items())[:3]]) if vk155_analysis.get('region_distribution') else 'N/A'}

#### VK157 (Elite Warrior - Sviatopolk I)
- **Average Genetic Distance**: {vk157_analysis.get('genetic_distance_stats', {}).get('mean', 'N/A'):.3f if vk157_analysis.get('genetic_distance_stats', {}).get('mean') else 'N/A'}
- **Strongest Match**: {vk157_analysis.get('top_10_matches', [{}])[0].get('description', 'N/A') if vk157_analysis.get('top_10_matches') else 'N/A'} (Distance: {vk157_analysis.get('top_10_matches', [{}])[0].get('genetic_distance', 'N/A'):.3f if vk157_analysis.get('top_10_matches') else 'N/A'})
- **Dominant Eras**: {', '.join([era for era, _ in list(vk157_analysis.get('era_distribution', {}).items())[:3]]) if vk157_analysis.get('era_distribution') else 'N/A'}
- **Top Regions**: {', '.join([region for region, _ in list(vk157_analysis.get('region_distribution', {}).items())[:3]]) if vk157_analysis.get('region_distribution') else 'N/A'}

### Bodzia Site Connections

Both samples show genetic connections to other Bodzia burials:
"""
    
    # Add Bodzia connections
    bodzia_conn = comparison.get('bodzia_connections', {})
    if bodzia_conn.get('vk155'):
        mta_section += "\n**VK155 matches to other Bodzia samples:**\n"
        for sample_id, data in bodzia_conn['vk155'].items():
            mta_section += f"- {sample_id}: Genetic Distance {data.get('distance', 'N/A'):.3f}, Rank {data.get('rank', 'N/A')}\n"
    
    if bodzia_conn.get('vk157'):
        mta_section += "\n**VK157 matches to other Bodzia samples:**\n"
        for sample_id, data in bodzia_conn['vk157'].items():
            mta_section += f"- {sample_id}: Genetic Distance {data.get('distance', 'N/A'):.3f}, Rank {data.get('rank', 'N/A')}\n"
    
    mta_section += f"""
### Detailed Analysis

For comprehensive analysis including:
- Complete match lists and statistics
- Geographic and temporal distribution patterns
- Comparison visualizations
- Deep Dive Results (shared DNA segments)

See: **[MTA Matches Analysis](MTA_MATCHES_ANALYSIS.md)**

### Data Files

- **VK155 Parsed Data**: `data/processed/ancient_dna/mta_vk155_matches.json`
- **VK157 Parsed Data**: `data/processed/ancient_dna/mta_vk157_matches.json`
- **Comparison Data**: `data/processed/ancient_dna/mta_comparison.json`
- **Visualizations**: `output/visualizations/mta/`

"""
    
    # Insert before References section
    if "## References" in content:
        content = content.replace("## References", mta_section + "\n## References")
    else:
        # Append at end if no References section
        content += mta_section
    
    with open(doc_path, 'w', encoding='utf-8') as f:
        f.write(content)


def generate_report(
    vk155_analysis: Dict,
    vk157_analysis: Dict,
    comparison: Dict,
    patterns: Dict,
    visualization_files: List[str]
) -> str:
    """Generate comprehensive markdown report"""
    report_path = project_root / "docs/MTA_MATCHES_ANALYSIS.md"
    
    report_content = f"""# My True Ancestry (MTA) Matches Analysis

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Samples Analyzed:** VK155 (Viking Age Elite Woman Bodzia Poland) & VK157 (Viking Age Elite Warrior Bodzia Poland)

---

## Executive Summary

This analysis examines genetic matches from My True Ancestry for two Bodzia archaeological samples:
- **VK155**: Elite Woman from Bodzia (1020 AD, mtDNA H1c)
- **VK157**: Elite Warrior from Bodzia (1015 AD, Y-DNA I1-S2077, possibly Sviatopolk I)

### Key Findings

- **VK155**: {vk155_analysis.get('total_top_matches', 0)} top matches identified
- **VK157**: {vk157_analysis.get('total_top_matches', 0)} top matches identified
- **Common Matches**: {comparison.get('common_matches_count', 0)} samples appear in both datasets
- **VK155 Unique**: {comparison.get('vk155_unique_count', 0)} samples only in VK155
- **VK157 Unique**: {comparison.get('vk157_unique_count', 0)} samples only in VK157

---

## VK155 Analysis

### Genetic Distance Statistics

"""
    
    vk155_stats = vk155_analysis.get('genetic_distance_stats', {})
    if vk155_stats:
        report_content += f"""
- **Minimum**: {vk155_stats.get('min', 'N/A'):.3f}
- **Maximum**: {vk155_stats.get('max', 'N/A'):.3f}
- **Mean**: {vk155_stats.get('mean', 'N/A'):.3f}
- **Median**: {vk155_stats.get('median', 'N/A'):.3f}
- **Standard Deviation**: {vk155_stats.get('stdev', 'N/A'):.3f if vk155_stats.get('stdev') else 'N/A'}

"""
    
    # Top matches
    report_content += "### Top 10 Matches\n\n"
    top_matches = vk155_analysis.get('top_10_matches', [])
    for i, match in enumerate(top_matches[:10], 1):
        date_str = match.get('date', {}).get('raw', 'Unknown')
        report_content += f"{i}. **{match.get('description', 'Unknown')}** ({date_str})  \n"
        report_content += f"   - Sample ID: {match.get('sample_id', 'N/A')}  \n"
        report_content += f"   - Genetic Distance: {match.get('genetic_distance', 'N/A'):.3f}  \n"
        if match.get('era'):
            report_content += f"   - Era: {match.get('era')}  \n"
        if match.get('regions'):
            report_content += f"   - Regions: {', '.join(match.get('regions', []))}  \n"
        report_content += "\n"
    
    # Era distribution
    report_content += "### Era Distribution\n\n"
    era_dist = vk155_analysis.get('era_distribution', {})
    if era_dist:
        for era, count in sorted(era_dist.items(), key=lambda x: x[1], reverse=True):
            report_content += f"- **{era}**: {count} matches\n"
    report_content += "\n"
    
    # Region distribution
    report_content += "### Geographic Region Distribution\n\n"
    region_dist = vk155_analysis.get('region_distribution', {})
    if region_dist:
        for region, count in sorted(region_dist.items(), key=lambda x: x[1], reverse=True)[:10]:
            report_content += f"- **{region}**: {count} matches\n"
    report_content += "\n"
    
    # Deep Dive stats
    deep_dive = vk155_analysis.get('deep_dive_stats', {})
    if deep_dive:
        report_content += "### Deep Dive Results (Shared DNA Segments)\n\n"
        report_content += f"- **Total Matches with Shared DNA**: {deep_dive.get('total_matches', 0)}\n"
        report_content += f"- **Total cM Shared**: {deep_dive.get('total_cm', 0):.2f} cM\n"
        report_content += f"- **Average cM per Match**: {deep_dive.get('avg_cm_per_match', 0):.2f} cM\n"
        report_content += f"- **Largest Match**: {deep_dive.get('largest_match_cm', 0):.2f} cM\n"
        report_content += "\n"
    
    # VK157 section
    report_content += "---\n\n## VK157 Analysis\n\n### Genetic Distance Statistics\n\n"
    
    vk157_stats = vk157_analysis.get('genetic_distance_stats', {})
    if vk157_stats:
        report_content += f"""
- **Minimum**: {vk157_stats.get('min', 'N/A'):.3f}
- **Maximum**: {vk157_stats.get('max', 'N/A'):.3f}
- **Mean**: {vk157_stats.get('mean', 'N/A'):.3f}
- **Median**: {vk157_stats.get('median', 'N/A'):.3f}
- **Standard Deviation**: {vk157_stats.get('stdev', 'N/A'):.3f if vk157_stats.get('stdev') else 'N/A'}

"""
    
    # Top matches VK157
    report_content += "### Top 10 Matches\n\n"
    top_matches_157 = vk157_analysis.get('top_10_matches', [])
    for i, match in enumerate(top_matches_157[:10], 1):
        date_str = match.get('date', {}).get('raw', 'Unknown')
        report_content += f"{i}. **{match.get('description', 'Unknown')}** ({date_str})  \n"
        report_content += f"   - Sample ID: {match.get('sample_id', 'N/A')}  \n"
        report_content += f"   - Genetic Distance: {match.get('genetic_distance', 'N/A'):.3f}  \n"
        if match.get('era'):
            report_content += f"   - Era: {match.get('era')}  \n"
        if match.get('regions'):
            report_content += f"   - Regions: {', '.join(match.get('regions', []))}  \n"
        report_content += "\n"
    
    # Comparison section
    report_content += "---\n\n## VK155 vs VK157 Comparison\n\n"
    report_content += f"### Common Matches\n\n"
    report_content += f"Both samples share **{comparison.get('common_matches_count', 0)}** common matches.\n\n"
    
    if comparison.get('common_matches'):
        report_content += "#### Top 20 Common Matches\n\n"
        report_content += "| Rank | Sample ID | Description | VK155 Distance | VK157 Distance | Difference |\n"
        report_content += "|------|-----------|-------------|----------------|----------------|------------|\n"
        for i, match in enumerate(comparison['common_matches'][:20], 1):
            report_content += f"| {i} | {match.get('sample_id', 'N/A')} | {match.get('description', '')[:40]}... | "
            report_content += f"{match.get('vk155_distance', 0):.3f} | {match.get('vk157_distance', 0):.3f} | "
            report_content += f"{match.get('distance_diff', 0):.3f} |\n"
        report_content += "\n"
    
    # Bodzia connections
    report_content += "### Bodzia Site Connections\n\n"
    bodzia_conn = comparison.get('bodzia_connections', {})
    if bodzia_conn:
        report_content += "#### VK155 Matches to Other Bodzia Samples\n\n"
        for sample_id, data in bodzia_conn.get('vk155', {}).items():
            report_content += f"- **{sample_id}**: Distance {data.get('distance', 'N/A'):.3f}, Rank {data.get('rank', 'N/A')}\n"
        report_content += "\n"
        
        report_content += "#### VK157 Matches to Other Bodzia Samples\n\n"
        for sample_id, data in bodzia_conn.get('vk157', {}).items():
            report_content += f"- **{sample_id}**: Distance {data.get('distance', 'N/A'):.3f}, Rank {data.get('rank', 'N/A')}\n"
        report_content += "\n"
    
    # Patterns
    report_content += "---\n\n## Identified Patterns\n\n"
    patterns_data = patterns
    
    report_content += "### Dominant Eras\n\n"
    dom_eras = patterns_data.get('dominant_eras', {})
    if dom_eras.get('vk155'):
        report_content += "**VK155**:\n"
        for era, count in dom_eras['vk155']:
            report_content += f"- {era}: {count} matches\n"
        report_content += "\n"
    if dom_eras.get('vk157'):
        report_content += "**VK157**:\n"
        for era, count in dom_eras['vk157']:
            report_content += f"- {era}: {count} matches\n"
        report_content += "\n"
    
    # Visualizations
    report_content += "---\n\n## Visualizations\n\n"
    for viz_file in visualization_files:
        viz_name = Path(viz_file).name
        report_content += f"![{viz_name}](../{viz_file})\n\n"
    
    # Data files
    report_content += "---\n\n## Data Files\n\n"
    report_content += "- **VK155 Parsed Data**: `data/processed/ancient_dna/mta_vk155_matches.json`\n"
    report_content += "- **VK157 Parsed Data**: `data/processed/ancient_dna/mta_vk157_matches.json`\n"
    report_content += "- **Comparison Data**: `data/processed/ancient_dna/mta_comparison.json`\n"
    
    # Write report
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report_content)
    
    return str(report_path)


if __name__ == "__main__":
    main()
