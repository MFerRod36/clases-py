resultado = 0
try:
    numero = input("Ingrese el primer número: ")
    numero = int(numero)
    resultado = 10 / numero
    print(resultado)
except ZeroDivisionError:
    print("No se puede dividir por cero.")
except NameError:
    print("La variable 'resultado' no está definida.")
except ValueError:
    print("Debe ingresar un número válido.")
except Exception as e:
    print(f"Ocurrió un error:{repr(e)}")
