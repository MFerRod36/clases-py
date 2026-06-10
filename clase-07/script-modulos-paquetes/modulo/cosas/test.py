#from cosas.mate import multiplicar #Path Absoluto
from .mate import multiplicar # Path Relativo.


if __name__ == "__main__":
    mul = multiplicar(2, 4)
    print(mul)