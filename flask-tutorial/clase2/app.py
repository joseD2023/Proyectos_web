from flask import Flask, render_template

app = Flask(__name__)

class pelicula: 
    def __init__(self, nombre, año, protagonista):
        self.nombre = nombre 
        self.año = año
        self.protagonista = protagonista


@app.route("/estructura")
def estructura_datos():

    #crear una lista de peliculas 
    peliculas = ["Avengers", "Harry Potter", "volver al futuro"] #esto va servir para pasar como parametros


    #ahora vamos a usar diccionario como una estructura de datos 
    lobo = {"Nombre":"El lobo de Wall Sreet", "año":2013, "protagonista": "Leonardo de caprio"} 


    #creamos un objeto de la clase pelicula 
    peli = pelicula("Toy Story", 2006, "Body y Buzz")


    return render_template("estructuras.html", movies = peliculas, destacada=lobo, nueva=peli) #le mandamos el nombre de la variable como parametro


if __name__ == "__main__":
    app.run(debug=True)


