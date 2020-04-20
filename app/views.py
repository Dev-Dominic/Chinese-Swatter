from flask import render_template
from app import app,db
from app.models import Character

@app.route('/')
@app.route('/home')
@app.route('/practice')
def practice(): 
    character_one = Character.query.all()
    return render_template('base.html', characters=character_one)

@app.route('/about')
def about(): 
    return 'about'
