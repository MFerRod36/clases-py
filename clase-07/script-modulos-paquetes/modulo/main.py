from ope import sumar, restar # Path Absolutos.
#from cosas.mate import multiplicar # Path Relativos.
from cosas.test import multiplicar
import random
import os
import time


resultado = sumar(4, 10)
print(f"La suma es: {resultado}")

resultado = restar(4, 5)
print(f"La resta es: {resultado}")

resultado = multiplicar(2, 5)
print(f"La multiplicacion es {resultado}")

print(random.choices([1, 2, 3, 4, 5]))