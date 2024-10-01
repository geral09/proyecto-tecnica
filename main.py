# region Importa las funciones principales de flask y librerias necesarias
# '''importar de archivos de modulos'''
import random
from modules.bd import all_user_quiz_user, get_id_user, all_users, insert_user, insert_user_quiz
from modules.questions import levels, questions_beginner, questions_intermediate, questions_advanced, questions, texts_advanced, add_lectura
from modules.funciones import saludar, numero_letra, list_ramdom, text_list_ramdom, text_string
from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
# Configuración básica de logging
import logging
logging.basicConfig(level=logging.INFO)
# '''importar de archivos de modulos'''

# '''importar de archivos de modulos'''

# '''importar de archivos de modulos'''


# endregion Importa las funciones principales de flask y librerias necesarias

# region propiedades de aplicacion flask
app = Flask(__name__)
# Necesario para usar sesiones
app.secret_key = 'supersecretkey'
# endregion propiedades de aplicacion flask

'''recorte de array'''

# region varibles Globales
"""en este bloque se encuentran todas las variables globales usadas"""

current_question_index = 0
user_answers = []
score = 0
total_questions = len(questions)
selected = None
authors = "Gerhard Medina , Camilo Estupiñan y Brian Chacon"
title_login = "Registro"
title_level = "Nivel"
title_test = "Test de Ingles"
title_result = "Resultados de Test"
title_record = "Historial de Test"
form_class_size = "form_quiz"
class_question = "questions"
reading_title = ""
reading_text = ""
selected_option = ""
questions_only = []
# endregion varibles Globales

# region registrar la función como un contexto de plantilla en html
# Registrar la función como un contexto de plantilla


@ app.context_processor
def utility_processor():
    return dict(numero_letra=numero_letra, list_ramdom=list_ramdom, text_list_ramdom=text_list_ramdom)

# endregion registrar la función como un contexto de plantilla en html


'''recorte de funciones de base de datos'''

# region funcion ruta de inicio por defecto


@ app.route('/')
def start():
    set_reading_text()
    # print(saludar('jorge'))
    # retorna la pagina con las varibles
    return render_template('login.html', authors=authors, title=title_login)

# endregion funcion ruta de inicio por defecto

# region funcion de ruta de redireccion de eleccion de nivel de quiz


@ app.route('/level')
def level():

    quiz_user = all_user_quiz_user(get_id_user(name, email))
    tamano_quiz_user = len(quiz_user)

    # retorna la pagina con las varibles
    authors_string = " , ".join(authors)
    return render_template('level.html', authors=authors, levels=levels, name=name, email=email, size=tamano_quiz_user, title=title_level)

# endregion funcion de ruta de redireccion de eleccion de nivel de quiz

# region funcion de ruta de login de registro e ingreso


@ app.route('/login')
def login():
    # global name, email
    # print(saludar('jorge'))
    return render_template('login.html', authors=authors, title=title_login)
# endregion funcion de ruta de login de registro e ingreso

# region funcion de ruta de acceso a la aplicacion


@ app.route('/accses', methods=['POST'])
def accses():
    global name, email
    # captura los valores de lso capos de texto
    name = request.form.get('name')
    email = request.form.get('email')

    # optenemos todos los usuarios de la base de datos
    users = all_users()
    # print(f"Resulatdos {users}")

    # if len(users) > 0:
    #    # Recorrer la lista de
    #     for user in users:
    #         print(f"ID: {user['id']}")
    #         print(f"Name: {user['name']}")
    #         print(f"Email: {user['email']}")
    #         print(f"Creation Date: {user['creation_date']}")
    #         print("-" * 40)  # Separador para claridad
    # else:
    #     print(f"no hay datos")
    #     print("-" * 40)  # Separador para claridad

    # Llamar a la función para obtener el ID del usuario
    user_id = get_id_user(name, email)

    quiz_user = all_user_quiz_user(user_id)
    tamano_quiz_user = len(quiz_user)

    if user_id > 0:
        print(f"El id del usario es {user_id} existe.\n")
    else:
        print(f"El id del usario es {user_id} no existe. sera registrado\n")
        # inserta el usuario nuevo
        insert_user(name, email)
    # retorna la pagina con las varibles
    return render_template('level.html', authors=authors, levels=levels, name=name, email=email, size=tamano_quiz_user, title=title_level)

# endregion funcion de ruta de acceso a la aplicacion

# region funcion de ruta de eleccion de nivel de la aplicacion


@ app.route('/level_quiz', methods=['POST'])
def level_quiz():
    global selected, questions, reading_text, reading_title
    # print("Nivel selccionado", selected)
    # print(questions_beginner)
    # print("questions_intermediate ",questions_intermediate)
    # print("questions_advanced ", questions_advanced)
    if not selected:
        flash(
            'No se ha seleccionado un nivel . Por favor, realiza una selección.', 'warning')
        return redirect(url_for('level'))
    else:
        if selected == "Principiante":
            questions = questions_beginner
        elif selected == "Intermedio":
            questions = questions_intermediate
        elif selected == "Avanzado":
            questions = questions_advanced
        return redirect(url_for('index'))
# endregion funcion de ruta de eleccion de nivel de la aplicacion

# region funcion de ruta de interface de quiz


@ app.route('/index')
def index():
    global current_question_index, question, questions, form_class_size, reading_text, reading_title

    random.shuffle(questions)
    # /app.logger.info("texto  ", lectura)  # Imprimir en consola
    if current_question_index >= len(questions):
        return redirect(url_for('result'))

    if selected == "Avanzado":
        form_class_size = "form_quiz_avanzado"
        class_question = "questions_avanzado"
    else:
        form_class_size = "form_quiz"
        class_question = "questions"

        # carga la pregunta atual
    question = questions[current_question_index]

    # lectura = [item["question"] for item in questions_advanced]
    # print(lectura)
    # reading_text = text_string(add_lectura(questions_advanced), " ")
    # reading_text = lectura

    # Extraer solo las preguntas
    questions_only = [item["question"] for item in questions]

    total_questions = len(questions)

    if selected == "Avanzado":
        for index, quest in enumerate(questions):
            if "title" in quest:
                print(
                    f"La pregunta {index + 1} tiene un título: {quest['title']}")
                reading_index = int(questions[current_question_index]['title'])
                reading_title = texts_advanced[reading_index]["title"]
                reading_text = texts_advanced[reading_index]["text"]
            # else:
            #     print(f"La pregunta {index + 1} no tiene un título.")

    # retorna la pagina con las varibles
    return render_template('index.html', authors=authors, question=question, questions_only=questions_only, levels=levels, score=score, total_questions=total_questions, index=current_question_index, selected=selected, name=name, email=email, title=title_test, form_class_size=form_class_size, class_question=class_question, reading_text=reading_text, reading_title=reading_title)

# endregion funcion de ruta de interface de quiz

# region funcion de ruta  que carga y guarda las respuestas elegidas por el usuario


@ app.route('/answer', methods=['POST'])
# funcion que pasa a la otra pregunta
def answer():
    global current_question_index, user_answers, score, questions_only, reading_text
    selected_option = request.form['option']
    correct_answer = questions[current_question_index]['answer']

    # Guardar la respuesta del usuario
    user_answers.append(selected_option)

    print(f"la respuestas ", user_answers)

    if selected == "Avanzado":
        # print(            f"la respuesta de la pregunta {current_question_index+1} selecionada es ", selected_option)
        # print(f"la preguntas ", questions[current_question_index]['question'])
        #    print(f"la  selecionada es {selected} ",reading_text_value)
        # = reading_text.split('______')
        # Dividir el texto por comas
        # resultadoarr = resultado.split(',')

        # valor = resultado[current_question_index] + ' ' + selected_option
        # Reemplazar "manzana" por "kiwi"
        # for i in range(len(resultado)):
        #     if i == current_question_index:
        #         resultado[i] = valor
        #     else:
        #       resultado[i]+='______'
        # reading_text = ' '.join(resultado).replace('______ ______', '______')
        # print(f"la resultado ", resultado)
        # reading_text=questions[current_question_index]['question']+selected_option

        # print(f"la respuesta del ususario {user_answers}")

        # Actualizar el puntaje
        if selected_option == correct_answer:
            score += 1

    # Avanzar a la siguiente pregunta
    current_question_index += 1

# retorna la pagina de inicio  de las preguntas
    return redirect(url_for('index'))

# endregion

# region funcion de ruta que carga la vista del total de las preguntas


@ app.route('/result')
# funcion que se en cargar las funciones correctas y incorrectas
def result():
    global current_question_index, user_answers, score, questions_beginner, questions_intermediate, questions_advanced, reading_text
    total_questions = len(questions)
    correct_answers = score
    incorrect_answers = total_questions - correct_answers
    gif_result = "../static/gif/good_job.gif"

    # Reiniciar el estado global para la próxima vez
    current_question_index = 0
    user_answers = []
    score = 0
    # print("preguntas por defecto ", questions_advanced_init)
    # selected = None
    # name = ""
    # email = ""

    # Llamar a la función para obtener el ID del usuario
    user_id = get_id_user(name, email)

    quiz_user = all_user_quiz_user(user_id)
    tamano_quiz_user = len(quiz_user)

    insert_user_quiz(user_id, selected, total_questions,
                     correct_answers, incorrect_answers)

    # Calcula el porcentaje de respuestas correctas
    percentage = (correct_answers / total_questions) * 100

    # Determina qué GIF mostrar basado en el porcentaje
    if percentage == 100 or percentage >= 90:
        gif_result = "../static/gif/good_job.gif"
    elif 50 <= percentage < 80:
        gif_result = "../static/gif/medium_job.gif"
    else:
        gif_result = "../static/gif/bad_job.gif"

# retorna la paguina de resultados
    return render_template('result.html', authors=authors, correct=correct_answers, incorrect=incorrect_answers, total=total_questions, selected=selected, name=name, email=email, size=tamano_quiz_user, title=title_result, gif_result=gif_result, percentage=percentage)

# endregion funcion de ruta que carga la vista del total de las preguntas

# region funcion de ruta que carga los quiz realizados por el usuario


@ app.route('/record')
def record():
    # Llamar a la función para obtener el ID del usuario
    user_id = get_id_user(name, email)
    # optenemos todos los usuarios de la base de datos
    user_quiz = all_user_quiz_user(user_id)
    # print(f"Resulatdos {user_quiz}")

    # if len(user_quiz) > 0:
    # Recorrer la lista de
    #     for user in user_quiz:
    #         if user['id_user'] == user_id:
    #             print(f"User: {user['id_user']}")
    #             print(f"Level: {user['quiz_level']}")
    #             print(f"Total: {user['question_total']}")
    #             print(f"Correct: {user['question_correct']}")
    #             print(f"Incorrect: {user['question_incorrect']}")
    #             print(f"Creation Date: {user['creation_date']}")
    #             print("-" * 40)  # Separador para claridad
    # else:
    #     print(f"no hay datos")
    #     print("-" * 40)  # Separador para claridad

    # retorna la paguina de resultados
    return render_template('record.html', authors=authors, name=name, user_quiz=user_quiz, title=title_record)

# endregion funcion de ruta que carga los quiz realizados por el usuario

# region funcion de ruta que captura la seleccion de nivel en tiempo real


@ app.route('/selected_item', methods=['POST'])
def selected_item():
    global selected
    selected = request.json.get('item')
    return jsonify({'selected_item': selected})


# endregion funcion de ruta que captura la seleccion de nivel en tiempo real

def set_reading_text():
    global reading_text
    # print("text ", add_lectura())
    reading_text = add_lectura()


# region funcion de ruta que inicializa toda la aplicacion
# se encarga de iniciar toda la aplicacion
if __name__ == '__main__':
    set_reading_text()
    app.run(debug=False)
    # app.run(debug=True)


# endregion funcion de ruta que inicializa toda la aplicacion
