from flask import Flask, render_template
import numpy as np
from joblib import load
import os 

# Cargar modelo
dt = load("dt1.joblib")

# Servidor
servidorWeb = Flask(__name__)

@servidorWeb.route("/holamundo", methods=['GET'])
def holamundo():
    return render_template("pagina1.html")

# Envio de datos
@servidorWeb.route("/modelo", methods=["POST"])
def modeloPrediccion():
    contenido = request.json
    return jsonfy({"resultado": "Hola"})
    

if __name__ == '__main__':
    servidorWeb.run(debug = False, host='0.0.0.0', port='8080')