print("Hello World!")

class Usuario:
    def __init__(self, nombre, correo, contraseña):
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña

# Ejemplo de uso:
usuario1 = Usuario("Juan Pérez", "juan@example.com", "contraseña123")
usuario2 = Usuario("Juan Pérez4", "juan@example4.com", "contraseña4123")
usuario3 = Usuario("Juan Pérez4", "juan@4.com", "contraseñ3a123")

# Accediendo a las propiedades del usuario
print("Nombre:", usuario1.nombre)
print("Correo:", usuario1.correo)
print("Contraseña:", usuario1.contraseña)
print("Nombre:", usuario2.nombre)
print("Correo:", usuario2.correo)
print("Contraseña:", usuario2.contraseña)