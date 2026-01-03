from flask import Flask, render_template, request

app = Flask(__name__)
lista = []


@app.route("/", methods =["GET", "POST"]) #aqui le indicamos a flask que metodos htpp puede usar o aceptar  (por le formulario que tenemos usamos post)
def formulario():
    if request.method == "POST": #aqui basicamente estamos diciendo si un usuario suo el formulario y esta enviando informacion entonces nosotrs necesitamos tener que guardarlo o decirlo que si lo tomamos pero como la recibimos a traves del metodo request y la funcion form.get("aqui le vamos a pasar el nombre del input donde esta name= "nombre_que_dimos ")

        informacion_formulario = request.form.get("contenido") #en mi caso mi name="contenido"
        lista.append(informacion_formulario) #cada dato capturado es almacenado en un arrays 
        print(informacion_formulario) #aqui para verificar si esta funcionando

    return render_template("formulario.html", v = informacion_formulario, arrays = lista)


if __name__ == "__main__":
    app.run(debug=True)