from flask import Flask
from app import app

@app.route('/')
@app.route('/home')
@app.route('/practice')
def practice(): 
    return 'practice'

@app.route('/about')
def about(): 
    return 'about'
