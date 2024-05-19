"""
Problema 4: Utilizando una tupla, genere un programa que determine con True o False si una letra que se
ingresa es una vocal o no.
"""

# Definir una tupla con las vocales
vocales = ("a", "e", "i", "o", "u")

# Solicitar al usuario que ingrese una letra
letra = input("Ingrese una letra: ")

# Convertir la letra a minúscula para hacer la comparación más fácil
letra = letra.lower()

# Determinar si la letra ingresada es una vocal
if letra in vocales:
    print("True: La letra", letra, "es una vocal.")
else:
    print("False: La letra", letra, "no es una vocal.")
