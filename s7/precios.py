# precios.py
# Programa que usa el módulo auxprecios

import auxprecios

precios = [10, 20, 5, 15, 30]

print("Lista de precios:", precios)
print("Precio máximo:", auxprecios.precio_maximo(precios))
print("Precio mínimo:", auxprecios.precio_minimo(precios))
print("Precio medio:", auxprecios.precio_medio(precios))
