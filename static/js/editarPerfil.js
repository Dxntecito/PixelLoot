let editMode = false;

document.getElementById('editar-btn').addEventListener('click', async function () {
    const inputs = document.querySelectorAll('#prf-informacion .form-control');
    const selects = document.querySelectorAll('#prf-informacion .form-select');

    if (!editMode) {
        // Activar edición
        inputs.forEach(input => {
            input.removeAttribute('readonly');
            input.style.backgroundColor = 'rgba(224, 224, 224, 0.3)';
        });
        selects.forEach(select => {
            select.removeAttribute('disabled');
            select.style.backgroundColor = 'rgba(224, 224, 224, 0.3)';
        });
        this.textContent = 'Confirmar Cambios';
        editMode = true;
    } else {
        // Recolectar datos
        const data = {
            username: document.getElementById('input-username').value,
            nombre: document.getElementById('input-nombre').value,
            correo: document.getElementById('input-correo').value,
            password: document.getElementById('input-password').value,
            telefono: document.getElementById('input-telefono').value,
            genero: document.getElementById('input-genero').value,
            pais: document.getElementById('pais-select').value,
            fecha_nacimiento: "2000-01-01" // puedes hacerlo dinámico luego si lo necesitas
        };

        try {
            const response = await fetch('/editar_perfil', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });

            const result = await response.json();

            if (result.success) {
                alert("Cambios guardados correctamente! 💜");
                // Forzar recarga para ver datos actualizados
                window.location.reload();
            } else {
                alert("Error al guardar cambios: " + result.message);
            }

        } catch (error) {
            console.error("Error en fetch:", error);
            alert("Error de red al guardar cambios");
        }
    }
});


document.getElementById('prf-imagenes-fondoPerfilInput').addEventListener('change', function() {
    const reader = new FileReader();
    reader.onload = function(e) {
        document.getElementById('prf-imagenes-encabezado').src = e.target.result;
    }
    reader.readAsDataURL(this.files[0]);
});

document.getElementById('prf-imagenes-perfilInput').addEventListener('change', function() {
    const reader = new FileReader();
    reader.onload = function(e) {
        document.getElementById('prf-imagenes-foto-perfil').src = e.target.result;
    }
    reader.readAsDataURL(this.files[0]);
});

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('prf-imagenes-cambiar-fondo').addEventListener('click', function(event) {
        event.preventDefault();
        document.getElementById('prf-imagenes-fondoPerfilInput').click();
    });

    document.getElementById('prf-imagenes-cambiar-perfil').addEventListener('click', function(event) {
        event.preventDefault();
        document.getElementById('prf-imagenes-perfilInput').click();
    });

    // Toggle password visibility
    const togglePassword = document.querySelector('.tem_juego_5');
    const passwordField = document.querySelector('.form-control[type="password"]');

    togglePassword.addEventListener('click', function() {
        const type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';
        passwordField.setAttribute('type', type);
        this.innerHTML = type === 'password' ? '<i class="fa-regular fa-eye"></i>' : '<i class="fa-regular fa-eye-slash"></i>';
    });
});