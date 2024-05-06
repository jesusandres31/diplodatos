"""
Problema 1: Escriba un programa que convierta una temperatura en grados Celsius que se ingresa por teclado
a grados Fahrenheit según la fórmula. Verificar el tipo de variable del valor ingresado. Imprima el resultado.
Tf=(9/5)T+32
"""

# Pedir al usuario que ingrese la temperatura en grados Celsius
temperatura_celsius = input("Ingrese la temperatura en grados Celsius: ")

# Convertir la temperatura a un número entero
temperatura_celsius = int(temperatura_celsius)

# Calcular la temperatura en grados Fahrenheit
temperatura_fahrenheit = (9 / 5) * temperatura_celsius + 32

# Imprimir el resultado
print("La temperatura en grados Fahrenheit es:", temperatura_fahrenheit)
