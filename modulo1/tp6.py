"""
Problema 6: En el siguiente diccionario se muestran los valores estándares de la tensión umbral de cada LED según su color:
leds_v_umbral = {'Rojo': 1.9 ,'Amarillo': {'min':1.7,'max':2},'Verde': 2.4,'Naranja': 2.4,'Blanco': 3.4,'Azul': 34,'Negro':50}
a) Eliminar el último par clave-valor.
b) Consulte el valor de tensión umbral del LED naranja.
c) Imprima en pantalla el valor máximo de la tensión umbral del LED amarillo.
d) Modifique el valor de la tensión umbral del LED azul a 3.4 V.
e) Cambie las claves para que sean todas minúsculas.
"""

# Definir el diccionario con los valores estándares de la tensión umbral de cada LED
leds_v_umbral = {
    "Rojo": 1.9,
    "Amarillo": {"min": 1.7, "max": 2},
    "Verde": 2.4,
    "Naranja": 2.4,
    "Blanco": 3.4,
    "Azul": 34,
    "Negro": 50,
}

# a) Eliminar el último par clave-valor
del leds_v_umbral["Negro"]

# b) Consultar el valor de tensión umbral del LED naranja
print("Tensión umbral del LED Naranja:", leds_v_umbral["Naranja"])

# c) Imprimir en pantalla el valor máximo de la tensión umbral del LED amarillo
print(
    "Valor máximo de la tensión umbral del LED Amarillo:",
    leds_v_umbral["Amarillo"]["max"],
)

# d) Modificar el valor de la tensión umbral del LED azul a 3.4 V
leds_v_umbral["Azul"] = 3.4

# e) Cambiar las claves para que sean todas minúsculas
leds_v_umbral = {clave.lower(): valor for clave, valor in leds_v_umbral.items()}

# Imprimir el diccionario actualizado
print("Diccionario con claves en minúsculas:")
print(leds_v_umbral)
