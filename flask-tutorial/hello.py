from flask import Flask #flask es la parte principal permite crear nuestra propia app web 
from flask import render_template #esto nos va a servir para trabajar con los templates de las paginas rendeizas 

app = Flask(__name__)#crea la app @SpringBootApplication y SpringApplication.run()

@app.route("/") #es como un endpoints  y la funcion es uncontrolador que maneja la ruta y decide que va a mostrar el return es lo que envia al navegador (El decorador route de la aplicación (app) es el encargado de decirle a Flask qué URL debe ejecutar su correspondiente función.)
def hello():
    return "Hello World, Flask con Delarosa"

#vamos a retornar html para tener una forma mas elegante 

@app.route("/elegante")
def hola_mundo():
    return """
<html> 
<body> 
<h1> Saludos Elegantes de HTML <h1> 
<p>Hola Mundo Jose De La Rosa <p> 
</body> 
</html>
"""

@app.route("/html")
def mostrar_template():
    return render_template("primera_pagina.html") #entonces aqui colocamos el nombre de nuestro archivo de html para poder renderizar y asi trabajar


@app.route("/saludo")
def saludo():
    return "Hola amigos de la Web, Estoy ingresando en el aprendizaje de Flask"


@app.route("/variables")
def hola_nombre():
    return render_template("variable.html", nombre="Jose De la rosa", curso="Flask con Python")
#entonces trabajamos con los que son parametros para mandarlo al html y que se nos muestre es tipo django render(request, diccionario o valores que le queremos mostrar dentro de un html)



if __name__ == "__main__": #esto asegura que el servidore solo ejecute este archivo y no le importa los otrso scripts 
    app.run(debug=True) #app arranca al servidor como si fuera sprintAplicationrun  (debug=True recarga de manera automatica si hay cambios dentro del codigo no se tiene que que reiniciar manualmente muestra errores completos en el navegador si algo falla)

#Un script es simplemente un archivo de código que se ejecuta línea por línea. En Python, cualquier archivo .py puede ser un script.

#@app.route() define la ruta o URL donde tu función “controlador” va a responder. Es como decir: “cuando alguien entre a esta dirección, ejecuta esta función”