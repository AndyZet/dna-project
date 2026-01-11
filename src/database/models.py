"""
SQLAlchemy models for genealogical database
"""
from sqlalchemy import create_engine, Column, Integer, String, Float, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()


class YDNAResult(Base):
    """Y-DNA test results"""
    __tablename__ = 'y_dna_results'
    
    id = Column(Integer, primary_key=True)
    individual_id = Column(String(100))
    haplogroup = Column(String(50))
    tmrca_years = Column(Integer)
    snp_count = Column(Integer)
    y_str_profile = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)


class Individual(Base):
    """Genealogical individual"""
    __tablename__ = 'individuals'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    birth_date = Column(String(50))
    death_date = Column(String(50))
    location = Column(String(200))
    notes = Column(Text)


class Family(Base):
    """Family relationships"""
    __tablename__ = 'families'
    
    id = Column(Integer, primary_key=True)
    husband_id = Column(Integer)
    wife_id = Column(Integer)
    marriage_date = Column(String(50))
    location = Column(String(200))


def create_database(db_path: str = 'data/processed/family_tree_normalized.db'):
    """Create database and tables"""
    engine = create_engine(f'sqlite:///{db_path}')
    Base.metadata.create_all(engine)
    return engine
