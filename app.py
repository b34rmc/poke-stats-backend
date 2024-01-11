from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask import Flask
from flask_bcrypt import Bcrypt

from db import db, init_db
import os
import subprocess
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv

from models.pokemon import Pokemon

from lib.demo_data.demo_data import run_demo_data

from routes.pokemon_routes import pokemon

import config

load_dotenv()

database_pre = os.environ.get("DATABASE_PRE")
database_addr = os.environ.get("DATABASE_ADDR")
database_user = os.environ.get("DATABASE_USER")
database_port = os.environ.get("DATABASE_PORT")
database_name = os.environ.get("DATABASE_NAME")

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = f"{database_pre}{database_addr}:{database_port}/{database_name}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app, db)
ma = Marshmallow(app)

app.register_blueprint(pokemon)

def create_all():
    with app.app_context():
        print("Creating Tables")
        db.create_all()
        
        run_demo_data()
        

CORS(app)
bcrypt = Bcrypt(app)

if __name__ == '__main__':
    create_all()
    app.run(host="0.0.0.0", port=8089, debug=True)