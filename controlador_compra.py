from bd import conectar

def registrar_venta(usuario_id, total):
    try:
        with conectar() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute("INSERT INTO venta (fecha) VALUES (CURDATE())")
                id_venta = cursor.lastrowid

                cursor.execute("""
                    SELECT id_carrito FROM carrito 
                    WHERE usuariosid_usuario = %s 
                    ORDER BY id_carrito DESC LIMIT 1
                """, (usuario_id,))
                carrito_data = cursor.fetchone()

                if not carrito_data:
                    return None, None  # No hay carrito

                id_carrito = carrito_data[0]

                cursor.execute("""
                    INSERT INTO detalle_venta (carritoid_carrito, ventaid_venta, total_venta)
                    VALUES (%s, %s, %s)
                """, (id_carrito, id_venta, total))

                cursor.execute("DELETE FROM detalle_carrito WHERE carritoid_carrito = %s", (id_carrito,))
                conexion.commit()

                return id_venta, id_carrito
    except Exception as e:
        print(f"Error en registrar_venta: {e}")
        return None, None
