# precioserror.py
# Programa que prueba el módulo con manejo de errores

import auxprecioserror

# Caso correcto
precios1 = [10, 20, 30]
print("\nCaso 1: lista válida")
print("Promedio:", auxprecioserror.precio_medio(precios1))

# Caso con error: lista vacía
precios2 = []
print("\nCaso 2: lista vacía")
print("Promedio:", auxprecioserror.precio_medio(precios2))

# Caso con error: lista con valores no numéricos
precios3 = [10, "hola", 20]
print("\nCaso 3: lista con error de tipo")
print("Máximo:", auxprecioserror.precio_maximo(precios3))
