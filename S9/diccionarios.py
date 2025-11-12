# Sistema de Tienda usando diccionarios

# Diccionario con productos y precios
tienda = {
    "manzanas": 1.2,
    "pan": 0.8,
    "leche": 1.5
}

# Mostrar productos iniciales
print("Productos actuales en la tienda:")
for producto, precio in tienda.items():
    print(f"- {producto}: €{precio}")

# Insertar un nuevo producto
nuevo_producto = input("\nIngresa un nuevo producto: ")
nuevo_precio = float(input("Ingresa su precio: "))
tienda[nuevo_producto] = nuevo_precio
print(f"{nuevo_producto} añadido correctamente.\n")

# Modificar un producto existente
producto_modificar = input("¿Qué producto deseas modificar? ")
if producto_modificar in tienda:
    nuevo_precio = float(input("Ingresa el nuevo precio: "))
    tienda[producto_modificar] = nuevo_precio
    print(f"Precio de {producto_modificar} actualizado.\n")
else:
    print("Ese producto no existe.\n")

# Eliminar un producto
producto_eliminar = input("¿Qué producto deseas eliminar? ")
if producto_eliminar in tienda:
    del tienda[producto_eliminar]
    print(f"{producto_eliminar} eliminado correctamente.\n")
else:
    print("Ese producto no existe.\n")

# Calcular una métrica: precio promedio de los productos
suma_precios = sum(tienda.values())
promedio = suma_precios / len(tienda)
print(f"El precio promedio de los productos es: ${promedio:.2f}")

# Adaptación personal: mostrar el producto más caro
producto_caro = max(tienda, key=tienda.get)
print(f"El producto más caro es '{producto_caro}' con un precio de ${tienda[producto_caro]:.2f}")

# Mostrar lista final de productos
print("\nLista final de productos:")
for producto, precio in tienda.items():
    print(f"- {producto}: ${precio}")
