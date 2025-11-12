# refactor.py
# Versión corregida y sencilla del programa

def pedir_numero(mensaje):
    """Pide un número al usuario y controla errores"""
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Error: introduce un número válido.")

def calcular_media(lista):
    """Calcula la media controlando división por cero"""
    if len(lista) == 0:
        print("No hay alumnos, no se puede calcular la media.")
        return 0
    return sum(lista) / len(lista)

def programa():
    alumnos = []
    n = pedir_numero("¿Cuántos alumnos? ")

    for i in range(n):
        nota = pedir_numero(f"Nota del alumno {i+1}: ")
        alumnos.append(nota)

    media = calcular_media(alumnos)
    print("\nMedia:", round(media, 2))

    print("Aprobados:")
    for nota in alumnos:
        if nota >= 5:
            print(nota)

# --- Ejecutar el programa ---
programa()
