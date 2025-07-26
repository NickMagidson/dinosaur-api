from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_, func
from models import (
    Dinosaur, DinosaurPeriod, DinosaurDiet, DinosaurSize, 
    DinosaurClade, DinosaurGroup, DinosaurLocomotion, 
    DinosaurHabitat, FossilQuality
)
from db_config import DinosaurModel, SessionLocal, create_tables, engine

class PostgreSQLDinosaurDatabase:
    def __init__(self):
        # Create tables if they don't exist
        create_tables()
        # Populate initial data if database is empty
        self._populate_initial_data_if_empty()
    
    def _get_db_session(self) -> Session:
        """Get a database session"""
        return SessionLocal()
    
    def _populate_initial_data_if_empty(self):
        """Populate the database with initial data if it's empty"""
        db = self._get_db_session()
        try:
            count = db.query(DinosaurModel).count()
            if count == 0:
                self._populate_initial_data()
        finally:
            db.close()
    
    def _populate_initial_data(self):
        """Populate the database with scientifically accurate dinosaur data"""
        initial_dinosaurs = [
            {
                "name": "Tyrannosaurus Rex",
                "species": "Tyrannosaurus rex",
                "genus": "Tyrannosaurus",
                "period": DinosaurPeriod.LATE_CRETACEOUS.value,
                "age_start_mya": 68.0,
                "age_end_mya": 66.0,
                "clade": DinosaurClade.SAURISCHIA.value,
                "group": DinosaurGroup.TYRANNOSAURIA.value,
                "diet": DinosaurDiet.CARNIVORE.value,
                "size": DinosaurSize.MASSIVE.value,
                "length_meters": 12.3,
                "height_meters": 4.0,
                "weight_kg": 8400,
                "skull_length_cm": 150,
                "locomotion": DinosaurLocomotion.BIPEDAL.value,
                "habitat": DinosaurHabitat.TERRESTRIAL.value,
                "special_features": ["Massive skull", "Powerful bite force", "Tiny arms", "Binocular vision"],
                "discovered_year": 1905,
                "discoverer": "Henry Fairfield Osborn",
                "location_found": "Montana, USA",
                "formation": "Hell Creek Formation",
                "fossil_quality": FossilQuality.EXCELLENT.value,
                "description": "One of the largest land predators ever known, T-Rex was a formidable apex predator with powerful jaws capable of crushing bone.",
                "interesting_facts": [
                    "Had a bite force of over 12,800 pounds",
                    "Possessed excellent vision and smell",
                    "Could grow up to 40 feet long",
                    "Lived in family groups"
                ],
                "is_valid_species": True,
                "synonyms": ["T-Rex", "King of the tyrant lizards"]
            },
            {
                "name": "Triceratops",
                "species": "Triceratops horridus",
                "genus": "Triceratops",
                "period": DinosaurPeriod.LATE_CRETACEOUS.value,
                "age_start_mya": 68.0,
                "age_end_mya": 66.0,
                "clade": DinosaurClade.ORNITHISCHIA.value,
                "group": DinosaurGroup.CERATOPSIA.value,
                "diet": DinosaurDiet.HERBIVORE.value,
                "size": DinosaurSize.LARGE.value,
                "length_meters": 9.0,
                "height_meters": 3.0,
                "weight_kg": 6000,
                "skull_length_cm": 250,
                "locomotion": DinosaurLocomotion.QUADRUPEDAL.value,
                "habitat": DinosaurHabitat.TERRESTRIAL.value,
                "special_features": ["Three facial horns", "Large bony frill", "Parrot-like beak"],
                "discovered_year": 1889,
                "discoverer": "Othniel Charles Marsh",
                "location_found": "Colorado, USA",
                "formation": "Lance Formation",
                "fossil_quality": FossilQuality.EXCELLENT.value,
                "description": "A large herbivorous dinosaur known for its distinctive three horns and large bony frill.",
                "interesting_facts": [
                    "Used its horns for defense and display",
                    "Had a powerful beak for cutting vegetation",
                    "One of the last dinosaur species before extinction",
                    "Lived in herds for protection"
                ],
                "is_valid_species": True,
                "synonyms": ["Three-horned face"]
            },
            {
                "name": "Velociraptor",
                "species": "Velociraptor mongoliensis",
                "genus": "Velociraptor",
                "period": DinosaurPeriod.LATE_CRETACEOUS.value,
                "age_start_mya": 75.0,
                "age_end_mya": 71.0,
                "clade": DinosaurClade.SAURISCHIA.value,
                "group": DinosaurGroup.DROMAEOSAURIDAE.value,
                "diet": DinosaurDiet.CARNIVORE.value,
                "size": DinosaurSize.SMALL.value,
                "length_meters": 2.0,
                "height_meters": 0.5,
                "weight_kg": 15,
                "skull_length_cm": 25,
                "locomotion": DinosaurLocomotion.BIPEDAL.value,
                "habitat": DinosaurHabitat.TERRESTRIAL.value,
                "special_features": ["Sickle-shaped claw", "Feathers", "High intelligence", "Pack hunting behavior"],
                "discovered_year": 1924,
                "discoverer": "Henry Fairfield Osborn",
                "location_found": "Mongolia",
                "formation": "Djadochta Formation",
                "fossil_quality": FossilQuality.GOOD.value,
                "description": "A small but intelligent raptor dinosaur known for its sickle-shaped killing claw and pack hunting behavior.",
                "interesting_facts": [
                    "Had feathers for display and temperature regulation",
                    "Hunted in coordinated packs",
                    "Could reach speeds of 40 mph",
                    "Much smaller than portrayed in movies"
                ],
                "is_valid_species": True,
                "synonyms": ["Swift thief", "Raptor"]
            }
        ]
        
        db = self._get_db_session()
        try:
            for dino_data in initial_dinosaurs:
                dino_model = DinosaurModel(**dino_data)
                db.add(dino_model)
            db.commit()
        finally:
            db.close()
    
    def _model_to_pydantic(self, dino_model: DinosaurModel) -> Dinosaur:
        """Convert SQLAlchemy model to Pydantic model"""
        return Dinosaur(
            id=dino_model.id,
            name=dino_model.name,
            species=dino_model.species,
            genus=dino_model.genus,
            period=DinosaurPeriod(dino_model.period),
            age_start_mya=dino_model.age_start_mya,
            age_end_mya=dino_model.age_end_mya,
            clade=DinosaurClade(dino_model.clade),
            group=DinosaurGroup(dino_model.group),
            diet=DinosaurDiet(dino_model.diet),
            size=DinosaurSize(dino_model.size),
            length_meters=dino_model.length_meters,
            height_meters=dino_model.height_meters,
            weight_kg=dino_model.weight_kg,
            skull_length_cm=dino_model.skull_length_cm,
            locomotion=DinosaurLocomotion(dino_model.locomotion),
            habitat=DinosaurHabitat(dino_model.habitat),
            special_features=dino_model.special_features or [],
            discovered_year=dino_model.discovered_year,
            discoverer=dino_model.discoverer,
            location_found=dino_model.location_found,
            formation=dino_model.formation,
            fossil_quality=FossilQuality(dino_model.fossil_quality),
            description=dino_model.description,
            interesting_facts=dino_model.interesting_facts or [],
            is_valid_species=dino_model.is_valid_species,
            synonyms=dino_model.synonyms or []
        )
    
    def get_all(
        self,
        skip: int = 0,
        limit: int = 100,
        period: Optional[DinosaurPeriod] = None,
        diet: Optional[DinosaurDiet] = None,
        size: Optional[DinosaurSize] = None,
        clade: Optional[DinosaurClade] = None,
        group: Optional[DinosaurGroup] = None,
        locomotion: Optional[DinosaurLocomotion] = None,
        habitat: Optional[DinosaurHabitat] = None,
        fossil_quality: Optional[FossilQuality] = None,
        min_length: Optional[float] = None,
        max_length: Optional[float] = None,
        min_age: Optional[float] = None,
        max_age: Optional[float] = None
    ) -> List[Dinosaur]:
        """Get all dinosaurs with filtering and pagination"""
        db = self._get_db_session()
        try:
            query = db.query(DinosaurModel)
            
            # Apply filters
            if period:
                query = query.filter(DinosaurModel.period == period.value)
            if diet:
                query = query.filter(DinosaurModel.diet == diet.value)
            if size:
                query = query.filter(DinosaurModel.size == size.value)
            if clade:
                query = query.filter(DinosaurModel.clade == clade.value)
            if group:
                query = query.filter(DinosaurModel.group == group.value)
            if locomotion:
                query = query.filter(DinosaurModel.locomotion == locomotion.value)
            if habitat:
                query = query.filter(DinosaurModel.habitat == habitat.value)
            if fossil_quality:
                query = query.filter(DinosaurModel.fossil_quality == fossil_quality.value)
            if min_length is not None:
                query = query.filter(DinosaurModel.length_meters >= min_length)
            if max_length is not None:
                query = query.filter(DinosaurModel.length_meters <= max_length)
            if min_age is not None:
                query = query.filter(DinosaurModel.age_start_mya >= min_age)
            if max_age is not None:
                query = query.filter(DinosaurModel.age_end_mya <= max_age)
            
            # Apply pagination
            dino_models = query.offset(skip).limit(limit).all()
            
            # Convert to Pydantic models
            return [self._model_to_pydantic(dino) for dino in dino_models]
        finally:
            db.close()
    
    def get_by_id(self, dinosaur_id: int) -> Optional[Dinosaur]:
        """Get a dinosaur by ID"""
        db = self._get_db_session()
        try:
            dino_model = db.query(DinosaurModel).filter(DinosaurModel.id == dinosaur_id).first()
            if dino_model:
                return self._model_to_pydantic(dino_model)
            return None
        finally:
            db.close()
    
    def search(self, query: str) -> List[Dinosaur]:
        """Search dinosaurs by name, species, or description"""
        db = self._get_db_session()
        try:
            search_term = f"%{query.lower()}%"
            dino_models = db.query(DinosaurModel).filter(
                or_(
                    func.lower(DinosaurModel.name).like(search_term),
                    func.lower(DinosaurModel.species).like(search_term),
                    func.lower(DinosaurModel.description).like(search_term),
                    func.lower(DinosaurModel.genus).like(search_term)
                )
            ).all()
            
            return [self._model_to_pydantic(dino) for dino in dino_models]
        finally:
            db.close()
    
    def get_stats(self) -> Dict[str, Any]:
        """Get database statistics"""
        db = self._get_db_session()
        try:
            total_count = db.query(DinosaurModel).count()
            
            if total_count == 0:
                return {
                    "total_dinosaurs": 0,
                    "periods": {},
                    "diets": {},
                    "sizes": {},
                    "average_length": 0,
                    "average_weight": 0
                }
            
            # Get period counts
            period_counts = {}
            period_stats = db.query(DinosaurModel.period, func.count(DinosaurModel.period)).group_by(DinosaurModel.period).all()
            for period, count in period_stats:
                period_counts[period] = count
            
            # Get diet counts
            diet_counts = {}
            diet_stats = db.query(DinosaurModel.diet, func.count(DinosaurModel.diet)).group_by(DinosaurModel.diet).all()
            for diet, count in diet_stats:
                diet_counts[diet] = count
            
            # Get size counts
            size_counts = {}
            size_stats = db.query(DinosaurModel.size, func.count(DinosaurModel.size)).group_by(DinosaurModel.size).all()
            for size, count in size_stats:
                size_counts[size] = count
            
            # Get averages
            avg_length = db.query(func.avg(DinosaurModel.length_meters)).scalar() or 0
            avg_weight = db.query(func.avg(DinosaurModel.weight_kg)).filter(DinosaurModel.weight_kg.isnot(None)).scalar() or 0
            
            return {
                "total_dinosaurs": total_count,
                "periods": period_counts,
                "diets": diet_counts,
                "sizes": size_counts,
                "average_length": float(avg_length),
                "average_weight": float(avg_weight)
            }
        finally:
            db.close()

# Global database instance
db = PostgreSQLDinosaurDatabase()
