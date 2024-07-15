# Pokémon API

This is a FastAPI project for serving a list of Pokémon with filtering capabilities.

## Setup Instructions

1. Create a virtual environment and install dependencies:
   python -m venv venv
   source venv/bin/activate

2. Initialize the database:
   python -m app.db.init_db

3. Run the application:
   uvicorn app.main:app --reload
   and run index.html

Package Used
fastapi
uvicorn
asyncpg
sqlalchemy[asyncio]
databases
psycopg2

1. Clone the repository:
   ```bash
   git clone https://github.com/sndpokhrel/pokemon_api.git
   cd pokemon_api
   ```
