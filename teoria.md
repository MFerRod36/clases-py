# Fundamentos de Python

## 0. Indentación y buenas prácticas

Python usa la **indentación** para definir bloques de código — no hay llaves `{}` ni palabras clave `end`. La estructura visual ES la estructura del programa:

```python
if True:
    print("esto es parte del bloque")   # 4 espacios
    print("esto también")
print("esto está fuera del bloque")
```

Un bloque mal indentado lanza `IndentationError`. Mezclar tabs con espacios lanza `TabError`.

**Reglas:**

- Usá **4 espacios** por nivel (estándar PEP 8). Nunca mezclés tabs con espacios — configurá tu editor para que los tabs se conviertan en espacios.
- Cada nivel de anidamiento suma 4 espacios más.

```python
for i in range(3):       # nivel 1
    if i > 0:            # nivel 2 — 4 espacios
        print(i)         # nivel 3 — 8 espacios
```

**Convenciones de nombres (PEP 8):**

| Estilo | Uso | Ejemplo |
|--------|-----|---------|
| `snake_case` | variables, funciones, módulos | `nombre_usuario`, `calcular_total()` |
| `PascalCase` | clases | `ClienteVIP`, `ProductoDigital` |
| `UPPER_SNAKE_CASE` | constantes | `MAX_INTENTOS`, `PI` |

**Otras buenas prácticas:**

- Máximo 79 caracteres por línea
- Dos líneas en blanco entre funciones y clases de nivel superior
- Los nombres deben ser descriptivos: `calcular_impuesto()` es mejor que `ci()`
- Los comentarios explican el **POR QUÉ**, no el qué (el código ya dice el qué)
- Preferí `is` / `is not` para comparar con `None`, nunca `==`

---

## 1. Tipos de Datos

### Datos básicos

Python tiene tipos de datos primitivos integrados:

| Tipo       | Descripción                   | Ejemplo             |
| ---------- | ----------------------------- | ------------------- |
| `int`      | Entero (sin límite de tamaño) | `42`, `-7`, `1_000` |
| `float`    | Número decimal (IEEE 754)     | `3.14`, `-0.5`      |
| `complex`  | Número complejo               | `2 + 3j`            |
| `bool`     | Booleano (subclase de `int`)  | `True`, `False`     |
| `str`      | Cadena de texto (inmutable)   | `"hola"`            |
| `NoneType` | Ausencia de valor             | `None`              |

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

**Operadores de comparación** — siempre devuelven `bool`:

```python
5 == 5    # True  — igualdad de valor
5 != 3    # True  — distinto
5 > 3     # True  — mayor que
5 < 3     # False — menor que
5 >= 5    # True  — mayor o igual
5 <= 4    # False — menor o igual
```

`==` compara **valores**. `is` compara **identidad** (si son el mismo objeto en memoria):

```python
a = [1, 2]
b = [1, 2]
a == b    # True  — mismo valor
a is b    # False — objetos distintos en memoria

# is / is not → SOLO para comparar con None
if resultado is None: ...
if resultado is not None: ...
```

**Comparaciones encadenadas** — Python permite encadenarlas directamente:

```python
if 18 <= edad < 65:      # equivale a: edad >= 18 and edad < 65
    print("En edad laboral")

if 0 <= nota <= 10:
    print("Nota válida")
```

**Operadores lógicos:**

```python
True and False   # False — ambos deben ser True
True or False    # True  — al menos uno debe ser True
not True         # False — invierte el valor
```

Python usa **evaluación en cortocircuito** — evalúa solo lo necesario:

```python
False and funcion_costosa()   # False — funcion_costosa() nunca se llama
True or funcion_costosa()     # True  — funcion_costosa() nunca se llama
```

Útil para guardarse de errores:

```python
if lista and lista[0] > 0:    # si lista está vacía, el segundo operando no se evalúa
    ...
```

**Operadores de pertenencia:**

```python
"admin" in roles        # True si "admin" está en la colección
"admin" not in roles    # True si NO está
```

Funciona con listas, tuplas, sets, strings y diccionarios (busca en claves).

---

**Expresión condicional (ternario):**

```python
estado = "mayor" if edad >= 18 else "menor"
```

**Ternarios anidados** — posible, pero con criterio (máximo dos niveles):

```python
# Legible
categoria = "joven" if edad < 30 else ("adulto" if edad < 60 else "mayor")

# Esto ya es demasiado — usá if/elif/else directamente
resultado = "A" if x > 90 else ("B" if x > 70 else ("C" if x > 50 else "D"))
```

**`match / case`** (Python 3.10+) — para múltiples casos concretos, más legible que una cadena de `elif`:

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

### Expresiones anidadas

**Condicionales anidadas** — un `if` dentro de otro:

```python
if edad >= 18:
    if tiene_dni:
        print("Puede ingresar")
    else:
        print("Necesita DNI")
else:
    print("Menor de edad")
```

Cuando ambas condiciones son necesarias al mismo tiempo, `and` es más claro:

```python
if edad >= 18 and tiene_dni:
    print("Puede ingresar")
```

Usá anidamiento cuando la segunda condición solo tiene sentido si la primera ya pasó.

**Usos comunes:**

```python
# Valor por defecto con or
nombre = entrada or "Anónimo"         # si entrada es vacía / None / 0, usa "Anónimo"

# Validación en cascada — and cortocircuita si alguna condición falla
if usuario and usuario.activo and usuario.tiene_permiso("admin"):
    ...

# Asignación condicional en una línea
descuento = 0.2 if es_vip else (0.1 if es_socio else 0)
```

---

### Bucles

**`for`** — itera sobre cualquier secuencia:

```python
frutas = ["manzana", "banana", "naranja"]

for fruta in frutas:
    print(fruta)
```

Con `range()` para iterar n veces. Firma: `range(stop)` / `range(start, stop)` / `range(start, stop, step)`:

```python
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):       # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):   # 0, 2, 4, 6, 8 — de 2 en 2
    print(i)

for i in range(5, 0, -1):   # 5, 4, 3, 2, 1 — hacia atrás
    print(i)
```

`range()` no genera la lista completa en memoria — es un objeto que produce valores bajo demanda. Eficiente para rangos grandes.

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

**`break`** — termina el bucle inmediatamente, sin importar la condición:

```python
for numero in range(100):
    if numero == 7:
        break       # sale del bucle al encontrar el 7
    print(numero)   # imprime 0, 1, 2, 3, 4, 5, 6
```

Caso típico: buscar un elemento y dejar de iterar cuando lo encontrás.

**`continue`** — salta el resto de la iteración actual y pasa a la siguiente:

```python
for i in range(10):
    if i % 2 == 0:
        continue    # si es par, salta — no ejecuta el print
    print(i)        # imprime solo impares: 1, 3, 5, 7, 9
```

Caso típico: filtrar elementos que no querés procesar.

**`pass`** — no hace nada. Es un placeholder para cuando la sintaxis exige un bloque pero no querés escribir código aún:

```python
for i in range(5):
    pass    # bloque vacío válido — útil mientras desarrollás

def funcion_pendiente():
    pass    # mismo uso en funciones o clases vacías
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

---

#### Acceso y modificación

Se accede a un elemento por su **índice** (posición). Los índices empiezan en `0`:

```python
frutas = ["manzana", "banana", "naranja"]

frutas[0]   # "manzana" — primer elemento
frutas[1]   # "banana"
frutas[2]   # "naranja"
```

Los índices **negativos** cuentan desde el final:

```python
frutas[-1]  # "naranja" — último
frutas[-2]  # "banana"
frutas[-3]  # "manzana"
```

Para **modificar** un elemento, simplemente asignás al índice:

```python
frutas[1] = "pera"   # ["manzana", "pera", "naranja"]
```

Acceder a un índice que no existe lanza `IndexError`:

```python
frutas[10]   # 💥 IndexError: list index out of range
```

---

#### Slicing (rebanado)

El slicing devuelve una **nueva lista** con una porción de la original. No modifica la lista:

```python
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

numeros[2:5]    # [2, 3, 4]       — desde índice 2 hasta 5 (sin incluir 5)
numeros[:4]     # [0, 1, 2, 3]    — desde el inicio hasta 4
numeros[6:]     # [6, 7, 8, 9]    # desde 6 hasta el final
numeros[:]      # copia completa de la lista
numeros[-3:]    # [7, 8, 9]       — últimos 3 elementos
```

El tercer parámetro es el **paso** (step):

```python
numeros[::2]    # [0, 2, 4, 6, 8]   — de 2 en 2
numeros[1::2]   # [1, 3, 5, 7, 9]   — impares
numeros[::-1]   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]   — invertida
```

---

#### Métodos para agregar elementos

```python
numeros = [1, 2, 3]

numeros.append(4)           # agrega al final → [1, 2, 3, 4]
numeros.insert(0, 0)        # inserta en posición → [0, 1, 2, 3, 4]
numeros.extend([5, 6, 7])   # agrega todos los elementos de otro iterable → [0, 1, 2, 3, 4, 5, 6, 7]
```

La diferencia clave entre `append` y `extend`:

```python
lista = [1, 2, 3]

lista.append([4, 5])    # [1, 2, 3, [4, 5]]  ← agrega la lista como un solo elemento
lista.extend([4, 5])    # [1, 2, 3, 4, 5]    ← agrega cada elemento por separado
```

---

#### Métodos para quitar elementos

```python
numeros = [1, 2, 3, 2, 4]

numeros.remove(2)   # elimina la PRIMERA ocurrencia de 2 → [1, 3, 2, 4]
numeros.pop()       # elimina y retorna el último → retorna 4, lista queda [1, 3, 2]
numeros.pop(0)      # elimina y retorna el de índice 0 → retorna 1, lista queda [3, 2]
numeros.clear()     # vacía la lista → []
del numeros[0]      # elimina el elemento en índice 0 (no retorna nada)
del numeros[1:3]    # elimina un rango con slicing
```

`remove` vs `pop`:

- `remove(valor)` → buscás por valor; si no existe, lanza `ValueError`
- `pop(índice)` → eliminás por posición y **te devuelve el valor**; si no existe el índice, lanza `IndexError`

---

#### Otras operaciones comunes

```python
numeros = [3, 1, 4, 1, 5]

len(numeros)        # 5 — cantidad de elementos
numeros.count(1)    # 2 — cuántas veces aparece el valor 1
numeros.index(4)    # 2 — índice de la primera ocurrencia de 4
numeros.sort()      # ordena in-place → [1, 1, 3, 4, 5] (modifica la lista)
sorted(numeros)     # retorna nueva lista ordenada (no modifica la original)
numeros.reverse()   # invierte in-place (modifica la lista)
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

Se accede igual que las listas con índices positivos y negativos, pero **no se pueden modificar**:

```python
coordenadas = (40.7128, -74.0060)

coordenadas[0]    # 40.7128
coordenadas[-1]   # -74.0060
coordenadas[0] = 99   # 💥 TypeError: 'tuple' object does not support item assignment
```

La inmutabilidad es una garantía — si pasás una tupla a una función, sabés que no puede ser modificada. Con una lista, no tenés esa certeza.

**Cuándo usar tupla vs lista:**

| Tupla | Lista |
|-------|-------|
| Datos que no deben cambiar (coordenadas, RGB, fecha) | Datos que crecen o se modifican |
| Retorno de múltiples valores de una función | Colección de ítems del mismo tipo |
| Clave de diccionario (es hasheable) | Cuando necesitás append/remove |

**Métodos disponibles** (son solo dos, porque no puede modificarse):

```python
punto = (1, 2, 1, 3, 1)

punto.count(1)   # 3 — cuántas veces aparece el valor 1
punto.index(3)   # 3 — índice de la primera ocurrencia de 3
```

**Desempaquetado:**

```python
x, y = coordenadas
print(x)  # 40.7128
print(y)  # -74.0060

# También funciona en retorno de funciones
def min_max(lista):
    return min(lista), max(lista)   # retorna una tupla

minimo, maximo = min_max([3, 1, 4, 1, 5])
```

---

### Diccionarios

**Mutables**, pares **clave → valor**, ordenados por inserción (desde Python 3.7).

**Creación:**

```python
# Literal con {}
persona = {"nombre": "Ana", "edad": 30, "activa": True}

# Función dict() con kwargs — útil cuando las claves son strings simples
persona = dict(nombre="Ana", edad=30, activa=True)

# Función dict() desde lista de pares (útil cuando los datos vienen de otro lado)
persona = dict([("nombre", "Ana"), ("edad", 30)])

# Diccionario vacío
vacio = {}
vacio = dict()
```

**Acceso a valores:**

```python
persona["nombre"]           # "Ana" — lanza KeyError si la clave no existe
persona.get("altura")       # None  — seguro, no lanza error
persona.get("altura", 0)    # 0     — con valor por defecto si no existe
```

Preferí `get()` sobre `[]` cuando la clave podría no estar.

**Agregar, modificar y eliminar:**

```python
persona["email"] = "a@b.com"  # agrega si no existe, sobreescribe si existe
del persona["activa"]          # elimina; lanza KeyError si no existe
persona.pop("edad")            # elimina y retorna el valor → 30
persona.pop("altura", 0)       # si no existe, retorna default en vez de lanzar error
persona.update({"email": "a@b.com", "edad": 31})  # agrega o sobreescribe varias claves
persona.update(email="a@b.com", edad=31)           # lo mismo con kwargs
```

**`setdefault()`** — inserta la clave con un default solo si NO existe; si ya existe, no toca el valor:

```python
persona.setdefault("apodo", "sin apodo")   # inserta "apodo": "sin apodo" si no estaba
persona.setdefault("nombre", "Anónimo")    # no hace nada, "nombre" ya existe
```

Útil para inicializar claves la primera vez sin pisar datos existentes.

**`"nombre" in persona`** — verifica si la clave existe:

```python
"nombre" in persona    # True
"altura" in persona    # False
```

**Iteración:**

```python
# Solo claves
for clave in persona:                  # equivale a iterar sobre persona.keys()
    print(clave)

# Solo valores
for valor in persona.values():
    print(valor)

# Claves y valores juntos
for clave, valor in persona.items():
    print(f"{clave}: {valor}")
```

---

### Conjuntos (`set`)

**Mutables**, **no ordenados**, **sin duplicados**. Se definen con `{}` o `set()`:

```python
colores = {"rojo", "verde", "azul"}          # literal
vacio = set()                                 # vacío — ojo: {} crea un dict, no un set
numeros = set([1, 2, 2, 3, 3])               # desde lista → {1, 2, 3} (elimina duplicados)
letras = set("banana")                        # desde string → {'b', 'a', 'n'}
```

**Operaciones de conjuntos** (devuelven un nuevo set, no modifican el original):

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a | b   # unión → {1, 2, 3, 4, 5, 6}
a & b   # intersección → {3, 4}
a - b   # diferencia → {1, 2}
a ^ b   # diferencia simétrica → {1, 2, 5, 6}
```

**Métodos de mutabilidad** (modifican el set in-place):

```python
colores = {"rojo", "verde", "azul"}

colores.add("amarillo")           # agrega un elemento
colores.discard("rojo")           # elimina si existe (sin error si no está)
colores.remove("verde")           # elimina; lanza KeyError si no existe
colores.pop()                     # elimina y retorna un elemento ALEATORIO (ojo — no ordenado)
colores.clear()                   # vacía el set → set()
colores.update({"rosa", "gris"})  # agrega todos los elementos de otro iterable (como extend en listas)
```

**Consultas de relación entre sets:**

```python
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
c = {6, 7}

a.issubset(b)     # True  — todos los de `a` están en `b`
b.issuperset(a)   # True  — `b` contiene a todos los de `a`
a.isdisjoint(c)   # True  — no comparten ningún elemento
a.isdisjoint(b)   # False — comparten elementos
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
def saludar():          # definición
    print("Hola")

saludar()               # llamada — esto la ejecuta
resultado = saludar()   # resultado es None si la función no tiene return
```

**Docstring** — documentación opcional que va como primer statement de la función:

```python
def calcular_area(base, altura):
    """Calcula el área de un triángulo."""
    return (base * altura) / 2

# Accesible en tiempo de ejecución
print(calcular_area.__doc__)   # "Calcula el área de un triángulo."
help(calcular_area)            # muestra la documentación formateada
```

---

### Funciones integradas (built-ins)

Python incluye funciones disponibles en todo momento, sin importar nada:

| Función | Qué hace |
|---------|----------|
| `len(x)` | Longitud de una secuencia |
| `type(x)` | Tipo del objeto |
| `isinstance(x, tipo)` | Verifica si x es de ese tipo |
| `print(*args)` | Imprime en stdout |
| `input(prompt)` | Lee una línea de stdin |
| `int()`, `float()`, `str()`, `bool()` | Conversión de tipos |
| `list()`, `tuple()`, `set()`, `dict()` | Conversión a colecciones |
| `range(start, stop, step)` | Genera una secuencia de enteros |
| `enumerate(iterable)` | Itera con índice |
| `zip(*iterables)` | Itera en paralelo |
| `sorted(iterable)` | Retorna nueva lista ordenada |
| `reversed(iterable)` | Iterador inverso |
| `min()`, `max()`, `sum()` | Operaciones de agregación |
| `abs(x)` | Valor absoluto |
| `round(x, n)` | Redondea a n decimales |
| `any(iterable)` | `True` si al menos un elemento es verdadero |
| `all(iterable)` | `True` si TODOS los elementos son verdaderos |
| `map(func, iterable)` | Aplica una función a cada elemento |
| `filter(func, iterable)` | Filtra elementos según una función |
| `chr(n)` | Carácter Unicode del número entero `n` |
| `ord(c)` | Número entero del carácter `c` |
| `id(x)` | Identidad del objeto (dirección en memoria) |
| `open(path, mode)` | Abre un archivo |

```python
numeros = [3, 1, 4, 1, 5]
len(numeros)         # 5
min(numeros)         # 1
max(numeros)         # 5
sum(numeros)         # 14
sorted(numeros)      # [1, 1, 3, 4, 5]
abs(-7)              # 7
round(3.14159, 2)    # 3.14
```

**`any()` y `all()`** — útiles para validar colecciones:

```python
edades = [22, 17, 30, 15]

any(e >= 18 for e in edades)   # True  — al menos uno es mayor de edad
all(e >= 18 for e in edades)   # False — no todos son mayores de edad

all(isinstance(x, int) for x in edades)   # True — todos son enteros
```

**`map()` y `filter()`** — aplican una función sobre un iterable:

```python
numeros = [1, 2, 3, 4, 5]

# map: transforma cada elemento
dobles = list(map(lambda x: x * 2, numeros))    # [2, 4, 6, 8, 10]

# filter: conserva solo los que cumplen la condición
pares = list(filter(lambda x: x % 2 == 0, numeros))  # [2, 4]
```

En la práctica, las comprehensions suelen ser más legibles que `map`/`filter`:

```python
dobles = [x * 2 for x in numeros]
pares  = [x for x in numeros if x % 2 == 0]
```

**`chr()` y `ord()`** — conversión entre caracteres y sus valores numéricos Unicode:

```python
ord("A")    # 65
ord("a")    # 97
chr(65)     # "A"
chr(97)     # "a"

# Útil para iterar sobre el alfabeto
for i in range(26):
    print(chr(ord("a") + i))   # a, b, c, ..., z
```

---

### Modularidad

Un módulo es un archivo `.py` con funciones, clases o variables que podés importar en otro archivo.

**Importar módulos de la biblioteca estándar:**

```python
import math
import os

math.sqrt(16)     # 4.0
math.pi           # 3.141592653589793
os.getcwd()       # directorio de trabajo actual
```

**Importar solo lo que necesitás:**

```python
from math import sqrt, pi
from datetime import datetime

sqrt(16)   # 4.0 — sin el prefijo math.
```

**Alias para nombres largos:**

```python
from datetime import datetime as dt

ahora = dt.now()
```

**Módulos propios** — cualquier archivo `.py` es un módulo:

```python
# utils.py
def saludar(nombre):
    return f"Hola, {nombre}"

# main.py
from utils import saludar

print(saludar("Ana"))   # "Hola, Ana"
```

---

### Parámetros y argumentos

Los **parámetros** son las variables que declara la función. Los **argumentos** son los valores que le pasás al llamarla.

**Posicionales** — se pasan en orden, por posición:

```python
def conectar(host, puerto, ssl):
    ...

conectar("localhost", 5432, False)   # orden importa
```

**Por palabra clave (keyword)** — se nombra explícitamente el parámetro:

```python
conectar(host="localhost", puerto=5432, ssl=False)   # orden no importa
conectar("localhost", ssl=False, puerto=5432)         # mix: posicional + keyword
```

Los keyword args siempre van DESPUÉS de los posicionales en la llamada.

**Valores por defecto** — si no se pasa el argumento, usa el default:

```python
def conectar(host, puerto=5432, ssl=False):
    ...

conectar("localhost")                    # usa puerto=5432, ssl=False
conectar("localhost", puerto=3306)       # sobreescribe solo puerto
conectar("localhost", 3306, True)        # todos posicionales
```

Los parámetros con default van **al final** de la firma — nunca antes de un sin-default.

**`*args`** — cantidad variable de argumentos posicionales (se reciben como tupla):

```python
def sumar(*args):
    return sum(args)

sumar(1, 2, 3)         # 6
sumar(1, 2, 3, 4, 5)   # 15
```

**`**kwargs`** — cantidad variable de argumentos por palabra clave (se reciben como diccionario):

```python
def crear_usuario(**kwargs):
    print(kwargs)

crear_usuario(nombre="Ana", edad=30, activo=True)
# {'nombre': 'Ana', 'edad': 30, 'activo': True}
```

**Combinados** — el orden en la firma es siempre: posicionales → `*args` → defaults → `**kwargs`:

```python
def registrar(evento, *detalles, nivel="info", **metadata):
    print(evento, detalles, nivel, metadata)

registrar("login", "ip:192.168.1.1", "browser:chrome", nivel="warn", user_id=42)
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

### Scope (alcance)

Las variables definidas **dentro** de una función son **locales** — solo existen ahí:

```python
def calcular():
    resultado = 42   # variable local

calcular()
print(resultado)   # NameError — resultado no existe afuera
```

Las variables definidas **afuera** son **globales** — se pueden leer desde dentro, pero no modificar directamente:

```python
limite = 100

def verificar(n):
    return n < limite   # puede leer la global

def romper():
    limite = 200        # crea una variable LOCAL llamada limite, no modifica la global
```

**`global`** — para modificar una variable global desde dentro de una función:

```python
contador = 0

def incrementar():
    global contador
    contador += 1

incrementar()
print(contador)   # 1
```

Usalo lo menos posible — las variables globales modificables hacen el código difícil de seguir.

**`UnboundLocalError`** — error frecuente cuando Python detecta una asignación local pero intentás leer la variable antes de asignarla:

```python
x = 10

def romper():
    print(x)    # 💥 UnboundLocalError: local variable 'x' referenced before assignment
    x = 20      # esta línea hace que Python trate x como local EN TODA LA FUNCIÓN
                # incluyendo el print de arriba, donde todavía no fue asignada
```

La causa: si hay CUALQUIER asignación a `x` dentro de la función, Python la trata como local en toda la función — no solo después de la asignación.

**Solución:** declarala `global`, o mejor aún, pasala como parámetro:

```python
def bien(x):
    print(x)
    x = 20
    return x
```

---

### Debugging

**Print debugging** — el método más simple: insertar `print()` para inspeccionar valores en puntos clave:

```python
def calcular(a, b):
    print(f"[DEBUG] a={a}, b={b}")   # inspeccionás los valores
    resultado = a / b
    print(f"[DEBUG] resultado={resultado}")
    return resultado
```

**Breakpoints en el IDE (VS Code / PyCharm)** — pausan la ejecución en una línea específica sin modificar el código:

1. Hacé click en el margen izquierdo de la línea → aparece un punto rojo
2. Ejecutá en modo **Debug** (F5 en VS Code)
3. La ejecución se pausa ahí y podés inspeccionar variables

**Controles de ejecución:**

| Acción | Tecla (VS Code) | Qué hace |
|--------|-----------------|----------|
| **Step Over** | F10 | Ejecuta la línea actual, no entra en funciones |
| **Step Into** | F11 | Entra dentro de la función que se llama |
| **Step Out** | Shift+F11 | Sale de la función actual |
| **Continue** | F5 | Continúa hasta el próximo breakpoint |

**Inspección de variables** — en el panel Debug podés ver el valor de todas las variables locales y globales en ese momento de la ejecución.

**`breakpoint()`** — función built-in (Python 3.7+) que abre el debugger `pdb` directamente desde el código:

```python
def calcular(a, b):
    breakpoint()    # pausa aquí y abre pdb en la terminal
    return a / b
```

Desde `pdb`: `n` (next/step over), `s` (step into), `p variable` (print variable), `q` (quit).

---

### Recursividad

Una función es **recursiva** cuando se llama a sí misma. Todo problema recursivo necesita dos partes:

1. **Caso base** — la condición que detiene la recursión (sin esto hay loop infinito)
2. **Caso recursivo** — la llamada a sí misma con un problema más pequeño

```python
def cuenta_regresiva(n):
    if n == 0:           # caso base
        print("¡Ya!")
        return
    print(n)
    cuenta_regresiva(n - 1)   # caso recursivo — n se reduce cada vez

cuenta_regresiva(3)   # 3, 2, 1, ¡Ya!
```

**Ejemplo clásico — factorial:**

```python
def factorial(n):
    if n == 0:               # caso base: 0! = 1
        return 1
    return n * factorial(n - 1)   # caso recursivo

factorial(5)   # 5 * 4 * 3 * 2 * 1 = 120
```

Lo que ocurre internamente (call stack):

```
factorial(5)
  → 5 * factorial(4)
       → 4 * factorial(3)
            → 3 * factorial(2)
                 → 2 * factorial(1)
                      → 1 * factorial(0)
                           → 1  ← caso base, empieza a retornar
```

**Límite de recursión** — Python tiene un límite de profundidad para evitar que el stack se desborde:

```python
import sys

sys.getrecursionlimit()    # 1000 (por defecto)
sys.setrecursionlimit(2000)   # se puede cambiar, con cuidado
```

Si lo superás, Python lanza `RecursionError: maximum recursion depth exceeded`.

```python
def infinita(n):
    return infinita(n + 1)   # nunca llega al caso base

infinita(0)   # 💥 RecursionError
```

**¿Cuándo usar recursión?**

Usala cuando el problema tiene estructura naturalmente recursiva (árboles, directorios, algoritmos divide-y-vencerás). Para problemas simples como factorial o Fibonacci, la versión iterativa suele ser más eficiente:

```python
# Iterativo — sin riesgo de RecursionError, más eficiente en memoria
def factorial_iter(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado
```

---

## 5. Errores y Excepciones

### try / except

Cuando Python encuentra un error en tiempo de ejecución lanza una **excepción**. Si no la manejás, el programa se detiene. `try/except` permite capturarla y reaccionar:

```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero")
```

**Múltiples except** — cada uno captura un tipo distinto:

```python
try:
    valor = int(input("Número: "))
    resultado = 10 / valor
except ValueError:
    print("Eso no es un número entero")
except ZeroDivisionError:
    print("No podés dividir por cero")
```

**`as e`** — captura el objeto excepción para inspeccionar el mensaje:

```python
try:
    int("abc")
except ValueError as e:
    print(f"Error: {e}")   # Error: invalid literal for int() with base 10: 'abc'
```

**`else`** — se ejecuta solo si NO hubo excepción. **`finally`** — se ejecuta siempre:

```python
try:
    resultado = 10 / 2
except ZeroDivisionError:
    print("Error de división")
else:
    print(f"Resultado: {resultado}")   # solo si el try tuvo éxito
finally:
    print("Siempre se ejecuta")        # con o sin excepción — ideal para limpiar recursos
```

**Jerarquía de excepciones comunes:**

```
BaseException
└── Exception
    ├── ValueError        — valor incorrecto para el tipo (int("abc"))
    ├── TypeError         — tipo incorrecto para la operación ("a" + 1)
    ├── KeyError          — clave no existe en diccionario
    ├── IndexError        — índice fuera de rango en lista/tupla
    ├── AttributeError    — atributo o método no existe en el objeto
    ├── NameError         — variable no definida
    ├── ZeroDivisionError — división por cero
    ├── FileNotFoundError — archivo no encontrado
    └── RecursionError    — límite de recursión superado
```

Capturá siempre el tipo más específico posible — nunca uses `except Exception` como primera opción, porque oculta errores reales.

---

### raise

`raise` lanza una excepción manualmente. Usalo para señalar condiciones inválidas en tu código:

```python
def dividir(a, b):
    if b == 0:
        raise ValueError("El divisor no puede ser cero")
    return a / b
```

**Re-lanzar** — dentro de un `except`, `raise` sin argumentos vuelve a lanzar la excepción original:

```python
try:
    conectar_db()
except ConnectionError as e:
    registrar_log(e)
    raise   # propaga el error hacia arriba sin modificarlo
```

**Buenas prácticas:**

- Usá el tipo más específico que describa el error real
- El mensaje debe explicar qué salió mal y si es posible por qué
- No lances `Exception` base — elegí o creá un subtipo
- No uses excepciones para control de flujo normal (no es un `if`)

**Convenciones de nombre:** los nombres de excepciones siempre terminan en `Error` (`ValueError`, `PagoRechazadoError`, `ConexionTimeoutError`).

---

### Excepciones personalizadas

Creá tus propias excepciones cuando necesitás representar errores específicos del dominio de tu aplicación:

```python
class PagoRechazadoError(Exception):
    """Se lanza cuando un pago no puede procesarse."""

    def __init__(self, monto, motivo):
        self.monto = monto
        self.motivo = motivo
        super().__init__(f"Pago de ${monto:.2f} rechazado: {motivo}")
```

```python
try:
    raise PagoRechazadoError(99.99, "fondos insuficientes")
except PagoRechazadoError as e:
    print(e.motivo)   # "fondos insuficientes"
    print(e.monto)    # 99.99
```

**Jerarquía propia** — creá una clase raíz para tu aplicación y derivá de ella:

```python
class AppError(Exception):
    """Raíz de todas las excepciones de la aplicación."""

class DatabaseError(AppError):
    pass

class ConexionTimeoutError(DatabaseError):
    def __init__(self, host, segundos):
        self.host = host
        super().__init__(f"Timeout al conectar con {host} después de {segundos}s")
```

Esto permite capturar toda la familia con un solo `except AppError`, o ser específico con `except ConexionTimeoutError`.

**Buenas prácticas:**

- Siempre heredá de `Exception` o de un subtipo (nunca de `BaseException` directamente)
- Creá una raíz propia (`AppError`, `LibraryError`) para poder capturar toda la familia
- Nombre siempre termina en `Error`
- Solo añadí atributos y métodos si realmente son necesarios para el manejo del error
- Documentá con docstring qué condición representa

---

### Context managers y `with`

Un **context manager** garantiza que un recurso se libere correctamente al terminar, incluso si ocurre una excepción.

```python
# Sin with — si ocurre error entre open() y close(), el archivo queda abierto
archivo = open("datos.txt", "r")
contenido = archivo.read()
archivo.close()

# Con with — cierra automáticamente al salir del bloque, con o sin error
with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
# archivo.close() se llama aquí automáticamente
```

**Múltiples recursos en un solo `with`:**

```python
with open("entrada.txt") as entrada, open("salida.txt", "w") as salida:
    salida.write(entrada.read())
```

**Modos de apertura de archivos:**

| Modo | Descripción |
|------|-------------|
| `"r"` | Lectura (por defecto) |
| `"w"` | Escritura (sobreescribe) |
| `"a"` | Append (agrega al final) |
| `"r+"` | Lectura y escritura |
| `"b"` | Binario (combinable: `"rb"`, `"wb"`) |

Cualquier objeto que implemente `__enter__` y `__exit__` funciona con `with` — no solo archivos. Conexiones a bases de datos, locks de threading, transacciones, etc.

---

## 6. Programación Orientada a Objetos (OOP)

### Conceptos: clase, objeto, instancia

| Concepto | Definición | Analogía |
|----------|-----------|---------|
| **Clase** | Plantilla que define estructura y comportamiento | Plano de un edificio |
| **Objeto / Instancia** | Ejemplar concreto creado a partir de la clase | El edificio construido |
| **Atributo** | Variable que pertenece a un objeto | Las habitaciones del edificio |
| **Método** | Función que pertenece a una clase | Las acciones que puede hacer el edificio |

```python
class Perro:       # definición de la clase (el molde)
    pass

firulais = Perro()     # instanciación — crea un objeto concreto
rex = Perro()          # otra instancia distinta, mismo molde

type(firulais)         # <class '__main__.Perro'>
isinstance(firulais, Perro)   # True
```

`firulais` y `rex` son **instancias independientes** — modificar una no afecta a la otra.

---

### Crear clases y métodos

```python
class Persona:
    """Representa una persona con nombre y edad."""

    especie = "Homo sapiens"      # atributo de clase — compartido por TODAS las instancias

    def __init__(self, nombre, edad):    # constructor — se llama al instanciar
        self.nombre = nombre             # atributo de instancia — único por objeto
        self.edad = edad

    def saludar(self):                   # método de instancia — siempre recibe self
        return f"Hola, soy {self.nombre}"

    def cumplir_anios(self):
        self.edad += 1

    def __str__(self):                   # representación legible (usa print())
        return f"Persona({self.nombre}, {self.edad})"

    def __repr__(self):                  # representación técnica (debugging, consola)
        return f"Persona(nombre={self.nombre!r}, edad={self.edad!r})"
```

**`self`** es la referencia al objeto actual — Python lo pasa automáticamente, vos no lo escribís al llamar el método.

**Atributo de clase vs atributo de instancia:**

```python
print(Persona.especie)     # "Homo sapiens" — acceso desde la clase
ana = Persona("Ana", 30)
print(ana.especie)         # "Homo sapiens" — también accesible desde la instancia
ana.especie = "mutante"    # crea un atributo de instancia que sombrea el de clase
print(Persona.especie)     # "Homo sapiens" — el de clase no cambió
```

---

### Instanciación y uso de métodos

```python
ana = Persona("Ana", 30)      # llama a __init__(self, "Ana", 30)

ana.nombre                    # "Ana"
ana.saludar()                 # "Hola, soy Ana"
ana.cumplir_anios()
ana.edad                      # 31

print(ana)                    # "Persona(Ana, 31)" — usa __str__
repr(ana)                     # "Persona(nombre='Ana', edad=31)" — usa __repr__
```

---

### Convenciones idiomáticas en Python para clases

| Elemento | Convención | Ejemplo |
|----------|-----------|---------|
| Nombre de clase | `PascalCase` | `ClienteVIP`, `ProductoDigital` |
| Atributos y métodos | `snake_case` | `nombre_completo`, `calcular_total()` |
| Primer parámetro de instancia | siempre `self` | `def saludar(self):` |
| Atributo "protegido" (interno) | prefijo `_` | `self._saldo` |
| Atributo "privado" (name mangling) | prefijo `__` | `self.__password` |
| Constructor | `__init__` | `def __init__(self, ...)` |
| Representación string | `__str__` | `def __str__(self):` |

El prefijo `_` es una **convención** — Python no impide el acceso, pero señala "esto es interno, no lo uses desde afuera".

---

### UML básico y mapeo a clases

**Estructura de una caja de clase:**

```
┌──────────────────────────┐
│         Persona          │  ← nombre (PascalCase)
├──────────────────────────┤
│ + especie: str           │  ← atributos (+ público, - privado, # protegido)
│ - nombre: str            │
│ - edad: int              │
├──────────────────────────┤
│ + __init__(nombre, edad) │  ← métodos con firma y tipo de retorno
│ + saludar(): str         │
│ + cumplir_anios()        │
└──────────────────────────┘
```

**Multiplicidad** — cuántos objetos participan en la relación:

```
1      exactamente uno     0..1   cero o uno (opcional)
*      cero o más          1..*   uno o más
```

**Tipos de relación:**

```
Herencia     ──────────▷   flecha vacía    "es-un"
Composición  ◆──────────   rombo relleno   "tiene-un" (parte no vive sin el todo)
Agregación   ◇──────────   rombo vacío     "tiene-un" (parte puede vivir sola)
Asociación   ───────────   línea simple    "usa-un"
Dependencia  - - - - - →   línea punteada  "depende de" (temporal)
```

```
Composición:  Casa ◆──── Habitacion      (destruís Casa → desaparecen las habitaciones)
Agregación:   Universidad ◇──── Estudiante  (cierra la uni → el estudiante sigue existiendo)
```

**Diagrama multi-clase con multiplicidad:**

```
┌───────────────┐        ┌────────────────┐
│    Persona    │        │    Direccion   │
├───────────────┤        ├────────────────┤
│ - nombre: str │ 1  ◆── │ - calle: str   │
│ - edad: int   │ tiene 1│ - ciudad: str  │
├───────────────┤        └────────────────┘
│ + saludar()   │
└───────────────┘
        △
        │ hereda
┌───────────────┐
│    Empleado   │
├───────────────┤
│ - empresa: str│
├───────────────┤
│ + trabajar()  │
└───────────────┘
```

**Mapeo UML → Python:**

| UML | Python |
|-----|--------|
| Caja de clase | `class NombreClase:` |
| Atributo de instancia | `self.nombre` en `__init__` |
| `+` público | sin prefijo |
| `-` privado | prefijo `__` |
| `#` protegido | prefijo `_` |
| Atributo de clase | variable dentro de la clase, fuera de `__init__` |
| Herencia `──▷` | `class Subclase(Base):` |
| Composición `◆──` | `self.parte = Parte()` dentro de `__init__` |

**Buenas prácticas:**

- Dibujá el UML ANTES de escribir el código en diseños complejos
- Una clase = una responsabilidad (principio S de SOLID)
- Preferí composición sobre herencia cuando el vínculo no es "es-un"

---

### Herencia

La herencia permite que una clase **extienda** el comportamiento de otra. La subclase hereda atributos y métodos, y puede agregar o sobrescribir:

```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        raise NotImplementedError

    def describir(self):
        return f"Soy {self.nombre} y digo: {self.hablar()}"


class Perro(Animal):
    def hablar(self):        # override del método
        return "Guau"


class Gato(Animal):
    def hablar(self):
        return "Miau"


perro = Perro("Rex")
print(perro.describir())   # "Soy Rex y digo: Guau" — describir() viene de Animal
```

**`super()`** — llama al método de la clase padre, útil para extender sin reemplazar:

```python
class Empleado(Persona):
    def __init__(self, nombre, edad, empresa):
        super().__init__(nombre, edad)   # delega la inicialización al padre
        self.empresa = empresa           # agrega lo propio

    def saludar(self):
        base = super().saludar()         # reutiliza el saludar del padre
        return f"{base}, trabajo en {self.empresa}"
```

**`isinstance()` e `issubclass()`:**

```python
isinstance(perro, Perro)    # True
isinstance(perro, Animal)   # True  — también es Animal por herencia
issubclass(Perro, Animal)   # True
issubclass(Animal, Perro)   # False
```

---

## 7. Encapsulamiento

### Convenciones para atributos "privados"

Python no tiene modificadores de acceso reales (`private`, `protected`). Usa **convenciones**:

| Prefijo | Significado | Acceso desde afuera |
|---------|-------------|---------------------|
| sin prefijo | público | libre |
| `_nombre` | "protegido" — uso interno | posible, pero no deberías |
| `__nombre` | "privado" — name mangling | `obj._Clase__nombre` (técnicamente posible pero nunca lo hagas) |

```python
class CuentaBancaria:
    def __init__(self, saldo):
        self._saldo = saldo        # convención: "no toques esto desde afuera"
        self.__pin = 1234          # name mangling → _CuentaBancaria__pin

cuenta = CuentaBancaria(1000)
cuenta._saldo           # 1000 — Python te deja, pero es una mala práctica
cuenta.__pin            # 💥 AttributeError — no existe tal atributo
cuenta._CuentaBancaria__pin   # 1234 — existe, pero jamás hagas esto
```

El `__` no es seguridad real — es una señal de "esto es REALMENTE interno".

---

### Propiedades con `@property`

`@property` convierte un método en un atributo de solo lectura, sin cambiar la interfaz pública:

```python
class Circulo:
    def __init__(self, radio):
        self._radio = radio

    @property
    def radio(self):             # getter — se llama como atributo: c.radio
        return self._radio

    @radio.setter
    def radio(self, valor):      # setter — se llama con asignación: c.radio = 5
        if valor < 0:
            raise ValueError("El radio no puede ser negativo")
        self._radio = valor

    @property
    def area(self):              # propiedad calculada — de solo lectura
        return 3.14159 * self._radio ** 2
```

```python
c = Circulo(5)
c.radio          # 5   — llama al getter
c.radio = 10     # llama al setter
c.radio = -1     # 💥 ValueError
c.area           # 314.159 — calculado al vuelo, no almacenado
```

---

### Refactor: ocultamiento del estado y API pública

**El problema** — empezás con atributos públicos y más adelante necesitás agregar validación:

```python
# Versión inicial — atributo público
class Producto:
    def __init__(self, precio):
        self.precio = precio    # cualquiera puede hacer producto.precio = -999
```

**El refactor sin romper la API** — con `@property` los usuarios externos no notan el cambio:

```python
class Producto:
    def __init__(self, precio):
        self.precio = precio    # ← interfaz pública idéntica, internamente llama al setter

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = valor
```

```python
p = Producto(100)
p.precio           # 100   — igual que antes
p.precio = 200     # OK
p.precio = -50     # 💥 ValueError — nuevo comportamiento, misma sintaxis
```

**Compatibilidad hacia atrás:** todo el código que usaba `producto.precio = x` sigue funcionando — no hay que cambiar los clientes. Esto es la clave de `@property`: podés **agregar lógica después** sin romper la interfaz.

**Separación entre estado interno y API pública:**

```python
class Temperatura:
    def __init__(self, celsius):
        self._celsius = celsius      # estado interno en °C

    @property
    def celsius(self):               # API pública
        return self._celsius

    @celsius.setter
    def celsius(self, valor):
        self._celsius = valor

    @property
    def fahrenheit(self):            # API pública alternativa — derivada del estado interno
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, valor):
        self._celsius = (valor - 32) * 5/9
```

```python
t = Temperatura(100)
t.fahrenheit    # 212.0
t.fahrenheit = 32
t.celsius       # 0.0
```

---

## 8. Herencia y Composición — Teoría y Patrones

### Herencia simple

Ya cubierto en ## 6. La regla para decidir si aplicarla: **¿el vínculo es "es-un"?**

- `Perro` es un `Animal` ✓ → herencia
- `Auto` es un `Motor` ✗ → composición (un Auto TIENE un Motor)

### Herencia vs Composición

```python
# ❌ Herencia mal aplicada — un Auto NO es un Motor
class Motor:
    def encender(self): ...

class Auto(Motor):   # conceptualmente incorrecto
    pass

# ✅ Composición — un Auto TIENE un Motor
class Auto:
    def __init__(self):
        self.motor = Motor()    # composición

    def encender(self):
        self.motor.encender()
```

**Regla práctica:** si podés decir "X es un Y", usá herencia. Si decís "X tiene un Y", usá composición. Cuando dudes, preferí composición — es más flexible y menos acoplada.

| | Herencia | Composición |
|---|---|---|
| Vínculo | "es-un" | "tiene-un" |
| Acoplamiento | alto | bajo |
| Flexibilidad | baja (estática) | alta (swappable) |
| Reutilización | implícita | explícita |

### Patrón Mixin

Un **mixin** es una clase diseñada para agregar comportamiento específico a otras clases sin ser una clase base completa. No tiene estado propio ni se instancia directamente:

```python
class JsonMixin:
    """Agrega capacidad de serialización JSON a cualquier clase."""
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class LogMixin:
    """Agrega logging automático a cualquier clase."""
    def log(self, mensaje):
        print(f"[{self.__class__.__name__}] {mensaje}")


class Usuario(LogMixin, JsonMixin):    # hereda los mixins
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

u = Usuario("Ana", "ana@mail.com")
u.to_json()       # '{"nombre": "Ana", "email": "ana@mail.com"}'
u.log("creado")   # "[Usuario] creado"
```

Convención: los nombres de mixins terminan en `Mixin` para dejar claro su propósito.

### Anti-patrones a evitar

**Cadenas de herencia profundas** — más de dos o tres niveles es una señal de problema:

```python
# ❌ Difícil de rastrear, altamente acoplado
class A: ...
class B(A): ...
class C(B): ...
class D(C): ...   # ¿qué métodos tiene D? Hay que rastrear 4 clases
```

**Herencia solo para reutilizar código** — si la subclase no es realmente "es-un":

```python
# ❌ Stack hereda de list solo para reutilizar append/pop, pero no es una lista
class Stack(list):
    pass   # pero ahora Stack tiene sort(), reverse(), etc. que no tienen sentido
```

**God class** — una clase que hace demasiadas cosas y acumula toda la lógica del sistema.

**Herencia múltiple sin mixins** — mezclar clases con estado propio en herencia múltiple lleva al problema del diamante y colisiones de nombres.

---

## 9. MRO y el Algoritmo C3

### ¿Qué es el MRO?

El **Method Resolution Order** (MRO) define el orden en que Python busca un método o atributo cuando hay herencia. Es la respuesta a: *"¿en qué clase busco primero?"*

```python
class A:
    def hablar(self): return "A"

class B(A):
    def hablar(self): return "B"

class C(B):
    pass

c = C()
c.hablar()   # "B" — Python busca: C → B → A → object, toma el primero que encuentra
```

### Inspección del MRO

```python
C.__mro__     # (<class 'C'>, <class 'B'>, <class 'A'>, <class 'object'>)
C.mro()       # misma información como lista
```

### Herencia en diamante

El problema clásico — dos clases comparten un padre común:

```
      A
     / \
    B   C
     \ /
      D
```

```python
class A:
    def hablar(self): return "A"

class B(A):
    def hablar(self): return "B"

class C(A):
    def hablar(self): return "C"

class D(B, C):
    pass

D().hablar()     # "B"
D.__mro__        # D → B → C → A → object
```

Sin C3, si `A` apareciera dos veces el resultado sería ambiguo. C3 garantiza que cada clase aparezca **exactamente una vez** en el MRO.

### Algoritmo C3 — Linearización

C3 construye el MRO con tres reglas:
1. Una subclase siempre aparece antes que sus bases
2. El orden de las bases se respeta tal como se declaró
3. Si una clase aparece en múltiples lugares, se incluye en el último posible

Para `class D(B, C)`:

```
MRO(D) = D + merge(MRO(B), MRO(C), [B, C])
       = D + merge([B, A, object], [C, A, object], [B, C])
       = D → B → C → A → object
```

Pythom lanza `TypeError` si el MRO es inconsistente (imposible linearizar):

```python
class X(A, B): pass
class Y(B, A): pass
class Z(X, Y): pass   # 💥 TypeError: Cannot create a consistent MRO
```

### Mixins y MRO

El orden en que declarás los mixins importa:

```python
class Base: pass

class MixinA(Base):
    def metodo(self): return "MixinA"

class MixinB(Base):
    def metodo(self): return "MixinB"

class MiClase(MixinA, MixinB, Base):
    pass

MiClase().metodo()     # "MixinA" — MixinA está primero en el MRO
MiClase.__mro__        # MiClase → MixinA → MixinB → Base → object
```

Convención: en herencia múltiple, los mixins van ANTES de la clase base principal.

---

## 10. Polimorfismo y Duck Typing

### Polimorfismo

**Polimorfismo** = misma interfaz (mismo nombre de método), comportamiento distinto según el tipo:

```python
class Perro:
    def hablar(self): return "Guau"

class Gato:
    def hablar(self): return "Miau"

class Persona:
    def hablar(self): return "Hola"

animales = [Perro(), Gato(), Persona()]

for a in animales:
    print(a.hablar())   # cada uno responde diferente al mismo mensaje
```

No importa el tipo concreto — si tiene `hablar()`, funciona.

### Duck Typing

> "If it walks like a duck and quacks like a duck, it's a duck."

Python no verifica tipos en tiempo de compilación. Si el objeto tiene el método que necesitás, funciona — no importa de qué clase sea:

```python
def hacer_hablar(animal):
    print(animal.hablar())   # no verificamos tipo, confiamos en la interfaz

hacer_hablar(Perro())     # "Guau"
hacer_hablar(Gato())      # "Miau"
hacer_hablar(Persona())   # "Hola"

# Incluso funciona con clases que no heredan de ninguna base común
class Robot:
    def hablar(self): return "Beep boop"

hacer_hablar(Robot())     # "Beep boop" — ¡funciona igual!
```

### EAFP vs LBYL

Dos estilos para manejar la incertidumbre de tipos:

```python
# LBYL — Look Before You Leap (verificás antes de actuar)
if hasattr(obj, "hablar"):
    obj.hablar()

# EAFP — Easier to Ask Forgiveness than Permission (intentás y capturás el error)
try:
    obj.hablar()
except AttributeError:
    pass
```

Python idiomático prefiere **EAFP** — es más limpio y no tiene race conditions.

### `typing.Protocol` — Duck typing con tipos estáticos (Python 3.8+)

Podés documentar qué métodos esperás sin exigir herencia:

```python
from typing import Protocol

class Hablante(Protocol):
    def hablar(self) -> str: ...    # define la interfaz esperada

def hacer_hablar(animal: Hablante) -> None:
    print(animal.hablar())
```

Cualquier clase que implemente `hablar()` satisface el protocolo — sin heredar de `Hablante`.

### Ventajas en APIs flexibles

```python
# ❌ Rígido — obliga a heredar de una clase específica
def procesar(animal: Animal):
    animal.hablar()

# ✅ Flexible — cualquier objeto con hablar() funciona
def procesar(animal):
    animal.hablar()

# ✅ Flexible con documentación de tipos
def procesar(animal: Hablante):
    animal.hablar()
```

Duck typing hace que las funciones sean reutilizables sin acoplarse a jerarquías de clases. Es la base de patrones como el Iterator, Context Manager y muchos otros protocolos de Python.
