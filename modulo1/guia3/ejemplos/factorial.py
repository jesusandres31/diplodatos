#
# definimos la funcion
#
def factorial(n, metodo="iterativo"):
    n = int(n)

    if metodo == "iterativo":
        # usamos un bucle "for"
        res = 1

        for i in range(1, n + 1):
            res = res * i

        return res

    elif metodo == "recursivo":
        print(f"ahora n vale: {n}")
        # usamos funcion recursiva
        if n < 0:
            return "Error. Ingrese un numero positivo"
        elif n == 0:
            return 1
        else:
            res = n * factorial(n - 1, metodo)
            return res

    else:
        return "metodo desconocido"


#
# ejecutamos la funcion
#
numero = input("Ingrese un numero: ")
metodo = input("Elija un metodo (iterativo o recursivo): ")

res = factorial(numero, metodo)
print(f"resultado: {res}")
