# '''importar de archivos de modulos'''
from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
import sqlite3
import os
from datetime import datetime
import random
# '''importar de archivos de modulos'''

# region funciones para manejo de la base de datos
"""en este bloque se encuentran las funciones que interactuan con la base de datos sqlite de la aplicacion"""
# region configuración de la base de datos
"""esta varible es la encargada de ar la ruta de conexion a la base da datos sqlite la cual se esta ejecutando localmente"""
'''DATABASE = os.path.join(os.path.dirname(__file__), 'data', 'db', 'quiz.db')'''
DATABASE = os.path.join(os.path.dirname(
    os.path.dirname(__file__)), 'data', 'db', 'quiz.db')
# endregion configuración de la base de datos

# region funcion de conecxion a la base de datos sqlite
"""essta funcion se encarga de realizar una conexion a la base de datos sqlite"""


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn
# endregion funcion de conecxion a la base de datos sqlite


# region funcion para ejecutar script sqlite
"""esta fucion se encarga de ejecutar uan consulta para insertar, actualizar u eliminar registros de la base de datos"""


def execute_query(query, params=(), fetch_results=False):
    try:
        # Conectar a la base de datos
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row  # Configurar la fábrica de filas
        cursor = conn.cursor()

        # Ejecutar la consulta SQL con los parámetros
        cursor.execute(query, params)

        if fetch_results:
            results = cursor.fetchall()

        # Confirmar los cambios si no estamos en modo fetch_results
        if not fetch_results:
            conn.commit()

        # Cerrar la conexión
        conn.close()

        if fetch_results:
            return results

        return True
    except sqlite3.Error as e:
        # Imprimir el error para depuración
        # print(f"Error al ejecutar la consulta: {e}")
        return False


def execute_query1(query, params=(), fetch_results=False):
    """
    Ejecuta una consulta SQL en la base de datos.

    :param query: La consulta SQL a ejecutar.
    :param params: Los parámetros para la consulta SQL (si hay alguno).
    :param fetch_results: Si True, retorna los resultados de la consulta.
    :return: True si la consulta se ejecuta correctamente, False si ocurre un error, o los resultados si fetch_results es True.
    """
    try:
        # Conectar a la base de datos
        conn = sqlite3.connect('data/db/quiz.db')
        cursor = conn.cursor()

        # Ejecutar la consulta SQL con los parámetros
        cursor.execute(query, params)

        if fetch_results:
            results = cursor.fetchall()

        # Confirmar los cambios si no estamos en modo fetch_results
        if not fetch_results:
            conn.commit()

        # Cerrar la conexión
        conn.close()

        if fetch_results:
            return results

        return True
    except sqlite3.Error as e:
        # Imprimir el error para depuración
        # print(f"Error al ejecutar la consulta: {e}")
        return False

# endregion fucion para ejecutar script sqlite

# region funcion para capturar la fecha hora del equipo


def localtime():
    # Obtener la fecha y hora local actual
    local_now = datetime.now()
    # print("Fecha y hora local actual:", local_now)

    # Formatear la fecha y hora
    formatted_now = local_now.strftime('%Y-%m-%d %H:%M:%S')
    # print("Fecha y hora local formateada:", formatted_now)
    return formatted_now
# endregion funcion para capturar la fecha hora del equipo

# region funciones de tabla users

# region funcion de eliminacion de todos los registros de la tabla users


def delete_all_users():
    id_user = 1
    query = 'DELETE FROM users WHERE id <> ?'
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(query, (id_user,))
    results = cursor.fetchall()
    conn.close()
# endregion funcion de eliminacion de todos los registros de la tabla users

# region funcion de ruta para mostrar todos los usuarios


def all_users():
    query = 'SELECT * FROM users'
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()

    # print("Resultados de la consulta:", results)

    if results and isinstance(results, list):
        users = [dict(row) for row in results]
        # print("Usuarios:", users)
        return users
    else:
        # print("No se obtuvieron resultados o el formato no es el esperado.")
        return []


def test_all_users():
    query = 'SELECT * FROM users'
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()

    # print("Resultados de la consulta:", results)

    if results and isinstance(results, list):
        users = [dict(row) for row in results]
        # print("Usuarios:", users)
        return users
    else:
        # print("No se obtuvieron resultados o el formato no es el esperado.")
        return 0
# endregion funcion de ruta para mostrar todos los usuarios

# region funcion para insertar usuario nuevo


def insert_user(name, email):
    """
    Inserta un nuevo usuario en la base de datos.
    :param name: El nombre del usuario.
    :param email: El correo electrónico del usuario.
    :return: None
    """
    # Definir la consulta de inserción
    insert_query = 'INSERT INTO users (name, email,creation_date) VALUES (?,?,?)'

    # Definir los parámetros para la consulta
    params = (name, email, localtime())

    # Ejecutar la consulta
    success = execute_query(insert_query, params)

    # Informar si la operación fue exitosa o no
    if success:
         print("Datos insertados correctamente.")
    else:
         print("Error al insertar datos.")

# endregion funcion para insertar usuario nuevo

# region funcion para actualizar usuario


def update_user(name, email):
    """
    Inserta un nuevo usuario en la base de datos.
    :param name: El nombre del usuario.
    :param email: El correo electrónico del usuario.
    :return: None
    """
    # Definir la consulta de inserción
    update_query = 'UPDATE users SET name = ?, email = ?, creation_date = ? WHERE id = ?'

    # Llamar a la función para obtener el ID del usuario
    user_id = get_id_user(name, email)

    # Definir los parámetros para la consulta
    params = (name, email, localtime(), user_id)

    # Ejecutar la consulta
    success = execute_query(update_query, params)

    # Informar si la operación fue exitosa o no
    if success:
         print("{user_id }Datos actualizados correctamente.")
    else:
        print("Error al actualizar datos.")

# endregion funcion para actualizar usuario

# region funcion para eliminar usuario


def delete_user(name, email):
    """
    Inserta un nuevo usuario en la base de datos.
    :param name: El nombre del usuario.
    :param email: El correo electrónico del usuario.
    :return: None
    """
    # Definir la consulta de inserción
    delete_query = 'DELETE FROM users WHERE id = ?'

    # Llamar a la función para obtener el ID del usuario
    user_id = get_id_user(name, email)

    # Definir los parámetros para la consulta
    params = (user_id)

    # Ejecutar la consulta
    success = execute_query(delete_query, params)

    # Informar si la operación fue exitosa o no
    if success:
         print("Datos eliminados correctamente.")
    else:
         print("Error al eliminar datos.")

# endregion funcion para eliminar usuario

# region obtiene el ID del usuario basado en su nombre y correo electrónico.


def get_id_user(name, email):
    """
    Obtiene el ID del usuario basado en su nombre y correo electrónico.

    :param name: El nombre del usuario.
    :param email: El correo electrónico del usuario.
    :return: El ID del usuario si se encuentra, o None si no se encuentra.
    """
    # Definir la consulta SQL para seleccionar el ID del usuario basado en el nombre y correo electrónico
    select_query = 'SELECT id FROM users WHERE name = ? AND email = ?'

    # Definir los parámetros para la consulta
    params = (name, email)

    # Ejecutar la consulta y obtener los resultados
    results = execute_query(select_query, params, fetch_results=True)

    # Verificar si se encontró el usuario
    if results:
        # Retornar el ID del primer resultado (asumimos que el nombre y correo electrónico juntos son únicos)
        user_id = results[0][0]
        # print(f"El id del usario {user_id} en la base de datos.")
        return user_id
    else:
        # Usuario no encontrado
        return 0

# endregion Obtiene el ID del usuario basado en su nombre y correo electrónico.

# endregion funciones de tabla users

# region funciones de tabla users quiz

# region funcion de ruta para mostrar todos los quiz de usuario


def all_user_quiz():
    query = 'SELECT * FROM user_quiz'
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()

    # print("Resultados de la consulta:", results)

    if results and isinstance(results, list):
        user_quiz = [dict(row) for row in results]
        # print("Usuarios:", user_quiz)
        return user_quiz
    else:
        # print("No se obtuvieron resultados o el formato no es el esperado.")
        return []


def all_user_quiz_user(id_user):
    # Reemplaza 'user_id' con el nombre de la columna correcta
    query = 'SELECT * FROM user_quiz WHERE id_user = ?'
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(query, (id_user,))
    results = cursor.fetchall()
    conn.close()

    if results and isinstance(results, list):
        user_quiz = [dict(row) for row in results]
        # print(f"resultados de usuario {user_quiz}")
        return user_quiz
    else:
        # print("No se obtuvieron resultados o el formato no es el esperado.")
        return []


def test_all_user_quiz():
    query = 'SELECT * FROM user_quiz'
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()

    # print("Resultados de la consulta:", results)

    if results and isinstance(results, list):
        user_quiz = [dict(row) for row in results]
        # print("Usuarios:", user_quiz)
        return user_quiz
    else:
        # print("No se obtuvieron resultados o el formato no es el esperado.")
        return 0
# endregion funcion de ruta para mostrar todos los quiz de usuario

# region funcion para insertar quiz de usuario


def insert_user_quiz(user_id, level, total, correct, incorrect):
    """
    Inserta un nuevo usuario en la base de datos.
    :param name: El nombre del usuario.
    :param email: El correo electrónico del usuario.
    :return: None
    """
    # Definir la consulta de inserción
    insert_query = 'INSERT INTO user_quiz (id_user,quiz_level,question_total,question_correct,question_incorrect,creation_date) VALUES (?,?,?,?,?,?)'

    # Llamar a la función para obtener el ID del usuario
    # user_id = get_id_user(name, email)

    # Definir los parámetros para la consulta
    params = (user_id, level, total, correct, incorrect, localtime())

    # Ejecutar la consulta
    success = execute_query(insert_query, params)

    # Informar si la operación fue exitosa o no
    if success:
        print("Datos insertados correctamente.")
    else:
        print("Error al insertar datos.")

# endregion funcion para insertar quiz de usuario

# region funcion para actualizar quiz de usuario


def update_user_quiz(name, email):
    """
    Inserta un nuevo usuario en la base de datos.
    :param name: El nombre del usuario.
    :param email: El correo electrónico del usuario.
    :return: None
    """
    # Definir la consulta de inserción
    update_query = 'UPDATE user_quiz SET name = ?, email = ?, creation_date = ? WHERE id = ?'

    # Llamar a la función para obtener el ID del usuario
    user_quiz_id = get_id_user_quiz(name, email)

    # Definir los parámetros para la consulta
    params = (name, email, localtime(), user_quiz_id)

    # Ejecutar la consulta
    success = execute_query(update_query, params)

    # Informar si la operación fue exitosa o no
    if success:
        print("{user_quiz_id }Datos actualizados correctamente.")
    else:
        print("Error al actualizar datos.")

# endregion funcion para actualizar quiz de usuario

# region funcion para eliminar quiz de usuario


def delete_user_quiz(name, email):
    """
    Inserta un nuevo usuario en la base de datos.
    :param name: El nombre del usuario.
    :param email: El correo electrónico del usuario.
    :return: None
    """
    # Definir la consulta de inserción
    delete_query = 'DELETE FROM user_quiz WHERE id = ?'

    # Llamar a la función para obtener el ID del usuario
    user_quiz_id = get_id_user_quiz(name, email)

    # Definir los parámetros para la consulta
    params = (user_quiz_id)

    # Ejecutar la consulta
    success = execute_query(delete_query, params)

    # Informar si la operación fue exitosa o no
    if success:
        print("Datos eliminados correctamente.")
    else:
         print("Error al eliminar datos.")

# endregion funcion para eliminar quiz de usuario

# region obtiene el ID del usuario basado en su nombre y correo electrónico.


def get_id_user_quiz(name, email):
    """
    Obtiene el ID del usuario basado en su nombre y correo electrónico.

    :param name: El nombre del usuario.
    :param email: El correo electrónico del usuario.
    :return: El ID del usuario si se encuentra, o None si no se encuentra.
    """
    # Definir la consulta SQL para seleccionar el ID del usuario basado en el nombre y correo electrónico
    select_query = 'SELECT id FROM user_quiz WHERE name = ? AND email = ?'

    # Definir los parámetros para la consulta
    params = (name, email)

    # Ejecutar la consulta y obtener los resultados
    results = execute_query(select_query, params, fetch_results=True)

    # Verificar si se encontró el usuario
    if results:
        # Retornar el ID del primer resultado (asumimos que el nombre y correo electrónico juntos son únicos)
        user_quiz_id = results[0][0]
        # print(f"El id del usario {user_quiz_id} en la base de datos.")
        return user_quiz_id
    else:
        # Usuario no encontrado
        return 0

# endregion Obtiene el ID del usuario basado en su nombre y correo electrónico.

# endregion funciones de tabla users quiz

# region funciones de la tabla admin quiz

# region funcion para la eliminacion de todos los registros de la tabla admin quiz


def delete_all_users():
    id_user = 1
    query = 'DELETE FROM admin_quiz WHERE id_user <> ?'
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(query, (id_user,))
    results = cursor.fetchall()
    conn.close()
# endregion funcion para la eliminacion de todos los registros de la tabla admin quiz

# endregion funciones de la tabla admin quiz

# endregion funciones para menejo de la base de datos
