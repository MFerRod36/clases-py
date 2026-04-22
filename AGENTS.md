# Code Review Rules — Python

## Naming Conventions (PEP 8)

- snake_case para variables, funciones y módulos
- PascalCase para clases
- UPPER_SNAKE_CASE para constantes
- Prefijo \_ para atributos/métodos privados
- Nombres descriptivos — sin variables de una letra salvo en loops simples

## Código

- Indentación: 4 espacios, nunca tabs
- Máximo 79 caracteres por línea
- 2 líneas en blanco entre funciones y clases
- 1 línea en blanco entre métodos dentro de una clase
- f-strings para formateo de strings (no % ni .format())
- Comparar con None usando `is` / `is not`, nunca `==`
- Sin variables globales salvo constantes
- Sin código duplicado — si se repite 2 veces, extraer función

## Imports

- Un import por línea
- Orden: stdlib → third-party → local
- Sin `import *`

## Documentación

- Docstring en toda función pública con: propósito, args y return
- Comentarios solo cuando el código no es autoexplicativo

## Testing

- Framework: pytest
- Archivos de test: `test_*.py`
- Cada función pública debe tener al menos un test

## Git

- Conventional commits: feat|fix|docs|refactor|test(scope): descripción
- Nunca mencionar Claude ni IA en commits
- Un commit por cambio lógico
