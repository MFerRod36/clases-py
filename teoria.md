# Clase 01 — Fundamentos de Python

## 1. Tipos de Datos

### Datos básicos

Python tiene tipos de datos primitivos integrados:

| Tipo      | Descripción                        | Ejemplo              |
|-----------|------------------------------------|----------------------|
| `int`     | Entero (sin límite de tamaño)      | `42`, `-7`, `1_000`  |
| `float`   | Número decimal (IEEE 754)          | `3.14`, `-0.5`       |
| `complex` | Número complejo                    | `2 + 3j`             |
| `bool`    | Booleano (subclase de `int`)       | `True`, `False`      |
| `str`     | Cadena de texto (inmutable)        | `"hola"`             |
| `NoneType`| Ausencia de valor                  | `None`               |

Para saber el tipo de una variable usás `type()`:

```python
type(42)      # <class 'int'>
type(3.14)    # <class 'float'>
type("hola")  # <class 'str'>
```

---

### Números

**Enteros (`int`)**: En Python 3 no tienen límite de tamaño. Podés usar `_` como separador visual:

```python
poblacion = 1_000_000
```

**Flotantes (`float`)**: Representan decimales. Ojo con la precisión:

```python
0.1 + 0.2  # 0.30000000000000004  ← esto es normal en punto flotante
```

**Operadores aritméticos:**

```python
10 + 3   # 13   → suma
10 - 3   # 7    → resta
10 * 3   # 30   → multiplicación
10 / 3   # 3.333... → división (siempre retorna float)
10 // 3  # 3    → división entera
10 % 3   # 1    → módulo (resto)
10 ** 3  # 1000 → potencia
```

---

### Cadenas (`str`)

Las cadenas son **inmutables** — no podés modificar un carácter individual.

```python
saludo = "Hola"
nombre = 'Python'
multilinea = """
Esto es
un texto largo
"""
```

**f-strings** (la forma correcta de formatear desde Python 3.6):

```python
edad = 25
mensaje = f"Tengo {edad} años"          # "Tengo 25 años"
precio = f"Total: {9.99 * 3:.2f}"      # "Total: 29.97"
```

**Operaciones comunes:**

```python
texto = "  Hola Mundo  "

len(texto)           # 14 — longitud
texto.strip()        # "Hola Mundo" — elimina espacios extremos
texto.lower()        # "  hola mundo  "
texto.upper()        # "  HOLA MUNDO  "
texto.replace("Hola", "Chau")  # "  Chau Mundo  "
texto.split()        # ["Hola", "Mundo"] — divide por espacios
"Mundo" in texto     # True — pertenencia
texto[2]             # "H" — indexación (empieza en 0)
texto[2:6]           # "Hola" — slicing
```

---

### Conversión de tipos

Python no convierte automáticamente entre tipos — hay que hacerlo explícitamente:

```python
int("42")       # 42       — str a int
int(3.9)        # 3        — float a int (trunca, no redondea)
float("3.14")   # 3.14     — str a float
str(100)        # "100"    — int a str
bool(0)         # False    — 0, "", [], {}, None → False; todo lo demás → True
list("abc")     # ["a", "b", "c"] — iterable a lista
tuple([1, 2])   # (1, 2)   — lista a tupla
set([1, 1, 2])  # {1, 2}   — lista a conjunto (elimina duplicados)
```

Para verificar el tipo sin convertir:

```python
isinstance(42, int)        # True
isinstance("hola", (int, str))  # True — acepta tupla de tipos
```

---

## 2. Control de Flujo

### Condicionales

**`if / elif / else`:**

```python
edad = 20

if edad < 18:
    print("Menor de edad")
elif edad < 65:
    print("Adulto")
else:
    print("Adulto mayor")
```

Los operadores de comparación: `==`, `!=`, `<`, `>`, `<=`, `>=`  
Los operadores lógicos: `and`, `or`, `not`  
Los operadores de pertenencia: `in`, `not in`

```python
if edad >= 18 and edad < 65:
    print("En edad laboral")

if "admin" not in roles:
    print("Sin permisos")
```

**Comparaciones encadenadas** — Python permite encadenarlas directamente:

```python
# En otros lenguajes necesitarías: edad >= 18 and edad < 65
if 18 <= edad < 65:
    print("En edad laboral")

if 0 <= nota <= 10:
    print("Nota válida")
```

**Expresión condicional (ternario):**

```python
estado = "mayor" if edad >= 18 else "menor"
```

**`match / case`** (Python 3.10+) — para múltiples casos concretos:

```python
comando = "salir"

match comando:
    case "iniciar":
        print("Iniciando...")
    case "salir":
        print("Saliendo...")
    case _:
        print("Comando desconocido")
```

---

### Bucles

**`for`** — itera sobre cualquier secuencia:

```python
frutas = ["manzana", "banana", "naranja"]

for fruta in frutas:
    print(fruta)
```

Con `range()` para iterar n veces:

```python
for i in range(5):      # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):   # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):  # 0, 2, 4, 6, 8 (de 2 en 2)
    print(i)
```

**`while`** — itera mientras una condición sea verdadera:

```python
contador = 0

while contador < 5:
    print(contador)
    contador += 1
```

**`enumerate()`** — cuando necesitás el índice además del valor:

```python
frutas = ["manzana", "banana", "naranja"]

for i, fruta in enumerate(frutas):
    print(f"{i}: {fruta}")
# 0: manzana
# 1: banana
# 2: naranja

for i, fruta in enumerate(frutas, start=1):  # índice desde 1
    print(f"{i}: {fruta}")
```

**`zip()`** — itera dos o más secuencias en paralelo:

```python
nombres = ["Ana", "Luis", "Eva"]
edades = [30, 25, 28]

for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")
```

**Control dentro de bucles:**

```python
for i in range(10):
    if i == 3:
        continue    # salta esta iteración
    if i == 7:
        break       # termina el bucle
    print(i)
```

**Walrus operator `:=`** (Python 3.8+) — asigna y evalúa en la misma expresión:

```python
# Sin walrus — lees el archivo dos veces o usás variable extra
linea = f.readline()
while linea:
    print(linea)
    linea = f.readline()

# Con walrus — más limpio
while linea := f.readline():
    print(linea)
```

**`pass`** — bloque vacío (no hace nada, es un placeholder):

```python
for i in range(5):
    pass    # útil cuando la sintaxis exige un bloque pero no querés hacer nada aún
```

**`else` en bucles** — se ejecuta solo si el bucle terminó SIN un `break`:

```python
for i in range(5):
    if i == 10:
        break
else:
    print("No se encontró el 10")   # esto se imprime

numeros = [1, 3, 5, 7]
for n in numeros:
    if n % 2 == 0:
        print("Encontré un par")
        break
else:
    print("No hay pares")   # se imprime porque no hubo break
```

---

## 3. Estructuras de Datos

### Listas

**Mutables**, ordenadas, permiten duplicados. Se definen con `[]`:

```python
numeros = [1, 2, 3, 4, 5]
mixta = [1, "hola", True, 3.14]
```

**Operaciones comunes:**

```python
numeros.append(6)       # agrega al final → [1, 2, 3, 4, 5, 6]
numeros.insert(0, 0)    # inserta en posición → [0, 1, 2, 3, 4, 5, 6]
numeros.remove(3)       # elimina primera ocurrencia de 3
numeros.pop()           # elimina y retorna el último elemento
numeros.pop(0)          # elimina y retorna el elemento en índice 0
len(numeros)            # cantidad de elementos
numeros.sort()          # ordena in-place
sorted(numeros)         # retorna nueva lista ordenada (no modifica)
numeros[1:3]            # slicing → sublista
```

**Comprehensions** — forma concisa de crear colecciones:

```python
# List comprehension
cuadrados = [x ** 2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

pares = [x for x in range(20) if x % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Dict comprehension
cuadrados_dict = {x: x ** 2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Set comprehension
letras = {c.lower() for c in "Hola Mundo"}
# {'h', 'o', 'l', 'a', ' ', 'm', 'u', 'n', 'd'}  — sin duplicados
```

---

### Tuplas

**Inmutables**, ordenadas, permiten duplicados. Se definen con `()`:

```python
coordenadas = (40.7128, -74.0060)
punto = (1,)        # tupla de un elemento — la coma es obligatoria
vacia = ()
```

Se accede igual que las listas, pero **no se pueden modificar**. Útiles para datos que no deben cambiar.

**Desempaquetado:**

```python
x, y = coordenadas
print(x)  # 40.7128
print(y)  # -74.0060
```

---

### Diccionarios

**Mutables**, pares **clave → valor**, ordenados por inserción (desde Python 3.7). Se definen con `{}`:

```python
persona = {
    "nombre": "Ana",
    "edad": 30,
    "activa": True
}
```

**Operaciones comunes:**

```python
persona["nombre"]           # "Ana" — acceso por clave
persona.get("altura", 0)    # 0 — acceso seguro con valor por defecto
persona["email"] = "a@b.com"  # agrega o modifica
del persona["activa"]       # elimina clave
"nombre" in persona         # True — verifica existencia

persona.keys()    # dict_keys(["nombre", "edad"])
persona.values()  # dict_values(["Ana", 30])
persona.items()   # pares clave-valor
```

**Iterar:**

```python
for clave, valor in persona.items():
    print(f"{clave}: {valor}")
```

---

### Conjuntos (`set`)

**Mutables**, **no ordenados**, **sin duplicados**. Se definen con `{}` o `set()`:

```python
colores = {"rojo", "verde", "azul"}
vacio = set()    # ojo: {} crea un dict vacío, no un set
```

Los conjuntos son útiles para eliminar duplicados y operaciones de conjuntos:

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a | b   # unión → {1, 2, 3, 4, 5, 6}
a & b   # intersección → {3, 4}
a - b   # diferencia → {1, 2}
a ^ b   # diferencia simétrica → {1, 2, 5, 6}

colores.add("amarillo")     # agrega elemento
colores.discard("rojo")     # elimina si existe (no lanza error si no está)
```

---

### `frozenset`

Igual que `set` pero **inmutable** — no se puede modificar después de crearlo. Útil como clave de diccionario o elemento de otro set (los sets mutables no pueden serlo):

```python
permisos = frozenset({"leer", "escribir"})

# Soporta las mismas operaciones de conjuntos
otros = frozenset({"leer", "ejecutar"})
permisos & otros   # frozenset({'leer'})
permisos | otros   # frozenset({'leer', 'escribir', 'ejecutar'})

# Uso como clave de dict (algo que set no puede hacer)
roles = {
    frozenset({"admin", "editor"}): "acceso total",
    frozenset({"lector"}): "solo lectura",
}
```

---

### Estructuras anidadas

Las estructuras se pueden combinar libremente — este patrón es muy común en datos reales:

```python
# Lista de diccionarios (típico al leer JSON o una base de datos)
usuarios = [
    {"nombre": "Ana", "edad": 30, "activo": True},
    {"nombre": "Luis", "edad": 25, "activo": False},
]

for usuario in usuarios:
    if usuario["activo"]:
        print(usuario["nombre"])

# Diccionario de listas (agrupar datos)
cursos = {
    "python": ["Ana", "Luis", "Eva"],
    "javascript": ["Carlos", "Ana"],
}

for curso, alumnos in cursos.items():
    print(f"{curso}: {len(alumnos)} alumnos")
```

---

## 4. Funciones

Una función es un bloque de código con nombre que podés reutilizar. Se define con `def`:

```python
def saludar():
    print("Hola")

saludar()   # llamada — esto la ejecuta
saludar()   # podés llamarla cuantas veces quieras
```

---

### Parámetros y argumentos

Los **parámetros** son las variables que declara la función. Los **argumentos** son los valores que le pasás al llamarla:

```python
def saludar(nombre):        # nombre es el parámetro
    print(f"Hola, {nombre}")

saludar("Ana")              # "Ana" es el argumento
saludar("Luis")
```

Podés tener varios parámetros:

```python
def sumar(a, b):
    print(a + b)

sumar(3, 5)   # 8
```

---

### `return`

`return` hace que la función **devuelva un valor** que podés usar después. Sin `return`, la función devuelve `None`:

```python
def sumar(a, b):
    return a + b

resultado = sumar(3, 5)   # guardás el valor devuelto
print(resultado)          # 8
```

La diferencia clave:

```python
# Sin return — solo imprime, no podés usar el resultado
def sumar_mal(a, b):
    print(a + b)

# Con return — podés usar el resultado
def sumar_bien(a, b):
    return a + b

x = sumar_bien(3, 5) * 2   # 16 — esto funciona
x = sumar_mal(3, 5) * 2    # error — None * 2 no existe
```

---

### Parámetros por defecto

Podés definir un valor por defecto para un parámetro — si no se pasa, usa el default:

```python
def saludar(nombre, saludo="Hola"):
    print(f"{saludo}, {nombre}")

saludar("Ana")              # "Hola, Ana"
saludar("Ana", "Buenos días")  # "Buenos días, Ana"
```

Los parámetros con default siempre van **al final**:

```python
def conectar(host, puerto=5432):   # correcto
    ...

def conectar(puerto=5432, host):   # error — el sin default va después
    ...
```

---

### Scope (alcance)

Las variables definidas **dentro** de una función solo existen ahí — no se ven afuera:

```python
def calcular():
    resultado = 42   # variable local

calcular()
print(resultado)   # NameError — resultado no existe acá afuera
```

Las variables de **afuera** sí se pueden leer dentro, pero no modificar directamente:

```python
limite = 100

def verificar(n):
    return n < limite   # puede leer limite

verificar(50)   # True
```
