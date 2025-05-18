from datetime import date
from bd import conectar  # función de conexión a la BD

def obtener_items_carrito(usuario_id):
    with conectar() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT dc.juegoid, j.nombre, j.precio, j.imagen, dc.cantidad
                FROM detalle_carrito dc
                JOIN juego j ON j.id = dc.juegoid
                WHERE dc.carritoid_carrito = (
                    SELECT id_carrito FROM carrito
                    WHERE usuariosid_usuario = %s
                    ORDER BY id_carrito DESC LIMIT 1
                )
            """, (usuario_id,))
            resultados = cursor.fetchall()

    return [
        {
            "product_id": row[0],
            "nombre": row[1],
            "precio": float(row[2]),
            "imagen": row[3],
            "cantidad": row[4]
        }
        for row in resultados
    ]


def agregar_al_carrito(juego_id, usuario_id):
    with conectar() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT id_carrito FROM carrito 
                WHERE usuariosid_usuario = %s 
                ORDER BY id_carrito DESC LIMIT 1
            """, (usuario_id,))
            carrito = cursor.fetchone()

            if carrito is None:
                cursor.execute("""
                    INSERT INTO carrito (fecha, usuariosid_usuario) 
                    VALUES (%s, %s)
                """, (date.today(), usuario_id))
                conexion.commit()
                carrito_id = cursor.lastrowid
            else:
                carrito_id = carrito[0]

            cursor.execute("""
                SELECT cantidad FROM detalle_carrito 
                WHERE juegoid = %s AND carritoid_carrito = %s
            """, (juego_id, carrito_id))
            detalle = cursor.fetchone()

            if detalle:
                nueva_cantidad = detalle[0] + 1
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

            conexion.commit()


def actualizar_cantidad_item(usuario_id, juego_id, incremento):
    with conectar() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT id_carrito FROM carrito 
                WHERE usuariosid_usuario = %s 
                ORDER BY id_carrito DESC LIMIT 1
            """, (usuario_id,))
            carrito = cursor.fetchone()

            if carrito:
                cursor.execute("""
                    UPDATE detalle_carrito
                    SET cantidad = GREATEST(1, cantidad + %s)
                    WHERE juegoid = %s AND carritoid_carrito = %s
                """, (incremento, juego_id, carrito[0]))
                conexion.commit()


def eliminar_item_carrito(usuario_id, juego_id):
    with conectar() as conexion:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT id_carrito FROM carrito 
                WHERE usuariosid_usuario = %s 
                ORDER BY id_carrito DESC LIMIT 1
            """, (usuario_id,))
            carrito = cursor.fetchone()

            if carrito:
                cursor.execute("""
                    DELETE FROM detalle_carrito 
                    WHERE juegoid = %s AND carritoid_carrito = %s
                """, (juego_id, carrito[0]))
                conexion.commit()
