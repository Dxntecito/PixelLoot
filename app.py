from flask import Flask, session, redirect, url_for, request, render_template, jsonify, flash
from flask_login import login_user, logout_user, login_required, current_user
from datetime import date

# Conexión a la base de datos
from bd import conectar

# Controladores de juegos
from controlador_juego import obtener_juegos, agregar_juego, obtener_juego_por_id, obtener_similares

# Controladores de usuario
from controlador_usuario import (
    insertar_usuario,
    validar_usuario,
    obtener_datos_completos_usuario,
    obtener_paises_distintos,
    editar_informacion
)

# Controladores de carrito
from controlador_carrito import (
    obtener_items_carrito,
    agregar_al_carrito,
    actualizar_cantidad_item,
    eliminar_item_carrito
)

# Controladores de tarjetas
from controlador_tarjeta import obtener_tarjetas_por_usuario



app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'


# Página principal
@app.route("/")
def index():
    print(url_for('carrito'))
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

@app.route("/lista-deseos")
def lista_deseos():
    return render_template("lista-deseos.html")

@app.route("/ruleta-game")
def ruleta_game():
    return render_template("ruleta-game.html")

@app.route("/tarjeta")
def tarjeta():
    return render_template("tarjeta.html")

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

@app.route("/confirmar-compra", methods=["GET", "POST"])
def confirmar_compra():
    if "usuario_id" not in session:
        return redirect(url_for("iniciar_sesion"))

    usuario_id = session["usuario_id"]

    if request.method == "POST":
        action = request.form.get("action")

        if action == "pay":
            tarjeta_id = session.get("tarjeta_seleccionada")
            if not tarjeta_id:
                flash("Debes seleccionar una tarjeta para pagar.", "warning")
                return redirect(url_for("confirmar_compra"))

            carrito = obtener_items_carrito(usuario_id)
            if not carrito:
                flash("Tu carrito está vacío.", "warning")
                return redirect(url_for("carrito"))

            subtotal = sum(item["precio"] * item["cantidad"] for item in carrito)
            descuento = round(subtotal * 0.10, 2)
            total = round(subtotal - descuento, 2)

            conexion = conectar()
            try:
                with conexion.cursor() as cursor:
                    cursor.execute("INSERT INTO venta (fecha) VALUES (CURDATE())")
                    id_venta = cursor.lastrowid

                    cursor.execute("SELECT id_carrito FROM carrito WHERE usuariosid_usuario = %s ORDER BY id_carrito DESC LIMIT 1", (usuario_id,))
                    carrito_data = cursor.fetchone()

                    if not carrito_data:
                        flash("No se encontró un carrito válido.", "danger")
                        return redirect(url_for("carrito"))

                    id_carrito = carrito_data[0]

                    cursor.execute("""
                        INSERT INTO detalle_venta (carritoid_carrito, ventaid_venta, total_venta)
                        VALUES (%s, %s, %s)
                    """, (id_carrito, id_venta, total))

                    conexion.commit()
                    flash("¡Compra realizada exitosamente!", "success")
                    session.pop("tarjeta_seleccionada", None)
                    cursor.execute("DELETE FROM detalle_carrito WHERE carritoid_carrito = %s", (id_carrito,))
                    conexion.commit()

                    return redirect(url_for("tienda"))

            except Exception as e:
                print(f"Error al procesar el pago: {e}")
                conexion.rollback()
                flash("Ocurrió un error al procesar el pago.", "danger")
                return redirect(url_for("confirmar_compra"))
            finally:
                conexion.close()

        elif action == "seleccionar_tarjeta":
            tarjeta_id = request.form.get("id_tarjeta_seleccionada")
            if tarjeta_id:
                session["tarjeta_seleccionada"] = int(tarjeta_id)
                flash("Tarjeta seleccionada correctamente", "info")
            return redirect(url_for("confirmar_compra"))

        elif action == "add_card":
            numero = request.form.get("numero_tarjeta", "").replace(" ", "")
            fecha_expiracion = request.form.get("fecha_expiracion")
            tipo = request.form.get("tipo_tarjeta", "Visa")

            if not numero or len(numero) != 16 or not numero.isdigit():
                flash("Número de tarjeta inválido. Debe tener 16 dígitos numéricos.", "danger")
            else:
                if agregar_tarjeta(usuario_id, numero, fecha_expiracion, tipo):
                    flash("Tarjeta agregada correctamente", "success")
                else:
                    flash("Error al guardar la tarjeta", "danger")

            return redirect(url_for("confirmar_compra"))

    carrito = obtener_items_carrito(usuario_id)
    if not carrito:
        return render_template("confirmarCompra.html", carrito=[], subtotal=0, descuento=0, total=0, tarjetas=[], tarjeta_seleccionada=None)

    subtotal = sum(item["precio"] * item["cantidad"] for item in carrito)
    descuento = round(subtotal * 0.10, 2)
    total = round(subtotal - descuento, 2)

    tarjetas = obtener_tarjetas_por_usuario(usuario_id)
    tarjeta_seleccionada = session.get("tarjeta_seleccionada")

    return render_template(
        "confirmarCompra.html",
        carrito=carrito,
        subtotal=subtotal,
        descuento=descuento,
        total=total,
        tarjetas=tarjetas,
        tarjeta_seleccionada=tarjeta_seleccionada
    )
    
'''
@app.route("/confirmar-compra", methods=["GET", "POST"])
def confirmar_compra():
    if "usuario_id" not in session:
        return redirect(url_for("iniciar_sesion"))

    usuario_id = session["usuario_id"]

    if request.method == "POST":
        action = request.form.get("action")

        if action == "pay":
            tarjeta_id = session.get("tarjeta_seleccionada")
            if not tarjeta_id:
                flash("Debes seleccionar una tarjeta para pagar.", "warning")
                return redirect(url_for("confirmar_compra"))

            carrito = obtener_items_carrito(usuario_id)
            if not carrito:
                flash("Tu carrito está vacío.", "warning")
                return redirect(url_for("carrito"))

            subtotal = sum(item["precio"] * item["cantidad"] for item in carrito)
            descuento = round(subtotal * 0.10, 2)
            total = round(subtotal - descuento, 2)

            conexion = conectar()
            try:
                with conexion.cursor() as cursor:
                    # Insertar en venta
                    cursor.execute("INSERT INTO venta (fecha) VALUES (CURDATE())")
                    id_venta = cursor.lastrowid

                    # Obtener el carrito más reciente del usuario
                    cursor.execute("SELECT id_carrito FROM carrito WHERE usuariosid_usuario = %s ORDER BY id_carrito DESC LIMIT 1", (usuario_id,))
                    carrito_data = cursor.fetchone()

                    if not carrito_data:
                        flash("No se encontró un carrito válido.", "danger")
                        return redirect(url_for("carrito"))

                    id_carrito = carrito_data[0]

                    # Insertar en detalle_venta
                    cursor.execute("""
                        INSERT INTO detalle_venta (carritoid_carrito, ventaid_venta, total_venta)
                        VALUES (%s, %s, %s)
                    """, (id_carrito, id_venta, total))

                    conexion.commit()
                    flash("¡Compra realizada exitosamente!", "success")
                    session.pop("tarjeta_seleccionada", None)
                    cursor.execute("DELETE FROM detalle_carrito WHERE carritoid_carrito = %s", (id_carrito,))
                    conexion.commit()

                    return redirect(url_for("tienda"))

            except Exception as e:
                print(f"Error al procesar el pago: {e}")
                conexion.rollback()
                flash("Ocurrió un error al procesar el pago.", "danger")
                return redirect(url_for("confirmar_compra"))
            finally:
                conexion.close()

        elif action == "seleccionar_tarjeta":
            tarjeta_id = request.form.get("id_tarjeta_seleccionada")
            if tarjeta_id:
                session["tarjeta_seleccionada"] = int(tarjeta_id)
                flash("Tarjeta seleccionada correctamente", "info")
            return redirect(url_for("confirmar_compra"))

        elif action == "add_card":
            flash("Formulario para agregar tarjeta mostrado", "info")
            return redirect(url_for("confirmar_compra"))

    carrito = obtener_items_carrito(usuario_id)
    if not carrito:
        return render_template("confirmarCompra.html", carrito=[], subtotal=0, descuento=0, total=0, tarjetas=[], tarjeta_seleccionada=None)

    subtotal = sum(item["precio"] * item["cantidad"] for item in carrito)
    descuento = round(subtotal * 0.10, 2)
    total = round(subtotal - descuento, 2)

    tarjetas = obtener_tarjetas_por_usuario(usuario_id)
    tarjeta_seleccionada = session.get("tarjeta_seleccionada")
    print("Form POST:", request.form.to_dict())
    print("Tarjeta en sesión:", session.get("tarjeta_seleccionada"))

    return render_template(
        "confirmarCompra.html",
        carrito=carrito,
        subtotal=subtotal,
        descuento=descuento,
        total=total,
        tarjetas=tarjetas,
        tarjeta_seleccionada=tarjeta_seleccionada
    )
'''

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
        return resultado  # o redirect('/')
    return render_template('agregar_juego.html')



@app.route('/detalle_juego/<int:id_juego>')
def detalle_juego(id_juego):
    juego = obtener_juego_por_id(id_juego)
    similares = obtener_similares(juego[0])  # <-- función nueva
    return render_template('producto.html', juego=juego, similares=similares)




@app.route('/agregar_al_carrito/<int:juego_id>', methods=['POST'])
def ruta_agregar_al_carrito(juego_id):
    if 'usuario_id' not in session:
        flash('Debes iniciar sesión para agregar productos al carrito.')
        return redirect(url_for('iniciar_sesion'))

    usuario_id = session['usuario_id']
    exito = agregar_al_carrito(juego_id, usuario_id)

    if exito:
        flash('Juego agregado al carrito con éxito.')
    else:
        flash('Hubo un error al agregar el juego al carrito.')

    return redirect(url_for('detalle_juego', id_juego=juego_id))




@app.route("/carrito", methods=["GET", "POST"])
def carrito():
    if "usuario_id" not in session:
        return redirect(url_for("iniciar_sesion"))

    usuario_id = session["usuario_id"]
    success = session.pop("success", None)
    error = session.pop("error", None)

    if request.method == "POST":
        action = request.form.get("action")
        product_id = int(request.form.get("product_id", 0))

        if action == "update_quantity":
            change = request.form.get("change")
            if change == "increase":
                actualizar_cantidad_item(usuario_id, product_id, 1)
                session['success'] = "Cantidad incrementada"
            elif change == "decrease":
                actualizar_cantidad_item(usuario_id, product_id, -1)
                session['success'] = "Cantidad disminuida"

        elif action == "remove":
            eliminar_item_carrito(usuario_id, product_id)
            session['last_removed'] = product_id
            session['success'] = "Juego eliminado"

        elif action == "undo_remove":
            last = session.pop("last_removed", None)
            if last:
                agregar_al_carrito(last, usuario_id)
                session['success'] = "Eliminación deshecha"
            else:
                session['error'] = "No se pudo deshacer"

        elif action == "add_to_cart":
            agregar_al_carrito(product_id, usuario_id)
            session['success'] = "Producto agregado"

        elif action == "select_payment":
            payment_method = request.form.get("payment_method")
            session["payment_method"] = payment_method

        return redirect(url_for("carrito"))

    cart = obtener_items_carrito(usuario_id)
    subtotal = round(sum(item["precio"] * item["cantidad"] for item in cart), 2)
    descuento = 0 #por el momento no tiene descuento
    total = subtotal - descuento
    payment_method = session.get("payment_method", "")

    # Puedes cambiar esto por tus propios juegos recomendados reales
    recommended = []  # si quieres agregar juegos aquí también dime

    print("=== CARGANDO CARRITO ===")
    print("session:", dict(session))

    cart = obtener_items_carrito(usuario_id)
    print("carrito cargado:", cart)

    subtotal = sum(item["precio"] * item["cantidad"] for item in cart)
    print("subtotal:", subtotal)


    return render_template("carrito.html",
        cart=cart,
        subtotal=subtotal,
        descuento=descuento,
        total=total,
        success=success,
        error=error,
        payment_method=payment_method,
        recommended=recommended
    )


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)  
