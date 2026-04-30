"""Ejercicio práctico
Dado un conjunto de números, crea un set para eliminar duplicados y verifica si un número dado pertenece al set.
Entrada
Primera línea: número entero N, cantidad de elementos
Segunda línea: N números enteros separados por espacios
Tercera línea: un número entero X para verificar pertenencia
Salida
Primera línea: el set resultante (elementos separados por espacio, orden no importa)
Segunda línea: "Sí" si X está en el set, "No" en caso contrario
"""

# Leer la cantidad de elementos
N = int(input())

# Leer N números enteros y crear un set para eliminar duplicados, asegurando el tope de N elementos
numeros = set(map(int, input().split()[:N]))

# Leer el número a verificar
X = int(input())

# Imprimir el set resultante
print((" ".join(map(str, sorted(numeros)))))

# Verificar si X pertenece al set
if X in numeros:
    print("Sí")
else:
    print("No")
