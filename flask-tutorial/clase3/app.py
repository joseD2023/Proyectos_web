from flask import Flask, render_template

app = Flask(__name__)

@app.route("/condicionales")
def condicionales():
    return render_template("condicional.html", equipo="inter milan")



if __name__ == "__main__":
    app.run(debug=True)