from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.pokemon import Pokemon

async def get_pokemons(db: AsyncSession, name: str = None, types: str = None):
    query = select(Pokemon)
    if name:
        query = query.filter(Pokemon.name.ilike(f"%{name}%"))
    if types:
        query = query.filter(Pokemon.types.ilike(f"%{types}%"))
    result = await db.execute(query)
    return result.scalars().all()

async def create_pokemon(db: AsyncSession, pokemon: Pokemon):
    db.add(pokemon)
    await db.commit()
    await db.refresh(pokemon)
    return pokemon
