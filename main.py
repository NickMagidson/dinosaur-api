from fastapi import FastAPI, HTTPException, Query, Path
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, List
from models import (
    Dinosaur, DinosaurResponse, DinosaurPeriod, DinosaurDiet, DinosaurSize,
    DinosaurClade, DinosaurGroup, DinosaurLocomotion, DinosaurHabitat,
    FossilQuality, ErrorResponse
)
from database import db

# Create FastAPI app with metadata
app = FastAPI(
    title="Comprehensive Dinosaur API",
    description="A scientifically accurate read-only REST API for dinosaur data with detailed taxonomic, anatomical, and paleontological information based on Wikipedia sources.",
    version="2.0.0",
    contact={
        "name": "Dinosaur API Support",
        "email": "support@dinosaurapi.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    }
)

# Add CORS middleware to allow frontend connections
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Root"])
async def root():
    """Welcome endpoint with API information"""
    return {
        "message": "Welcome to the Comprehensive Dinosaur API! 🦕🦴",
        "description": "A scientific read-only API for dinosaur data with detailed taxonomic and paleontological information",
        "version": "2.0.0",
        "docs_url": "/docs",
        "features": [
            "Comprehensive taxonomic classification",
            "Detailed physical characteristics",
            "Geological time periods",
            "Discovery and fossil information",
            "Advanced filtering capabilities"
        ],
        "endpoints": {
            "get_all_dinosaurs": "/dinosaurs",
            "get_dinosaur_by_id": "/dinosaurs/{id}",
            "search_dinosaurs": "/dinosaurs/search",
            "get_statistics": "/stats",
            "get_periods": "/periods",
            "get_clades": "/clades",
            "get_groups": "/groups",
            "get_diets": "/diets",
            "get_sizes": "/sizes",
            "get_locomotion_types": "/locomotion",
            "get_habitats": "/habitats"
        }
    }

@app.get("/dinosaurs", response_model=DinosaurResponse, tags=["Dinosaurs"])
async def get_dinosaurs(
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(100, ge=1, le=1000, description="Maximum number of records to return"),
    period: Optional[DinosaurPeriod] = Query(None, description="Filter by geological period"),
    diet: Optional[DinosaurDiet] = Query(None, description="Filter by diet type"),
    size: Optional[DinosaurSize] = Query(None, description="Filter by size category"),
    clade: Optional[DinosaurClade] = Query(None, description="Filter by dinosaur clade"),
    group: Optional[DinosaurGroup] = Query(None, description="Filter by taxonomic group"),
    locomotion: Optional[DinosaurLocomotion] = Query(None, description="Filter by locomotion type"),
    habitat: Optional[DinosaurHabitat] = Query(None, description="Filter by habitat type"),
    fossil_quality: Optional[FossilQuality] = Query(None, description="Filter by fossil quality"),
    min_length: Optional[float] = Query(None, ge=0, description="Minimum length in meters"),
    max_length: Optional[float] = Query(None, ge=0, description="Maximum length in meters"),
    min_age: Optional[float] = Query(None, ge=0, description="Minimum age in millions of years ago"),
    max_age: Optional[float] = Query(None, ge=0, description="Maximum age in millions of years ago")
):
    """Get all dinosaurs with comprehensive filtering and pagination options"""
    dinosaurs = db.get_all(
        skip=skip, 
        limit=limit, 
        period=period, 
        diet=diet, 
        size=size,
        clade=clade,
        group=group,
        locomotion=locomotion,
        habitat=habitat,
        fossil_quality=fossil_quality,
        min_length=min_length,
        max_length=max_length,
        min_age=min_age,
        max_age=max_age
    )
    total = len(db.get_all(
        period=period, 
        diet=diet, 
        size=size,
        clade=clade,
        group=group,
        locomotion=locomotion,
        habitat=habitat,
        fossil_quality=fossil_quality,
        min_length=min_length,
        max_length=max_length,
        min_age=min_age,
        max_age=max_age
    ))
    
    return DinosaurResponse(
        dinosaurs=dinosaurs,
        total=total,
        page=skip // limit + 1,
        per_page=limit
    )

@app.get("/dinosaurs/{dinosaur_id}", response_model=Dinosaur, tags=["Dinosaurs"])
async def get_dinosaur(
    dinosaur_id: int = Path(..., description="The ID of the dinosaur to retrieve", gt=0)
):
    """Get a specific dinosaur by ID"""
    dinosaur = db.get_by_id(dinosaur_id)
    if not dinosaur:
        raise HTTPException(
            status_code=404, 
            detail=f"Dinosaur with ID {dinosaur_id} not found"
        )
    return dinosaur

@app.get("/dinosaurs/search/", response_model=List[Dinosaur], tags=["Search"])
async def search_dinosaurs(
    q: str = Query(..., description="Search query for dinosaur names, species, or descriptions", min_length=1)
):
    """Search dinosaurs by name, species, or description"""
    results = db.search(q)
    return results

@app.get("/stats", tags=["Statistics"])
async def get_statistics():
    """Get database statistics and insights"""
    stats = db.get_stats()
    return {
        "database_stats": stats,
        "api_info": {
            "total_endpoints": 12,
            "version": "2.0.0",
            "type": "Read-only scientific database",
            "last_updated": "2025-01-24"
        }
    }

@app.get("/periods", response_model=List[str], tags=["Reference Data"])
async def get_periods():
    """Get all available geological periods"""
    return [period.value for period in DinosaurPeriod]

@app.get("/clades", response_model=List[str], tags=["Reference Data"])
async def get_clades():
    """Get all available dinosaur clades"""
    return [clade.value for clade in DinosaurClade]

@app.get("/groups", response_model=List[str], tags=["Reference Data"])
async def get_groups():
    """Get all available taxonomic groups"""
    return [group.value for group in DinosaurGroup]

@app.get("/diets", response_model=List[str], tags=["Reference Data"])
async def get_diets():
    """Get all available diet types"""
    return [diet.value for diet in DinosaurDiet]

@app.get("/sizes", response_model=List[str], tags=["Reference Data"])
async def get_sizes():
    """Get all available size categories"""
    return [size.value for size in DinosaurSize]

@app.get("/locomotion", response_model=List[str], tags=["Reference Data"])
async def get_locomotion_types():
    """Get all available locomotion types"""
    return [locomotion.value for locomotion in DinosaurLocomotion]

@app.get("/habitats", response_model=List[str], tags=["Reference Data"])
async def get_habitats():
    """Get all available habitat types"""
    return [habitat.value for habitat in DinosaurHabitat]

@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint for monitoring"""
    return {
        "status": "healthy",
        "timestamp": "2025-07-24",
        "database_status": "connected",
        "total_dinosaurs": db.get_stats()["total_dinosaurs"]
    }