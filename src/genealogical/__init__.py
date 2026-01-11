"""
Genealogical Data Handling Module
"""
from .data_manager import GenealogyDataManager
from .gedcom_parser import parse_family_tree

__all__ = ['GenealogyDataManager', 'parse_family_tree']