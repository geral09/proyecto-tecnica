
preguntas = [
    {
        "pregunta": "¿fCuál es el tiempo verbal incorrecto en la siguiente frase? 'She have a dog.'",
        "opciones": ["A) have", "B) is having", "C) has", "D) haves"],
        "respuesta_correcta": "D"
    },
    {
        "pregunta": "¿Qué significa 'to chill out' en inglés?",
        "opciones": ["A) Estar helado", "B) Relajarse", "C) Estar emocionado", "D) Tener calor"],
        "respuesta_correcta": "B"
    },
    {
        "pregunta": "¿Cuál es el plural de 'child'?",
        "opciones": ["A) childs", "B) childes", "C) children", "D) child's"],
        "respuesta_correcta": "C"
    }
]

def presentar_cuestionario(preguntas):
    puntaje = 0
    for pregunta in preguntas:
        print(pregunta["pregunta"])
        for opcion in pregunta["opciones"]:
            print(opcion)
        
        respuesta_usuario = input("Ingrese la opción correcta (A, B, C, o D): ").upper()
        
        if respuesta_usuario == pregunta["respuesta_correcta"]:
            print("¡Respuesta correcta!\n")
            puntaje += 1
        else:
            print(f"Respuesta incorrecta. La respuesta correcta era {pregunta['respuesta_correcta']}.\n")
    
    print(f"Has terminado el cuestionario. Puntaje total: {puntaje}/{len(preguntas)}")

    return puntaje

if __name__ == "__main__":
    puntaje_final = presentar_cuestionario(preguntas)
    # Aquí podrías guardar el puntaje final en una base de datos o archivo si lo deseas
