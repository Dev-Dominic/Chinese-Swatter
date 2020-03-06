from app import app

@app.route("/")
def home(): 
    return "home"

@app.route("/about")
def about(): 
    return "about"
