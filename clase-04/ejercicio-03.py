"""
Práctica de depuración: Factorial con error de alcance.
En este ejercicio, tienes un script que calcula el factorial de un número usando una función recursiva.
Sin embargo, el código tiene un error relacionado con el alcance de las variables que provoca un resultado incorrecto.

Tu tarea es:
1. Colocar breakpoints en la función factorial y en la llamada principal.
2. Usar la depuración paso a paso para inspeccionar las variables locales y globales.
3. Identificar el error de alcance y corregirlo.

Instrucciones para depurar:
1. Coloca un breakpoint en la línea resultado = 1 dentro de la función factorial.
2. Coloca otro breakpoint en la línea fact = factorial(num).
3. Ejecuta el depurador y observa el valor de n y resultado en cada llamada.
4. Inspecciona cómo se actualiza resultado y verifica si el valor es correcto.
5. Corrige el código si encuentras que el valor de resultado no se mantiene correctamente.

"""

# Factorial de un número n es el producto de todos los enteros positivos menores o iguales a n.


# Función para calcular el factorial de un número con un error de alcance, con breakpoints para depuración.
def factorial(n):
    resultado = (
        1  # Este resultado se reinicia en cada llamada, lo que es un error de alcance.
    )
    if n == 0 or n == 1:
        return resultado
    else:
        resultado *= n * factorial(
            n - 1
        )  # Aquí se multiplica el resultado, pero no se mantiene el valor acumulado.
        return resultado


# Llamada principal para calcular el factorial de un número.
num = 5
fact = factorial(num)
print(f"El factorial de {num} es: {fact}")
