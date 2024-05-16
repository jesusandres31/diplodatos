def mcd(m, n, metodo="iterativo"):

    if metodo == "iterativo":
        while n != 0:
            m, n = n, m % n
        return m

    elif metodo == "recursivo":
        if n == 0:
            return m
        else:
            return mcd(n, m % n)

    else:
        return "metodo desconocido"
