calls_count = 0  # Variable global para contar el número de llamadas recursivas


def fibonacci_recursivo(n):
    """
    Calcula el n-ésimo término en la secuencia de Fibonacci de forma recursiva.

    Parámetros:
    - n: Número entero no negativo.

    Devuelve:
    - El n-ésimo término en la secuencia de Fibonacci.

    Ejemplo:
    >>> fibonacci_recursivo(5)
    5
    """
    global calls_count  # Acceder a la variable global

    calls_count += 1  # Incrementar el contador de llamadas recursivas

    if n <= 1:
        return n
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


# Reiniciar el contador de llamadas recursivas
calls_count = 0

# Pruebas
if __name__ == "__main__":
    # Ejemplo de uso y prueba
    print(fibonacci_recursivo(5))
    print("Número de llamadas recursivas:", calls_count)
