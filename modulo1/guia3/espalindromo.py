import re


def espalindromo(palabra):
    # Paso 1: Transformar la palabra para ignorar mayúsculas/minúsculas, espacios en blanco, signos de puntuación, números y otros caracteres
    palabra_procesada = re.sub(r"[^abcdefghijklmnñopqrstuvwxyz]", "", palabra.lower())

    # Paso 2: Comparar los caracteres correspondientes
    return palabra_procesada == palabra_procesada[::-1]


def main():
    palabra = input("Ingrese una palabra o frase: ")

    if espalindromo(palabra):
        print("La palabra o frase es un palíndromo.")
    else:
        print("La palabra o frase no es un palíndromo.")


if __name__ == "__main__":
    main()
