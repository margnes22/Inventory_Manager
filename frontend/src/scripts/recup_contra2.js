(function(){
	'use strict';

    const backBtn = document.querySelector('.back-button');

	// Volver al login (intenta navegar a login.html en la carpeta Login)
	if(backBtn){
		backBtn.addEventListener('click', function(){
			// Intentar navegar a la página de login en el proyecto
			const possiblePath = '/frontend/src/pages/recup_contra1.html';
			// Si la página existe en producción, se redirigirá; en demo solo cambiamos location
			location.href = possiblePath;
		});
	}
	// Toggle visibility for both password fields
	const pwd1 = document.getElementById('password1');
	const pwd2 = document.getElementById('password2');

	const toggle1 = document.getElementById('togglePwd1');
	const eyeOpen1 = document.getElementById('eyeOpen1');
	const eyeClosed1 = document.getElementById('eyeClosed1');

	const toggle2 = document.getElementById('togglePwd2');
	const eyeOpen2 = document.getElementById('eyeOpen2');
	const eyeClosed2 = document.getElementById('eyeClosed2');

	function attachToggle(toggleEl, pwdEl, openEl, closedEl){
		if(toggleEl && pwdEl){
			toggleEl.addEventListener('click', function(){
				const isPwd = pwdEl.getAttribute('type') === 'password';
				pwdEl.setAttribute('type', isPwd ? 'text' : 'password');
				if(openEl && closedEl){
					openEl.style.display = isPwd ? 'none' : 'inline';
					closedEl.style.display = isPwd ? 'inline' : 'none';
				}
				toggleEl.setAttribute('title', isPwd ? 'Ocultar contraseña' : 'Mostrar contraseña');
			});
		}
	}

	attachToggle(toggle1, pwd1, eyeOpen1, eyeClosed1);
	attachToggle(toggle2, pwd2, eyeOpen2, eyeClosed2);

	// form validation for reset
	const form = document.getElementById('resetForm');
	if(form){
		form.addEventListener('submit', function(e){
			e.preventDefault();
			const p1 = pwd1 ? pwd1.value.trim() : '';
			const p2 = pwd2 ? pwd2.value.trim() : '';

			if(!p1 || !p2){
				alert('Por favor completa ambos campos de contraseña');
				return;
			}
			if(p1.length < 8){
				alert('La contraseña debe tener al menos 8 caracteres');
				return;
			}
			if(p1 !== p2){
				alert('Las contraseñas no coinciden');
				return;
			}

			// Simular envío al servidor para guardar nueva contraseña
			console.log('Guardando nueva contraseña (demo)');
			alert('Tu contraseña ha sido actualizada correctamente.');
			// Redirigir al login (ruta relativa desde esta página)
			location.href = '/frontend/src/pages/login.html';
		});
	}

})();

