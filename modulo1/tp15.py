"""
Problema 15: Un año es año bisiesto si es divisible por 4, excepto los años que son divisibles por 100 aunque
los que son divisibles por 400 si lo son. Escriba un script que pregunte por un año al usuario y que el programa
determine si es año bisiesto.
"""

# Solicitar al usuario que ingrese un año
year = int(input("Ingrese un año: "))

# Verificar si el año es bisiesto
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "es un año bisiesto.")
else:
    print(year, "no es un año bisiesto.")
