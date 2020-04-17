# Flask Config 
from flask import Flask
app = Flask(__name__)

print("hello world")

from app import views

