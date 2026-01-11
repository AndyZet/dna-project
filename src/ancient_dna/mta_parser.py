"""
Parser for My True Ancestry (MTA) match data from markdown files
"""
import re
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime


class MTAParser:
    """Parse MTA markdown files to extract match data"""
    
    def __init__(self):
        """Initialize parser"""
        self.era_patterns = {
            'Mesolithic': r'Mesolithic',
            'Neolithic': r'Neolithic',
            'Copper Age': r'Copper Age',
            'Bronze Age': r'Bronze Age|CWC|Corded Ware|Bell Beaker|Unetice',
            'Iron Age': r'Iron Age|Hallstatt|La Tène|Scythian',
            'Roman': r'Roman|Gallo Roman',
            'Migration Period': r'Migration Period|Vendel Age|Gothic|Visigoth|Ostrogoth',
            'Viking Age': r'Viking Age|Viking|Viking Era|Pre-Viking',
            'Medieval': r'Medieval|Early Medieval|Late Medieval|Post Viking',
            'Post-Medieval': r'Post-Medieval|Early Modern|Late Medieval'
        }
        
        self.region_patterns = {
            'Poland': r'Poland|Polish|Pommerania|Silesia|Masovia|Wielkopolska',
            'Sweden': r'Sweden|Swedish|Gotland|Sigtuna|Stockholm|Oland|Uppland',
            'Denmark': r'Denmark|Danish|Jutland|Zealand|Funen|Sealand',
            'Norway': r'Norway|Norwegian|Trondelag',
            'Ukraine': r'Ukraine|Ukrainian|Kiev|Kievan|Rus\'|Staraya Ladoga|Gnezdovo',
            'Czech': r'Czech|Bohemia|Moravia|Prague|Pohansko',
            'Germany': r'Germany|German|Bavaria|Saxony|Thuringia|Lower Saxony',
            'Hungary': r'Hungary|Hungarian|Arpad|Carolingian',
            'Russia': r'Russia|Russian|Novgorod|Gorokhovets|Shekshovo',
            'England': r'England|English|Britain|Yorkshire|Oxford|Sussex',
            'Ireland': r'Ireland|Irish',
            'France': r'France|French',
            'Serbia': r'Serbia|Serbian|Viminacium',
            'Slovakia': r'Slovakia|Slovak',
            'Baltic': r'Baltic|Latvia|Lithuania|Estonia|Saaremaa'
        }
    
    def parse_file(self, file_path: str) -> Dict[str, Any]:
        """
        Parse MTA markdown file and extract all match data.
        
        Args:
            file_path: Path to MTA markdown file
            
        Returns:
            Dictionary with parsed data including top matches and Deep Dive results
        """
        file_path = Path(file_path)
        if not file_path.exists():
            raise FileNotFoundError(f"MTA file not found: {file_path}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract kit information
        kit_info = self._extract_kit_info(content)
        
        # Parse top matches
        top_matches = self._parse_top_matches(content)
        
        # Parse Deep Dive Results (shared DNA segments)
        deep_dive_results = self._parse_deep_dive_results(content)
        
        return {
            'kit_info': kit_info,
            'top_matches': top_matches,
            'deep_dive_results': deep_dive_results,
            'total_top_matches': len(top_matches),
            'total_deep_dive_matches': len(deep_dive_results),
            'parsed_date': datetime.now().isoformat()
        }
    
    def _extract_kit_info(self, content: str) -> Dict[str, Any]:
        """Extract kit information from file"""
        kit_match = re.search(r'Kit:\s*(.+?)(?:\n|$)', content)
        kit_name = kit_match.group(1).strip() if kit_match else "Unknown"
        
        # Extract sample ID (e.g., VK155, VK157)
        sample_id_match = re.search(r'\(([A-Z0-9]+)\)', kit_name)
        sample_id = sample_id_match.group(1) if sample_id_match else None
        
        return {
            'kit_name': kit_name,
            'sample_id': sample_id
        }
    
    def _parse_top_matches(self, content: str) -> List[Dict[str, Any]]:
        """
        Parse top matching samples section.
        Format:
        1. Description
        Date AD - Genetic Distance: X.XXX - SampleID
        Top X % match vs all users
        """
        matches = []
        
        # Split content into lines and find numbered entries
        lines = content.split('\n')
        i = 0
        
        while i < len(lines):
            line = lines[i].strip()
            
            # Look for numbered entry: "1. Description"
            match = re.match(r'^(\d+)\.\s+(.+)$', line)
            if match:
                rank = int(match.group(1))
                description = match.group(2).strip()
                
                # Look ahead for date/genetic distance line
                if i + 1 < len(lines):
                    next_line = lines[i + 1].strip()
                    
                    # Pattern: "950 AD - Genetic Distance: 2.768 - PCA148_Niemcza34    ?"
                    dist_match = re.search(
                        r'([0-9]+(?:\s+BC)?)\s+AD?\s*-\s*Genetic Distance:\s*([\d.]+)\s*-\s*([A-Z0-9_\.\?]+(?:\s+\?)?)',
                        next_line
                    )
                    
                    if dist_match:
                        date_str = dist_match.group(1).strip()
                        genetic_distance = float(dist_match.group(2))
                        sample_id = dist_match.group(3).strip().rstrip('?').strip()
                        
                        # Look for percentile on next line
                        percentile = None
                        if i + 2 < len(lines):
                            percentile_line = lines[i + 2].strip()
                            perc_match = re.search(r'Top\s+(\d+)\s*%\s*match', percentile_line)
                            if perc_match:
                                percentile = int(perc_match.group(1))
                        
                        # Parse date
                        date_info = self._parse_date(date_str)
                        
                        # Extract era and region
                        era = self._categorize_era(description)
                        regions = self._extract_regions(description)
                        
                        matches.append({
                            'rank': rank,
                            'description': description,
                            'date': date_info,
                            'genetic_distance': genetic_distance,
                            'sample_id': sample_id,
                            'percentile': percentile,
                            'era': era,
                            'regions': regions
                        })
            
            i += 1
        
        return matches
    
    def _parse_deep_dive_results(self, content: str) -> List[Dict[str, Any]]:
        """
        Parse Deep Dive Results section with shared DNA segments.
        Format includes sample name, haplogroups, shared DNA info, and chromosome data.
        """
        results = []
        
        # Find Deep Dive section (starts after "Deep Dive Results" or "Ancient Relatives")
        deep_dive_start = re.search(r'Deep Dive|Ancient Relatives', content, re.IGNORECASE)
        if not deep_dive_start:
            return results
        
        deep_dive_content = content[deep_dive_start.start():]
        
        # Pattern to match sample entries in Deep Dive section
        # Format variations:
        # "Sample Name Date AD\n  SampleID\n\nmtDNA: ...\nShared DNA: ..."
        # "Sample Name Date AD\n  SampleID\n\nShared DNA: ..." (no haplogroups)
        # Try to match with haplogroups first, then without
        sample_pattern_with_haplo = r'([A-Za-z0-9\s\-\'\.]+?)\s+([0-9]+(?:\s+BC)?)\s+AD?\s*\n\s*([A-Z0-9_]+[A-Z0-9_\.\?]*)\s*\n\s*(?:mtDNA:\s*([A-Z0-9\?]+))?\s*(?:Y-DNA:\s*([A-Z0-9\-\?]+))?\s*\n\s*Shared DNA:\s*\(Sample Quality:\s*(\d+)\)\s*\n\s*(\d+)\s+SNP chain[s]?\s*\(min\.\s*\d+\s+SNPs\)\s*/\s*([\d.]+)\s+cM\s*\n\s*Largest chain:\s*(\d+)\s+SNPs\s*/\s*([\d.]+)\s+cM'
        sample_pattern_no_haplo = r'([A-Za-z0-9\s\-\'\.]+?)\s+([0-9]+(?:\s+BC)?)\s+AD?\s*\n\s*([A-Z0-9_]+[A-Z0-9_\.\?]*)\s*\n\s*Shared DNA:\s*\(Sample Quality:\s*(\d+)\)\s*\n\s*(\d+)\s+SNP chain[s]?\s*\(min\.\s*\d+\s+SNPs\)\s*/\s*([\d.]+)\s+cM\s*\n\s*Largest chain:\s*(\d+)\s+SNPs\s*/\s*([\d.]+)\s+cM'
        
        # Try pattern with haplogroups first
        for match in re.finditer(sample_pattern_with_haplo, deep_dive_content, re.MULTILINE):
            sample_name = match.group(1).strip()
            date_str = match.group(2).strip()
            sample_id = match.group(3).strip()
            mtDNA = match.group(4) if match.group(4) else None
            yDNA = match.group(5) if match.group(5) else None
            sample_quality = int(match.group(6))
            num_chains = int(match.group(7))
            total_cm = float(match.group(8))
            largest_chain_snps = int(match.group(9))
            largest_chain_cm = float(match.group(10))
            
            # Parse date
            date_info = self._parse_date(date_str)
            
            # Extract chromosome data (look for "Chr. X" followed by SNP count)
            chromosome_data = self._extract_chromosome_data(deep_dive_content, sample_id)
            
            # Extract era and regions
            era = self._categorize_era(sample_name)
            regions = self._extract_regions(sample_name)
            
            # Find percentile if available (look for "X % closer than other matching users")
            percentile_match = re.search(
                rf'{re.escape(sample_id)}.*?(\d+)\s*%\s*closer than other matching users',
                deep_dive_content,
                re.DOTALL
            )
            percentile = int(percentile_match.group(1)) if percentile_match else None
            
            results.append({
                'sample_name': sample_name,
                'sample_id': sample_id,
                'date': date_info,
                'mtDNA': mtDNA,
                'yDNA': yDNA,
                'sample_quality': sample_quality,
                'num_snp_chains': num_chains,
                'total_cm': total_cm,
                'largest_chain_snps': largest_chain_snps,
                'largest_chain_cm': largest_chain_cm,
                'chromosomes': chromosome_data,
                'percentile': percentile,
                'era': era,
                'regions': regions
            })
        
        # Also try pattern without haplogroups (to catch entries that might have been missed)
        for match in re.finditer(sample_pattern_no_haplo, deep_dive_content, re.MULTILINE):
            sample_name = match.group(1).strip()
            date_str = match.group(2).strip()
            sample_id = match.group(3).strip()
            sample_quality = int(match.group(4))
            num_chains = int(match.group(5))
            total_cm = float(match.group(6))
            largest_chain_snps = int(match.group(7))
            largest_chain_cm = float(match.group(8))
            
            # Skip if already added
            if any(r.get('sample_id') == sample_id for r in results):
                continue
            
            # Parse date
            date_info = self._parse_date(date_str)
            
            # Extract chromosome data
            chromosome_data = self._extract_chromosome_data(deep_dive_content, sample_id)
            
            # Extract era and regions
            era = self._categorize_era(sample_name)
            regions = self._extract_regions(sample_name)
            
            # Find percentile
            percentile_match = re.search(
                rf'{re.escape(sample_id)}.*?(\d+)\s*%\s*closer than other matching users',
                deep_dive_content,
                re.DOTALL
            )
            percentile = int(percentile_match.group(1)) if percentile_match else None
            
            results.append({
                'sample_name': sample_name,
                'sample_id': sample_id,
                'date': date_info,
                'mtDNA': None,
                'yDNA': None,
                'sample_quality': sample_quality,
                'num_snp_chains': num_chains,
                'total_cm': total_cm,
                'largest_chain_snps': largest_chain_snps,
                'largest_chain_cm': largest_chain_cm,
                'chromosomes': chromosome_data,
                'percentile': percentile,
                'era': era,
                'regions': regions
            })
        
        return results
    
    def _extract_chromosome_data(self, content: str, sample_id: str) -> List[Dict[str, Any]]:
        """Extract chromosome-specific SNP data for a sample"""
        chromosomes = []
        
        # Find the section for this sample
        sample_section = re.search(
            rf'{re.escape(sample_id)}.*?(?=\n\n[A-Z]|\n\n\d+\.|$)',
            content,
            re.DOTALL
        )
        
        if not sample_section:
            return chromosomes
        
        section_content = sample_section.group(0)
        
        # Pattern: "Chr. X\n\nSNP_count SNPs"
        chr_pattern = r'Chr\.\s*(\d+)\s*\n\s*(\d+)\s+SNPs'
        
        for match in re.finditer(chr_pattern, section_content):
            chr_num = int(match.group(1))
            snp_count = int(match.group(2))
            chromosomes.append({
                'chromosome': chr_num,
                'snps': snp_count
            })
        
        return chromosomes
    
    def _parse_date(self, date_str: str) -> Dict[str, Any]:
        """Parse date string (e.g., '975 AD', '1448 BC', '950-1020 AD')"""
        date_str = date_str.strip()
        
        # Check for BC
        is_bc = 'BC' in date_str.upper()
        date_str = re.sub(r'\s*BC\s*', '', date_str, flags=re.IGNORECASE)
        
        # Extract year(s)
        year_match = re.search(r'(\d+)', date_str)
        if not year_match:
            return {'year': None, 'is_bc': is_bc, 'raw': date_str}
        
        year = int(year_match.group(1))
        if is_bc:
            year = -year  # Negative for BC
        
        # Check for date range
        range_match = re.search(r'(\d+)\s*-\s*(\d+)', date_str)
        if range_match:
            year_start = int(range_match.group(1))
            year_end = int(range_match.group(2))
            if is_bc:
                year_start = -year_start
                year_end = -year_end
            return {
                'year': (year_start + year_end) / 2,  # Average
                'year_start': year_start,
                'year_end': year_end,
                'is_bc': is_bc,
                'is_range': True,
                'raw': date_str
            }
        
        return {
            'year': year,
            'is_bc': is_bc,
            'is_range': False,
            'raw': date_str
        }
    
    def _categorize_era(self, description: str) -> Optional[str]:
        """Categorize sample by historical era"""
        description_lower = description.lower()
        
        for era, pattern in self.era_patterns.items():
            if re.search(pattern, description, re.IGNORECASE):
                return era
        
        return None
    
    def _extract_regions(self, description: str) -> List[str]:
        """Extract geographic regions from description"""
        regions = []
        
        for region, pattern in self.region_patterns.items():
            if re.search(pattern, description, re.IGNORECASE):
                regions.append(region)
        
        return regions
    
    def parse_both_files(
        self,
        vk155_path: str,
        vk157_path: str
    ) -> Dict[str, Any]:
        """
        Parse both VK155 and VK157 files.
        
        Args:
            vk155_path: Path to VK155 MTA file
            vk157_path: Path to VK157 MTA file
            
        Returns:
            Dictionary with parsed data for both samples
        """
        vk155_data = self.parse_file(vk155_path)
        vk157_data = self.parse_file(vk157_path)
        
        return {
            'vk155': vk155_data,
            'vk157': vk157_data,
            'parsed_date': datetime.now().isoformat()
        }
