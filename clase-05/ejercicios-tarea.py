"""
Representación del siguiente escenario en un diagrama de clases:
1. La clase `Persona` actúa como clase base.
2. `Empleado` y `Cliente` heredan de `Persona`.
3. `Empleado` tiene un atributo de `sueldo_bruto`.
4. `Directivo` (una subclase de `Empleado`) tiene una `categoría` y subordinados.
5. `Cliente` añade un `telefono_de_contacto`.
"""


# Clase base
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


# Clase Empleado que hereda de Persona
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo_bruto):
        super().__init__(nombre, edad)
        self.sueldo_bruto = sueldo_bruto


# Clase Cliente que hereda de Persona
class Cliente(Persona):
    def __init__(self, nombre, edad, telefono_de_contacto):
        super().__init__(nombre, edad)
        self.telefono_de_contacto = telefono_de_contacto


# Clase Directivo que hereda de Empleado
class Directivo(Empleado):
    def __init__(self, nombre, edad, sueldo_bruto, categoria):
        super().__init__(nombre, edad, sueldo_bruto)
        self.categoria = categoria
        self.subordinados = []

    def agregar_subordinado(self, empleado):
        self.subordinados.append(empleado)


# Ejemplo de uso
if __name__ == "__main__":
    # Crear un cliente
    cliente1 = Cliente("Juan Pérez", 30, "555-1234")

    # Crear un empleado
    empleado1 = Empleado("Ana Gómez", 28, 3000)

    # Crear un directivo
    directivo1 = Directivo("Carlos López", 45, 5000, "Gerente")

    # Agregar el empleado como subordinado del directivo
    directivo1.agregar_subordinado(empleado1)

    # Imprimir información del cliente
    print(
        f"Cliente: {cliente1.nombre}, Edad: {cliente1.edad}, Teléfono: {cliente1.telefono_de_contacto},"
    )

    # Imprimir información del empleado
    print(
        f"Empleado: {empleado1.nombre}, Edad: {empleado1.edad}, Sueldo Bruto: {empleado1.sueldo_bruto},"
    )

    # Imprimir información del directivo y sus subordinados
    print(
        f"Directivo: {directivo1.nombre}, Edad: {directivo1.edad}, Sueldo Bruto: {directivo1.sueldo_bruto}, Categoría: {directivo1.categoria},"
    )
    print("Subordinados:")
    for subordinado in directivo1.subordinados:
        print(f"- {subordinado.nombre}")
