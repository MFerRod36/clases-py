"""
En este ejercicio, trabajarás con un diccionario que representa un inventario de productos y sus cantidades.
Deberás implementar funciones que utilicen los métodos esenciales de diccionarios para realizar operaciones comunes:
1- Obtener la cantidad de un producto con un valor por defecto si no existe (get).
2- Listar todas las claves (productos) disponibles (keys).
3- Listar todos los pares producto-cantidad (items).
4- Actualizar el inventario con nuevos productos o cantidades (update).
5- Eliminar un producto del inventario y devolver su cantidad (pop).

** Formato de entrada
1- La primera línea contiene un entero N, el número de productos iniciales.
2- Las siguientes N líneas contienen un producto (cadena sin espacios) y su cantidad (entero), separados por espacio.
3- La siguiente línea contiene un entero M, el número de operaciones a realizar.
4- Las siguientes M líneas contienen una operación y sus argumentos:
get producto valor_defecto
keys
items
update K seguido de K líneas con producto y cantidad para actualizar
pop producto valor_defecto

*** Formato de salida
Para cada operación:
get: imprimir la cantidad del producto o el valor por defecto si no existe.
keys: imprimir las claves separadas por espacio, en orden de inserción.
items: imprimir cada par producto:cantidad separados por espacio, en orden de inserción.
update: no imprimir nada.
pop: imprimir la cantidad eliminada o el valor por defecto si no existía.
"""


def main():
    n = int(input())
    inventario = {}
    for _ in range(n):
        producto, cantidad = input().split()
        inventario[producto] = int(cantidad)

    m = int(input())
    for _ in range(m):
        linea = input().split()
        operacion = linea[0]

        if (
            operacion == "keys"
        ):  # Imprime las claves del inventario separadas por espacio, en orden de inserción.
            print(" ".join(inventario.keys()))
        elif (
            operacion == "get"
        ):  # Imprime la cantidad del producto o el valor por defecto si no existe.
            producto, valor_defecto = linea[1], int(linea[2])
            print(inventario.get(producto, valor_defecto))
        elif (
            operacion == "pop"
        ):  # Imprime la cantidad eliminada o el valor por defecto si no existía.
            producto, valor_defecto = linea[1], int(linea[2])
            print(inventario.pop(producto, valor_defecto))
        elif (
            operacion == "items"
        ):  # Imprime cada par producto:cantidad separados por espacio, en orden de inserción.
            print(" ".join(f"{clave}:{valor}" for clave, valor in inventario.items()))
        elif (
            operacion == "update"
        ):  # Actualiza el inventario con nuevos productos o cantidades (update).
            k = int(linea[1])
            for _ in range(k):
                producto, cantidad = input().split()
                inventario[producto] = int(cantidad)


if __name__ == "__main__":
    main()
