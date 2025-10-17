(function(){
	'use strict';

	// Elementos
	const form = document.getElementById('recoveryForm');
	const emailInput = document.getElementById('email');
	const backBtn = document.querySelector('.back-button');

	// Volver al login (intenta navegar a login.html en la carpeta Login)
	if(backBtn){
		backBtn.addEventListener('click', function(){
			// Intentar navegar a la página de login en el proyecto
			const possiblePath = '/frontend/src/pages/login.html';
			// Si la página existe en producción, se redirigirá; en demo solo cambiamos location
			location.href = possiblePath;
		});
	}

	// Validación simple de email
	function isValidEmail(email){
		return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
	}

	if(form && emailInput){
		form.addEventListener('submit', function(e){
			e.preventDefault();
			const email = emailInput.value.trim();
			if(!email){
				alert('Por favor ingresa tu correo electrónico');
				emailInput.focus();
				return;
			}
			if(!isValidEmail(email)){
				alert('Por favor ingresa un correo electrónico válido');
				emailInput.focus();
				return;
			}

			// Simular envío al servidor
			console.log('Solicitando código de recuperación para:', email);
			// Aquí iría un fetch POST al endpoint real
			// fetch('/api/recover', { method: 'POST', body: JSON.stringify({ email }) })...

			// Mostrar mensaje de éxito y opcionalmente redirigir
			alert('Si el correo existe en nuestro sistema, recibirás un email con instrucciones.');
			// Opcional: redirigir al login
			location.href = '/frontend/src/pages/recup_contra1.html';
		});
	}

})();

