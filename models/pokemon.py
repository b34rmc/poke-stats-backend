import marshmallow as ma

from db import db


class Pokemon(db.Model):
    __tablename__ = 'Pokemon'
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    name = db.Column(db.String(), nullable=False)
    front_default = db.Column(db.String(), nullable=True)
    front_shiny = db.Column(db.String(), nullable=True)
    additional_info = db.Column(db.String())
    
    def __init__(self, id, name, front_default, front_shiny, additional_info):
        self.id = id
        self.name = name
        self.front_default = front_default
        self.front_shiny = front_shiny
        self.additional_info = additional_info
    
    
class PokemonSchema(ma.Schema):
    class Meta:
        fields = ['id', 'name', 'front_default', 'front_shiny', 'additional_info']
        

pokemon_schema = PokemonSchema()
pokemons_schema = PokemonSchema(many=True)