# 🦕 Dinosaur API

A comprehensive REST API for managing dinosaur data, built with FastAPI and PostgreSQL. Perfect for educational apps, games, or any project that needs dinosaur information!

## 🚀 Features

- **Comprehensive Dinosaur Database**: Detailed information about various dinosaur species
- **Advanced Filtering**: Filter by period, diet, size, habitat, and more
- **PostgreSQL Integration**: Robust database with full ACID compliance
- **RESTful API**: Clean, intuitive endpoints
- **Interactive Documentation**: Automatic API docs with Swagger UI
- **Fast Performance**: Built with FastAPI for high performance

## 🛠️ Setup Instructions

### Prerequisites

- Python 3.8+
- PostgreSQL 12+ (or Docker for easy setup)
- pip (Python package manager)

### Option 1: Using Docker (Recommended)

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd dinosaur-api
   ```

2. **Start PostgreSQL with Docker**
   ```bash
   docker-compose up -d
   ```

3. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**
   ```bash
   python setup_database.py
   ```

5. **Start the API**
   ```bash
   uvicorn main:app --reload
   ```

### Option 2: Using Local PostgreSQL

1. **Install PostgreSQL** on your system

2. **Create a database**
   ```sql
   CREATE DATABASE dinosaur_db;
   ```

3. **Update environment variables**
   Edit the `.env` file with your PostgreSQL credentials:
   ```
   DATABASE_URL=postgresql://your_username:your_password@localhost:5432/dinosaur_db
   ```

4. **Install dependencies and setup**
   ```bash
   pip install -r requirements.txt
   python setup_database.py
   ```

5. **Start the API**
   ```bash
   uvicorn main:app --reload
   ```

## 📚 API Documentation

Once the server is running, visit:
- **Interactive Docs**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **API Health**: http://localhost:8000/health

## 🔗 API Endpoints

### Core Endpoints
- `GET /` - API information and welcome message
- `GET /dinosaurs` - Get all dinosaurs (with filtering and pagination)
- `GET /dinosaurs/{id}` - Get a specific dinosaur by ID
- `GET /dinosaurs/search/` - Search dinosaurs by name or description

### Reference Data
- `GET /periods` - Get all geological periods
- `GET /clades` - Get all dinosaur clades
- `GET /groups` - Get all taxonomic groups
- `GET /diets` - Get all diet types
- `GET /sizes` - Get all size categories
- `GET /locomotion` - Get all locomotion types
- `GET /habitats` - Get all habitat types

### Statistics
- `GET /stats` - Get database statistics
- `GET /health` - Health check endpoint

## 🔍 Example Usage

### Get all dinosaurs
```bash
curl http://localhost:8000/dinosaurs
```

### Filter dinosaurs by period
```bash
curl "http://localhost:8000/dinosaurs?period=Late Cretaceous"
```

### Search for dinosaurs
```bash
curl "http://localhost:8000/dinosaurs/search/?q=tyrannosaurus"
```

### Get specific dinosaur
```bash
curl http://localhost:8000/dinosaurs/1
```

## 🗄️ Database Schema

The PostgreSQL database includes a comprehensive `dinosaurs` table with:
- **Basic Info**: Name, species, genus
- **Temporal Data**: Geological period, age ranges
- **Physical Characteristics**: Size, weight, dimensions
- **Taxonomic Classification**: Clade, group, family
- **Behavioral Data**: Diet, locomotion, habitat
- **Discovery Information**: Year, discoverer, location
- **Additional Features**: Special characteristics, interesting facts

## 🛡️ Environment Variables

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/dinosaur_db
```

## 🧪 Development

### Running Tests
```bash
pytest tests/
```

### Code Formatting
```bash
black .
flake8 .
```

### Database Migrations
The database schema is automatically created when you run the setup script. For production deployments, consider using Alembic for database migrations.

## 📦 Dependencies

- **FastAPI**: Modern web framework
- **SQLAlchemy**: SQL toolkit and ORM
- **psycopg2-binary**: PostgreSQL adapter
- **python-dotenv**: Environment variable management
- **uvicorn**: ASGI server

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🦴 Data Sources

The dinosaur data in this API is compiled from various paleontological sources and scientific literature. All information is intended for educational purposes.

---

Made with 🦕 by the Dinosaur API team
