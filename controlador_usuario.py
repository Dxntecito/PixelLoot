from bd import conectar
import hashlib
import pymysql
def insertar_usuario(nombre_usuario,nombre_real, correo, genero, contraseña,
                     telefono, pais, fecha_nacimiento, rolid_rol,
                     foto_perfil, foto_portada):
    conexion = conectar()
    with conexion.cursor() as cursor:
        cursor.execute(
            "INSERT INTO usuario (nombre_usuario,nombre_real, correo, genero, contraseña, telefono, pais, fecha_nacimiento, rolid_rol, foto_perfil, foto_portada) "
            "VALUES (%s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (nombre_usuario, nombre_real, correo, genero, contraseña, telefono, pais, fecha_nacimiento, rolid_rol, foto_perfil, foto_portada)
        )
    conexion.commit()
    conexion.close()

def editar_informacion(id_usuario, nombre_usuario, nombre_real, correo, genero, contraseña,
                     telefono, pais, fecha_nacimiento, rolid_rol,
                     foto_perfil, foto_portada):
    conexion = conectar()
    with conexion.cursor() as cursor:
        cursor.execute(
            """
            UPDATE usuario 
            SET nombre_usuario = %s,
                nombre_real = %s,
                correo = %s,
                genero = %s,
                contraseña = %s,
                telefono = %s,
                pais = %s,
                fecha_nacimiento = %s,
                rolid_rol = %s,
                foto_perfil = %s,
                foto_portada = %s
            WHERE id_usuario = %s
            """,
            (nombre_usuario, nombre_real, correo, genero, contraseña, telefono, pais,
             fecha_nacimiento, rolid_rol, foto_perfil, foto_portada, id_usuario)
        )
    conexion.commit()
    conexion.close()

def validar_usuario(nombre_usuario, contraseña):
    try:
        # Establece la conexión a la base de datos
        conexion = conectar()

        # Crea un cursor con el que puedes ejecutar consultas
        cursor = conexion.cursor(pymysql.cursors.DictCursor)

        # Depuración: Verificar los valores recibidos
        print(f"Nombre de usuario: {nombre_usuario}")
        print(f"Contraseña: {contraseña}")

        # Ejecuta la consulta para buscar el usuario
        query = "SELECT * FROM usuario WHERE nombre_usuario = %s AND contraseña = %s"
        cursor.execute(query, (nombre_usuario, contraseña))

        # Obtiene el primer resultado (usuario)
        usuario = cursor.fetchone()

        # Depuración: Verificar si se encontró un usuario
        print(f"Usuario encontrado: {usuario}")

        # Cierra el cursor después de usarlo
        cursor.close()

        # Retorna el usuario encontrado o None si no se encontró
        return usuario

    except pymysql.MySQLError as err:
        print(f"Error de MySQL: {err}")
        return None
    except Exception as e:
        print(f"Error desconocido: {e}")
        return None
    finally:
        # Cierra la conexión, si fue abierta
        if 'conexion' in locals() and conexion.open:
            conexion.close()


def obtener_datos_usuario(id_usuario):
    conexion = conectar()
    try:
        with conexion.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM usuario WHERE id_usuario = %s AND estado = 1", (id_usuario,))
            return cursor.fetchone()
    except Exception as e:
        print(f"Error al obtener datos del usuario: {e}")
        return None
    finally:
        conexion.close()

def obtener_datos_completos_usuario(id_usuario):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT u.*, 
                       t.id_tarjeta, t.numero_tarjeta, t.ccv, t.ciudad AS ciudad_tarjeta, 
                       t.fecha_expiracion, t.tipo
                FROM usuario u
                LEFT JOIN tarjeta t ON u.id_usuario = t.usuariosid_usuario
                WHERE u.id_usuario = %s
            """, (id_usuario,))
            columns = [col[0] for col in cursor.description]
            results = [dict(zip(columns, row)) for row in cursor.fetchall()]
            return results
    except Exception as e:
        print(f"Error al obtener datos completos del usuario: {e}")
        return None
    finally:
        conexion.close()

def obtener_paises_distintos():
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT DISTINCT pais FROM usuario WHERE pais IS NOT NULL AND pais != ''")  # Obtiene países únicos
            return [pais[0] for pais in cursor.fetchall()]  # Devuelve una lista de países
    except Exception as e:
        print(f"Error al obtener países: {e}")
        return []
    finally:
        conexion.close()

def actualizar_usuario(username, nombre, genero, correo, telefono, pais, password, usuario_id):
    # Obtener la conexión a la base de datos
    conexion = conectar()
    
    with conexion.cursor() as cursor:
        # Ejecutar la consulta de actualización
        cursor.execute("""
            UPDATE usuario 
            SET nombre_usuario = %s, nombre_real = %s, genero = %s, correo = %s, telefono = %s, pais = %s, contraseña = %s 
            WHERE id = %s
        """, (username, nombre, genero, correo, telefono, pais, password, usuario_id))
    
    # Confirmar los cambios en la base de datos
    conexion.commit()
    conexion.close()

