# 🦕 Dinosaur API

A comprehensive REST API for managing dinosaur data, built with FastAPI. Perfect for educational applications, games, museums, or any project that needs dinosaur information!

## Features

- **Complete CRUD Operations**: Create, read, update, and delete dinosaurs
- **Advanced Filtering**: Filter by period, diet, and size
- **Search Functionality**: Search dinosaurs by name, species, or description
- **Pagination Support**: Efficient data loading with pagination
- **Data Validation**: Robust input validation using Pydantic models
- **Interactive Documentation**: Auto-generated API docs with Swagger UI
- **CORS Enabled**: Ready for frontend integration
- **Statistics Endpoint**: Get insights about your dinosaur database

## Quick Start

### Installation

1. Clone or create the project directory
2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the API

Start the development server:
```bash
uvicorn main:app --reload
```

The API will be available at:
- **API Base URL**: http://localhost:8000
- **Interactive Docs**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc

## API Endpoints

### Core Dinosaur Operations

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message and API info |
| GET | `/dinosaurs` | Get all dinosaurs (with filtering & pagination) |
| GET | `/dinosaurs/{id}` | Get a specific dinosaur by ID |
| POST | `/dinosaurs` | Create a new dinosaur |
| PUT | `/dinosaurs/{id}` | Update an existing dinosaur |
| DELETE | `/dinosaurs/{id}` | Delete a dinosaur |

### Search & Discovery

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/dinosaurs/search/?q={query}` | Search dinosaurs by name, species, or description |
| GET | `/stats` | Get database statistics and insights |

### Reference Data

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/periods` | Get all geological periods |
| GET | `/diets` | Get all diet types |
| GET | `/sizes` | Get all size categories |
| GET | `/health` | Health check endpoint |

## Data Models

### Dinosaur Properties

- **id**: Unique identifier (auto-generated)
- **name**: Common name (e.g., "Tyrannosaurus Rex")
- **species**: Scientific name (e.g., "Tyrannosaurus rex")
- **period**: Geological period (Triassic, Jurassic, Cretaceous)
- **diet**: Diet type (Herbivore, Carnivore, Omnivore)
- **size**: Size category (Small, Medium, Large, Massive)
- **length_meters**: Length in meters
- **weight_kg**: Weight in kilograms (optional)
- **description**: Detailed description
- **discovered_year**: Year of discovery (optional)
- **location_found**: Discovery location (optional)

## Example Usage

### Get All Dinosaurs
```bash
curl "http://localhost:8000/dinosaurs"
```

### Filter by Period and Diet
```bash
curl "http://localhost:8000/dinosaurs?period=Cretaceous&diet=Carnivore"
```

### Search for Dinosaurs
```bash
curl "http://localhost:8000/dinosaurs/search/?q=rex"
```

### Create a New Dinosaur
```bash
curl -X POST "http://localhost:8000/dinosaurs" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Spinosaurus",
    "species": "Spinosaurus aegyptiacus",
    "period": "Cretaceous",
    "diet": "Carnivore",
    "size": "Massive",
    "length_meters": 15.0,
    "weight_kg": 7400,
    "description": "A large carnivorous dinosaur with a distinctive sail on its back."
  }'
```

### Update a Dinosaur
```bash
curl -X PUT "http://localhost:8000/dinosaurs/1" \
  -H "Content-Type: application/json" \
  -d '{
    "description": "Updated description with new fossil evidence."
  }'
```

## Pre-loaded Data

The API comes with 8 famous dinosaurs pre-loaded:

1. **Tyrannosaurus Rex** - The king of dinosaurs
2. **Triceratops** - Three-horned herbivore
3. **Brachiosaurus** - Long-necked giant
4. **Velociraptor** - Intelligent pack hunter
5. **Stegosaurus** - Spiked herbivore
6. **Allosaurus** - Jurassic predator
7. **Diplodocus** - Extremely long sauropod
8. **Parasaurolophus** - Musical duck-billed dinosaur

## Frontend Integration

The API is designed to be frontend-friendly:

- **CORS enabled** for cross-origin requests
- **Consistent JSON responses**
- **Proper HTTP status codes**
- **Detailed error messages**
- **Pagination support** for large datasets

### Example Frontend Usage (JavaScript)

```javascript
// Fetch all dinosaurs
const response = await fetch('http://localhost:8000/dinosaurs');
const data = await response.json();
console.log(data.dinosaurs);

// Search for dinosaurs
const searchResponse = await fetch('http://localhost:8000/dinosaurs/search/?q=carnivore');
const searchResults = await searchResponse.json();

// Create a new dinosaur
const newDinosaur = await fetch('http://localhost:8000/dinosaurs', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    name: 'Carnotaurus',
    species: 'Carnotaurus sastrei',
    period: 'Cretaceous',
    diet: 'Carnivore',
    size: 'Large',
    length_meters: 8.0,
    description: 'A fast-running carnivore with horns above its eyes.'
  })
});
```

## Production Deployment

For production deployment, consider:

1. **Use a production ASGI server**: Gunicorn with Uvicorn workers
2. **Configure CORS properly**: Set specific allowed origins
3. **Add authentication**: Implement API keys or OAuth
4. **Use a real database**: Replace in-memory storage with PostgreSQL/MongoDB
5. **Add rate limiting**: Prevent API abuse
6. **Set up monitoring**: Health checks and logging

### Example Production Command
```bash
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

## Contributing

Feel free to extend this API with additional features:
- User authentication
- Image upload for dinosaurs
- Fossil location mapping
- Timeline visualization data
- More detailed taxonomy information

## License

This project is open source and available under the MIT License.
# dinosaur-api
