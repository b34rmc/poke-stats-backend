import json
import requests
from models.pokemon import Pokemon
# from models.shiny_pokemon import ShinyPokemon
from db import db

def insert_pokemon_images(pokemon_id):
    request_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(request_url)

    if response.status_code == 200:
        data = response.json()

        default_image_url = data.get('sprites', {}).get('other', {}).get('official-artwork', {}).get('front_default', None)
        shiny_image_url = data.get('sprites', {}).get('other', {}).get('official-artwork', {}).get('front_shiny', None)

        if default_image_url:
            print(f"Default Image URL for Pokemon {pokemon_id}: {default_image_url}")
            pokemon_to_update = Pokemon.query.get(pokemon_id)

            pokemon_to_update.front_default = default_image_url
        else:
            print(f"Default Image URL not found for Pokemon {pokemon_id}")

        if shiny_image_url:
            print(f"Shiny Image URL for Pokemon {pokemon_id}: {shiny_image_url}")
            pokemon_to_update.front_shiny = shiny_image_url
        else:
            print(f"Shiny Image URL not found for Pokemon {pokemon_id}")

        db.session.commit()
    else:
        print(f"Failed to retrieve data for Pokemon {pokemon_id}. Status code: {response.status_code}")
