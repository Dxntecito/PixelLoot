from bd import conectar
import pymysql


def insertar_usuario(nombre_usuario, nombre_real, correo, genero, contraseña,
                     telefono, pais, fecha_nacimiento, rolid_rol,
                     foto_perfil, foto_portada):
    with conectar() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute("""
                INSERT INTO usuario (
                    nombre_usuario, nombre_real, correo, genero, contraseña,
                    telefono, pais, fecha_nacimiento, rolid_rol, foto_perfil, foto_portada
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (nombre_usuario, nombre_real, correo, genero, contraseña, telefono, pais,
                  fecha_nacimiento, rolid_rol, foto_perfil, foto_portada))
        conexion.commit()


def editar_informacion(id_usuario, nombre_usuario, nombre_real, correo, genero, contraseña,
                       telefono, pais, fecha_nacimiento, rolid_rol,
                       foto_perfil, foto_portada):
    with conectar() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute("""
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
            """, (
                nombre_usuario, nombre_real, correo, genero, contraseña,
                telefono, pais, fecha_nacimiento, rolid_rol,
                foto_perfil, foto_portada, id_usuario
            ))
        conexion.commit()


def validar_usuario(nombre_usuario, contraseña):
    try:
        with conectar() as conexion:
            with conexion.cursor(pymysql.cursors.DictCursor) as cursor:
                query = """
                    SELECT * FROM usuario 
                    WHERE nombre_usuario = %s AND contraseña = %s
                """
                cursor.execute(query, (nombre_usuario, contraseña))
                usuario = cursor.fetchone()
                print(f"🔎 Usuario encontrado: {usuario}")
                return usuario
    except pymysql.MySQLError as err:
        print(f"Error de MySQL: {err}")
        return None
    except Exception as e:
        print(f"Error desconocido: {e}")
        return None


def obtener_datos_usuario(id_usuario):
    try:
        with conectar() as conexion:
            with conexion.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute("""
                    SELECT * FROM usuario 
                    WHERE id_usuario = %s AND estado = 1
                """, (id_usuario,))
                return cursor.fetchone()
    except Exception as e:
        print(f"Error al obtener datos del usuario: {e}")
        return None


def obtener_datos_completos_usuario(id_usuario):
    try:
        with conectar() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute("""
                    SELECT u.*, 
                           t.id_tarjeta, t.numero_tarjeta, t.ccv, 
                           t.ciudad AS ciudad_tarjeta, 
                           t.fecha_expiracion, t.tipo
                    FROM usuario u
                    LEFT JOIN tarjeta t ON u.id_usuario = t.usuariosid_usuario
                    WHERE u.id_usuario = %s
                """, (id_usuario,))
                columnas = [col[0] for col in cursor.description]
                datos = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
                return datos
    except Exception as e:
        print(f"Error al obtener datos completos del usuario: {e}")
        return []


def obtener_paises_distintos():
    try:
        with conectar() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute("""
                    SELECT DISTINCT pais 
                    FROM usuario 
                    WHERE pais IS NOT NULL AND pais != ''
                """)
                return [fila[0] for fila in cursor.fetchall()]
    except Exception as e:
        print(f" Error al obtener países: {e}")
        return []


def actualizar_usuario(username, nombre, genero, correo, telefono, pais, password, usuario_id):
    with conectar() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute("""
                UPDATE usuario 
                SET nombre_usuario = %s,
                    nombre_real = %s,
                    genero = %s,
                    correo = %s,
                    telefono = %s,
                    pais = %s,
                    contraseña = %s
                WHERE id_usuario = %s
            """, (username, nombre, genero, correo, telefono, pais, password, usuario_id))
        conexion.commit()
