from bd import conectar

def obtener_tarjetas_por_usuario(usuario_id):
    try:
        with conectar() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute("""
                    SELECT 
                        id_tarjeta,
                        RIGHT(numero_tarjeta, 4) AS ultimos_digitos,
                        fecha_expiracion,
                        tipo
                    FROM tarjeta
                    WHERE usuariosid_usuario = %s
                """, (usuario_id,))
                return cursor.fetchall()
    except Exception as e:
        print(f"Error al obtener tarjetas del usuario: {e}")
        return []

def agregar_tarjeta(usuario_id, numero_tarjeta, ccv, ciudad, fecha_raw, tipo):
    # Convertir "YYYY-MM" a "MM/YYYY"
    try:
        partes = fecha_raw.split("-")  # ["2025", "05"]
        fecha_expiracion = f"{partes[1]}/{partes[0]}"  # "05/2025"
    except Exception:
        fecha_expiracion = "01/2000"  # valor por defecto en caso de error

    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                INSERT INTO tarjeta (
                    usuariosid_usuario,
                    numero_tarjeta,
                    ccv,
                    ciudad,
                    fecha_expiracion,
                    tipo
                ) VALUES (%s, %s, %s, %s, %s, %s)
            """, (usuario_id, numero_tarjeta, ccv, ciudad, fecha_expiracion, tipo))
            conexion.commit()
            return True
    except Exception as e:
        print(f"Error al guardar tarjeta: {e}")
        return False
    finally:
        conexion.close()


