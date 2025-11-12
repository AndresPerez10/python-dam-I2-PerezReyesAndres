# auxprecioserror.py
# Versión mejorada del módulo con manejo de errores

def precio_maximo(lista):
    try:
        if not lista:
            raise ValueError("La lista está vacía")
        return max(lista)
    except TypeError:
        print("Error: la lista debe contener solo números.")
    except ValueError as e:
        print("Error:", e)
    finally:
        print("Ejecución de precio_maximo finalizada.")

def precio_minimo(lista):
    try:
        if not lista:
            raise ValueError("La lista está vacía")
        return min(lista)
    except Exception as e:
        print("Error:", e)
    finally:
        print("Ejecución de precio_minimo finalizada.")

def precio_medio(lista):
    try:
        if not lista:
            raise ValueError("La lista está vacía")
        return sum(lista) / len(lista)
    except ZeroDivisionError:
        print("Error: división entre cero.")
    except TypeError:
        print("Error: la lista debe contener solo números.")
    except ValueError as e:
        print("Error:", e)
    else:
        print("Cálculo del promedio completado correctamente.")
    finally:
        print("Ejecución de precio_medio finalizada.")
