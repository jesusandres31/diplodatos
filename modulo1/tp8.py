"""
Problema 8: Escribir un programa en Python que solicite al usuario que ingrese un valor numérico y que
imprima en pantalla un arreglo donde se muestre el resultado de elevar ese número a las siguientes potencias:
2, 3, 4 y 5.
"""

# Solicitar al usuario que ingrese un valor numérico
numero = float(input("Ingrese un valor numérico: "))

# Inicializar un arreglo para almacenar las potencias
potencias = []

# Calcular y almacenar las potencias en el arreglo
for exponente in range(2, 6):
    potencias.append(numero**exponente)

# Imprimir el arreglo de potencias
print("Potencias de", numero, ":")
for i, potencia in enumerate(potencias, start=2):
    print(numero, "elevado a la potencia", i, "es igual a", potencia)
