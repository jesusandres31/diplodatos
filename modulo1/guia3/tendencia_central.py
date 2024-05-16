#
# definimos la funcion
#
def tendencia_central(lista, tipo="media"):
    """
    Calcula la tendencia central de una lista de numeros.
    """

    if tipo == "media":
        return sum(lista) / len(lista)

    elif tipo == "mediana":
        sorted_list = sorted(lista)
        n = len(sorted_list)
        if n % 2 == 0:
            return (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2
        else:
            return sorted_list[n // 2]

    elif tipo == "moda":
        counts = {x: lista.count(x) for x in set(lista)}
        max_count = max(counts.values())
        return [key for key, value in counts.items() if value == max_count]

    else:
        return "tipo desconocido"


#
# ejecutamos la funcion
#
# [8, 2, 3, 8, 0, 7, 5, 1, 2, 3]
#
lista = input("Ingrese una lista: ")
metodo = input("Elija un metodo (media, mediana o moda): ")

res = tendencia_central(lista, metodo)
print(res)
