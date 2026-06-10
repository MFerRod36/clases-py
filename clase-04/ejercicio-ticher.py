"""Vamos a practicar definiendo y llamando funciones simples en Python.

1. Abre tu editor de código preferido (VS Code, PyCharm) o el REPL de Python.
2. Define una función llamada saludar que reciba un parámetro nombre y que imprima un saludo personalizado, por ejemplo: "¡Hola, Ana!".
3. Llama a la función saludar con diferentes nombres para ver cómo cambia el mensaje.
4. Define otra función llamada calcular_area_rectangulo que reciba dos parámetros: base y altura, y que imprima el área del rectángulo.
5. Llama a calcular_area_rectangulo con valores numéricos y verifica que el resultado sea correcto.
6. Recuerda usar la indentación correcta y agregar comentarios para explicar tu código.

Al finalizar, tendrás dos funciones básicas que demuestran cómo definir y reutilizar código en Python.
"""


# Paso 1: Definir la función saludar
def saludar(nombre):
    """Imprime un saludo personalizado."""
    print(f"¡Hola, {nombre}!")


# Paso 2: Llamar a la función saludar con diferentes nombres
saludar("Ana")
saludar("Carlos")
saludar("María")


# Paso 3: Definir la función calcular_area_rectangulo
def calcular_area_rectangulo(base, altura):
    """Imprime el área del rectángulo."""
    area = base * altura
    print(f"El área del rectángulo es: {area}")


# Paso 4: Llamar a la función calcular_area_rectangulo con valores numéricos
calcular_area_rectangulo(5, 3)
calcular_area_rectangulo(10, 7)

# Paso 5: Verificar que el resultado sea correcto
# Para el primer caso, el área debería ser 15 (5 * 3)
# Para el segundo caso, el área debería ser 70 (10 * 7)
