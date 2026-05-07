"""
Ejercicio guiado: Conteo de ocurrencias con diccionarios
Descripción:
=> Dado un texto pequeño, queremos contar cuántas veces aparece cada palabra.
=> Para ello, usaremos un diccionario donde cada clave es una palabra y su valor es la cantidad de veces que aparece.

Objetivos:
1. Practicar el uso de diccionarios para almacenar pares clave-valor.
2. Usar métodos para agregar y actualizar valores en el diccionario.
3. Presentar los resultados ordenados alfabéticamente.

Formato de entrada:
1. La primera línea contiene un entero N, el número de palabras en el texto.
2. La segunda línea contiene N palabras separadas por espacios.

Formato de salida:
1. Para cada palabra única, imprimir una línea con la palabra y su frecuencia, separadas por un espacio.
2. Las palabras deben aparecer en orden alfabético.
-----------
Ejemplo:
Entrada:
6
hola mundo hola python mundo mundo

Salida:
hola 2
mundo 3
python 1
-----------
Pista:
Puedes usar un diccionario vacío y el método get para actualizar el conteo de cada palabra.
"""

# Paso 1: Leer el número de palabras
N = int(input())

# Paso 2: Leer las palabras y almacenarlas en una lista.
palabras = input().lower().split()

# Verificar que el número de palabras ingresadas coincide con N
if len(palabras) != N:
    print("Error: El número de palabras ingresadas no coincide con N.")
    exit(1)

# Paso 3: Crear un diccionario para contar las ocurrencias
conteo = {}

# Paso 4: Contar las ocurrencias de cada palabra
for palabra in palabras:
    conteo[palabra] = conteo.get(palabra, 0) + 1

# Paso 5: Imprimir las palabras y sus conteos ordenados alfabéticamente
for palabra in sorted(conteo.keys()):
    print(f"{palabra} {conteo[palabra]}")
