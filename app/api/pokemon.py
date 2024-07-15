from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.db.database import SessionLocal
from app.schemas.pokemon import Pokemon, PokemonCreate
from app.crud.pokemon import get_pokemons, create_pokemon

router = APIRouter()

async def get_db():
    async with SessionLocal() as session:
        yield session

@router.get("/pokemons", response_model=List[Pokemon])
async def read_pokemons(name: str = None, types: str = None, db: AsyncSession = Depends(get_db)):
    pokemons = await get_pokemons(db, name=name, types=types)
    return pokemons
