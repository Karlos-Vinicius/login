from flask import render_template, redirect, Flask, request


from . import db


app = Flask(__name__)
db = db.DataBase()


@app.route("/")
def index():
    return redirect("/singin")

@app.route("/cadastro", methods=["POST", "GET"])
def cadastro():
    if request.method == "POST":
        db.init()
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        rpassword = request.form.get("rpassword")

        print(name, email, password, rpassword)

        print((not email) == (not name) == (not password) == (not rpassword))

        if not name and not email and not password and not rpassword:
            return redirect("/fail")
        
        if password != rpassword:
            return redirect("/fail")
        
        db.cadastrar_pessoa(name=name, email=email, password=password)

        db.close()

        return redirect("/certo")
    
    return render_template("cadastro.html")


@app.route("/singin", methods=["POST", "GET"])
def singin():
    if request.method == "POST":
        db.init()
        email = request.form.get("email")
        password = request.form.get("password")

        rows = db.resgatar_usuario(email, password)
        print(rows)

        db.close()

        if len(rows) == 0:
            return redirect("/fail")

        return redirect("/certo")

    return render_template("login.html")


@app.route("/certo")
def certo():
    return render_template("certo.html")

@app.route("/fail")
def fail(): 
    return render_template("fail.html")
