const btnAudio = document.getElementById('play-sound');
const image = document.getElementById('play-sound-img');

const listaBotones = document.querySelectorAll('button');
const listaA = document.querySelectorAll('a');

//audio.play();
//audio.pause();

/*btnAudio.onclick = function () {
    playSonido();
    image.src = './audio/female-register.mp3';
};*/

function playSonido() {
	console.log(play);
	if (play) {
		document.getElementById('sound-ambient').pause();
		play = false;
	} else {
		document.getElementById('sound-ambient').play();
		play = true;
	}
}

document.addEventListener('DOMContentLoaded', () => {
	/*document.body.click();
    document.getElementById('name').click();*/
	listarBotones();
});

if (document.getElementById('register')) {
	document.getElementById('register').addEventListener('mouseenter', () => {
		/*const audio = new Audio('../static/audio/female-register.mp3');
        if (audio.paused) {
            audio.play();
            } */
	});
}

function listarBotones() {
	let audio = new Audio('../static/audio/Pharrell_Williams_Happy.mp3'); // Declara el audio fuera del loop
	let isPlaying = false;
	listaBotones.forEach(element => {
		//console.log(element);

		try {
			element.addEventListener('mouseenter', () => {
				/*const audio = new Audio('../static/audio/female-register.mp3');
                if (audio.paused) {
                    audio.play();
                const tooltipText = document.getElementById('tooltip-text');
                tooltipText.style.visibility = 'visible';
                tooltipText.style.opacity = '1';
                }*/
			});
		} catch (error) {}
	});

	/*listaA.forEach(element => {
        if (element.id == 'play-sound') {
            console.log(element);
        }

        try {
            element.addEventListener('click', () => {
                if (audio.paused) {
                    audio.play();
                    image.src = '/static/image/volume-mute-sound-speaker-w.png';
                }else{
                    audio.paused();
                    image.src = '/static/image/volume-max-sound-speaker-w.png';
                }
            });
        } catch (error) {

        }

    });*/
	listaA.forEach(element => {
		if (element.id == 'play-sound') {
			try {
				element.addEventListener('click', () => {
					if (audio.paused) {
						audio.play();
						image.src = '/static/image/volume-mute-sound-speaker-w.png';
					} else {
						audio.pause(); // Cambiado de paused() a pause()
						audio.currentTime = 0; // Opcional: reinicia el audio
						image.src = '/static/image/volume-max-sound-speaker-w.png';
					}
				});
			} catch (error) {
				console.error('Error al agregar el evento:', error);
			}
		}
	});
}
