# Python modules

import os

# Flask modules

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Initial app setup

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('CHINESE_SWATTER_SECRET_KEY') 
app.config['DEBUG'] = os.environ.get('DEBUG')

# Database config

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import views, models


