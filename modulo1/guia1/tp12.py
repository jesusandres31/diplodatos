"""
Problema 12: Crear un código que pida ingresar un número menor a 10 y que lo vaya incrementando de 3 en 3
en cada iteración hasta llegar a un valor menor o igual a 50. En caso de que se ingrese un número mayor o igual
a 10, se debe mostrar un mensaje de error.
"""

# Solicitar al usuario que ingrese un número menor a 10
numero = int(input("Ingrese un número menor a 10: "))

# Verificar si el número ingresado es menor a 10
if numero >= 10:
    print("Error: El número ingresado es mayor o igual a 10.")
else:
    # Iterar hasta que el número sea menor o igual a 50
    while numero <= 50:
        # Imprimir el número actual
        print(numero)
        # Incrementar el número en 3
        numero += 3
