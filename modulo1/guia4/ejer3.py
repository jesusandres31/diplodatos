import numpy as np

# a) Crear un array de dimensión (4,4) y extraer:
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

# Elemento de la fila 3 y columna 2 (índices comienzan en 0, así que fila 3 es índice 2 y columna 2 es índice 1)
elemento = arr[2, 1]

# La segunda fila (índice 1)
segunda_fila = arr[1, :]

# La tercera columna (índice 2)
tercera_columna = arr[:, 2]

print("Elemento en la fila 3 y columna 2:")
print(elemento)
print()

print("Segunda fila:")
print(segunda_fila)
print()

print("Tercera columna:")
print(tercera_columna)
print()

# b) Del array del ejercicio anterior, ¿Qué pasa si hacemos arr[1] = np.array([10,10,10,10])?
arr[1] = np.array([10, 10, 10, 10])

print("Array después de asignar arr[1] = np.array([10,10,10,10]):")
print(arr)
print()

# c) ¿Y qué pasa si hacemos arr[1] = 99?
arr[1] = 99

print("Array después de asignar arr[1] = 99:")
print(arr)
