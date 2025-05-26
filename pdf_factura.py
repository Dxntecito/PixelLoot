from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from datetime import datetime
import os
import random
import string

def generar_llave():
    return '-'.join(''.join(random.choices(string.ascii_uppercase + string.digits, k=4)) for _ in range(4))

def generar_factura_pdf(nombre_archivo, usuario, carrito, subtotal, descuento, total, id_venta):
    ruta = os.path.join("static", "facturas", nombre_archivo)
    c = canvas.Canvas(ruta, pagesize=letter)
    width, height = letter

    c.setFillColorRGB(0.13, 0.15, 0.2)
    c.rect(0, 0, width, height, fill=1, stroke=0)

    logo_path = "static/imagenes/logo_pxl.jpg"
    if os.path.exists(logo_path):
        c.drawImage(logo_path, 50, height - 100, width=72, height=72, mask='auto')

    c.setFont("Helvetica-Bold", 20)
    c.setFillColor(colors.white)
    c.drawString(140, height - 60, "PixelLoot - Factura de Compra")

    saludo = f"Hola {usuario['nombre']}, gracias por tu reciente compra."
    agradecimiento = "El equipo de PixelLoot te lo agradece 💜"
    c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(width / 2, height - 130, saludo)
    c.drawCentredString(width / 2, height - 150, agradecimiento)

    c.setStrokeColor(colors.whitesmoke)
    c.line(40, height - 160, width - 40, height - 160)

    y = height - 180
    fecha = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    c.setFont("Helvetica-Bold", 10)
    c.drawString(50, y, "ID Venta:")
    c.setFont("Helvetica", 10)
    c.drawString(150, y, f"#{id_venta}")
    y -= 15

    c.setFont("Helvetica-Bold", 10)
    c.drawString(50, y, "Fecha de emisión:")
    c.setFont("Helvetica", 10)
    c.drawString(150, y, fecha)
    y -= 20

    c.line(40, y, width - 40, y)
    y -= 20

    c.setFont("Helvetica-Bold", 10)
    c.drawString(50, y, "Correo:")
    c.setFont("Helvetica", 10)
    c.drawString(150, y, usuario['correo'])
    y -= 15

    c.setFont("Helvetica-Bold", 10)
    c.drawString(50, y, "Teléfono:")
    c.setFont("Helvetica", 10)
    c.drawString(150, y, usuario['telefono'])

    y -= 20
    c.line(40, y, width - 40, y)
    y -= 25

    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Producto")
    c.drawString(300, y, "Cantidad")
    c.drawString(400, y, "Precio")
    y -= 20

    c.setFont("Helvetica", 10)
    for item in carrito:
        imagen_path = item.get("imagen", "").replace("\\", "/")
        if imagen_path and os.path.exists(imagen_path):
            c.drawImage(imagen_path, 50, y - 20, width=40, height=40, preserveAspectRatio=True, mask='auto')
            text_x = 100
        else:
            text_x = 50

        c.setFont("Helvetica-Bold", 10)
        c.drawString(text_x, y, item["nombre"])
        c.setFont("Helvetica", 10)
        c.drawString(300, y, str(item["cantidad"]))
        precio_total = item["precio"] * item["cantidad"]
        c.drawString(400, y, f"S/. {precio_total:.2f}")
        y -= 15

        c.setFont("Helvetica-Bold", 9)
        c.drawString(text_x, y, "Llaves:")
        c.setFont("Helvetica", 9)
        llave_y = y
        for i in range(item["cantidad"]):
            clave = generar_llave()
            c.drawString(text_x + 50, llave_y, f"{clave}")
            llave_y -= 12 

        y = llave_y - 20 

    c.line(40, y, width - 40, y)
    y -= 20

    
    c.setFont("Helvetica-Bold", 10)
    c.drawString(300, y, "Subtotal:")
    c.setFont("Helvetica", 10)
    c.drawString(400, y, f"S/. {subtotal:.2f}")
    y -= 15

    c.setFont("Helvetica-Bold", 10)
    c.drawString(300, y, "Descuento:")
    c.setFont("Helvetica", 10)
    c.drawString(400, y, f"S/. {descuento:.2f}")
    y -= 15

    c.setFont("Helvetica-Bold", 10)
    c.drawString(300, y, "Total:")
    c.setFont("Helvetica", 10)
    c.drawString(400, y, f"S/. {total:.2f}")

    c.save()
    return ruta