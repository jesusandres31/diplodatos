def mat_mul(A, B):
    """
    Calcula el producto de dos matrices A y B.

    Argumentos:
    A (list of lists): Matriz A
    B (list of lists): Matriz B

    Retorna:
    list of lists: Matriz resultante del producto A * B
    """
    # Verificar dimensiones compatibles
    if len(A[0]) != len(B):
        raise ValueError(
            "Las dimensiones de las matrices no son compatibles para la multiplicación."
        )

    # Inicializar matriz resultante
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    # Calcular producto de matrices
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result


# Testear la función
if _name_ == "_main_":
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[7, 8], [9, 10], [11, 12]]

    try:
        result = mat_mul(A, B)
        print("El producto de las matrices es:")
        for row in result:
            print(row)
    except ValueError as e:
        print(e)
