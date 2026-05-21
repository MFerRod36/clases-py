# Clase y objeto


class Gato:
    def __init__(self, nombre, edad=5):  # Método constructor => Inicializa el objeto
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"El gato se llama {self.nombre} y tiene {self.edad} años."

    def maullar(self, otro_nombre):
        return f"{self.nombre} dice: Miau! y {otro_nombre} responde: Miao!"

    def caminar(self):
        return f"{self.nombre} está caminando."

    def informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"


gato1 = Gato("Michi", 3)  # Crea un objeto de la clase Gato
print(gato1)  # Llama al método __str__
print(gato1.maullar("Garfield"))  # Llama al método maullar
print(gato1.caminar())  # Llama al método caminar
print(gato1.informacion())  # Llama al método informacion
