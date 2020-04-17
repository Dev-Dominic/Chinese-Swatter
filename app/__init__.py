from flask import Flask
app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('CHINESE_SWATTER_SECRET_KEY') 

from app import views

