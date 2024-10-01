
def hacer_preguntas():
    preguntas = [
        "Please leave your room by 11 AM? A) In a Inn B) In a Cottage C) In a school D) In a room",
        "Please stand behind the yellow line? A) In a hardware store B) In a station plataform C) In a bakery D) In a school"
        "Your tray table should be in the upright position for take -off and landing? A) In a boat B) In a boat C) In a airport D) In a airplane",
        "There will be one interval of sisteen minutes? A) In a theater B) In a hall C) In a movie theater D) In a Field",
        "Get 2 tent pay 1? A) In a museum B) At an airport C) In a camping site D) In a room",
        "Do not swim alone? A) On a tub B) In the shower C) In a theater D) At a beach",
        "Bed and breafast? A) In  furniture store B) In a swiming pool C) Artist D) In an Inn",
        "Field closed for maintenance? A) In a movie theater B) In a sports club C) In a nursery center D) In a Hospital",
        "Children playing? A) In a butchery B) In a art gallery C)In a playground D) In a  hall",
        "Special meat and chicken? A) In a butchery B) In a bakery C) In a nursery center D)In a hardware store"
    ]

 
    respuestas_correctas = [
        "A", "B", "A", "A", "C", "D", "D", "B", "C", "A"
    ]

    respuestas_usuario = []

    for i, pregunta in enumerate(preguntas, start=1):
        respuesta = input(f"{pregunta} ")
        respuestas_usuario.append(respuesta)

        if respuesta.upper() == respuestas_correctas[i - 1]:
            print("¡Respuesta correcta!\n")
        else:
            print(f"Respuesta incorrecta. La respuesta correcta era {respuestas_correctas[i - 1]}\n")

    print("\n¡Gracias por responder las preguntas!")
    print("Tus respuestas fueron:")
    for i, respuesta in enumerate(respuestas_usuario, start=1):
        print(f"{i}. {respuesta}")

def hacer_preguntas():
    preguntas = [
        "Please leave your room by 11 AM? A) In a Inn B) In a Cottage C) In a school D) In a room",
        "Please stand behind the yellow line? A) In a hardware store B) In a station plataform C) In a bakery D) In a school"
        "Your tray table should be in the upright position for take -off and landing? A) In a boat B) In a boat C) In a airport D) In a airplane",
        "There will be one interval of sisteen minutes? A) In a theater B) In a hall C) In a movie theater D) In a Field",
        "Get 2 tent pay 1? A) In a museum B) At an airport C) In a camping site D) In a room",
        "Do not swim alone? A) On a tub B) In the shower C) In a theater D) At a beach",
        "Bed and breafast? A) In  furniture store B) In a swiming pool C) Artist D) In an Inn",
        "Field closed for maintenance? A) In a movie theater B) In a sports club C) In a nursery center D) In a Hospital",
        "Children playing? A) In a butchery B) In a art gallery C)In a playground D) In a  hall",
        "Special meat and chicken? A) In a butchery B) In a bakery C) In a nursery center D)In a hardware store"
    ]

    respuestas_correctas = [
        "A", "B", "A", "A", "C", "D", "D", "B", "C", "A"
    ]

    respuestas_usuario = []

    for i, pregunta in enumerate(preguntas, start=1):
        respuesta = input(f"{pregunta} ")
        respuestas_usuario.append(respuesta)

        if respuesta.upper() == respuestas_correctas[i - 1]:
            print("¡Respuesta correcta!\n")
        else:
            print(f"Respuesta incorrecta. La respuesta correcta era {respuestas_correctas[i - 1]}\n")

    print("\n¡Gracias por responder las preguntas!")
    print("Tus respuestas fueron:")
    for i, respuesta in enumerate(respuestas_usuario, start=1):
        print(f"{i}. {respuesta}")   
if __name__ == "__main__":
    hacer_preguntas()

# Solicita al usuario que ingrese nombre, apellido y correo
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
correo = input("Ingresa tu correo electrónico: ")

# Muestra un saludo personalizado
print(f"¡Hola, {nombre} {apellido}! Tu correo es {correo}.")


for i, pregunta in enumerate(preguntas, start=1):
        respuesta = input(f"{pregunta} ")
        respuestas_usuario.append(respuesta)

        if respuesta.upper() == respuestas_correctas[i - 1]:
            print("¡Respuesta correcta!\n")
        else:
            print(f"Respuesta incorrecta. La respuesta correcta era {respuestas_correctas[i - 1]}\n")

  

def hacer_preguntas():
    preguntas = [
        "This lift is out of order? A)In a hotel B)In a motel C)In a cottage"
        "Please waited to be seated? A)In a theather B)In a clothing shop C)In a church"
        "Handiccaped reserved? A)In a sidewalk B)In a parking lot C)On a road"
        "Store in fridge after opening? A)A bar of soap B)A bar of butter C)A cup of tea"
        "Our information desk makes booking? A)In a hotel B)In a court house C)In a library"
        "Keep this parcels away from fire? A)In a factory B)In a warehouse C)In a laundromat"
        "Chemist closed for lunch? A)In a laboratory B)In a cloth shop C)In a pub"
        "Look both ways? A)In a port B)In a harbor C)On a road"
        "Fasten seat belt? A)In a shp B)In a airplane C)In a boat"
        "Recycable only A)In a booth B)In a bowl C)In a trashcan"
        "Out of order? A)In a container B)In a cash machine C)In a traytable"
        "Keep off the grass? A)In a playground B)In a building office C)In a pub"
        "Mind your head? A)In a furniture store B)In a construction site C)In a hardware store"
        "Wet paint do not touch? A)On a flask B)On a bench C)On a bag of plums"
        "Mens underwear? A)In a department store B)In a parking lot C)In a travel agency"
        "Fresh consume inmediately? A)On a dish of jelly B)On a tray of ham C)On a jar of jam"
    ]

    respuestas_corrrectas = [
        "A", "A", "B", "B", "A", "B", "A", "C", "B", "C"
    ]


