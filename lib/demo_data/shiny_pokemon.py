from db import db
from models.shiny_pokemon import ShinyPokemon
import lib.demo_data.seed_data.shiny_pokemon_data as seed_data


def add_shiny_pokemon():
    for shiny_pokemon in seed_data.shiny_pokemon.values():
        existing_shiny = ShinyPokemon.query.filter_by(name=shiny_pokemon["name"]).first()
        
        if existing_shiny == None:
            new_shiny_pokemon = ShinyPokemon(
                id=shiny_pokemon["id"],
                name=shiny_pokemon["name"],
                found_egg=shiny_pokemon["found_egg"],
                found_evolution=shiny_pokemon["found_evolution"],
                found_photobomb=shiny_pokemon["found_photobomb"],
                found_raid=shiny_pokemon["found_raid"],
                found_research=shiny_pokemon["found_research"],
                found_wild=shiny_pokemon["found_wild"],
                front_default="",
                front_shiny="",
                additional_info=""
            )
            db.session.add(new_shiny_pokemon)

    db.session.commit()