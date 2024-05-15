# Versión Recursiva
def factorial_recursivo(n):
    """
    Calcula el factorial de un número entero no negativo n de forma recursiva.

    Parámetros:
    - n: Número entero no negativo.

    Devuelve:
    - El factorial de n.

    Ejemplo:
    >>> factorial_recursivo(5)
    120
    """
    if n == 0:
        return 1
    else:
        return n * factorial_recursivo(n - 1)


# Versión Iterativa
def factorial_iterativo(n):
    """
    Calcula el factorial de un número entero no negativo n de forma iterativa.

    Parámetros:
    - n: Número entero no negativo.

    Devuelve:
    - El factorial de n.

    Ejemplo:
    >>> factorial_iterativo(5)
    120
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Pruebas
if __name__ == "__main__":
    # Ejemplos de uso y pruebas
    print(factorial_recursivo(5))
    print(factorial_iterativo(5))
