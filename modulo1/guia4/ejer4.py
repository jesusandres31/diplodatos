import numpy as np

# a) Crear un array de 12 elementos en una fila. Utilizar el comando reshape(). ¿Qué argumentos de entrada puede tomar? Mostrar dos ejemplos.
arr = np.arange(12)  # Array de 12 elementos: [0, 1, 2, ..., 11]

# Ejemplo 1: Reshape a una matriz 3x4
arr_reshaped_1 = arr.reshape(3, 4)

# Ejemplo 2: Reshape a una matriz 2x6
arr_reshaped_2 = arr.reshape(2, 6)

print("Array original:")
print(arr)
print()

print("Array reshape a 3x4:")
print(arr_reshaped_1)
print()

print("Array reshape a 2x6:")
print(arr_reshaped_2)
print()

# b) En el array del ejercicio anterior, aplicar el comando split(). Mostrar 3 ejemplos.
# Ejemplo 1: Split en 3 sub-arrays
arr_split_1 = np.split(arr, 3)

# Ejemplo 2: Split en 4 sub-arrays
arr_split_2 = np.split(arr, 4)

# Ejemplo 3: Split en posiciones específicas
arr_split_3 = np.split(arr, [3, 6, 9])

print("Array split en 3 sub-arrays:")
print(arr_split_1)
print()

print("Array split en 4 sub-arrays:")
print(arr_split_2)
print()

print("Array split en posiciones específicas [3, 6, 9]:")
print(arr_split_3)
print()

# c) Crear dos arrays de 1D y usar el operador concatenate.
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

concatenado_1d = np.concatenate((arr1, arr2))

print("Concatenate de dos arrays 1D:")
print(concatenado_1d)
print()

# Luego usar el mismo operador en dos arrays de dimensión (2,2). Probar con el parámetro axis=0, y axis=1.
arr3 = np.array([[1, 2], [3, 4]])
arr4 = np.array([[5, 6], [7, 8]])

concatenado_2d_axis0 = np.concatenate((arr3, arr4), axis=0)
concatenado_2d_axis1 = np.concatenate((arr3, arr4), axis=1)

print("Concatenate de dos arrays 2D con axis=0:")
print(concatenado_2d_axis0)
print()

print("Concatenate de dos arrays 2D con axis=1:")
print(concatenado_2d_axis1)
