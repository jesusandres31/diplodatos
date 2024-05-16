import datetime


class Persona(object):
    def __init__(self, name, apellido=""):
        self.nombre = name
        self.apellido = apellido
        self.fecha_nacimiento = None

    def setBirthday(self, birthDate):
        self.fecha_nacimiento = birthDate

    def getLastName(self):
        return self.apellido

    def getAge(self):
        if self.fecha_nacimiento:
            today = datetime.date.today()
            age = (
                today.year
                - self.fecha_nacimiento.year
                - (
                    (today.month, today.day)
                    < (self.fecha_nacimiento.month, self.fecha_nacimiento.day)
                )
            )
            return age
        else:
            return None

    def __gt__(self, other):
        return self.getAge() > other.getAge()

    def __str__(self):
        return self.nombre


# Ejemplo de uso
if __name__ == "__main__":
    # Crear personas
    persona1 = Persona("Juan", "Gómez")
    persona2 = Persona("María", "López")

    # Definir fechas de nacimiento
    persona1.setBirthday(datetime.date(1990, 5, 15))
    persona2.setBirthday(datetime.date(1985, 10, 25))

    # Comparar edades
    if persona1 > persona2:
        print(persona1, "es mayor que", persona2)
    else:
        print(persona2, "es mayor que", persona1)
