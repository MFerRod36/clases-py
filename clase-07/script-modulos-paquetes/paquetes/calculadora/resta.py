def restar(a, b):
    return a - b


class Calculadora:
    SUMA = "+"

    def __init__(self, numero_1, numero_2):
        self.numero_1 = numero_1
        self.numero_2 = numero_2

    def __str__(self):
        return f"Calculadora({self.numero_1}, {self.numero_2})"

    def sumar(self):
        return self.numero_1 + self.numero_2
