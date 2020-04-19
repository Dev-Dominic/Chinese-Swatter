# Python modules

import os

# from dotenv import load_dotenv # Loading environment variables from .env file
# load_dotenv()

# Flask modules

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Initial app setup

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') 

# Database config

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silences error messages

# Setup database instace of SQLAlchemy 
# and Migration creation of migration instance

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
db = SQLAlchemy(app)
migrate = Migrate(app, db)



from app import views, models # Loading views and models


