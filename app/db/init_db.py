import httpx
from app.db.database import SessionLocal
from app.models.pokemon import Pokemon
from app.crud.pokemon import create_pokemon
import asyncio
import traceback

POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon?limit=100"

async def init_db():
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(POKEAPI_URL)
            response.raise_for_status()
            data = response.json()
        except httpx.HTTPStatusError as exc:
            print(f"HTTP error occurred: {exc}")
            return
        except httpx.RequestError as exc:
            print(f"Request error occurred: {exc}")
            return
        
        async with SessionLocal() as db:
            for result in data['results']:
                try:
                    pokemon_data = await client.get(result['url'])
                    pokemon_data.raise_for_status()
                    pokemon_info = pokemon_data.json()
                    
                    types = [t['type']['name'] for t in pokemon_info.get('types', [])]
                    
                    pokemon = Pokemon(
                        name=pokemon_info['name'],
                        image=pokemon_info['sprites']['front_default'],
                        types=types
                    )
                    
                    await create_pokemon(db, pokemon)
                except httpx.HTTPStatusError as exc:
                    print(f"HTTP error occurred fetching Pokemon data: {exc}")
                except httpx.RequestError as exc:
                    print(f"Request error occurred fetching Pokemon data: {exc}")
                except Exception as exc:
                    print(f"Error occurred: {exc}")
                    traceback.print_exc()

if __name__ == "__main__":
    try:
        asyncio.run(init_db())
    except KeyboardInterrupt:
        print("Process interrupted by user.")
    except Exception as e:
        print(f"Error occurred: {e}")
