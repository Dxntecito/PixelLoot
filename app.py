from flask import Flask, session, redirect, url_for, request, render_template, flash, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from datetime import date
from bd import conectar
from controlador_juego import obtener_juegos
from controlador_juego import agregar_juego
import controlador_juego
from controlador_juego import obtener_juego_por_id
from controlador_juego import obtener_similares
from controlador_usuario import insertar_usuario,validar_usuario,obtener_datos_completos_usuario,obtener_paises_distintos, editar_informacion
import pymysql.cursors 

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'


# Página principal
@app.route("/")
def index():
    return render_template("index.html")


# Rutas del menú principal
@app.route('/tienda')
def tienda():
    juegos = obtener_juegos()
    return render_template('tienda.html', juegos=juegos)

@app.route("/sobre-nosotros")
def sobre_nosotros():
    return render_template("sobre-nosotros.html")


@app.route("/soporte")
def soporte():
    return render_template("soporte.html")

@app.route('/perfil')
def perfil():
    if "usuario_id" not in session:
        return redirect(url_for("iniciar_sesion"))
    
    datos_completos = obtener_datos_completos_usuario(session["usuario_id"])
    paises = obtener_paises_distintos()
    print(f"Lista de países: {paises}")
    if not datos_completos:
        return render_template("perfil.html", usuario=None, tarjetas=[],paises=paises)

    # Usuario (solo una vez)
    usuario = {
        "username": datos_completos[0]["nombre_usuario"],
        "nombre": datos_completos[0]["nombre_real"],
        "genero": datos_completos[0]["genero"],
        "correo": datos_completos[0]["correo"],
        "password": datos_completos[0]["contraseña"],
        "telefono": datos_completos[0]["telefono"],
         "pais": datos_completos[0]["pais"] 
    }

    # Tarjetas asociadas
    tarjetas = [
        {
            "id_tarjeta": t.get("id_tarjeta"),
            "numero_tarjeta": t.get("numero_tarjeta")
        }
        for t in datos_completos if t["id_tarjeta"] is not None
    ]

    return render_template("perfil.html", usuario=usuario, tarjetas=tarjetas)

@app.route('/cerrar_sesion')
def cerrar_sesion():
    session.clear()  # elimina todos los datos de sesión
    return redirect(url_for('iniciar_sesion'))

@app.route("/carrito")
def carrito():
    return render_template("carrito.html")

@app.route("/iniciar-sesion", methods=["GET", "POST"])
def iniciar_sesion():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        # Imprimir los valores para verificar que se reciben correctamente
        print(f"Usuario: {username}")
        print(f"Contraseña: {password}")

        # Verificar que ambos campos estén presentes
        if not username or not password:
            error = "Por favor, ingrese ambos campos."
            return render_template("iniciar-sesion.html", error=error)
        
        # Aquí verificamos el usuario y la contraseña
        usuario = validar_usuario(username, password)
        
        if usuario and "id_usuario" in usuario:
            session["usuario_id"] = usuario["id_usuario"]  # Guardar la sesión del usuario
            return redirect(url_for("perfil"))  # Redirigir a la página principal
        else:
            error = "Credenciales incorrectas"
            return render_template("iniciar-sesion.html", error=error)

    return render_template("iniciar-sesion.html")

#Ruta editar perfil :v
@app.route("/editar_perfil", methods=["POST"])
def editar_perfil():
    data = request.get_json()

    try:
        # Asegúrate que el usuario esté autenticado
        if "usuario_id" not in session:
            return jsonify({"success": False, "message": "Usuario no autenticado."}), 401

        editar_informacion(
            id_usuario=session["usuario_id"],
            nombre_usuario=data.get("username"),
            nombre_real=data.get("nombre"),
            correo=data.get("correo"),
            genero=data.get("genero"),
            contraseña=data.get("password"),
            telefono=data.get("telefono"),
            pais=data.get("pais"),
            fecha_nacimiento=data.get("fecha_nacimiento", "2000-01-01"),  # predeterminado si no lo envías
            rolid_rol=1,  # si el rol no cambia, puedes dejarlo fijo
            foto_perfil="",  # si aún no manejas imágenes
            foto_portada=""
        )
        return jsonify({"success": True, "message": "Perfil actualizado correctamente ✅"})

    except Exception as e:
        print(f"Error actualizando perfil: {e}")
        return jsonify({"success": False, "message": f"Error al actualizar perfil: {e}"}), 500

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

@app.route("/categoria/accion")
def categoria_accion():
    return render_template("Accion.html")

@app.route("/categoria/aventura")
def categoria_aventura():
    return render_template("Aventura.html")

@app.route("/categoria/retro")
def categoria_retro():
    return render_template("Retro.html")

@app.route("/categoria/terror")
def categoria_terror():
    return render_template("Terror.html")

@app.route("/categoria/rol")
def categoria_rol():
    return render_template("Rol.html")

@app.route("/categoria/sandbox")
def categoria_sandbox():
    return render_template("Sandbox.html")

@app.route("/contactanos")
def contactanos():
    return render_template("contactanos.html")

@app.route("/historial-compras")
def historial_compras():
    return render_template("historial-compras.html")

@app.route('/agregar_a_favoritos/<int:juego_id>', methods=['POST'])
def agregar_a_favoritos(juego_id):
    if 'usuario_id' not in session:
        flash('Debes iniciar sesión para añadir a favoritos.')
        return redirect(url_for('iniciar_sesion'))

    usuario_id = session['usuario_id']
    conn = conectar()
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT * FROM favorito WHERE usuariosid_usuario = %s AND juegoid = %s
            """, (usuario_id, juego_id))
            existente = cursor.fetchone()

            if not existente:
                cursor.execute("""
                    INSERT INTO favorito (usuariosid_usuario, juegoid)
                    VALUES (%s, %s)
                """, (usuario_id, juego_id))
                conn.commit()

        flash('Juego agregado a Favoritos.')
        return redirect(url_for('detalle_juego', id_juego=juego_id))
    finally:
        conn.close()

@app.route('/lista-deseos', methods=['GET', 'POST'])
def lista_deseos():
    if 'usuario_id' not in session:
        return redirect(url_for('iniciar_sesion'))

    usuario_id = session['usuario_id']
    conn = conectar()

    try:
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:

            # Si vienen datos por POST (eliminar o añadir al carrito)
            if request.method == 'POST':
                action = request.form.get("action")
                juego_id = request.form.get("product_id")

                if action == "remove":
                    cursor.execute("""
                        DELETE FROM favorito 
                        WHERE usuariosid_usuario = %s AND juegoid = %s
                    """, (usuario_id, juego_id))
                    conn.commit()

                elif action == "add_to_cart":
                    # Obtener o crear carrito
                    cursor.execute("SELECT id_carrito FROM carrito WHERE usuariosid_usuario = %s", (usuario_id,))
                    carrito = cursor.fetchone()

                    if not carrito:
                        cursor.execute("""
                            INSERT INTO carrito (fecha, usuariosid_usuario) 
                            VALUES (%s, %s)
                        """, (date.today(), usuario_id))
                        conn.commit()
                        carrito_id = cursor.lastrowid
                    else:
                        carrito_id = carrito["id_carrito"]

                    # Verificar si el producto ya está en el carrito
                    cursor.execute("""
                        SELECT cantidad 
                        FROM detalle_carrito 
                        WHERE juegoid = %s AND carritoid_carrito = %s
                    """, (juego_id, carrito_id))
                    detalle = cursor.fetchone()

                    if detalle:
                        nueva_cantidad = detalle["cantidad"] + 1
                        cursor.execute("""
                            UPDATE detalle_carrito 
                            SET cantidad = %s 
                            WHERE juegoid = %s AND carritoid_carrito = %s
                        """, (nueva_cantidad, juego_id, carrito_id))
                    else:
                        cursor.execute("""
                            INSERT INTO detalle_carrito (juegoid, carritoid_carrito, cantidad)
                            VALUES (%s, %s, 1)
                        """, (juego_id, carrito_id))
                    conn.commit()

            # Obtener favoritos actualizados
            cursor.execute("""
                SELECT j.id AS product_id, j.nombre, j.precio, j.imagen
                FROM favorito f
                JOIN juego j ON f.juegoid = j.id
                WHERE f.usuariosid_usuario = %s
            """, (usuario_id,))
            favoritos = cursor.fetchall()

        return render_template("lista-deseos.html", wishlist=favoritos)

    finally:
        conn.close()


@app.route("/ruleta-game")
def ruleta_game():
    return render_template("ruleta-game.html")


@app.route("/registrar-usuario", methods=["GET","POST"])
def registrar_usuario():
    if request.method == "POST":
        usuario = request.form.get("username-user")
        nombre = request.form.get("name")
        password = request.form.get("password")
        email = request.form.get("email")
        telefono = request.form.get("phone")
        country = request.form.get("country")
        birth_date = request.form["birth_date"]
        gender = request.form["gender"]
        rolid_rol = 1  # Si hay un valor fijo para el rol, ajusta esto según sea necesario
        foto_perfil = "static/imagenes/MenuPrincipalyPerfil/perfil.jpg"  # O usa un valor predeterminado
        foto_portada = "static/imagenes/MenuPrincipalyPerfil/fondoPerfilAuto.jpg"  # O usa un valor predeterminado
        insertar_usuario(usuario,nombre,email,gender,password,telefono,country,birth_date,rolid_rol,foto_perfil,foto_portada)
        juegos= obtener_juegos()
        return render_template("tienda.html",juegos=juegos)
    else:
        return render_template("registrar-usuario.html")

@app.route("/perdida-contrasena")
def perdida_contrasena():
    return render_template("perdida-contrasena.html")

@app.route("/confirmar-compra")
def confirmar_compra():
    if not current_user.is_authenticated:
        return redirect(url_for("iniciar_sesion"))
    return render_template("confirmarCompra.html")

@app.route('/producto/god-of-war-artbook')
def god_of_war_artbook():
    return render_template('prd-godA.html')

@app.route('/producto/god-of-war-deluxe')
def god_of_war_deluxe():
    return render_template('prd-godD.html')

@app.route('/producto/resident-evil-2-deluxe')
def resident_evil_2_deluxe():
    return render_template('prd-residentevil2D.html')

@app.route('/producto/resident-evil-4-gold')
def resident_evil_4_gold():
    return render_template('prd-residentevil4G.html')


# LO QUE ESTÁ HACIENDO SMAILLIPENE

@app.route('/agregar_juego', methods=['GET', 'POST'])
def ruta_agregar():
    if request.method == 'POST':
        resultado = agregar_juego(request)
        return redirect(url_for('Menu_PolloFrito'))
    return render_template('agregar_juego.html')



@app.route('/producto/<int:id_juego>')
def detalle_juego(id_juego):
    juego = obtener_juego_por_id(id_juego)
    similares = obtener_similares(juego[0])  # <-- función nueva
    return render_template('producto.html', juego=juego, similares=similares)


@app.route("/Menu_PolloFrito")
def Menu_PolloFrito():
    Menu_PolloFrito = controlador_juego.listar_juegos()
    return render_template("Menu_PolloFrito.html", Menu_PolloFrito=Menu_PolloFrito)

@app.route("/eliminar_juego", methods=["POST"])
def eliminar_juego():
    controlador_juego.eliminar_juego(request.form["id"])
    return redirect("/Menu_PolloFrito")


if __name__ == "__main__":
    app.run(debug=True)