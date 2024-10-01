const init = () => {
	console.log('Init function called');
};

let selectedItem = null;

function updateSelectedItem(item, element) {
	try {
		// Deshabilitar el ítem seleccionado
		if (selectedItem) {
			document.querySelectorAll('li').forEach(li => li.classList.remove('disabled'));
		}
		selectedItem = item;

		// Hacer la solicitud AJAX para enviar el ítem seleccionado
		fetch('/selected_item', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({ item: item })
		})
			.then(response => response.json())
			.then(data => {
				document.getElementById('selected-item').textContent = `Seleccionaste el nivel: ${data.selected_item}`;

				// Inhabilitar los ítems no seleccionados
				document.querySelectorAll('li').forEach(li => {
					if (li.textContent !== data.selected_item) {
						li.classList.add('disabled');
					}
					document.getElementById('start_quiz').classList.remove('disabled');
				});
			});
	} catch (e) {
		// Manejo del error
		console.error('Ocurrió un error:', e.message);
	}
}

window.addEventListener('load', function() {
	// Tu código aquí, que se ejecutará después de que todos los recursos se hayan cargado
	console.log('Todos los recursos de la página se han cargado.');
	reading_text();
});

// Habilitar los ítems cuando la página se carga
document.addEventListener('DOMContentLoaded', () => {
	try {
		// document.querySelectorAll('li').forEach(li => {
		// 	li.addEventListener('click', function() {
		// 		updateSelectedItem(this.textContent, this);
		// 	});
		// });
		// //document.querySelector('input').classList.add('disabled');
		if (document.getElementById('select-again')) {
			// Agrega un manejador de eventos
			document.getElementById('select-again').addEventListener('click', function() {
				document.querySelectorAll('li').forEach(li => li.classList.remove('disabled'));
				document.getElementById('selected-item').textContent = '';
				document.getElementById('selected-item').textContent = 'Seleccione el nivel :';
				selectAgain();

				document.getElementById('img-info-nivel').src = `static/image/inicial.png`;
			});
		}
		if (document.getElementById('name')) {
			document.getElementById('name').classList.remove('disabled');
		}
		selectAgain();
		reading_text();
		// alert(document.body.clientWidth,"  ",document.body.clientHeight);
	} catch (e) {
		// Manejo del error
		console.error('Ocurrió un error:', e.message);
	}
});

function selectAgain() {
	try {
		document.querySelectorAll('li').forEach(li => {
			li.addEventListener('click', function() {
				updateSelectedItem(this.textContent, this);
				//alert(this.textContent.toLocaleLowerCase());
				///static/image/exit-w.png
				document.getElementById('img-info-nivel').src = `static/image/${this.textContent.toLocaleLowerCase()}.png`;
			});
		});
		if (document.getElementById('start_quiz')) {
			document.getElementById('start_quiz').classList.add('disabled');
		}
	} catch (e) {
		// Manejo del error
		console.error('Ocurrió un error:', e.message);
	}
}

function reading_text() {
	try {
		let respuesta = '';
		let texto = '';
		let pregunta = '';
		if (document.getElementById('question')) {
			pregunta = document.getElementById('question').innerText;
		}
		if (document.getElementById('reading_text')) {
			texto = document.getElementById('reading_text').innerText;
			const frutas = texto.split('______'); // Separar por coma
			//console.log(frutas); // ["manzana", "banana", "naranja"]
			for (let i = 0; i < frutas.length; i++) {
				//console.log(frutas[i]); // Imprime cada fruta
			}

			// const seleccionado = document.querySelectorAll('input[type="radio"');

			// console.log('Seleccionado:', seleccionado);
			// const radios = document.querySelectorAll('input[name="opcion"]');

			// for (const radio of radios) {
			// 	if (radio.checked) {
			// 		mensaje += radio.value;
			// 		console.log('Seleccionado:', mensaje);
			// 		break;
			// 	}
			// }
			document.querySelectorAll('input[type="radio"]').forEach(radio => {
				radio.addEventListener('click', () => {
					respuesta = `${radio.value}`;
					var delline=pregunta.replace("______","");
					//1document.getElementById('mensaje').innerText = mensaje;
					console.log('Seleccionado:', respuesta);
					console.log('Texto:',texto);
					console.log('Pregunta:', pregunta);
					document.getElementById('question').innerHTML=delline+' <u id="reply">'+respuesta+'</u>';
					// document.getElementById('reply').innerText=respuesta;

				});
			});

			// // document.getElementById('mensaje').innerText = mensaje;

			// // if (seleccionado) {
			// // 	console.log('Seleccionado:', seleccionado.value);
			// // } else {
			// // 	console.log('No se ha seleccionado ninguna opción.');
			// // }
		}
	} catch (e) {
		// Manejo del error
		console.error('Ocurrió un error:', e.message);
	}
}
