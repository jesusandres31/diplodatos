import numpy as np

# a) Crear un arreglo de 4 elementos y aplicar la máscara [False, True, True, False]. ¿Qué resulta?
arr = np.array([10, 20, 30, 40])
mask = [False, True, True, False]

resultado_mask = arr[mask]

print("Array original:")
print(arr)
print("Máscara:")
print(mask)
print("Resultado aplicando la máscara:")
print(resultado_mask)
print()

# b) Crear un arreglo unidimensional de números enteros aleatorios y filtrar por los valores mayores al promedio,
# números impares y números pares menores al promedio.
arr_random = np.random.randint(
    1, 100, 10
)  # Array de 10 números enteros aleatorios entre 1 y 99

promedio = arr_random.mean()
mayores_al_promedio = arr_random[arr_random > promedio]
impares = arr_random[arr_random % 2 != 0]
pares_menores_al_promedio = arr_random[(arr_random % 2 == 0) & (arr_random < promedio)]

print("Array de números enteros aleatorios:")
print(arr_random)
print("Promedio del array:")
print(promedio)
print("Valores mayores al promedio:")
print(mayores_al_promedio)
print("Números impares:")
print(impares)
print("Números pares menores al promedio:")
print(pares_menores_al_promedio)
print()

# c) En un arreglo bidimensional A de valores aleatorios enteros, ¿qué diferencia hay entre hacer A > A.mean() y A[A > A.mean()]?
A = np.random.randint(
    1, 100, (3, 3)
)  # Array 3x3 de números enteros aleatorios entre 1 y 99

mask_A = A > A.mean()
valores_mayores_al_promedio = A[A > A.mean()]

print("Arreglo bidimensional A:")
print(A)
print("Máscara (A > A.mean()):")
print(mask_A)
print("Valores mayores al promedio (A[A > A.mean()]):")
print(valores_mayores_al_promedio)
