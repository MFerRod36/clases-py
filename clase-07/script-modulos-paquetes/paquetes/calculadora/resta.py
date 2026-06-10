from .suma import sumar
def restar(a, b):
    return a - b


class Calculadora:
    SUMA = " + " # Att de clase
    def __init__(self, numero_1, numero_2):
        self.num_1 = numero_1 # Att de instancia.
        self.num_2 = numero_2
        
    def __str__(self):
        return f"Es una calculadora con 2 numeros {self.num_1} y {self.num_2}"

    def sumar(self):
        return sumar(self.num_1, self.num_2)
