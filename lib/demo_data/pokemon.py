from db import db
from models.pokemon import Pokemon
import lib.demo_data.seed_data.pokemon_seed_data as seed_data


def add_pokemon():
    for pokemon in seed_data.pokemon_names.values():
        existing_pokemon = Pokemon.query.filter_by(name=pokemon["name"]).first()
        
        if existing_pokemon == None:
            new_pokemon = Pokemon(id=pokemon["id"], name=pokemon["name"])
            db.session.add(new_pokemon)
            
    db.session.commit()