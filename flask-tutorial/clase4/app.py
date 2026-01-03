from flask import Flask, render_template

app = Flask(__name__)

@app.route("/for-loop")
def loop_for():

    #recorrer lista en el html (lista prueba)
    equipos = ["Real Madrid", "FC Barcelona", "Milan AC", "Liverpool", "Bayer Munich", "Ajax", "Inter Milan", "Juventus", "Manchester United"]

    #recorrer diccionario html (diccionario prueba)
    equipos_champ = {"Real Madrid": 15, "Mila":7, "Liverpool":6, "Bayern Múnich":6, "Barcelona":5, "Ajax":4, "Manchester United":3}
    return render_template("for_loop.html", teams = equipos, ganadores = equipos_champ) 


if __name__ == "main": 
    app.run(debug=True)
