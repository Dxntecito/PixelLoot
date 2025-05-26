import os
from bd import conectar


def guardar_imagen(archivo, carpeta_destino='static/imagenes'):
    if archivo and archivo.filename:
        os.makedirs(carpeta_destino, exist_ok=True)
        ruta = os.path.join(carpeta_destino, archivo.filename)
        archivo.save(ruta)
        return ruta.replace("\\", "/")
    return None


def agregar_juego(request):
    nombre = request.form['nombre']
    precio = request.form['precio']
    cantidad = request.form['cantidad']
    descripcion = request.form['descripcion']

    # Imágenes
    ruta_imagen = guardar_imagen(request.files.get('imagen'))
    ruta_imagene1 = guardar_imagen(request.files.get('imagene1'))
    ruta_imagene2 = guardar_imagen(request.files.get('imagene2'))
    ruta_imagene3 = guardar_imagen(request.files.get('imagene3'))

    if ruta_imagen:
        conexion = conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO juego (
                        nombre, precio, estado, imagen, imagene1, imagene2, imagene3, cantidad, descripcion_juego
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (
                    nombre, precio, 1, ruta_imagen, ruta_imagene1,
                    ruta_imagene2, ruta_imagene3, cantidad, descripcion
                ))
                conexion.commit()
            return "Juego agregado con éxito"
        except Exception as e:
            return f"Error al insertar juego: {e}"
        finally:
            conexion.close()
    return "No se encontró la imagen principal"


def editar_juego(id_juego, request):
    nombre = request.form['nombre']
    precio = request.form['precio']
    cantidad = request.form['cantidad']
    descripcion = request.form['descripcion']

    ruta_imagen = guardar_imagen(request.files.get('imagen'))
    ruta_imagene1 = guardar_imagen(request.files.get('imagene1'))
    ruta_imagene2 = guardar_imagen(request.files.get('imagene2'))
    ruta_imagene3 = guardar_imagen(request.files.get('imagene3'))

    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                UPDATE juego SET
                    nombre = %s,
                    precio = %s,
                    cantidad = %s,
                    descripcion_juego = %s
                WHERE id = %s
            """, (nombre, precio, cantidad, descripcion, id_juego))

            if ruta_imagen:
                cursor.execute("UPDATE juego SET imagen = %s WHERE id = %s", (ruta_imagen, id_juego))
            if ruta_imagene1:
                cursor.execute("UPDATE juego SET imagene1 = %s WHERE id = %s", (ruta_imagene1, id_juego))
            if ruta_imagene2:
                cursor.execute("UPDATE juego SET imagene2 = %s WHERE id = %s", (ruta_imagene2, id_juego))
            if ruta_imagene3:
                cursor.execute("UPDATE juego SET imagene3 = %s WHERE id = %s", (ruta_imagene3, id_juego))

            conexion.commit()
            return True
    except Exception as e:
        print(f"Error al editar juego: {e}")
        return False
    finally:
        conexion.close()


def obtener_juegos():
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM juego WHERE estado = 1")
            return cursor.fetchall()
    except Exception as e:
        print(f"Error al obtener juegos: {e}")
        return []
    finally:
        conexion.close()


def obtener_juego_por_id(id_juego):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM juego WHERE id = %s AND estado = 1", (id_juego,))
            return cursor.fetchone()
    except Exception as e:
        print(f"Error al obtener juego por ID: {e}")
        return None
    finally:
        conexion.close()


def obtener_similares(id_actual):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT * FROM juego
                WHERE id != %s AND estado = 1
                ORDER BY RAND() LIMIT 6
            """, (id_actual,))
            return cursor.fetchall()
    except Exception as e:
        print("Error al obtener similares:", e)
        return []
    finally:
        conexion.close()


def listar_juegos():
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id, nombre, precio, cantidad FROM juego")
            return cursor.fetchall()
    except Exception as e:
        print("Error al listar juegos:", e)
        return []
    finally:
        conexion.close()


def eliminar_juego(id):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM juego WHERE id = %s", (id,))
            conexion.commit()
    except Exception as e:
        print(f"Error al eliminar juego: {e}")
    finally:
        conexion.close()
