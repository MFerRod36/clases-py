def pedir_numero():
    while True:
        try:
            numero = int(input("Ingrese un número: "))
            break
        except (ValueError, ZeroDivisionError):
            print("Error: Ingrese un número válido.")
        except Exception as e:
            print(f"Error: {e}. Por favor, ingrese un número válido.")
            numero = input("Ingrese un número: ")
            if numero.isdigit():
                numero = int(numero)
                break
    return numero


print(pedir_numero())
