import time
from flask import jsonify
import flask
import requests
from db import db
from models.pokemon import Pokemon, pokemon_schema, pokemons_schema
from models.shiny_pokemon import ShinyPokemon, shiny_pokemon_schema, shiny_pokemons_schema

from insert_pokemon import insert_pokemon_images


def get_all_pokemon(req: flask.Request) -> flask.Response:
    pokemon = db.session.query(Pokemon).order_by(Pokemon.id.asc()).all()
    
    if pokemon:
        return jsonify({"Results": len(pokemon), "pokemon": pokemons_schema.dump(pokemon)}), 200
    
    return jsonify("no pokemon found"), 404


def get_all_shiny(req: flask.Request) -> flask.Response:
    shiny_pokemon = db.session.query(ShinyPokemon).order_by(ShinyPokemon.id.asc()).all()
    
    if shiny_pokemon:
        return jsonify({"Results": len(shiny_pokemon), "pokemon": shiny_pokemons_schema.dump(shiny_pokemon)}), 200
    
    return jsonify("no shiny pokemon found"), 404


def pokemon_get_by_search(req: flask.Request) -> flask.Response:
    search_term = req.args.get('q').lower()
    
    pokemon_query = db.session.query(Pokemon).filter(db.func.lower(Pokemon.name).contains(search_term))
    pokemon_data = pokemon_query.order_by(Pokemon.name.asc()).all()
    
    return jsonify({"message": "pokemon found", "results": pokemons_schema.dump(pokemon_data)}), 200


def insert_new_pokemon(req: flask.Request) -> flask.Response:
    request_url = "https://pokeapi.co/api/v2/pokemon?offset=0&limit=1302"
    response = requests.get(request_url)
    data = response.json()

    # Iterate over the results and insert into the database
    for result in data.get("results", []):
        pokemon_id = int(result["url"].split("/")[-2])
        pokemon_name = result["name"]
        pokemon_url = result["url"]

        # Create a Pokemon instance and insert into the database
        pokemon = Pokemon(id=pokemon_id, name=pokemon_name, front_default="", front_shiny="", additional_info=pokemon_url)
        db.session.add(pokemon)

    # Commit the changes to the database
    db.session.commit()
    return jsonify({"message": "Pokemon data inserted successfully"}), 200


def insert_image(req: flask.Request) -> flask.Response:
    all_pokemon = db.session.query(Pokemon).order_by(Pokemon.id.asc()).all()
    
    for pokemon in all_pokemon:
        insert_pokemon_images(pokemon.id)
        time.sleep(2)
        
    return jsonify({"message": "pokemon images updated"})