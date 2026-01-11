"""
Data layer for genealogy management: GEDCOM and JSON storage
"""
import json
import os
from typing import Dict, List, Optional, Any
from pathlib import Path


class GenealogyDataManager:
    """Manages genealogy data in GEDCOM and JSON formats"""
    
    def __init__(self, data_dir: str = "data/processed/genealogy"):
        """
        Initialize data manager.
        
        Args:
            data_dir: Directory for storing genealogy data files
        """
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)
    
    def load_gedcom(self, gedcom_path: str) -> Dict[str, Any]:
        """
        Load GEDCOM file and convert to internal format.
        
        Args:
            gedcom_path: Path to GEDCOM file
            
        Returns:
            Dictionary with parsed genealogy data
        """
        try:
            from gedcom.parser import Parser
            
            parser = Parser()
            parser.parse_file(gedcom_path)
            
            # Convert to internal format
            data = {
                'individuals': [],
                'families': [],
                'sources': [],
                'notes': []
            }
            
            # Extract individuals
            for individual in parser.individuals:
                ind_data = {
                    'id': individual.id,
                    'name': self._get_name(individual),
                    'birth': self._get_event(individual, 'BIRT'),
                    'death': self._get_event(individual, 'DEAT'),
                    'sex': individual.sex if hasattr(individual, 'sex') else None,
                    'notes': self._get_notes(individual)
                }
                data['individuals'].append(ind_data)
            
            # Extract families
            for family in parser.families:
                fam_data = {
                    'id': family.id,
                    'husband_id': family.husband.id if family.husband else None,
                    'wife_id': family.wife.id if family.wife else None,
                    'children': [child.id for child in family.children] if family.children else [],
                    'marriage': self._get_event(family, 'MARR')
                }
                data['families'].append(fam_data)
            
            return data
            
        except ImportError:
            # Fallback to python-gedcom
            try:
                from gedcom import Gedcom
                g = Gedcom(gedcom_path)
                return self._convert_gedcom_to_dict(g)
            except Exception as e:
                raise ValueError(f"Failed to parse GEDCOM file: {e}")
    
    def _get_name(self, individual) -> str:
        """Extract name from individual record"""
        if hasattr(individual, 'name') and individual.name:
            return str(individual.name)
        return f"Unknown {individual.id}"
    
    def _get_event(self, record, event_type: str) -> Optional[Dict]:
        """Extract event information"""
        if hasattr(record, 'events'):
            for event in record.events:
                if hasattr(event, 'type') and event.type == event_type:
                    return {
                        'date': str(event.date) if hasattr(event, 'date') else None,
                        'place': str(event.place) if hasattr(event, 'place') else None
                    }
        return None
    
    def _get_notes(self, record) -> List[str]:
        """Extract notes from record"""
        notes = []
        if hasattr(record, 'notes'):
            for note in record.notes:
                notes.append(str(note))
        return notes
    
    def _convert_gedcom_to_dict(self, gedcom_obj) -> Dict[str, Any]:
        """Convert python-gedcom object to dictionary"""
        data = {
            'individuals': [],
            'families': [],
            'sources': [],
            'notes': []
        }
        
        # Extract individuals
        for individual in gedcom_obj.individuals:
            ind_data = {
                'id': individual.pointer,
                'name': individual.name if hasattr(individual, 'name') else f"Unknown {individual.pointer}",
                'birth': None,
                'death': None,
                'sex': None,
                'notes': []
            }
            
            # Extract birth/death dates
            for event in individual.events:
                if event.type == 'BIRT':
                    ind_data['birth'] = {
                        'date': event.date if hasattr(event, 'date') else None,
                        'place': event.place if hasattr(event, 'place') else None
                    }
                elif event.type == 'DEAT':
                    ind_data['death'] = {
                        'date': event.date if hasattr(event, 'date') else None,
                        'place': event.place if hasattr(event, 'place') else None
                    }
            
            data['individuals'].append(ind_data)
        
        # Extract families
        for family in gedcom_obj.families:
            fam_data = {
                'id': family.pointer,
                'husband_id': family.husband.pointer if family.husband else None,
                'wife_id': family.wife.pointer if family.wife else None,
                'children': [child.pointer for child in family.children] if family.children else [],
                'marriage': None
            }
            
            # Extract marriage date
            for event in family.events:
                if event.type == 'MARR':
                    fam_data['marriage'] = {
                        'date': event.date if hasattr(event, 'date') else None,
                        'place': event.place if hasattr(event, 'place') else None
                    }
            
            data['families'].append(fam_data)
        
        return data
    
    def save_json(self, data: Dict[str, Any], filename: str) -> str:
        """
        Save genealogy data to JSON file.
        
        Args:
            data: Genealogy data dictionary
            filename: Output filename (without extension)
            
        Returns:
            Path to saved file
        """
        output_path = self.data_dir / f"{filename}.json"
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        return str(output_path)
    
    def load_json(self, filename: str) -> Dict[str, Any]:
        """
        Load genealogy data from JSON file.
        
        Args:
            filename: Input filename (with or without extension) or full path
            
        Returns:
            Dictionary with genealogy data
        """
        # Check if it's already a full path
        file_path = Path(filename)
        if not file_path.is_absolute() and not file_path.exists():
            # Try relative to data_dir
            if not filename.endswith('.json'):
                filename += '.json'
            file_path = self.data_dir / filename
        
        if not file_path.exists():
            raise FileNotFoundError(f"JSON file not found: {file_path}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def export_gedcom(self, data: Dict[str, Any], output_path: str) -> str:
        """
        Export genealogy data to GEDCOM format.
        
        Args:
            data: Genealogy data dictionary
            output_path: Path for output GEDCOM file
            
        Returns:
            Path to saved file
        """
        lines = [
            "0 HEAD",
            "1 SOUR Genealogy Data Manager",
            "2 VERS 5.5.1",
            "1 GEDC",
            "2 VERS 5.5.1",
            "1 CHAR UTF-8",
            "1 SUBM @SUBM@",
            "0 @SUBM@ SUBM",
            ""
        ]
        
        # Export individuals
        for ind in data.get('individuals', []):
            ind_id = ind['id']
            lines.append(f"0 {ind_id} INDI")
            
            # Name
            name_parts = ind.get('name', 'Unknown').split()
            if len(name_parts) >= 2:
                given = ' '.join(name_parts[:-1])
                surname = name_parts[-1]
                lines.append(f"1 NAME {given} /{surname}/")
            else:
                lines.append(f"1 NAME {ind.get('name', 'Unknown')}")
            
            # Sex
            sex = ind.get('sex', '').upper()
            if sex in ['M', 'F']:
                lines.append(f"1 SEX {sex}")
            
            # Birth
            if ind.get('birth'):
                birth = ind['birth'] if isinstance(ind['birth'], dict) else {}
                lines.append("1 BIRT")
                if birth.get('date'):
                    lines.append(f"2 DATE {birth['date']}")
                if birth.get('place'):
                    lines.append(f"2 PLAC {birth['place']}")
            
            # Death
            if ind.get('death'):
                death = ind['death'] if isinstance(ind['death'], dict) else {}
                lines.append("1 DEAT")
                if death.get('date'):
                    lines.append(f"2 DATE {death['date']}")
                if death.get('place'):
                    lines.append(f"2 PLAC {death['place']}")
            
            lines.append("")
        
        # Export families
        for fam in data.get('families', []):
            fam_id = fam['id']
            lines.append(f"0 {fam_id} FAM")
            
            if fam.get('husband_id'):
                lines.append(f"1 HUSB {fam['husband_id']}")
            if fam.get('wife_id'):
                lines.append(f"1 WIFE {fam['wife_id']}")
            
            for child_id in fam.get('children', []):
                lines.append(f"1 CHIL {child_id}")
            
            if fam.get('marriage'):
                marriage = fam['marriage'] if isinstance(fam['marriage'], dict) else {}
                lines.append("1 MARR")
                if marriage.get('date'):
                    lines.append(f"2 DATE {marriage['date']}")
                if marriage.get('place'):
                    lines.append(f"2 PLAC {marriage['place']}")
            
            lines.append("")
        
        lines.append("0 TRLR")
        
        # Write to file
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        
        return str(output_file)
    
    def list_files(self) -> List[str]:
        """List all genealogy data files"""
        return [f.name for f in self.data_dir.glob("*.json")] + \
               [f.name for f in self.data_dir.glob("*.ged")]
