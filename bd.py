import pymysql

def conectar():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='pixelloot'
    )

# Verificación de la conexión
try:
    conexion = conectar()
    print("Conexión exitosa a la base de datos.")
    conexion.close()
except pymysql.MySQLError as e:
    print("Error al conectar a la base de datos:", e)