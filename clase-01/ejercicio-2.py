"""
Ejercicio A: Eliminar duplicados manteniendo el orden
Dado un listado de elementos, queremos eliminar los duplicados pero manteniendo el orden original de aparición.
Ejemplo:
Entrada: [3, 5, 3, 2, 5, 1]
Salida esperada: [3, 5, 2, 1]


Ejercicio B: Comparar elementos entre dos listas
Dadas dos listas, queremos encontrar los elementos que están en ambas (intersección) y los que están en una pero no en la otra (diferencia).
Ejemplo:
Lista A: [1, 2, 3, 4]
Lista B: [3, 4, 5, 6]
Elementos comunes: [3, 4]
Elementos en A no en B: [1, 2]
Elementos en B no en A: [5, 6]
Usa la entrada estándar para leer los datos y la salida estándar para imprimir los resultados.
"""


# Solución al ejercicio A: Eliminar duplicados manteniendo el orden.
def eliminar_duplicados(lista):
    resultado = []
    vistos = set()
    for elemento in lista:
        if elemento not in vistos:
            resultado.append(elemento)
            vistos.add(elemento)
    return resultado


# Solución al ejercicio B: Comparar elementos entre dos listas. Elementos comunes (intersección) y elementos en A pero no en B (diferencia) y elementos en B pero no en A (diferencia).
def comparar_listas(lista1, lista2):
    set1 = set(lista1)
    set2 = set(lista2)

    comunes = set1.intersection(set2)
    diferencia_a_b = set1.difference(set2)
    diferencia_b_a = set2.difference(set1)

    return comunes, diferencia_a_b, diferencia_b_a


# Ejemplo de uso
if __name__ == "__main__":
    n = int(input())
    lista = list(map(int, input().split()))
    resultado = eliminar_duplicados(lista)
    print(" ".join(map(str, resultado)))

    # Lectura y ejecución para ejercicio 2
    m = int(input())
    lista1 = list(map(int, input().split()))
    k = int(input())
    lista2 = list(map(int, input().split()))
    comunes, diferencia_a_b, diferencia_b_a = comparar_listas(lista1, lista2)
    print(" ".join(map(str, sorted(comunes))))
    print(" ".join(map(str, sorted(diferencia_a_b))))
    print(" ".join(map(str, sorted(diferencia_b_a))))
