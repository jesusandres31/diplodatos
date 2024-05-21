import numpy as np

# a) Crear dos arrays y aplicar las operaciones arr1 + arr2 y arr1 * arr2. ¿Qué condiciones deben cumplir arr1 y arr2?
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

suma = arr1 + arr2
multiplicacion = arr1 * arr2

print("Suma de arr1 y arr2:")
print(suma)
print()

print("Multiplicación elemento a elemento de arr1 y arr2:")
print(multiplicacion)
print()

# Condiciones que deben cumplir arr1 y arr2:
# Para realizar la suma y la multiplicación elemento a elemento, arr1 y arr2 deben tener la misma forma.

# b) Verificar la multiplicación de un escalar por un array.
escalar = 3
arr3 = np.array([[1, 2, 3], [4, 5, 6]])

multiplicacion_escalar = escalar * arr3

print("Multiplicación de un escalar por un array:")
print(multiplicacion_escalar)
print()

# c) De un array de 2D obtener la matriz traspuesta.
matriz_original = np.array([[1, 2, 3], [4, 5, 6]])

matriz_traspuesta = np.transpose(matriz_original)

print("Matriz original:")
print(matriz_original)
print()

print("Matriz traspuesta:")
print(matriz_traspuesta)
print()

# d) Realizar la multiplicación de dos matrices de dimensiones apropiadas.
matriz_a = np.array([[1, 2], [3, 4]])
matriz_b = np.array([[5, 6], [7, 8]])

multiplicacion_matrices = np.dot(matriz_a, matriz_b)

print("Multiplicación de dos matrices:")
print(multiplicacion_matrices)
