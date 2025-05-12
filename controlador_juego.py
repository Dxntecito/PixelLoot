# controlador_juegos.py
import os
from bd import conectar

import os
from bd import conectar

def agregar_juego(request):
    nombre = request.form['nombre']
    precio = request.form['precio']
    cantidad = request.form['cantidad']
    descripcion = request.form['descripcion']

    # Obtener imágenes
    imagen = request.files.get('imagen')
    imagene1 = request.files.get('imagene1')
    imagene2 = request.files.get('imagene2')
    imagene3 = request.files.get('imagene3')

    # Ruta base
    carpeta_destino = 'static/imagenes'
    os.makedirs(carpeta_destino, exist_ok=True)

    # Función auxiliar para guardar imagen
    def guardar_imagen(archivo):
        if archivo and archivo.filename:
            ruta = os.path.join(carpeta_destino, archivo.filename)
            archivo.save(ruta)
            return ruta.replace("\\", "/")
        return None

    # Guardar cada imagen si existe
    ruta_imagen = guardar_imagen(imagen)
    ruta_imagene1 = guardar_imagen(imagene1)
    ruta_imagene2 = guardar_imagen(imagene2)
    ruta_imagene3 = guardar_imagen(imagene3)

    if ruta_imagen:
        conexion = conectar()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO juego (
                        nombre, precio, estado, imagen, imagene1, imagene2, imagene3, cantidad, descripcion_juego
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (
                    nombre, precio, 1, ruta_imagen, ruta_imagene1, ruta_imagene2, ruta_imagene3, cantidad, descripcion
                ))
                conexion.commit()
            return "Juego agregado con éxito"
        except Exception as e:
            return f"Error al insertar juego: {e}"
        finally:
            conexion.close()
    return "No se encontró la imagen principal"






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
















def obtener_juegos():
    conexion = conectar()
    try:
        juegos = []
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * From juego WHERE estado = 1")
            juegos = cursor.fetchall()
            return juegos
    except Exception as e:
        print(f"Error al obtener juegos: {e}")
        return []
    finally:
        conexion.close()
