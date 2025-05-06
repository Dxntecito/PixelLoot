from flask import Flask, render_template
from bd import conectar 

app = Flask(__name__)

# Página principal
@app.route("/")
def index():
    return render_template("index.html")

# Rutas del menú principal
@app.route("/tienda")
def tienda():
    return render_template("tienda.html")

@app.route("/sobre-nosotros")
def sobre_nosotros():
    return render_template("sobre-nosotros.html")

@app.route("/soporte")
def soporte():
    return render_template("soporte.html")

# Rutas del menú de usuario
@app.route("/perfil")
def perfil():
    return render_template("perfil.html")

@app.route("/carrito")
def carrito():
    return render_template("carrito.html")

@app.route("/iniciar-sesion")
def iniciar_sesion():
    return render_template("iniciar-sesion.html")

# Rutas de productos individuales
@app.route("/producto/god-of-war")
def god_of_war():
    return render_template("prd-god.html")

@app.route("/producto/celeste")
def celeste():
    return render_template("prd-celeste.html")

@app.route("/producto/days-gone")
def days_gone():
    return render_template("prd-daysgone.html")

@app.route("/producto/dark-souls")
def dark_souls():
    return render_template("prd-darksouls.html")

@app.route("/producto/resident-evil-4")
def resident_evil_4():
    return render_template("prd-residentevil4.html")

@app.route("/producto/resident-evil-2")
def resident_evil_2():
    return render_template("prd-residentevil2.html")

if __name__ == "__main__":
    app.run(debug=True)