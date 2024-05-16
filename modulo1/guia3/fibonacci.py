#
# definimos variable global y la funcion
#
nun_llamadas = 0


def fibonacci(n):
    global nun_llamadas  # para poder modificar la variable global
    nun_llamadas += 1

    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


#
# ejecutamos la funcion
#
n = input("Ingrese n-ésimo término en la secuencia quiera calcular: ")

res = fibonacci(n)

print("secuencia:", res)
print(f"numero de llamadas: {nun_llamadas}")
