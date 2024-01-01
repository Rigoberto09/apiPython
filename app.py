# app.py
# Desarollo de API usando Flask

# crear requerimientos de [pip freeze > requirements.txt]
# instalar todos los requermientos de la app.py [pip install -r requirements.txt]

# Correr el entorno virutal [./venv/Scripts/activate]
#Salir del entorno virtual [deactivate]

# correr la app [python app.py]
from flask import Flask, render_template



app = Flask(__name__)

# Inicio o ruta predeterminda a la carpeta de templates
@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)