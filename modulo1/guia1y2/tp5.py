"""
Problema 5: Cree una lista con 10 elementos de distintos tipos. Con el comando append ingrese dos valores
más. Invierta la lista. Imprima los elementos de índice 5 al 10. Elimine el elemento de índice 4. Verificar
imprimiendo el largo de la lista.
"""

# Crear una lista con 10 elementos de distintos tipos
mi_lista = [
    10,
    "Hola",
    3.14,
    True,
    [1, 2, 3],
    "a",
    False,
    (4, 5),
    {"key": "value"},
    None,
]

# Usar el comando append para ingresar dos valores más
mi_lista.append("nuevo_elemento1")
mi_lista.append(42)

# Invertir la lista
mi_lista.reverse()

# Imprimir los elementos de índice 5 al 10
print("Elementos de índice 5 al 10:", mi_lista[5:10])

# Imprimir largo de la lista
print("Largo de la lista:", len(mi_lista))

# Eliminar el elemento de índice 4
del mi_lista[4]

# Verificar e imprimir el largo de la lista
print("Largo de la lista después de eliminar el elemento de índice 4:", len(mi_lista))
