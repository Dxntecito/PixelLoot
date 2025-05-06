document.addEventListener('DOMContentLoaded', function () {
    const userIcon = document.getElementById('user-icon');
    const userMenu = document.getElementById('user');
    const toggle = document.getElementById('toggle');
    const responsiveMenu = document.getElementById('responsive-menu');
    const navContainer = document.getElementById('caja2');
    const nav = document.getElementById('nav-menu');
    const userList = document.getElementById('user-menu');

    const saltoLinea = document.createElement('hr');


    userIcon.addEventListener('click', function () {
        userMenu.classList.toggle('active');
    });

    // Opcional: Cerrar el menú si se hace clic fuera de él
    document.addEventListener('click', function (event) {
        if (!userIcon.contains(event.target) && !userMenu.contains(event.target)) {
            userMenu.classList.remove('active');
        }
    });

    toggle.addEventListener('click', function () {
        responsiveMenu.classList.toggle('active');

        if (responsiveMenu.classList.contains('active')) {
            responsiveMenu.appendChild(nav);
            responsiveMenu.appendChild(saltoLinea);
            responsiveMenu.appendChild(userList);
            document.body.style.overflow = 'hidden';    //evita deslizar la página cuando el menú responsivo esté activo
        } else {
            navContainer.appendChild(nav);
            userMenu.appendChild(userList);
            responsiveMenu.removeChild(saltoLinea);
            document.body.style.overflow = '';          //permite deslizar la página cuando el menú responsivo esté inactivo
        }
    });


    /** Crea las tarjetas de productos teniendo en cuenta la lista en bicicletas.js */
    function crearTarjetasProductosTienda(productos) {
        const contenedorTarjetas = document.getElementById("juegos-contenedor");
        productos.forEach(producto => {
            const nuevoJuego = document.createElement("div");
            nuevoJuego.classList.add("tarjeta-producto");
            nuevoJuego.innerHTML = `
            <img src="./imagenes/${producto.id}.jpg" alt="${producto.nombre}">
            <h3><a href="prd-${producto.sub}.html">${producto.nombre}</a></h3>
            <p class="precio">S/${producto.precio}</p>`;
            contenedorTarjetas.appendChild(nuevoJuego);
        });
    }
    crearTarjetasProductosTienda(juegos);
   
    const checkboxes = document.querySelectorAll('.categorias input[type="checkbox"]');
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function () {
            if (this.checked) {
                const categoria = this.value;
                window.location.href = `${categoria}.html`;
            }
        });

    });
});

// Codigo para la funcionalidad del carrito

// Función para agregar un juego al carrito
function agregarAlCarrito(nombre, precio, imagen) {
    // Obtener el carrito del localStorage
    let carrito = JSON.parse(localStorage.getItem('carrito')) || [];
    let carritoVacio = carrito.length === 0;

    // Verificar si el juego ya existe en el carrito
    let juegoExistente = carrito.find(juego => juego.nombre === nombre);

    if (juegoExistente) {
        // Si el juego ya existe, incrementar su cantidad
        juegoExistente.cantidad++;
    } else {
        // Si el juego no existe, crear un nuevo objeto juego y añadirlo al carrito
        const nuevoJuego = { nombre, precio, imagen, cantidad: 1 };
        carrito.push(nuevoJuego);

    }

    // Guardar el carrito actualizado en el localStorage
    localStorage.setItem('carrito', JSON.stringify(carrito));

    // Actualizar la visualización del carrito
    mostrarCarrito();


}



//Funcion para agregar carrito y animacion
function agregarAlCarritoAnimado(nombre, precio, imagen) {
    // Obtener el carrito del localStorage
    let carrito = JSON.parse(localStorage.getItem('carrito')) || [];
    let carritoVacio = carrito.length === 0;

    // Verificar si el juego ya existe en el carrito
    let juegoExistente = carrito.find(juego => juego.nombre === nombre);

    if (juegoExistente) {
        // Si el juego ya existe, incrementar su cantidad
        juegoExistente.cantidad++;
    } else {
        // Si el juego no existe, crear un nuevo objeto juego y añadirlo al carrito
        const nuevoJuego = { nombre, precio, imagen, cantidad: 1 };
        carrito.push(nuevoJuego);

        // Mostrar la animación circular solo si el carrito estaba vacío
        if (carritoVacio) {
            mostrarAnimacionCircular();
        }
    }

    // Guardar el carrito actualizado en el localStorage
    localStorage.setItem('carrito', JSON.stringify(carrito));

    // Actualizar la visualización del carrito
    mostrarCarrito();
}





// Función para eliminar un juego del carrito
let juegoEliminado = null;  // Variable para almacenar el juego eliminado

function eliminarDelCarrito(index) {
    let carrito = JSON.parse(localStorage.getItem('carrito')) || [];
    juegoEliminado = carrito.splice(index, 1)[0];
    localStorage.setItem('carrito', JSON.stringify(carrito));
    mostrarCarrito();
    mostrarMensajeEliminado();

}

// Función para deshacer la eliminación del juego
function deshacerEliminar() {
    if (juegoEliminado) {
        let carrito = JSON.parse(localStorage.getItem('carrito')) || [];
        carrito.push(juegoEliminado);
        localStorage.setItem('carrito', JSON.stringify(carrito));
        juegoEliminado = null;
        mostrarCarrito();
        ocultarMensajeEliminado();
    }
}

// Función para mostrar el mensaje de juego eliminado
function mostrarMensajeEliminado() {
    const mensajeEliminado = document.getElementById('mensaje-eliminado');
    mensajeEliminado.style.display = 'block';
    setTimeout(ocultarMensajeEliminado, 5000); // Ocultar el mensaje después de 5 segundos
}

// Función para ocultar el mensaje de juego eliminado
function ocultarMensajeEliminado() {
    const mensajeEliminado = document.getElementById('mensaje-eliminado');
    mensajeEliminado.style.display = 'none';
}

// Función para cambiar la cantidad de un juego en el carrito
function cambiarCantidad(index, incremento) {
    let carrito = JSON.parse(localStorage.getItem('carrito')) || [];
    if (carrito[index].cantidad + incremento >= 1) {
        carrito[index].cantidad += incremento;
    }
    localStorage.setItem('carrito', JSON.stringify(carrito));
    mostrarCarrito();
    mostrarCarritoCompra();
}

// Función para mostrar el contenido del carrito en la página
function mostrarCarrito() {
    let carrito = JSON.parse(localStorage.getItem('carrito')) || [];
    const carritoItemsBody = document.getElementById('carrito-items').getElementsByTagName('tbody')[0];
    carritoItemsBody.innerHTML = '';

    carrito.forEach((juego, index) => {
        const tr = document.createElement('tr');
        tr.className = 'carrito-item';
        tr.innerHTML = `
            <td ><img src="${juego.imagen}" alt="${juego.nombre}"></td>
            
                <td>${juego.nombre}</td>
                <td>S/.${juego.precio}</td>
                <td class="cantidad">
                    <button class="btnCantidad" onclick="cambiarCantidad(${index}, -1)" ${juego.cantidad <= 1 ? 'disabled' : ''}>-</button>
                    <span>${juego.cantidad}</span>
                    <button class="btnCantidad" onclick="cambiarCantidad(${index}, 1)">+</button>
                </td>
            
            <td><button class="eliminar" onclick="eliminarDelCarrito(${index})"><i class="fas fa-trash"></i></button></td>
        `;
        carritoItemsBody.appendChild(tr);
    });

    mostrarPagoTotal();
}



function mostrarAnimacionCircular() {
    const overlay = document.getElementById('overlay');
    const caja3 = document.getElementById('caja3');
    const circularAnimation = document.getElementById('circular-animation');
    const message = document.getElementById('circular-animation-message');

    // Verificar que los elementos existen
    if (!overlay || !circularAnimation || !message || !caja3) {
        console.error('Uno o más elementos no se encontraron.');
        return;
    }

    // Obtener la posición y el tamaño de caja3
    const caja3Rect = caja3.getBoundingClientRect();

    // Posicionar la animación circular y el mensaje
    circularAnimation.style.top = `${caja3Rect.top + caja3Rect.height / 2 - 50}px`;
    circularAnimation.style.left = `${caja3Rect.left + caja3Rect.width / 2 - 50}px`;
    message.style.top = `${caja3Rect.top + caja3Rect.height / 2 + 60}px`;
    message.style.left = `${circularAnimation.style.left}px`;

    overlay.style.display = 'block';
    circularAnimation.style.display = 'block';
    message.style.display = 'block';

    setTimeout(() => {
        overlay.style.display = 'none';
        circularAnimation.style.display = 'none';
        message.style.display = 'none';
    }, 1800); // Ocultar la animación después de 1.8 segundos
}





document.addEventListener('DOMContentLoaded', function () {
    mostrarCarrito();
});
// Función para mostrar el total a pagar
function mostrarPagoTotal() {
    let carrito = JSON.parse(localStorage.getItem('carrito')) || [];
    const total = carrito.reduce((acc, juego) => acc + juego.precio * juego.cantidad, 0);
    document.getElementById('total-pago-valor').textContent = total.toFixed(2);
    document.getElementById('subTotal').textContent = total.toFixed(2);
}

document.addEventListener('DOMContentLoaded', mostrarCarrito);

//Validar que solo se puede seleccionar un checkbox
document.addEventListener('DOMContentLoaded', function () {
    // Mostrar el carrito cuando el DOM esté completamente cargado
    mostrarCarrito();

    // Obtener todos los checkboxes de métodos de pago
    const checkboxes = document.querySelectorAll('.paymentMethod input[type="checkbox"]');
    checkboxes.forEach(function (checkbox) {
        // Añadir un evento 'change' a cada checkbox
        checkbox.addEventListener('change', function () {
            if (this.checked) {
                // Si el checkbox actual es marcado, desmarcar los otros checkboxes
                checkboxes.forEach(function (otherCheckbox) {
                    if (otherCheckbox !== checkbox) {
                        otherCheckbox.checked = false;
                    }
                });
            }
        });
    });

    // Añadir un evento 'click' al botón de pago
    document.querySelector('.Btn').addEventListener('click', function (event) {
        let isChecked = false;

        // Verificar si al menos un checkbox está marcado
        checkboxes.forEach(function (checkbox) {
            if (checkbox.checked) {
                isChecked = true;
            }
        });

        // Obtener el carrito del localStorage y verificar si no está vacío
        let carrito = JSON.parse(localStorage.getItem('carrito')) || [];
        let carritoNoVacio = carrito.length > 0;

        if (!isChecked || !carritoNoVacio) {
            // Prevenir la redirección y mostrar una alerta apropiada
            event.preventDefault();
            if (!isChecked) {
                alert('Por favor, selecciona un método de pago.');
            } else if (!carritoNoVacio) {
                alert('Por favor, añade al menos un juego al carrito.');
            }
        } else {
            // Redirigir a la página de confirmación de compra
            window.location.href = 'confirmarCompra.html';
        }
    });

    document.querySelector('.Btn2').addEventListener('click', function (event) {
        let isChecked = false;

        // Verificar si al menos un checkbox está marcado
        checkboxes.forEach(function (checkbox) {
            if (checkbox.checked) {
                isChecked = true;
            }
        });

        // Obtener el carrito del localStorage y verificar si no está vacío
        let carrito = JSON.parse(localStorage.getItem('carrito')) || [];
        let carritoNoVacio = carrito.length > 0;

        if (!isChecked || !carritoNoVacio) {
            // Prevenir la redirección y mostrar una alerta apropiada
            event.preventDefault();
            if (!isChecked) {
                alert('Por favor, selecciona un método de pago.');
            } else if (!carritoNoVacio) {
                alert('Por favor, añade al menos un juego al carrito.');
            }
        } else {
            // Redirigir a la página de confirmación de compra
            window.location.href = 'confirmarCompra.html';
        }
    });
});


//Para el responsivo del carrito
document.getElementById('btn-detalles').addEventListener('click', function () {
    var details = document.getElementById('resumen-details');
    if (details.style.display === 'block') {
        details.style.display = 'none';
        document.querySelector('.resumen-container').style.height = '60px';
    } else {
        details.style.display = 'block';
        document.querySelector('.resumen-container').style.height = 'auto';
    }
});

document.getElementById('btn-pagar').addEventListener('click', function () {
    var details = document.getElementById('resumen-details');
    details.style.display = 'block';
    document.querySelector('.resumen-container').style.height = 'auto';
});




//Apartado de tarjetas añadidas


function guardarDatos() {
    const nombre = document.getElementById("name-text").value;
    const number = document.getElementById("card-number").value;
    const validDate = document.getElementById("valid-date").value;
    const cvv = document.getElementById("cvv-text").value;

    if (nombre && number && validDate && cvv) {
        localStorage.setItem(`nombre_${number}`, nombre);
        localStorage.setItem(`number_${number}`, number);
        localStorage.setItem(`validDate_${number}`, validDate);
        localStorage.setItem(`cvv_${number}`, cvv);
        recuperarDatos();
        limpiarCampos();
        document.querySelector('.ui').style.display = 'none';
    } else {
        alert("Por favor, rellena todos los campos.");
    }


}

function recuperarDatos() {
    const tarjetasList = document.getElementById("tarjetas-list");
    tarjetasList.innerHTML = "";

    for (let i = 0; i < localStorage.length; i++) {
        const key = localStorage.key(i);
        if (key.startsWith("number_")) {
            const number = localStorage.getItem(key);
            const lastFourDigits = number.slice(-4);

            tarjetasList.innerHTML += `
                <div class="listaTarjetas">
                    <input type="checkbox" name="tarjeta" value="${number}" onclick="seleccionarTarjeta(this)">
                    <img src="imagenes/metodoPago/visaTarjeta.png" alt="Imagen" style="width:68px;height:68px;">
                    <span>${lastFourDigits}</span>
                    <button onclick="eliminarDatos('${number}')">Eliminar tarjeta</button>
                </div>
            `;
        }
    }
}

function eliminarDatos(number) {
    localStorage.removeItem(`nombre_${number}`);
    localStorage.removeItem(`number_${number}`);
    localStorage.removeItem(`validDate_${number}`);
    localStorage.removeItem(`cvv_${number}`);
    recuperarDatos();
}

function mostrarFormulario() {
    document.querySelector('.ui').style.display = 'block';
}

function limpiarCampos() {
    document.getElementById("name-text").value = "";
    document.getElementById("card-number").value = "";
    document.getElementById("valid-date").value = "";
    document.getElementById("cvv-text").value = "";
}

function seleccionarTarjeta(checkbox) {
    const checkboxes = document.querySelectorAll('input[name="tarjeta"]');
    checkboxes.forEach((cb) => {
        if (cb !== checkbox) {
            cb.checked = false;
        }
    });
}

//Vaciar el carrito completo
function vaciarCarrito() {
    localStorage.removeItem('carrito');
    mostrarCarrito(); // Actualiza la visualización del carrito
}

function realizarPago() {
    const selectedCard = document.querySelector('input[name="tarjeta"]:checked');
    if (selectedCard) {
        const number = selectedCard.value;
        const nombre = localStorage.getItem(`nombre_${number}`);
        const validDate = localStorage.getItem(`validDate_${number}`);
        const cvv = localStorage.getItem(`cvv_${number}`);
        // Procesar el pago aquí con los datos de la tarjeta seleccionada
        alert(`Procesando pago con la tarjeta terminada en ${number.slice(-4)}`);
        alert(`Pago confirmado, tu(s) llave(s) se enviaran a tu correo en ul plazo de 24Horas`);
        alert(`¡MUCHAS GRACIAS POR TU COMPRA!`);  

        vaciarCarrito();

        window.location.href = 'tienda.html'
    } else {
        alert("Por favor, selecciona una tarjeta para procesar el pago.");
    }
}

window.onload = recuperarDatos;


/*Función para validar el inicio de sesión*/
function validarInicioSesion() {
    const usernameInput = document.getElementById('username-user');
    const passwordInput = document.getElementById('password-user');

    const username = usernameInput.value;
    const password = passwordInput.value;

    if ((username === "LeoMeFlo" || username === "leomeflo@gmail.com") && password === "leomeflo09") {
        window.location.href = "index.html";
    } else {
        alert("Usuario o Contraseña Incorrectos. Inténtalo de nuevo.");
    }
}

/*Función para validar el registro de nuevo usuario*/
function validarRegistro() {
    const fullName = document.getElementById('new-name').value;
    const username = document.getElementById('new-username').value;
    const phone = document.getElementById('new-phone').value;
    const email = document.getElementById('new-email').value;
    const password = document.getElementById('new-password').value;
    const confirmPassword = document.getElementById('new-confirm-password').value;
    const terms = document.getElementById('terms').checked;
    
    const nameRegex = /^[a-zA-Z\s]+$/;
    const usernameRegex = /^\S+$/;
    const phoneRegex = /^[0-9]+$/;
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    
    if (!nameRegex.test(fullName)) {
        alert('El nombre completo solo puede contener letras y espacios.');
        return false;
    }

    if (!usernameRegex.test(username)) {
        alert('El username no puede contener espacios.');
        return false;
    }

    if (!phoneRegex.test(phone)) {
        alert('El teléfono solo puede contener números.');
        return false;
    }

    if (!emailRegex.test(email)) {
        alert('Por favor, ingrese un correo electrónico válido.');
        return false;
    }

    if (password !== confirmPassword) {
        alert('Las contraseñas no coinciden.');
        return false;
    }

    if (!terms) {
        alert('Debe aceptar los términos y condiciones.');
        return false;
    }

    window.location.href = "index.html";
}
