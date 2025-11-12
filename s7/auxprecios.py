# auxprecios.py
# Módulo con funciones para analizar una lista de precios

def precio_maximo(lista):
    """Devuelve el precio máximo de una lista"""
    return max(lista)

def precio_minimo(lista):
    """Devuelve el precio mínimo de una lista"""
    return min(lista)

def precio_medio(lista):
    """Devuelve el precio medio de una lista"""
    return sum(lista) / len(lista)
