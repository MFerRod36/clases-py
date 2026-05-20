"""
En este ejercicio, practicarás cómo definir funciones con parámetros, devolver valores y llamar a esas funciones para reutilizar código. Implementarás dos funciones:
1. saludo(nombre): recibe un nombre y devuelve un saludo personalizado.
2. suma(a, b): recibe dos números y devuelve su suma.

Luego, leerás datos desde la entrada estándar, llamarás a las funciones y mostrarás los resultados en la salida estándar.

* Formato de entrada:
La primera línea contiene un nombre (cadena de texto).
La segunda línea contiene dos números enteros separados por espacio.

* Formato de salida:
La primera línea debe mostrar el saludo personalizado.
La segunda línea debe mostrar la suma de los dos números.
"""


# Función para generar un saludo personalizado con un nombre
def mi_saludo_personalizado(nombre):
    return f"Hola, {nombre}!"


# Función para calcular la suma de dos números
def suma(a, b):
    return a + b


# Leer el nombre desde la entrada estándar
nombre = input()

# Leer los dos números desde la entrada estándar y convertirlos a enteros
numeros = input().split()

a = int(numeros[0])
b = int(numeros[1])

# Llamar a la función de saludo personalizado y mostrar el resultado
saludo = mi_saludo_personalizado(nombre)
print(saludo)

# Llamar a la función de suma y mostrar el resultado
resultado = suma(a, b)
print(resultado)
