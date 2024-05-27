from flask import render_template, redirect, Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return redirect("/cadastro")

@app.route("/cadastro", methods=["POST", "GET"])
def cadastro():
    if request.method == "GET":
        return render_template("cadastro.html")
    return redirect("/certo")

@app.route("/certo")
def certo():
    return render_template("certo.html")