def mat_mul(A, B):
    """
    Calcula el producto de dos matrices A y B.

    Parámetros:
    - A: Primera matriz (lista de listas).
    - B: Segunda matriz (lista de listas).

    Devuelve:
    - La matriz resultante del producto de A y B (lista de listas).

    Ejemplo:
    >>> mat_mul([[1, 2], [3, 4]], [[5, 6], [7, 8]])
    [[19, 22], [43, 50]]
    """

    # Verifica que las dimensiones de las matrices sean compatibles
    if len(A[0]) != len(B):
        raise ValueError(
            "Las dimensiones de las matrices no son compatibles para la multiplicación"
        )

    # Inicializa la matriz resultante
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    # Calcula el producto de las matrices
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result


# Pruebas
if __name__ == "__main__":
    # Ejemplo de uso y prueba
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    print(mat_mul(A, B))
