import marshmallow as ma

from db import db


class ShinyPokemon(db.Model):
    __tablename__ = 'ShinyPokemon'
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    name = db.Column(db.String(), nullable=False)
    found_egg = db.Column(db.Boolean, nullable=False)
    found_evolution = db.Column(db.Boolean, nullable=False)
    found_photobomb = db.Column(db.Boolean, nullable=False)
    found_raid = db.Column(db.Boolean, nullable=False)
    found_research = db.Column(db.Boolean, nullable=False)
    found_wild = db.Column(db.Boolean, nullable=False)
    front_default = db.Column(db.String(), nullable=True)
    front_shiny = db.Column(db.String(), nullable=True)
    additional_info = db.Column(db.String())
    
        
    def __init__(self, id, name, found_egg, found_evolution, found_photobomb, found_raid, found_research, found_wild, front_default, front_shiny, additional_info):
        self.id = id
        self.name = name
        self.found_egg = found_egg
        self.found_evolution = found_evolution
        self.found_photobomb = found_photobomb
        self.found_raid = found_raid
        self.found_research = found_research
        self.found_wild = found_wild
        self.front_default = front_default
        self.front_shiny = front_shiny
        self.additional_info = additional_info
    
    
class ShinyPokemonSchema(ma.Schema):
    class Meta:
        fields = ['id', 'name', 'found_egg', 'found_evolution', 'found_photobomb', 'found_raid', 'found_research', 'found_wild', 'front_default', 'front_shiny', 'additional_info']
        

shiny_pokemon_schema = ShinyPokemonSchema()
shiny_pokemons_schema = ShinyPokemonSchema(many=True)

# sprites.other.official-artwork.front_default
# sprites.other.official-artwork.front_shiny