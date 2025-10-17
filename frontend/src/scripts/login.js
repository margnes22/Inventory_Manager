(function(){
    'use strict';

    // Toggle password visibility
    const pwd = document.getElementById('password');
    const toggle = document.getElementById('togglePwd');
    const eyeOpen = document.getElementById('eyeOpen');
    const eyeClosed = document.getElementById('eyeClosed');

    if(toggle && pwd){
        toggle.addEventListener('click', function(){
            const isPwd = pwd.getAttribute('type') === 'password';
            pwd.setAttribute('type', isPwd ? 'text' : 'password');
            if(eyeOpen && eyeClosed){
                eyeOpen.style.display = isPwd ? 'none' : 'inline';
                eyeClosed.style.display = isPwd ? 'inline' : 'none';
            }
            toggle.setAttribute('title', isPwd ? 'Ocultar contraseña' : 'Mostrar contraseña');
        });
    }

    // basic form validation demo
    const form = document.getElementById('loginForm');
    if(form){
        form.addEventListener('submit', function(e){
            e.preventDefault();
            const username = document.getElementById('username').value.trim();
            const password = pwd ? pwd.value : '';
            if(!username){
                alert('Por favor ingresa tu usuario');
                return;
            }
            if(!password){
                alert('Por favor ingresa tu contraseña');
                return;
            }

            // Aquí se enviaría el formulario al servidor (fetch / XHR)
            // Demo: mostrar datos en consola y simular redirección
            console.log({username, password});
            // Simular éxito
            const success = true;
            if(success){
                // reemplaza por la URL real en producción
                alert('Inicio de sesión exitoso (demo)');
                // location.href = '/dashboard.html';
            }
        });
    }

})();