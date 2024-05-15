"""
Problema 7: Realice un programa que nos imprima la secuencia de Fibonacci hasta un número dado Nmax. La
secuencia de Fibonacci suma los dos últimos números de la secuencia para generar uno nuevo comenzando
por 0 y 1.
"""


def fibonacci(Nmax):
    # Inicializar los primeros dos términos de la secuencia de Fibonacci
    a, b = 0, 1

    # Imprimir el primer término de la secuencia
    print(a)

    # Mientras el siguiente término sea menor o igual a Nmax
    while b <= Nmax:
        # Imprimir el término actual de la secuencia
        print(b)
        # Calcular el siguiente término de la secuencia sumando los dos últimos
        a, b = b, a + b


# Solicitar al usuario que ingrese el valor máximo de la secuencia
Nmax = int(input("Ingrese el número máximo para la secuencia de Fibonacci: "))

# Llamar a la función fibonacci con el valor máximo dado por el usuario
print("Secuencia de Fibonacci hasta", Nmax, ":")
fibonacci(Nmax)
