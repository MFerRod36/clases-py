# Defino la clase user, la plantilla para crear usuarios con atributos username y password y
# un método constructor para inicializar esos atributos al crear una instancia de la clase.

"""
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    # Método para representar el objeto como una cadena de texto, útil para imprimir el objeto.
    def __str__(self):
        return f"User information: username={self.username}, password={self.password}"

"""

# Instanciar la clase es sacar de esa plantilla un objeto concreto, con valores específicos para los atributos.
"""
print(User)

user1 = User("juan", "1234")
print(user1)
print(user1.username)
print(user1.password) 
"""

# Encapsulamiento: ocultar los atributos de una clase para protegerlos de accesos no autorizados.
# En Python, se puede lograr esto utilizando un guion bajo (_) antes del nombre del atributo para indicar que es privado.
# Sin embargo, esto es solo una convención y no impide realmente el acceso a los atributos desde fuera de la clase.

""" 
class User2:
    def __init__(self, username, password):
        self.username = username
        self.__password = password  # Atributo privado


user2 = User2("maria", "5678")
print(user2)
print(user2.username)
print(
    user2.__password
)  # Esto generará un error porque __password es un atributo privado y no se puede acceder directamente desde fuera de la clase.
"""


class User3:
    def __init__(self, username, password):
        self.username = username
        self.__password = password  # Atributo privado
        self.__logueado = (
            False  # Atributo privado para indicar si el usuario está logueado o no
        )

    # Método para mostrar la información del usuario reemplazando la contraseña por asteriscos
    def show_info(self):
        if self.__logueado:
            return f"User information: username={self.username}, password={'*' * len(self.__password)}"
        else:
            return (
                "User information: username={}, password=**** (login required)".format(
                    self.username
                )
            )

    # Método para loguear al usuario, cambiando el estado de logueado a True
    def login(self, password):
        if password == self.__password:
            self.__logueado = True
            return "Login successful"
        else:
            return "Login failed: Incorrect password"


user3 = User3("pedro", "abcd")
print(user3)
print(user3.show_info())
print(user3.login("abcd"))
print(user3.show_info())
