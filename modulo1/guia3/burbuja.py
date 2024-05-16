#
# definimos la funcion
#
def burbuja(seq):
    n = len(seq)

    for i in range(n):
        intercambio_realizado = False

        for j in range(0, n - i - 1):
            if seq[j] > seq[j + 1]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
                intercambio_realizado = True

        if not intercambio_realizado:
            break

    return seq


#
# ejecutamos la funcion
#
# [8, 2, 3, 8, 0, 7, 5, 1, 2, 3]
#
lista = input("Ingrese una lista: ")
metodo = input("Elija un metodo (iterativo o recursivo): ")

res = burbuja(lista)

print("lista original:", lista)
print("lista ordenada:", res)
