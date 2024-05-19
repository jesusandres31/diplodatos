"""
Problema 10: Cree un código que pida ingresar una palabra y que luego vaya incrementando el valor de una
variable α, con una condición inicial α0 = 10, de dos en dos, tantas veces como letras tenga la palabra
ingresada. El nuevo valor de la variable deberá ser mostrado en cada iteración. Por ejemplo, si se ingresa una
palabra de 3 letras, al ejecutar el código deberá mostrar los valores 12, 14 y 16.
"""

# Pedir al usuario que ingrese una palabra
palabra = input("Ingrese una palabra: ")

# Inicializar la variable alpha con valor inicial 10
alpha = 10

# Iterar sobre cada letra de la palabra
for letra in palabra:
    # Incrementar alpha en 2
    alpha += 2
    # Mostrar el nuevo valor de alpha en cada iteración
    print(alpha)
