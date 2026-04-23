def main():
    n = [int(x) for x in input("Ingrese números: ").split()]

    conjunto = set(n)
    print(" ".join(str(x) for x in conjunto))

    x = int(input("Ingrese un número para verificar si está en el conjunto: "))
    if x in conjunto:
        print("Sí")
    else:
        print("No")


main()
