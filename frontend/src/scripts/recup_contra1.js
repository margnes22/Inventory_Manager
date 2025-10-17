(function(){
	'use strict';

	// Elementos
	const form = document.getElementById('recoveryForm');
	const codeInput = document.getElementById('code');
	const backBtn = document.querySelector('.back-button');

	// Volver al login (intenta navegar a login.html en la carpeta Login)
	if(backBtn){
		backBtn.addEventListener('click', function(){
			// Intentar navegar a la página de login en el proyecto
			const possiblePath = '/frontend/src/pages/recup_contra.html';
			// Si la página existe en producción, se redirigirá; en demo solo cambiamos location
			location.href = possiblePath;
		});
	}

	// Validación simple de código de 6 dígitos
	function isValidCode(code){
		return /^\d{6}$/.test(code);
	}

	if(form && codeInput){
		form.addEventListener('submit', function(e){
			e.preventDefault();
			const code = codeInput.value.trim();
			if(!code){
				alert('Por favor ingresa el código de verificación');
				codeInput.focus();
				return;
			}
			if(!isValidCode(code)){
				alert('El código debe tener solo numeros y 6 dígitos');
				codeInput.focus();
				return;
			}

			// Simular verificación con el servidor
			console.log('Verificando código:', code);
			// Aquí iría un fetch POST al endpoint real de verificación
			// fetch('/api/verify-code', { method: 'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({ code }) })...

			// Mostrar mensaje de éxito y redirigir al cambio de contraseña
			alert('Código verificado. Serás redirigido para crear una nueva contraseña.');
			// Ejemplo de redirección (ajusta la ruta según tu proyecto)
			location.href = '/frontend/src/pages/recup_contra2.html';
		});
	}

})();

