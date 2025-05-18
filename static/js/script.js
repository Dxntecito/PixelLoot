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
            document.body.style.overflow = 'hidden';
        } else {
            navContainer.appendChild(nav);
            userMenu.appendChild(userList);
            responsiveMenu.removeChild(saltoLinea);
            document.body.style.overflow = '';
        }
    });

    const checkboxes = document.querySelectorAll('.categorias input[type="checkbox"]');
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function () {
            if (this.checked) {
                const categoria = this.value;
                window.location.href = `${categoria}.html`;
            }
        });
    });

    // Envío automático al seleccionar una tarjeta
    document.querySelectorAll('input[name="id_tarjeta_seleccionada"]').forEach(function (radio) {
        radio.addEventListener('change', function () {
            this.closest('form').submit();
        });
    });
});

// Animación de carrito visual (opcional, mantener)
function mostrarAnimacionCircular() {
    const overlay = document.getElementById('overlay');
    const caja3 = document.getElementById('caja3');
    const anim = document.getElementById('circular-animation');
    const msg = document.getElementById('circular-animation-message');
    if (!overlay || !anim || !msg || !caja3) return;
    const rect = caja3.getBoundingClientRect();
    anim.style.top = `${rect.top + rect.height / 2 - 50}px`;
    anim.style.left = `${rect.left + rect.width / 2 - 50}px`;
    msg.style.top = `${rect.top + rect.height / 2 + 60}px`;
    msg.style.left = `${anim.style.left}`;
    overlay.style.display = anim.style.display = msg.style.display = 'block';
    setTimeout(() => {
        overlay.style.display = anim.style.display = msg.style.display = 'none';
    }, 1800);
}

// Vista previa de tarjeta (solo si usas formulario flotante)
function mostrarFormularioTarjeta() {
    document.getElementById("form-tarjeta-overlay").style.display = "flex";
}

function cerrarFormularioTarjeta() {
    document.getElementById("form-tarjeta-overlay").style.display = "none";
}

function actualizarPreview(campo, valor) {
    if (campo === "numero") {
        const num = valor.replace(/\D/g, '').padEnd(16, '•');
        document.getElementById("preview-numero").textContent =
            num.match(/.{1,4}/g).join(" ");
    } else if (campo === "nombre") {
        document.getElementById("preview-nombre").textContent = valor || "NOMBRE";
    } else if (campo === "fecha") {
        const [yyyy, mm] = valor.split("-");
        document.getElementById("preview-fecha").textContent = mm && yyyy ? `${mm}/${yyyy.slice(2)}` : "MM/YY";
    }
}
