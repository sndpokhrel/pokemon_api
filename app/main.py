from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import pokemon
from app.db.database import engine, Base

app = FastAPI()


# Define CORS policies
origins = [
    "http://127.0.0.1:5500",  # Adjust this to match your frontend origin
    "http://localhost:5500",  # Additional origins can be added here
]

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(pokemon.router, prefix="/api/v1")
