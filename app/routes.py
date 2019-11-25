from app import app
from flask import render_template

user = {"username":"sziyan", "email":"sziyan@hotmail.com"}

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", user=user)

