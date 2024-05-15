"""
Problema 13: Crear un código donde se ingresen los coeficientes de una ecuación de 2do grado y determine las
distintas soluciones para obtener las raíces de la misma.
a(x^2)+bx+c=0
Tener en cuenta los casos en que el discriminante cuadrático (b^2)−4ac sea mayor, menor e igual a 0.

---

El **discriminante** es un término que proviene de la fórmula cuadrática general que se utiliza para encontrar
las raíces de una ecuación cuadrática de la forma \( ax^2 + bx + c = 0 \). La fórmula cuadrática general es:

\[ x = \frac{{-b \pm \sqrt{{b^2 - 4ac}}}}{{2a}} \]

El discriminante, denotado como \( \Delta \), es la parte dentro de la raíz cuadrada en esta fórmula. 
Es decir, \( b^2 - 4ac \).

El valor del discriminante es importante porque nos dice mucho sobre las raíces de la ecuación cuadrática:

- Si \( \Delta > 0 \), entonces hay dos raíces reales y distintas.
- Si \( \Delta = 0 \), entonces hay una raíz real doble.
- Si \( \Delta < 0 \), entonces las raíces son complejas o imaginarias.

Entonces, al calcular el discriminante, podemos determinar cuántas soluciones tiene la ecuación 
cuadrática y qué tipo de soluciones son.
"""

import math

# Solicitar al usuario que ingrese los coeficientes de la ecuación
a = float(input("Ingrese el coeficiente 'a' de la ecuación de segundo grado: "))
b = float(input("Ingrese el coeficiente 'b' de la ecuación de segundo grado: "))
c = float(input("Ingrese el coeficiente 'c' de la ecuación de segundo grado: "))

# Calcular el discriminante
discriminante = b**2 - 4 * a * c

# Determinar las raíces de la ecuación
if discriminante > 0:
    # Dos raíces reales distintas
    x1 = (-b + math.sqrt(discriminante)) / (2 * a)
    x2 = (-b - math.sqrt(discriminante)) / (2 * a)
    print("Las raíces son:", x1, "y", x2)
elif discriminante == 0:
    # Una raíz real doble
    x = -b / (2 * a)
    print("La raíz doble es:", x)
else:
    # Raíces imaginarias
    parte_real = -b / (2 * a)
    parte_imaginaria = math.sqrt(abs(discriminante)) / (2 * a)
    raiz_1 = complex(parte_real, parte_imaginaria)
    raiz_2 = complex(parte_real, -parte_imaginaria)
    print("Las raíces son complejas:", raiz_1, "y", raiz_2)
