from typing import List, Optional, Dict, Any
from models import (
    Dinosaur, DinosaurPeriod, DinosaurDiet, DinosaurSize, 
    DinosaurClade, DinosaurGroup, DinosaurLocomotion, 
    DinosaurHabitat, FossilQuality
)

class DinosaurDatabase:
    def __init__(self):
        self.dinosaurs: Dict[int, Dinosaur] = {}
        self.next_id = 1
        self._populate_initial_data()
    
    def _populate_initial_data(self):
        """Populate the database with scientifically accurate dinosaur data"""
        initial_dinosaurs = [
            {
                "name": "Tyrannosaurus Rex",
                "species": "Tyrannosaurus rex",
                "genus": "Tyrannosaurus",
                "period": DinosaurPeriod.LATE_CRETACEOUS,
                "age_start_mya": 68.0,
                "age_end_mya": 66.0,
                "clade": DinosaurClade.SAURISCHIA,
                "group": DinosaurGroup.TYRANNOSAURIA,
                "diet": DinosaurDiet.CARNIVORE,
                "size": DinosaurSize.MASSIVE,
                "length_meters": 12.3,
                "height_meters": 4.0,
                "weight_kg": 8400,
                "skull_length_cm": 150,
                "locomotion": DinosaurLocomotion.BIPEDAL,
                "habitat": DinosaurHabitat.TERRESTRIAL,
                "special_features": ["Massive skull", "Powerful bite force", "Tiny arms", "Binocular vision"],
                "discovered_year": 1905,
                "discoverer": "Henry Fairfield Osborn",
                "location_found": "Montana, USA",
                "formation": "Hell Creek Formation",
                "fossil_quality": FossilQuality.EXCELLENT,
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
                "period": DinosaurPeriod.LATE_CRETACEOUS,
                "age_start_mya": 68.0,
                "age_end_mya": 66.0,
                "clade": DinosaurClade.ORNITHISCHIA,
                "group": DinosaurGroup.CERATOPSIA,
                "diet": DinosaurDiet.HERBIVORE,
                "size": DinosaurSize.LARGE,
                "length_meters": 9.0,
                "height_meters": 3.0,
                "weight_kg": 5400,
                "skull_length_cm": 250,
                "locomotion": DinosaurLocomotion.QUADRUPEDAL,
                "habitat": DinosaurHabitat.TERRESTRIAL,
                "special_features": ["Three facial horns", "Large bony frill", "Beak-like mouth", "Dental batteries"],
                "discovered_year": 1889,
                "discoverer": "Othniel Charles Marsh",
                "location_found": "Colorado, USA",
                "formation": "Lance Formation",
                "fossil_quality": FossilQuality.EXCELLENT,
                "description": "A large herbivorous dinosaur with three distinctive facial horns and a large bony frill that likely lived in herds.",
                "interesting_facts": [
                    "The frill may have been used for display and species recognition",
                    "Had a powerful beak for cutting vegetation",
                    "Lived alongside T. rex in the same time and place",
                    "One of the last dinosaurs to exist before the mass extinction"
                ],
                "is_valid_species": True,
                "synonyms": ["Three-horned face"]
            },
            {
                "name": "Brachiosaurus",
                "species": "Brachiosaurus altithorax",
                "genus": "Brachiosaurus",
                "period": DinosaurPeriod.LATE_JURASSIC,
                "age_start_mya": 156.0,
                "age_end_mya": 145.0,
                "clade": DinosaurClade.SAURISCHIA,
                "group": DinosaurGroup.BRACHIOSAURIDAE,
                "diet": DinosaurDiet.HERBIVORE,
                "size": DinosaurSize.MASSIVE,
                "length_meters": 26.0,
                "height_meters": 12.0,
                "weight_kg": 56000,
                "skull_length_cm": 80,
                "locomotion": DinosaurLocomotion.QUADRUPEDAL,
                "habitat": DinosaurHabitat.TERRESTRIAL,
                "special_features": ["Extremely long neck", "High-positioned nostrils", "Columnar legs", "Long front legs"],
                "discovered_year": 1903,
                "discoverer": "Elmer S. Riggs",
                "location_found": "Colorado, USA",
                "formation": "Morrison Formation",
                "fossil_quality": FossilQuality.PARTIAL,
                "description": "A massive long-necked dinosaur that could reach vegetation high up in trees, with front legs longer than back legs.",
                "interesting_facts": [
                    "Could reach heights of up to 40 feet",
                    "Weighed as much as 12 elephants",
                    "Had a unique body plan with longer front legs",
                    "Lived in herds and migrated seasonally"
                ],
                "is_valid_species": True,
                "synonyms": ["Arm lizard"]
            },
            {
                "name": "Velociraptor",
                "species": "Velociraptor mongoliensis",
                "genus": "Velociraptor",
                "period": DinosaurPeriod.LATE_CRETACEOUS,
                "age_start_mya": 75.0,
                "age_end_mya": 71.0,
                "clade": DinosaurClade.SAURISCHIA,
                "group": DinosaurGroup.DROMAEOSAURIDAE,
                "diet": DinosaurDiet.CARNIVORE,
                "size": DinosaurSize.SMALL,
                "length_meters": 2.0,
                "height_meters": 0.5,
                "weight_kg": 15,
                "skull_length_cm": 25,
                "locomotion": DinosaurLocomotion.BIPEDAL,
                "habitat": DinosaurHabitat.TERRESTRIAL,
                "special_features": ["Sickle-shaped claw", "Feathers", "Long tail", "Large brain"],
                "discovered_year": 1924,
                "discoverer": "Henry Fairfield Osborn",
                "location_found": "Gobi Desert, Mongolia",
                "formation": "Djadochta Formation",
                "fossil_quality": FossilQuality.GOOD,
                "description": "A small but intelligent pack hunter with a large sickle-shaped claw on each foot, covered in feathers.",
                "interesting_facts": [
                    "Much smaller than depicted in popular media",
                    "Had feathers but couldn't fly",
                    "Hunted in coordinated packs",
                    "The famous fighting dinosaurs fossil shows one locked in combat with Protoceratops"
                ],
                "is_valid_species": True,
                "synonyms": ["Swift thief", "Raptor"]
            },
            {
                "name": "Stegosaurus",
                "species": "Stegosaurus stenops",
                "genus": "Stegosaurus",
                "period": DinosaurPeriod.LATE_JURASSIC,
                "age_start_mya": 155.0,
                "age_end_mya": 150.0,
                "clade": DinosaurClade.ORNITHISCHIA,
                "group": DinosaurGroup.STEGOSAURIA,
                "diet": DinosaurDiet.HERBIVORE,
                "size": DinosaurSize.LARGE,
                "length_meters": 9.0,
                "height_meters": 4.0,
                "weight_kg": 3500,
                "skull_length_cm": 40,
                "locomotion": DinosaurLocomotion.QUADRUPEDAL,
                "habitat": DinosaurHabitat.TERRESTRIAL,
                "special_features": ["Double row of plates", "Four tail spikes", "Small head", "Beak-like mouth"],
                "discovered_year": 1877,
                "discoverer": "Othniel Charles Marsh",
                "location_found": "Colorado, USA",
                "formation": "Morrison Formation",
                "fossil_quality": FossilQuality.EXCELLENT,
                "description": "A large herbivorous dinosaur with distinctive double rows of plates along its back and four spikes on its tail.",
                "interesting_facts": [
                    "The plates may have been used for temperature regulation",
                    "Had a brain the size of a walnut",
                    "The tail spikes are called a 'thagomizer'",
                    "State fossil of Colorado"
                ],
                "is_valid_species": True,
                "synonyms": ["Roof lizard"]
            },
            {
                "name": "Spinosaurus",
                "species": "Spinosaurus aegyptiacus",
                "genus": "Spinosaurus",
                "period": DinosaurPeriod.EARLY_CRETACEOUS,
                "age_start_mya": 112.0,
                "age_end_mya": 94.0,
                "clade": DinosaurClade.SAURISCHIA,
                "group": DinosaurGroup.SPINOSAURIDAE,
                "diet": DinosaurDiet.PISCIVORE,
                "size": DinosaurSize.MASSIVE,
                "length_meters": 15.0,
                "height_meters": 5.5,
                "weight_kg": 7400,
                "skull_length_cm": 175,
                "locomotion": DinosaurLocomotion.FACULTATIVE,
                "habitat": DinosaurHabitat.SEMI_AQUATIC,
                "special_features": ["Large sail on back", "Crocodile-like skull", "Webbed feet", "Dense bones"],
                "discovered_year": 1912,
                "discoverer": "Ernst Stromer",
                "location_found": "Egypt",
                "formation": "Bahariya Formation",
                "fossil_quality": FossilQuality.PARTIAL,
                "description": "The largest predatory dinosaur, adapted for an aquatic lifestyle with a distinctive sail and crocodile-like features.",
                "interesting_facts": [
                    "Longer than T. rex and may have been heavier",
                    "Spent much of its time in water hunting fish",
                    "The sail may have been used for display",
                    "Original fossils were destroyed in WWII bombing"
                ],
                "is_valid_species": True,
            },
            {
                "name": "Velociraptor",
                "species": "Velociraptor mongoliensis",
                "genus": "Velociraptor",
                "period": DinosaurPeriod.LATE_CRETACEOUS,
                "age_start_mya": 75.0,
                "age_end_mya": 71.0,
                "clade": DinosaurClade.SAURISCHIA,
                "group": DinosaurGroup.DROMAEOSAURIDAE,
                "diet": DinosaurDiet.CARNIVORE,
                "size": DinosaurSize.SMALL,
                "length_meters": 2.0,
                "height_meters": 0.5,
                "weight_kg": 20,
                "skull_length_cm": 25,
                "locomotion": DinosaurLocomotion.BIPEDAL,
                "habitat": DinosaurHabitat.TERRESTRIAL,
                "special_features": ["Sickle-shaped claws", "Pack hunting behavior", "High intelligence", "Feathers"],
                "discovered_year": 1924,
                "discoverer": "Henry Fairfield Osborn",
                "location_found": "Mongolia",
                "formation": "Djadochta Formation",
                "fossil_quality": FossilQuality.GOOD,
                "description": "A small but intelligent pack hunter with a distinctive sickle-shaped claw on each foot, now known to have been feathered.",
                "interesting_facts": [
                    "Much smaller than depicted in movies",
                    "Likely had feathers for display and temperature regulation",
                    "Hunted in coordinated packs",
                    "Famous for the 'Fighting Dinosaurs' fossil"
                ],
                "is_valid_species": True,
                "synonyms": ["Raptor"]
            },
            {
                "name": "Stegosaurus",
                "species": "Stegosaurus stenops",
                "genus": "Stegosaurus",
                "period": DinosaurPeriod.LATE_JURASSIC,
                "age_start_mya": 155.0,
                "age_end_mya": 145.0,
                "clade": DinosaurClade.ORNITHISCHIA,
                "group": DinosaurGroup.STEGOSAURIA,
                "diet": DinosaurDiet.HERBIVORE,
                "size": DinosaurSize.LARGE,
                "length_meters": 9.0,
                "height_meters": 2.75,
                "weight_kg": 2300,
                "skull_length_cm": 40,
                "locomotion": DinosaurLocomotion.QUADRUPEDAL,
                "habitat": DinosaurHabitat.TERRESTRIAL,
                "special_features": ["Double row of plates", "Four tail spikes (thagomizer)", "Small brain", "Bird-like beak"],
                "discovered_year": 1877,
                "discoverer": "Othniel Charles Marsh",
                "location_found": "Colorado, USA",
                "formation": "Morrison Formation",
                "fossil_quality": FossilQuality.EXCELLENT,
                "description": "A herbivorous dinosaur known for its distinctive row of large triangular plates along its back and spiked tail.",
                "interesting_facts": [
                    "Brain was only the size of a walnut",
                    "Plates may have been used for temperature regulation",
                    "The tail spikes are called a 'thagomizer'",
                    "Colorado's state fossil"
                ],
                "is_valid_species": True,
                "synonyms": ["Roof lizard"]
            },
            {
                "name": "Allosaurus",
                "species": "Allosaurus fragilis",
                "genus": "Allosaurus",
                "period": DinosaurPeriod.LATE_JURASSIC,
                "age_start_mya": 155.0,
                "age_end_mya": 145.0,
                "clade": DinosaurClade.SAURISCHIA,
                "group": DinosaurGroup.ALLOSAURIDAE,
                "diet": DinosaurDiet.CARNIVORE,
                "size": DinosaurSize.LARGE,
                "length_meters": 8.5,
                "height_meters": 3.0,
                "weight_kg": 1700,
                "skull_length_cm": 84,
                "locomotion": DinosaurLocomotion.BIPEDAL,
                "habitat": DinosaurHabitat.TERRESTRIAL,
                "special_features": ["Large claws", "Powerful jaw", "Long arms", "Distinctive skull ridges"],
                "discovered_year": 1877,
                "discoverer": "Othniel Charles Marsh",
                "location_found": "Colorado, USA",
                "formation": "Morrison Formation",
                "fossil_quality": FossilQuality.EXCELLENT,
                "description": "A large carnivorous dinosaur that was one of the top predators of the Jurassic period, known for its distinctive skull horns.",
                "interesting_facts": [
                    "Utah's state fossil",
                    "Had distinctive lacrimal horns above its eyes",
                    "Could reach speeds of up to 25 mph",
                    "May have hunted in packs"
                ],
                "is_valid_species": True,
                "synonyms": ["Different lizard"]
            },
            {
                "name": "Diplodocus",
                "species": "Diplodocus longus",
                "genus": "Diplodocus",
                "period": DinosaurPeriod.LATE_JURASSIC,
                "age_start_mya": 154.0,
                "age_end_mya": 145.0,
                "clade": DinosaurClade.SAURISCHIA,
                "group": DinosaurGroup.DIPLODOCIDAE,
                "diet": DinosaurDiet.HERBIVORE,
                "size": DinosaurSize.MASSIVE,
                "length_meters": 26.0,
                "height_meters": 6.0,
                "weight_kg": 11000,
                "skull_length_cm": 60,
                "locomotion": DinosaurLocomotion.QUADRUPEDAL,
                "habitat": DinosaurHabitat.TERRESTRIAL,
                "special_features": ["Extremely long neck", "Whip-like tail", "Peg-like teeth", "Nostrils on top of head"],
                "discovered_year": 1878,
                "discoverer": "Samuel Wendell Williston",
                "location_found": "Colorado, USA",
                "formation": "Morrison Formation",
                "fossil_quality": FossilQuality.EXCELLENT,
                "description": "An extremely long dinosaur with a whip-like tail and a long neck for reaching vegetation at various heights.",
                "interesting_facts": [
                    "Could crack its tail like a whip",
                    "Despite its size, had a relatively small head",
                    "May have reared up on hind legs to reach high vegetation",
                    "Had a second brain in its hip region"
                ],
                "is_valid_species": True,
                "synonyms": ["Double beam"]
            },
            {
                "name": "Parasaurolophus",
                "species": "Parasaurolophus walkeri",
                "genus": "Parasaurolophus",
                "period": DinosaurPeriod.LATE_CRETACEOUS,
                "age_start_mya": 76.0,
                "age_end_mya": 73.0,
                "clade": DinosaurClade.ORNITHISCHIA,
                "group": DinosaurGroup.HADROSAURIDAE,
                "diet": DinosaurDiet.HERBIVORE,
                "size": DinosaurSize.MEDIUM,
                "length_meters": 9.5,
                "height_meters": 4.5,
                "weight_kg": 2500,
                "skull_length_cm": 160,
                "locomotion": DinosaurLocomotion.FACULTATIVE,
                "habitat": DinosaurHabitat.TERRESTRIAL,
                "special_features": ["Hollow cranial crest", "Duck-like bill", "Musical capabilities", "Complex social behavior"],
                "discovered_year": 1922,
                "discoverer": "William Parks",
                "location_found": "Alberta, Canada",
                "formation": "Dinosaur Park Formation",
                "fossil_quality": FossilQuality.EXCELLENT,
                "description": "A duck-billed dinosaur known for its distinctive hollow crest that could produce musical sounds for communication.",
                "interesting_facts": [
                    "Could produce musical notes through its crest",
                    "Different species had different crest shapes and sounds",
                    "Lived in large herds for protection",
                    "Had hundreds of small teeth for grinding plants"
                ],
                "is_valid_species": True,
                "synonyms": ["Near crested lizard"]
            }
        ]
        
        for i, dino_data in enumerate(initial_dinosaurs, 1):
            dinosaur = Dinosaur(id=i, **dino_data)
            self.dinosaurs[i] = dinosaur
            
        self.next_id = len(initial_dinosaurs) + 1
    
    def get_all(self, skip: int = 0, limit: int = 100, 
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
                max_age: Optional[float] = None) -> List[Dinosaur]:
        """Get all dinosaurs with comprehensive filtering options"""
        dinosaurs = list(self.dinosaurs.values())
        
        # Make this less DRY?
        # Apply filters
        if period:
            dinosaurs = [d for d in dinosaurs if d.period == period]
        if diet:
            dinosaurs = [d for d in dinosaurs if d.diet == diet]
        if size:
            dinosaurs = [d for d in dinosaurs if d.size == size]
        if clade:
            dinosaurs = [d for d in dinosaurs if d.clade == clade]
        if group:
            dinosaurs = [d for d in dinosaurs if d.group == group]
        if locomotion:
            dinosaurs = [d for d in dinosaurs if d.locomotion == locomotion]
        if habitat:
            dinosaurs = [d for d in dinosaurs if d.habitat == habitat]
        if fossil_quality:
            dinosaurs = [d for d in dinosaurs if d.fossil_quality == fossil_quality]
        if min_length is not None:
            dinosaurs = [d for d in dinosaurs if d.length_meters and d.length_meters >= min_length]
        if max_length is not None:
            dinosaurs = [d for d in dinosaurs if d.length_meters and d.length_meters <= max_length]
        if min_age is not None:
            dinosaurs = [d for d in dinosaurs if d.age_end_mya and d.age_end_mya >= min_age]
        if max_age is not None:
            dinosaurs = [d for d in dinosaurs if d.age_start_mya and d.age_start_mya <= max_age]
        
        # Apply pagination
        return dinosaurs[skip:skip + limit]
    
    def get_by_id(self, dinosaur_id: int) -> Optional[Dinosaur]:
        """Get a dinosaur by ID"""
        return self.dinosaurs.get(dinosaur_id)
    
    def search(self, query: str) -> List[Dinosaur]:
        """Search dinosaurs by name, species, or description"""
        query = query.lower()
        results = []
        for dinosaur in self.dinosaurs.values():
            if (query in dinosaur.name.lower() or 
                query in dinosaur.species.lower() or 
                query in dinosaur.genus.lower() or
                query in dinosaur.description.lower() or
                any(query in fact.lower() for fact in dinosaur.interesting_facts)):
                results.append(dinosaur)
        return results
    
    def get_stats(self) -> Dict[str, Any]:
        """Get database statistics"""
        dinosaurs = list(self.dinosaurs.values())
        
        if not dinosaurs:
            return {
                "total_dinosaurs": 0,
                "periods": {},
                "diets": {},
                "sizes": {},
                "average_length": 0,
                "average_weight": 0
            }
        
        period_counts = {}
        diet_counts = {}
        size_counts = {}
        
        for dino in dinosaurs:
            period_counts[dino.period.value] = period_counts.get(dino.period.value, 0) + 1
            diet_counts[dino.diet.value] = diet_counts.get(dino.diet.value, 0) + 1
            size_counts[dino.size.value] = size_counts.get(dino.size.value, 0) + 1
        
        lengths = [d.length_meters for d in dinosaurs]
        weights = [d.weight_kg for d in dinosaurs if d.weight_kg is not None]
        
        return {
            "total_dinosaurs": len(dinosaurs),
            "periods": period_counts,
            "diets": diet_counts,
            "sizes": size_counts,
            "average_length": sum(lengths) / len(lengths) if lengths else 0,
            "average_weight": sum(weights) / len(weights) if weights else 0
        }

# Global database instance
db = DinosaurDatabase()
