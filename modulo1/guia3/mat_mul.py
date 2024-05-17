#
# definimos la funcion
#
def obtener_dimension_matriz(matriz):
    long_fila = len(matriz)
    long_columna = len(matriz[0])  # asumimos que pasamos todas las col de la misma long
    return [long_fila, long_columna]


def mat_mul(a, b):
    # convertir a y b a list
    a = eval(a)
    b = eval(b)

    dim_a = obtener_dimension_matriz(a)
    dim_b = obtener_dimension_matriz(b)

    if dim_a[1] != dim_b[0]:
        return "tus matrices no tiene dimensiones compatibles"

    # inicializar matriz resultante
    result = []

    # multiplicar matrices
    for i in range(dim_a[0]):
        row_result = []
        for j in range(dim_b[1]):
            sum = 0
            for k in range(dim_a[1]):  # dim_a[1] debe ser igual a dim_b[0]
                sum += a[i][k] * b[k][j]
            row_result.append(sum)
        result.append(row_result)

    return result


#
# ejecutamos la funcion
#
a = input("ingrese la matriz a:")
b = input("ingrese la matriz b:")

res = mat_mul(a, b)
print("resultado de a x b: ", res)
