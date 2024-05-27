from flask import render_template, redirect, Flask

app = Flask(__name__)

@app.route("/")
def index():
    return redirect("/login")

@app.route("/login")
def login():
    return render_template("login/index.html")
