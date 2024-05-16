def ordenar_palabras(lista_palabras):
    # Eliminar duplicados y ordenar alfabéticamente
    lista_ordenada = sorted(set(lista_palabras))
    return lista_ordenada


def main():
    # Solicitar al usuario que ingrese las palabras
    palabras = input("Ingrese las palabras separadas por coma: ").split(",")

    # Llamar a la función para ordenar las palabras
    palabras_ordenadas = ordenar_palabras(palabras)

    # Imprimir la lista de palabras ordenadas
    print("Palabras ordenadas:")
    for palabra in palabras_ordenadas:
        print(palabra.strip())  # Eliminar espacios en blanco alrededor de las palabras


if __name__ == "__main__":
    main()
