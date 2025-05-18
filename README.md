# PixelLoot 

PixelLoot es una tienda virtual de videojuegos construida con Flask. Permite a los usuarios explorar distintos títulos por categoría, agregarlos al carrito, 
hacer compras y hasta usar una ruleta de recomendaciones.  🎮💜

Gestión de usuarios

    El sistema debe permitir el registro de nuevos usuarios capturando datos personales (nombre, correo, país, contraseña).

    Los usuarios podrán iniciar y cerrar sesión mediante autenticación con verificación de credenciales.

    Se debe permitir la recuperación de contraseña a través de una funcionalidad específica.

    El usuario podrá editar su información personal desde su perfil.

Navegación y exploración de catálogo

    Los usuarios podrán visualizar el catálogo de videojuegos organizados por categoría (Acción, Aventura, Terror, etc.).

    Al seleccionar un producto, se mostrará una página con detalles completos del juego, incluyendo nombre, descripción, precio e imagen.

    El sistema ofrecerá una ruleta aleatoria que sugiere un videojuego de manera dinámica.

Carrito de compras y lista de deseos

    El usuario podrá agregar juegos al carrito de compras, eliminarlos o modificar cantidades.

    También podrá guardar juegos en su lista de deseos como favoritos.

    Al confirmar la compra, se debe registrar una transacción y vaciar el carrito.

Historial de compras

    El sistema debe almacenar y mostrar el historial de juegos adquiridos por cada usuario, permitiendo su consulta posterior.

Gestión de videojuegos (CRUD)

    Desde una vista administrativa, se podrá crear, leer, actualizar y eliminar videojuegos del sistema.

    Cada juego debe incluir campos como título, género, descripción, precio, imagen y disponibilidad.

Soporte al cliente

    El sistema debe contar con una página de contacto donde los usuarios puedan enviar consultas o reportar problemas.

Validaciones y control de flujo

    Los formularios deben implementar validaciones del lado del cliente (JavaScript) y del servidor (Python).

    Se deben controlar los errores de entrada, como campos vacíos, formatos incorrectos, duplicados, etc.

Persistencia de datos y seguridad

    La información debe almacenarse en una base de datos relacional estructurada.

    Las contraseñas deben ser encriptadas antes de ser almacenadas.

    Las rutas protegidas deben usar decoradores como @login_required para limitar el acceso a usuarios autenticados.