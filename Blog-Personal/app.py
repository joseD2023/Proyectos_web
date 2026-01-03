from flask import Flask, render_template, request
from pymongo import MongoClient
import datetime


app = Flask(__name__)


cliente = MongoClient("mongodb+srv://Delarosa_BD_Mongo:DelarosaJose2004Usac@mongobasedatos.ztbtilc.mongodb.net/")
app.db = cliente.blog_personal

entradas = [entrada for entrada in app.db.entradas.find({})]


@app.route("/", methods=["GET", "POST"]) 
def home(): 
    if request.method == "POST": 
        titulo = request.form.get("tit")
        contenido = request.form.get("content")
        fecha_formato = datetime.datetime.today().strftime("%d-%m-%Y")
        json = {"titulo": titulo, "contenido":contenido, "fecha":fecha_formato}
        entradas.append(json)
        app.db.entradas.insert_one(json)

    return render_template("index.html", entradas = entradas)


if __name__ == "__main__":
    app.run(debug=True)