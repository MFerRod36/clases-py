print("Hola Mundo")


# Listas:
""" 
numeros = [1, 2, 3, 4, 5]
mixta = [1, "Hola", 3.14, True]
print(numeros)
print(mixta)
"""

# Diccionarios:
"""
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
}
print(persona)

persona["nombre"] = "Ana"  # Modifica el valor de un campo existente
persona["nombre2"] = "Cristina"  # Agrega un nuevo campo al diccionario
print(persona)

del persona["nombre2"]  # Elimina un campo del diccionario
print(persona)

nombre = persona.pop("nombre")  # Elimina el campo "nombre" y devuelve su valor
print(nombre)  # Imprime el valor eliminado
print(persona)

persona.clear()  # Elimina todos los campos del diccionario
print(persona)

ciudad = persona.get(
    "ciudad", "Valor por defecto"
)  # Devuelve el valor del campo "ciudad" o "Valor por defecto" si no existe
print(ciudad)


print(persona.keys())  # Devuelve una lista de las claves del diccionario
print(persona.values())  # Devuelve una lista de los valores del diccionario
print(persona.items())  # Devuelve una lista de tuplas (clave, valor) del diccionario
"""

# Conjuntos:
"""
colores = {"rojo", "verde", "azul"}
print(colores)

vacio = set()  # Crea un conjunto vacío
print(vacio)

colores.add("amarillo")  # Agrega un elemento al conjunto
print(colores)

colores.remove("rosa")  # Elimina un elemento del conjunto
print(colores)

colores.discard(
    "morado"
)  # Elimina un elemento del conjunto sin generar error si no existe
print(colores)

colores.pop()  # Elimina y devuelve un elemento aleatorio del conjunto
print(colores)

colores.clear()  # Elimina todos los elementos del conjunto
print(colores)
"""
