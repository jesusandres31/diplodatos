"""
Problema 11: Hacer un código que cree una lista vacía y utilizando while, que en cada iteración pida ingresar
por teclado un elemento nuevo a la lista, hasta que ingrese la cadena fin.
"""

# Crear una lista vacía
lista = []

# Utilizar un bucle while para pedir al usuario que ingrese elementos
while True:
    # Solicitar al usuario que ingrese un elemento
    elemento = input("Ingrese un elemento (o 'fin' para terminar): ")

    # Verificar si el usuario ingresó "fin" para terminar el bucle
    if elemento.lower() == "fin":
        break

    # Agregar el elemento a la lista
    lista.append(elemento)

# Imprimir la lista resultante
print("Lista final:", lista)
