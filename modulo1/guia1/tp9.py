"""
Problema 9: Crear una función con cuatro parámetros de entrada a1, a2, b1, b2 que representen los valores de
una matriz de dimensión (2, 2). La función debe calcular el determinante y evaluar si la matriz es singular 
(determinante igual a cero) o no singular (determinante distinto de cero). La salida de la función debe ser True
si la matriz es singular.
"""


def es_singular(a1, a2, b1, b2):
    # Calcular el determinante de la matriz
    determinante = a1 * b2 - a2 * b1

    # Verificar si el determinante es igual a cero (matriz singular)
    if determinante == 0:
        return True
    else:
        return False


# Ejemplo de uso de la función
resultado = es_singular(1, 2, 3, 4)
print("¿La matriz es singular?", resultado)
