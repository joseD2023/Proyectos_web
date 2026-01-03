from flask import Flask, render_template, request
from pymongo import MongoClient #libreria que le pertence a la base de datos de Mongo

app = Flask(__name__)

cliente = MongoClient("mongodb+srv://Delarosa_BD_Mongo:DelarosaJose2004Usac@mongobasedatos.ztbtilc.mongodb.net/") #con esto ya accedemos a nuestra base de datos 

app.db = cliente.ejemplo #vamos llamar a la base de datos ejemplo usamos el cliente osea la base de datos se llama ejemplo porque asi le pusimos cuando construimos nuestra base de datos en mongol

usuarios = [usuario for usuario in app.db.usuarios.find({})] #esta recorriendo los usuarios de la base de datos
print(usuarios)


@app.route("/", methods =["GET", "POST"]) 
def formulario():
    if request.method == "POST":

        informacion_formulario = request.form.get("contenido") #en mi caso mi name="contenido"

        parametros = {"nombres": informacion_formulario}

        app.db.usuarios.insert_one(parametros)
        usuarios.append(informacion_formulario) #cada dato capturado es almacenado en un arrays 


    return render_template("formulario.html", usuarios = usuarios)


if __name__ == "__main__":
    app.run(debug=True)