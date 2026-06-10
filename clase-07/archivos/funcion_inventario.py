PRODUCTOS = {"manzanas": 10, "leche": 2, "pan": 1, "huevos": 12, "arroz": 5}

MENU = {
    1: "Listar productos",
    2: "Modificar cantidad de un producto",
    3: "Eliminar productos",
    4: "Ver producto",
    5: "Agregar producto",
    6: "Salir",
}
INVENTARIO_FILE = "inventario.json"
import json


def guardar_inventario():
    """
    Guarda el diccionario PRODUCTOS en un archivo JSON.
    """
    with open(INVENTARIO_FILE, "w", encoding="utf-8") as f:
        json.dump(PRODUCTOS, f, indent=4)


def cargar_inventario():
    """
    Carga el inventario desde un archivo JSON si existe.
    """
    global PRODUCTOS
    try:
        with open(INVENTARIO_FILE, "r", encoding="utf-8") as f:
            PRODUCTOS = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print(
            "No se encontró un archivo de inventario válido. Usando valores predeterminados."
        )


def verificar_existencia_del_producto(producto, mostrar_msj=True):
    """
    Recibe un producto[str] y un valor bool para mostrar un msj.
    Devuelve un valor booleano, segun el producto recibido.
    """
    if producto == "":
        return False
    if PRODUCTOS.get(producto.lower()) is None:
        if mostrar_msj:
            print("No existe el producto")
        return False
    return True


def mostrar_menu():
    """
    Muestra un menu con print().
    """
    print("Menu:")
    for item, opcion in MENU.items():
        print(f"{item}: {opcion}")


def pedir_numero_acotado(mensaje, opc_min, opc_max):
    """
    Recibe un mensaje[str] y opc_min[int], opc_max[int].
    Pide un valor al usuario y valida con los parametros.
    Devuelve un valor int.
    """
    opcion = input(mensaje)
    if opcion.isdigit() and opc_min < int(opcion) <= opc_max:
        return int(opcion)
    while not (opcion.isdigit() and opc_min < int(opcion) <= opc_max):
        print("nro invalido, vuelva a ingresar uno dif.")
        opcion = input(mensaje)
    return int(opcion)


def pedir_info_con_confirmacion(msj):
    """
    Recibe un mensaje.
    Pide un dato al usuario y lo valida con una confirmacion extra del usuario.
    Devuelve un dato[str].
    """
    validacion = False
    while not validacion:
        respuesta = input(msj)
        aux = pedir_numero_acotado(
            f"Ingreso: {respuesta}, estas seguro?.\n1 - Afirmativo.\n2 - Volver a ingresar.\n3 - salir.\nopcion: ",
            0,
            3,
        )
        if aux == 1:
            validacion = True
        elif aux == 3:
            validacion = True
            respuesta = ""
    return respuesta


def listar_productos():
    """
    Imprime por pantalla la lista de productos en el inventario.
    """
    print("Listado de productos")
    for producto, cantidad in PRODUCTOS.items():
        print(f"{producto.capitalize()}: {cantidad} unidad/es")
    print()


def verificar_negativo(nro):
    """
    Recibe un nro[str] y lo valida si es un nro negativo
    Devuelve un valor booleano.
    """
    if nro.startswith("-") and nro[1:].isdigit():
        return True
    return False


def pedir_nro(msj, permitir_negativo=False):
    """
    Recibe un msj a mostrar y pide un dato al usuario, validandolo.
    Devuelve un valor[int]
    """
    while True:
        cantidad = input(msj)
        if (permitir_negativo and verificar_negativo(cantidad)) or cantidad.isdigit():
            return int(cantidad)
        print("Ingreso un nro invalido, vuelva a intenar.")


def modificar_inventario():
    """
    Se encarga de administrar las modificaciones del inventario.
    """
    print("Modificación de inventario")
    producto = pedir_info_con_confirmacion("ingrese el nombre del producto: ")
    if not verificar_existencia_del_producto(producto):
        return None
    cantidad = pedir_nro(
        "Ingrese la cantidad(numero negativo restara): ", permitir_negativo=True
    )
    if (PRODUCTOS[producto] + cantidad) < 0:
        print("No hay suficiente stock")
    else:
        PRODUCTOS[producto] = PRODUCTOS[producto] + cantidad
        print(f"El nuevo stock de {producto.capitalize()} es: {PRODUCTOS[producto]}")
    print()
    return None


def eliminar_producto():
    """
    Pide un producto y si existe lo elimina del inventario.
    """
    print("Elminiar producto")
    producto = pedir_info_con_confirmacion("ingrese el nombre del producto: ")
    if not verificar_existencia_del_producto(producto):
        return None
    print(f"El producto {PRODUCTOS.pop(producto).capitalize()} fue eliminado")
    print()
    return None


def ver_producto():
    """
    Busca y si encuentra el producto muestra su informacion.
    """
    print("Ver inventario")
    producto = input("ingrese el nombre del producto: ")
    if not verificar_existencia_del_producto(producto):
        return None
    print(f"La cantidad de {producto.capitalize()} es: {PRODUCTOS[producto]}")
    print()
    return None


def agregar_producto():
    """
    Se encarga de pedir y agregar un nuevo producto al inventario.
    Si existe no agrega nada.
    """
    print("Agregar producto")
    producto = pedir_info_con_confirmacion("ingrese el nombre del producto: ")
    if verificar_existencia_del_producto(producto, mostrar_msj=False):
        print("Producto ya existente.")
        return None
    cantidad = pedir_nro("Ingrese la cantidad del producto: ")
    PRODUCTOS[producto.lower()] = int(cantidad)
    print()
    return None


def main():
    """
    Fucion principal que maneja el inventario.
    """
    cargar_inventario()
    while True:
        mostrar_menu()
        opcion = pedir_numero_acotado("Elija una opcion del Menu: ", 0, len(MENU))
        print()
        if opcion == 1:
            listar_productos()
        elif opcion == 2:
            modificar_inventario()
        elif opcion == 3:
            eliminar_producto()
        elif opcion == 4:
            ver_producto()
        elif opcion == 5:
            agregar_producto()
        elif opcion == 6:
            print("Hasta pronto")
            guardar_inventario()
            break


if __name__ == "__main__":
    main()
