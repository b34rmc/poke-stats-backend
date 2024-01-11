from flask import request, Response, Blueprint

import controllers

pokemon = Blueprint('pokemon', __name__)

@pokemon.route("/pokemon", methods=["GET"])
def get_all_pokemon() -> Response:
    return controllers.get_all_pokemon(request)

@pokemon.route("/shiny-pokemon", methods=["GET"])
def get_all_shiny() -> Response:
    return controllers.get_all_shiny(request)

@pokemon.route("/pokemon/search", methods=["GET"])
def pokemon_get_by_search() -> Response:
    return controllers.pokemon_get_by_search(request)

@pokemon.route("/insert-pokemon", methods=["POST"])
def insert_new_pokemon() -> Response:
    return controllers.insert_new_pokemon(request)

@pokemon.route("/pokemon-images", methods=["POST"])
def insert_images() -> Response:
    return controllers.insert_image(request)