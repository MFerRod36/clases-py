from calculadora.resta import restar
from calculadora import *

resultado = sumar(4, 5)
print(f"El resultado de la suma es: {resultado}")

resultado_resta = restar(10, 4)
print(f"El resultado de la resta es: {resultado_resta}")

calc = Calculadora(5, 5)
print(calc.sumar())
