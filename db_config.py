import os
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, Text, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost:5432/dinosaur_db")

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# SQLAlchemy model for Dinosaur
class DinosaurModel(Base):
    __tablename__ = "dinosaurs"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    species = Column(String)
    genus = Column(String)
    period = Column(String)
    age_start_mya = Column(Float)
    age_end_mya = Column(Float)
    clade = Column(String)
    group = Column(String)
    diet = Column(String)
    size = Column(String)
    length_meters = Column(Float)
    height_meters = Column(Float)
    weight_kg = Column(Float, nullable=True)
    skull_length_cm = Column(Float, nullable=True)
    locomotion = Column(String)
    habitat = Column(String)
    special_features = Column(ARRAY(String))
    discovered_year = Column(Integer, nullable=True)
    discoverer = Column(String, nullable=True)
    location_found = Column(String, nullable=True)
    formation = Column(String, nullable=True)
    fossil_quality = Column(String)
    description = Column(Text)
    interesting_facts = Column(ARRAY(String))
    is_valid_species = Column(Boolean, default=True)
    synonyms = Column(ARRAY(String))

def get_db():
    """Get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    """Create database tables"""
    Base.metadata.create_all(bind=engine)
