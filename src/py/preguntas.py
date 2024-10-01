# preguntas.py
from flask import Flask, render_template, request, send_file

# Función para manejar el formulario
def submit():
    if request.method == 'POST':        
        nombre = request.form['nombre']  # Captura el dato del input con name='nombre'
        #return f'El nombre que enviaste es: {nombre}'        
        #return send_file('templates/submit.html', variable=nombre)
        #return f'<h2 id="resul" name="resul">nombre: {nombre}</h2>'
        #return render_template('templates/submit.html', nombre=nombre)
        return render_template('submit.html', nombre=nombre)
        #return render_template('submit.html', nombre=nombre)
        #return render_template('submit.html')
        #return send_file('templates/submit.html')
    # Si no es POST, puedes renderizar un formulario o redireccionar a otra página

    #return render_template('../templates/submit.html')

