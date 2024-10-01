function ajustarNivelAvanzado() {
	if (document.getElementById('textarea-container')) {
		document.getElementById('form-questions').style.height = 'auto';
		alert(documentd.getElementByI('form-questions').style.height);
	}
}

document.addEventListener('DOMContentLoaded', () => {
	console.log('Todo el contenido de la página ha sido completamente cargado.');
	console.log(document.getElementById('form-questions').style.height);
});

window.addEventListener('load', function() {});
