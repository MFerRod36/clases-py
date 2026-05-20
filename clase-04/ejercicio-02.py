"""
Problema 1: Calcular el área de un rectángulo
=> Define una función llamada calcular_area que reciba dos parámetros: base y altura (ambos números enteros o flotantes) y retorne el área del rectángulo.
* Entrada: Dos números separados por espacio: base y altura.
* Salida: Un número que representa el área.


Problema 2: Formatear un saludo
=> Define una función llamada saludo_personalizado que reciba dos parámetros: nombre (cadena) y edad (entero, con valor por defecto 0).
La función debe retornar un string con el formato:
"Hola, {nombre}! Tienes {edad} años."
Si no se proporciona la edad, debe retornar:
"Hola, {nombre}!"

* Entrada: Una línea con el nombre y opcionalmente la edad.
* Salida: El saludo formateado.


Problema 3: Composición de funciones - calcular el área de un círculo usando funciones auxiliares
=> Define dos funciones:
calcular_area_circulo(radio): retorna el área del círculo con el radio dado.
formatear_area(area): recibe un número y retorna un string con el área formateada con 2 decimales, por ejemplo: "Área: 12.57"
Lee un número r desde la entrada, calcula el área usando calcular_area_circulo y luego imprime el resultado formateado usando formatear_area.

* Entrada: Un número flotante que representa el radio.
* Salida: Un string con el área formateada.

Problema 4: Recursividad básica - suma de números naturales
=> Define una función recursiva llamada suma_natural(n) que retorne la suma de los números naturales desde 1 hasta n.
Lee un entero n y muestra la suma.
* Entrada: Un entero positivo.
* Salida: Un entero que es la suma.
"""

import math  # Importamos la biblioteca math para usar pi


# Solución al problema 1:
def calcular_area(base, altura):
    return base * altura


# Solución al problema 2:
def saludo_personalizado(nombre, edad=0):
    if edad > 0:
        return f"Hola, {nombre}! Tienes {edad} años."
    else:
        return f"Hola, {nombre}!"


# Solución al problema 3:
def calcular_area_circulo(radio):
    return math.pi * radio**2  # Fórmula del área del círculo: A = πr²


def formatear_area(area):
    return f"Área: {area:.2f}"  # Formateamos el área con 2 decimales usando :.2f


# Solución al problema 4:
def suma_natural(n):
    if n <= 0:
        return 0
    else:
        return n + suma_natural(
            n - 1
        )  # Llamada recursiva para sumar el número actual con la suma de los anteriores


# Uso de las funciones:
# Problema 1:
base = float(input())
altura = float(input())
area_rectangulo = calcular_area(base, altura)
print(area_rectangulo)

# Problema 2:
entrada = input().split()
nombre = entrada[0]
edad = int(entrada[1]) if len(entrada) > 1 else 0
saludo = saludo_personalizado(nombre, edad)
print(saludo)

# Problema 3:
radio = float(input())
area_circulo = calcular_area_circulo(
    radio
)  # Calculamos el área del círculo usando la función auxiliar
print(formatear_area(area_circulo))

# Problema 4: La recursividad es una técnica de programación donde una función se llama a sí misma para resolver un problema.
n = int(input())
print(suma_natural(n))
