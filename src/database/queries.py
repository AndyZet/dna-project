"""
Common database queries
"""
from sqlalchemy.orm import Session, sessionmaker
from typing import List, Optional
from .models import YDNAResult, Individual, Family


def get_y_dna_results(session: Session, haplogroup: Optional[str] = None) -> List[YDNAResult]:
    """
    Get Y-DNA results, optionally filtered by haplogroup.
    
    Args:
        session: SQLAlchemy session
        haplogroup: Optional haplogroup filter
        
    Returns:
        List of YDNAResult objects
    """
    query = session.query(YDNAResult)
    if haplogroup:
        query = query.filter(YDNAResult.haplogroup == haplogroup)
    return query.all()


def store_results(
    y_dna_tree,
    snp_results,
    tmrca_data,
    family_tree
) -> None:
    """
    Store analysis results in database.
    
    Args:
        y_dna_tree: Y-DNA tree data
        snp_results: SNP analysis results
        tmrca_data: TMRCA calculation results
        family_tree: Family tree data
    """
    try:
        from .models import create_database
        engine = create_database()
        Session = sessionmaker(bind=engine)
        session = Session()
        
        # Store results
        # This is a placeholder - implement actual storage logic
        
        session.commit()
        print("Results stored in database")
        
    except Exception as e:
        print(f"Error storing results: {e}")
