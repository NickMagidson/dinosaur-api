from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum

class DinosaurPeriod(str, Enum):
    # Triassic subdivisions
    EARLY_TRIASSIC = "Early Triassic"
    MIDDLE_TRIASSIC = "Middle Triassic"
    LATE_TRIASSIC = "Late Triassic"
    
    # Jurassic subdivisions
    EARLY_JURASSIC = "Early Jurassic"
    MIDDLE_JURASSIC = "Middle Jurassic"
    LATE_JURASSIC = "Late Jurassic"
    
    # Cretaceous subdivisions
    EARLY_CRETACEOUS = "Early Cretaceous"
    LATE_CRETACEOUS = "Late Cretaceous"

class DinosaurDiet(str, Enum):
    HERBIVORE = "Herbivore"
    CARNIVORE = "Carnivore"
    OMNIVORE = "Omnivore"
    PISCIVORE = "Piscivore"  # Fish-eater
    INSECTIVORE = "Insectivore"  # Insect-eater

class DinosaurSize(str, Enum):
    TINY = "Tiny"  # < 1 meter
    SMALL = "Small"  # 1-3 meters
    MEDIUM = "Medium"  # 3-10 meters
    LARGE = "Large"  # 10-20 meters
    MASSIVE = "Massive"  # > 20 meters

class DinosaurClade(str, Enum):
    ORNITHISCHIA = "Ornithischia"  # Bird-hipped
    SAURISCHIA = "Saurischia"  # Lizard-hipped

class DinosaurGroup(str, Enum):
    # Theropods (carnivorous dinosaurs)
    THEROPODA = "Theropoda"
    TYRANNOSAURIA = "Tyrannosauria"
    DROMAEOSAURIDAE = "Dromaeosauridae"
    SPINOSAURIDAE = "Spinosauridae"
    ALLOSAURIDAE = "Allosauridae"
    COMPSOGNATHIDAE = "Compsognathidae"
    ORNITHOMIMOSAURIA = "Ornithomimosauria"
    THERIZINOSAURIDAE = "Therizinosauridae"
    OVIRAPTOROSAURIA = "Oviraptorosauria"
    TROODONTIDAE = "Troodontidae"
    
    # Sauropodomorphs (long-necked herbivores)
    SAUROPODOMORPHA = "Sauropodomorpha"
    DIPLODOCIDAE = "Diplodocidae"
    BRACHIOSAURIDAE = "Brachiosauridae"
    TITANOSAURIA = "Titanosauria"
    CAMARASAURIDAE = "Camarasauridae"
    
    # Ornithischians (bird-hipped herbivores)
    STEGOSAURIA = "Stegosauria"
    ANKYLOSAURIA = "Ankylosauria"
    CERATOPSIA = "Ceratopsia"
    HADROSAURIDAE = "Hadrosauridae"
    PACHYCEPHALOSAURIA = "Pachycephalosauria"
    ORNITHOPODA = "Ornithopoda"

class DinosaurLocomotion(str, Enum):
    BIPEDAL = "Bipedal"
    QUADRUPEDAL = "Quadrupedal"
    FACULTATIVE = "Facultative"  # Could switch between two and four legs

class DinosaurHabitat(str, Enum):
    TERRESTRIAL = "Terrestrial"
    SEMI_AQUATIC = "Semi-aquatic"
    ARBOREAL = "Arboreal"  # Tree-dwelling
    COASTAL = "Coastal"

class FossilQuality(str, Enum):
    EXCELLENT = "Excellent"  # Nearly complete skeleton
    GOOD = "Good"  # Substantial remains
    PARTIAL = "Partial"  # Incomplete remains
    FRAGMENTARY = "Fragmentary"  # Only fragments

class DinosaurBase(BaseModel):
    # Basic identification
    name: str = Field(..., description="Common name of the dinosaur")
    species: str = Field(..., description="Scientific species name (genus + species)")
    genus: str = Field(..., description="Scientific genus name")
    
    # Temporal information
    period: DinosaurPeriod = Field(..., description="Geological period when the dinosaur lived")
    age_start_mya: Optional[float] = Field(None, description="Start of age range in millions of years ago")
    age_end_mya: Optional[float] = Field(None, description="End of age range in millions of years ago")
    
    # Taxonomic classification
    clade: DinosaurClade = Field(..., description="Major dinosaur clade (Ornithischia or Saurischia)")
    group: DinosaurGroup = Field(..., description="Taxonomic group/family")
    
    # Physical characteristics
    diet: DinosaurDiet = Field(..., description="Dinosaur's diet type")
    size: DinosaurSize = Field(..., description="Relative size category")
    length_meters: Optional[float] = Field(None, ge=0, description="Estimated length in meters")
    height_meters: Optional[float] = Field(None, ge=0, description="Estimated height in meters")
    weight_kg: Optional[float] = Field(None, ge=0, description="Estimated weight in kilograms")
    skull_length_cm: Optional[float] = Field(None, ge=0, description="Skull length in centimeters")
    
    # Behavioral and anatomical traits
    locomotion: DinosaurLocomotion = Field(..., description="Mode of locomotion")
    habitat: DinosaurHabitat = Field(..., description="Primary habitat type")
    special_features: Optional[List[str]] = Field(default=[], description="Notable anatomical features")
    
    # Discovery and research information
    discovered_year: Optional[int] = Field(None, ge=1800, le=2025, description="Year of first discovery")
    discoverer: Optional[str] = Field(None, description="Name of the discoverer(s)")
    location_found: Optional[str] = Field(None, description="Geographic location where fossils were found")
    formation: Optional[str] = Field(None, description="Geological formation where discovered")
    fossil_quality: Optional[FossilQuality] = Field(None, description="Quality/completeness of fossil remains")
    
    # Descriptive information
    description: str = Field(..., description="Detailed description of the dinosaur")
    interesting_facts: Optional[List[str]] = Field(default=[], description="Interesting facts about this dinosaur")
    
    # Modern classification status
    is_valid_species: bool = Field(True, description="Whether this is considered a valid species")
    synonyms: Optional[List[str]] = Field(default=[], description="Alternative names or synonyms")

class DinosaurCreate(DinosaurBase):
    pass

class DinosaurUpdate(BaseModel):
    name: Optional[str] = None
    species: Optional[str] = None
    genus: Optional[str] = None
    period: Optional[DinosaurPeriod] = None
    age_start_mya: Optional[float] = Field(None, ge=0)
    age_end_mya: Optional[float] = Field(None, ge=0)
    clade: Optional[DinosaurClade] = None
    group: Optional[DinosaurGroup] = None
    diet: Optional[DinosaurDiet] = None
    size: Optional[DinosaurSize] = None
    length_meters: Optional[float] = Field(None, ge=0)
    height_meters: Optional[float] = Field(None, ge=0)
    weight_kg: Optional[float] = Field(None, ge=0)
    skull_length_cm: Optional[float] = Field(None, ge=0)
    locomotion: Optional[DinosaurLocomotion] = None
    habitat: Optional[DinosaurHabitat] = None
    special_features: Optional[List[str]] = None
    discovered_year: Optional[int] = Field(None, ge=1800, le=2025)
    discoverer: Optional[str] = None
    location_found: Optional[str] = None
    formation: Optional[str] = None
    fossil_quality: Optional[FossilQuality] = None
    description: Optional[str] = None
    interesting_facts: Optional[List[str]] = None
    is_valid_species: Optional[bool] = None
    synonyms: Optional[List[str]] = None

class Dinosaur(DinosaurBase):
    id: int = Field(..., description="Unique identifier for the dinosaur")
    
    class Config:
        from_attributes = True

class DinosaurResponse(BaseModel):
    dinosaurs: List[Dinosaur]
    total: int
    page: int
    per_page: int

class ErrorResponse(BaseModel):
    detail: str
    status_code: int
