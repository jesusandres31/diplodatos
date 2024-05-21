import numpy as np

# a) Crear dos arrays de NumPy y asignarlos en variables. El primero debe ser de 1 dimensión y el segundo de 2 dimensiones. Aplicar en cada uno los métodos shape, ndim y size.
array_1d = np.array([1, 2, 3, 4, 5])
array_2d = np.array([[1, 2, 3], [4, 5, 6]])

print("Array 1D:")
print("Shape:", array_1d.shape)
print("Number of dimensions:", array_1d.ndim)
print("Size:", array_1d.size)
print()

print("Array 2D:")
print("Shape:", array_2d.shape)
print("Number of dimensions:", array_2d.ndim)
print("Size:", array_2d.size)
print()

# b) Crear un array de ceros de dimensión (3,3) y un array de unos de dimensión (2,4).
array_zeros = np.zeros((3, 3))
array_ones = np.ones((2, 4))

print("Array de ceros (3x3):")
print(array_zeros)
print()

print("Array de unos (2x4):")
print(array_ones)
print()

# c) Crear un array definido con valores en el intervalo abierto [10,30) con un step de 2.
array_interval = np.arange(10, 30, 2)

print("Array con valores en el intervalo [10,30) con step de 2:")
print(array_interval)
print()

# d) Crear dos arrays de 2D con valores aleatorios de la distribución normal. Utilizar np.random.randn() y np.random.normal().
array_randn = np.random.randn(3, 3)
array_normal = np.random.normal(0, 1, (3, 3))

print("Array con np.random.randn() (distribución normal estándar):")
print(array_randn)
print()

print(
    "Array con np.random.normal() (distribución normal con media 0 y desviación estándar 1):"
)
print(array_normal)
print()

# e) Crear un array con el comando linspace.
array_linspace = np.linspace(0, 1, 10)

print("Array con np.linspace(0, 1, 10):")
print(array_linspace)
