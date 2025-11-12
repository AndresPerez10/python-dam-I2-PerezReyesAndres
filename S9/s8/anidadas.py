# Anidadas.py
# Ejemplo simple de lista de diccionarios (estructura anidada)

# Lista vacía de alumnos
alumnos = []

# Función para añadir un alumno
def añadir_alumno(nombre, edad, nota):
    # Comprobamos errores
    if not nombre or not isinstance(edad, int) or not isinstance(nota, (int, float)):
        print("Error: datos incorrectos.")
        return
    for a in alumnos:
        if a["nombre"] == nombre:
            print("Error: el alumno ya existe.")
            return
    # Si todo va bien, se añade
    alumnos.append({"nombre": nombre, "edad": edad, "nota": nota})
    print("Alumno añadido correctamente.")

# Función para buscar un alumno por nombre
def buscar_alumno(nombre):
    for a in alumnos:
        if a["nombre"] == nombre:
            return a
    print("No se encontró el alumno.")
    return None

# Función para calcular la media de notas
def media_notas():
    if not alumnos:
        print("No hay alumnos registrados.")
        return
    notas = [a["nota"] for a in alumnos]
    media = sum(notas) / len(notas)
    print("La media de notas es:", round(media, 2))

# --- Ejemplo de uso ---
añadir_alumno("Ana", 20, 8)
añadir_alumno("Luis", 22, 6)
añadir_alumno("Marta", 19, 9)

print("\nBuscar alumno:")
print(buscar_alumno("Ana"))

print("\nCálculo de media:")
media_notas()
