import smtplib
from email.message import EmailMessage
import os

def enviar_factura_pdf(correo_remitente, clave_remitente, correo_destino, archivo_pdf):
    try:
        msg = EmailMessage()
        msg["Subject"] = "Tu factura de compra - PixelLoot"
        msg["From"] = correo_remitente
        msg["To"] = correo_destino
        msg.set_content("Gracias por tu compra. Adjuntamos tu factura en PDF.")

        with open(archivo_pdf, "rb") as f:
            contenido = f.read()
            msg.add_attachment(contenido, maintype="application", subtype="pdf", filename=os.path.basename(archivo_pdf))

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(correo_remitente, clave_remitente)
            smtp.send_message(msg)

        print("Correo enviado con éxito.")
        return True
    except Exception as e:
        print(f"Error al enviar correo: {e}")
        return False