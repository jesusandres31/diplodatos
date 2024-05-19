"""
Problema 3: Defina una lista que contenga números de tipo float y determine: el largo de la lista, el valor
mínimo, el valor máximo y la suma de los elementos de la misma. Luego ingrese un valor y determine si el
mismo pertenece o no a la lista.
"""

# Definir una lista que contenga números de tipo float
numeros = [3.14, 2.718, 1.618, 9.81, 6.67]

# Calcular el largo de la lista
largo_lista = len(numeros)

# Calcular el valor mínimo, máximo y la suma de los elementos de la lista
valor_minimo = min(numeros)
valor_maximo = max(numeros)
suma_elementos = sum(numeros)

# Imprimir los resultados
print("Largo de la lista:", largo_lista)
print("Valor mínimo:", valor_minimo)
print("Valor máximo:", valor_maximo)
print("Suma de los elementos:", suma_elementos)

# Solicitar al usuario que ingrese un valor
valor_ingresado = float(
    input("Ingrese un valor para verificar si pertenece a la lista: ")
)

# Determinar si el valor ingresado pertenece a la lista
if valor_ingresado in numeros:
    print("El valor", valor_ingresado, "pertenece a la lista.")
else:
    print("El valor", valor_ingresado, "no pertenece a la lista.")
