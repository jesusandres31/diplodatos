"""
Problema 14: Crear un código que determine los primeros 15 números primos.
"""


def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True


numeros_primos = []
numero = 2

while len(numeros_primos) < 15:
    if es_primo(numero):
        numeros_primos.append(numero)
    numero += 1

print("Los primeros 15 números primos son:", numeros_primos)
