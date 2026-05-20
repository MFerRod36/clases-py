# Validar un usuario:
def validate_user(user):
    if "password" not in user:
        return "Error: El usuario debe tener una contraseña"
    if len(user["password"]) < 8:
        return "Error: La contraseña debe tener al menos 8 caracteres"
    return "Usuario válido"


# Ejemplo de uso:
persona_pepe = {
    "name": "Pepe",
    "password": "12345678",
    "email": "pepe@example.com",
}

print(validate_user(persona_pepe))


# Pasar parámetros posicionales::
anio_actual = 2026


def calcular_edad(anio_nacimiento):
    return anio_actual - anio_nacimiento


print(calcular_edad(1990))


# Pasar parámetros por palabra clave:
def calcular_edad_kw(anio_nacimiento, anio_actual=2026):
    return anio_actual - anio_nacimiento


print(calcular_edad_kw(anio_nacimiento=1990))


# Pasar parámetros por valor por defecto:
# La diferencia entre valor por defecto y palabra clave está en cómo se llaman los parámetros al momento de invocar la función.
def calcular_edad_default(anio_nacimiento, anio_actual=2026):
    return anio_actual - anio_nacimiento


print(calcular_edad_default(1990))


# Una sola función puede tener parámetros posicionales, por palabra clave y por valor por defecto al mismo tiempo:
def calcular_edad_completa(anio_nacimiento, anio_actual=2026):
    return anio_actual - anio_nacimiento


calcular_edad_completa(1990)  # Parámetro posicional
calcular_edad_completa(anio_nacimiento=1990)  # Parámetro por palabra clave
calcular_edad_completa(1990, anio_actual=2026)  # Parámetro por valor por defecto
calcular_edad_completa(
    anio_nacimiento=1990, anio_actual=2026
)  # Parámetro por palabra clave y valor por defecto

# -----------------------------------------------------------------------------------------------------------------

# Alcance:
test = "Variable global"


def funcion_prueba():
    tuti = "Variable local"
    print(test)  # Accede a la variable global
    print(tuti)  # Accede a la variable local


funcion_prueba()

print(test)

# -----------------------------------------------------------------------------------------------------------------
