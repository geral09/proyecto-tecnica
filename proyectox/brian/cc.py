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


# Aplicación de preguntas en inglés con opciones A, B, C, D y verificación de respuestas



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
        "Keep this city tidy take your litter home? A)In a lake B)On a road C)In a harbor"
        "Drop your pants? A)In a clothing store B)In a pharmacy C)In a laundry service"
        "Keep this area clean? A)In a toy store B)In an employee lounge C)In a church"
        "Cakes and cupcakes on sale? A)In a bakery B)In a butchery C)In a jewelry"
        "Wet floor be careful? A)In a corridor B)On the grass C)In a book"
        "Water weekly and put in a sunny place? A)In a cafe B)In a swimming pool C)On a plant"
        "Peach flavor sweet cream? A)A can of tuna B)A can of jam C)A can of ham"
        "Foot protection must be worn? A)In a hospital B)In a museum C)In a construction site"
        "Delays possible? A)At an airport B)At a restaurant C)In a bakery"
        "New timetable starts from september? A)In a train station B)At an airport C)In a gas station"
        "Small parts not for children under 3 years? A)On a box of toys B)On a label C)On a can of soup"
        "Hunting is prohibited in this place? A)In a nuclear plant B)In a natural park C)In a factory"
        "Free delivery up to 5 miles away? A)In a post office B)In a construction site C)In a restaurant"
        "Bridge closed to traffic because of high wind? A)At a hospital B)On a station C)On a road"
        "Beware strong currents A)In a building site B)In a nuclear plant C)In a natural park"


    ]

    respuestas_corrrectas = [
        "A", "A", "B", "B", "A", "B", "A", "C", "B", "C", "B", "A", "A", "B", "A", "B", "B", "C", "B", "A", "A", "C", "B", "C", "A", "A", "A", "B", "A", "C", "C"
    ]

def hacer_preguntas():
    preguntas = [
        "You take your car here to fill it up with oil? A) Court B)Magazine  C) In a school D) Petrol Station",
        "Its used to make calls? A) Phone B) Call C) Happy D) Wallet"
        "If you play tennis,you book one...? A) Coach B) Envelope C) Court D) Sport club",
        "This is what you call your sister son? A) Aunt B) Nephew C) Uncle D) son",
        "This is how you feel when you win a game? A) In a museum B) Happy C)Enjoy D) Blushing",
        "You put your clothes in this when you travel? A) Suitcase B) Socks C) In a theater D) Flight",
        "You get this when someone answers your phone? A) Call B) Phone C) Artist D) Message",
        "This is a plaace  where you can buy tools to fix things? A) Hardware store B) In a sports club C) In a nursery center D) In a Hospital",
        "If you travel on it ,you will do exercises and save time? A) In a butchery B) In a playground C) Bike D) In a  hall",
        "You need this if you want to play tennis...? A) Ball B)CourtC) Coach D)Soccer"
    ]

    respuestas_correctas = [
        "D", "A", "C", "B", "B", "A", "D", "A", "C", "A"
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
        "This in an adhesive substance used for sticking objects together? A) Court B)Magazine  C) Glue D) Petrol Station",
        "People play to take this public transport by road? A) Phone B) Call C) Happy D) Coach"
        "This has interesting articles every week? A) Magazine B) Envelope C) Court D) Sport club",
        "People spend nights here in this place ? A) Inn B) Ball C) Field D) Bored",
        "Most people use a rectangular object for lying the head or sleeping? A) In a museum B) Pillow C)Enjoy D) Blushing",
        "Its small and grey and can run fast? A) Suitcase B) Socks C) Mouse D) Flight",
        "These are  used to reduce the discomfort in the throat? A) Call B) Phone C) Cough drops D) Message",
        "This person brings your food in a restaurant? A) Waiter B) In a sports club C) Sunscreen D) Warehouse",
        "A person feels like this when they needto sleep after a long day? A) In a butchery B) In a playground C) Bike D) Tired",
        "When we hate something,we sometimes feel like this? A) Ball B)Bored C) Coach D)Soccer"
    ]

    respuestas_correctas = [
        "C", "D", "A", "A", "B", "C", "C", "A", "C", "B"
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

        def hacer_preguntas(): preguntas = [
        "You put your soup or salad in this? A) Bowl B) Tray CLabel In a school D) Flask",
        "You fry eggs and  omelettes in this? A) Lamp B) Pan C) Closet D) In a school"
        "Traffic goes very fast along this road and you must  not stop here? A) Boat B) Carpet C) Street D) Highway",
        "This place where you buy chairs and  tables? A) Furniture  store  B) In a store C) In a movie theater D) In a Field",
        "You can cook and keep your food  here? A) In a museum B) At an airport C) Pot D) In a room",
        "My Mother or Father mother is my ? A) Sister B) Aunt C) Son D) Grandmother",
        "This is a  kind  of chair used by people who cannot walk? A) Weelchair B) Carpet C) Artist D) Field",
        "This is used carrying plates, dishes and food? A) Bowl B) Tray C) Flask D) Table",
        "This protects your skin in summer days? A) fragrance B) In a art gallery C)Sunscreen D) Lamp",
        "People used this electrical device for producing light? A) Wheelchair B) Waiter C)Fridge D)Lamp"
    ]

    respuestas_correctas = [
        "A", "B", "D", "A", "C", "D", "A", "B", "C", "D"
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
        
        