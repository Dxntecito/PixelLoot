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
