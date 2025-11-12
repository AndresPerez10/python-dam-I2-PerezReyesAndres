# módulos_favs.py
# Ejemplo simple de módulos en Python

# --- Módulo estándar: math ---
import math

print("=== MÓDULO ESTÁNDAR: math ===")
print("Raíz cuadrada de 9:", math.sqrt(9))
print("Factorial de 4:", math.factorial(4))
print("Valor de pi:", math.pi)

# --- Módulo no estándar: colorama ---
# (Si no está instalado, se puede hacer con: pip install colorama)
from colorama import Fore, Style

print("\n=== MÓDULO NO ESTÁNDAR: colorama ===")
print(Fore.RED + "Este texto está en rojo" + Style.RESET_ALL)
print(Fore.GREEN + "Y este texto está en verde" + Style.RESET_ALL)
