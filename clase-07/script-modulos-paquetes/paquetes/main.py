from calculadora import *
from funciones_validar import validar_numero

resultado = sumar(4, 5)
print(f"La suma es: {resultado}")

resultado = restar(4, 5)
print(f"La resta es: {resultado}")

calc = Calculadora(5, 5)
print(calc)
calc.sumar()