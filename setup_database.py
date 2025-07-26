#!/usr/bin/env python3
"""
Database setup script for the Dinosaur API
This script will create the PostgreSQL database and tables
"""

import os
import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from dotenv import load_dotenv

def create_database():
    """Create the PostgreSQL database if it doesn't exist"""
    load_dotenv()
    
    # Parse DATABASE_URL to get connection details
    database_url = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost:5432/dinosaur_db")
    
    # Extract components from URL
    # Format: postgresql://username:password@host:port/database_name
    url_parts = database_url.replace("postgresql://", "").split("/")
    database_name = url_parts[1]
    host_part = url_parts[0].split("@")[1]
    user_pass = url_parts[0].split("@")[0]
    
    host, port = host_part.split(":")
    username, password = user_pass.split(":")
    
    print(f"Creating database '{database_name}' if it doesn't exist...")
    
    try:
        # Connect to PostgreSQL server (not to a specific database)
        conn = psycopg2.connect(
            host=host,
            port=port,
            user=username,
            password=password,
            database='postgres'  # Connect to default postgres database
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()
        
        # Check if database exists
        cursor.execute(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{database_name}'")
        exists = cursor.fetchone()
        
        if not exists:
            cursor.execute(f'CREATE DATABASE "{database_name}"')
            print(f"✅ Database '{database_name}' created successfully!")
        else:
            print(f"✅ Database '{database_name}' already exists.")
        
        cursor.close()
        conn.close()
        
    except psycopg2.Error as e:
        print(f"❌ Error creating database: {e}")
        return False
    
    return True

def create_tables():
    """Create tables using SQLAlchemy"""
    try:
        from db_config import create_tables as create_db_tables
        create_db_tables()
        print("✅ Database tables created successfully!")
        return True
    except Exception as e:
        print(f"❌ Error creating tables: {e}")
        return False

def populate_data():
    """Populate initial data"""
    try:
        from database_postgres import db
        print("✅ Initial data populated successfully!")
        return True
    except Exception as e:
        print(f"❌ Error populating data: {e}")
        return False

def main():
    """Main setup function"""
    print("🦕 Setting up Dinosaur API Database...")
    print("="*50)
    
    # Step 1: Create database
    if not create_database():
        sys.exit(1)
    
    # Step 2: Create tables
    if not create_tables():
        sys.exit(1)
    
    # Step 3: Populate initial data
    if not populate_data():
        sys.exit(1)
    
    print("="*50)
    print("🎉 Database setup completed successfully!")
    print("\nNext steps:")
    print("1. Make sure PostgreSQL is running")
    print("2. Install dependencies: pip install -r requirements.txt")
    print("3. Start the API: uvicorn main:app --reload")

if __name__ == "__main__":
    main()
