import random  # Módulo estándar

# Función 1: Crear personaje
def crear_personaje(nombre):
    try:
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        fuerza = random.randint(1, 10)
        vida = random.randint(10, 100)
        return nombre, fuerza, vida
    except ValueError as e:
        print("Error:", e)
        return None

# Función 2: Mostrar personaje
def mostrar_personaje(personaje):
    try:
        nombre, fuerza, vida = personaje
        print("Nombre:", nombre)
        print("Fuerza:", fuerza)
        print("Vida:", vida)
    except TypeError:
        print("No se puede mostrar un personaje vacío.")

# Función 3: Mejorar fuerza
def mejorar_fuerza(personaje, incremento):
    try:
        nombre, fuerza, vida = personaje
        fuerza += incremento
        print(f"¡{nombre} mejora su fuerza en {incremento}!")
        return nombre, fuerza, vida
    except TypeError:
        print("No se puede mejorar un personaje vacío.")
        return personaje

# ----------------------
# Programa principal
# ----------------------
nombre = input("Escribe el nombre de tu personaje: ")
personaje = crear_personaje(nombre)
if personaje:
    mostrar_personaje(personaje)
    incremento = random.randint(1,5)
    personaje = mejorar_fuerza(personaje, incremento)
    mostrar_personaje(personaje)
