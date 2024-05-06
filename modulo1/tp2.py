"""
Problema 2: Escriba un programa donde se ingrese el radio y el largo de un cilindro e imprima la superficie y el
volumen del mismo con dos cifras decimales.
A=2π(r^2)(r+l)
V=π(r^2)l
"""

import math

# Pedir al usuario que ingrese el radio y la altura del cilindro
radio = float(input("Ingrese el radio del cilindro: "))
altura = float(input("Ingrese la altura del cilindro: "))

# Calcular la superficie del cilindro
area_cilindro = 2 * math.pi * radio * (radio + altura)

# Calcular el volumen del cilindro
volumen_cilindro = math.pi * radio**2 * altura

# Imprimir la superficie y el volumen con dos cifras decimales
print("La superficie del cilindro es:", "{:.2f}".format(area_cilindro))
print("El volumen del cilindro es:", "{:.2f}".format(volumen_cilindro))
