# modulos/funciones.py
import os
import random


def saludar(nombre):
    DATABASE = os.path.join(os.path.dirname(__file__), 'data', 'db', 'quiz.db')
    # Suponiendo que este script está en 'modulos'
    ruta_db = os.path.join(os.path.dirname(
        os.path.dirname(__file__)), 'data', 'db', 'quiz.db')
    return f"Hola, {nombre}! la conexion es, {DATABASE} la ruta correcta es {ruta_db}  "


def numero_letra(numero):
    if 1 <= numero <= 26:
        return chr(64 + numero)
    return None


def list_ramdom(lista):
    random.shuffle(lista)
    # random.sample(lista, len(lista))


def text_list_ramdom(lista):
    # print("llega ",lista)
    # print("convierto ",opciones)
    # random.shuffle(lista)
    lista_mezclada = random.sample(lista, len(lista))
    return lista_mezclada


def text_string(list, separator):
    # Convertir la lista en un solo texto
    texto_unido = separator.join(list)

    # Mostrar el resultado
    return texto_unido
