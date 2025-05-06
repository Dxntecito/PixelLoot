
let editMode = false;

document.getElementById('editar-btn').addEventListener('click', function() {
    const inputs = document.querySelectorAll('#prf-informacion .form-control');
    const selects = document.querySelectorAll('#prf-informacion .form-select');
    
    if (!editMode) {
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
        inputs.forEach(input => {
            input.setAttribute('readonly', true);
            input.style.backgroundColor = '#E0E0E0';
        });
        selects.forEach(select => {
            select.setAttribute('disabled', true);
            select.style.backgroundColor = '#E0E0E0';
        });
        this.textContent = 'Editar Información';
        editMode = false;
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