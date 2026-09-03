# Calculadora básica

Programa en Python que permite realizar las operaciones básicas de suma, resta, multiplicación y división.

## Uso

```python
from calculadora import dividir, sumar

print(sumar(8, 2))
print(dividir(8, 2))
```

## Prácticas de calidad aplicadas

1. **Coding standards:** configuré `ruff` como linter y formateador en `pyproject.toml`, el cual se ejecuta con `ruff check .` y `ruff format --check .`. Esta práctica me ayuda a detectar problemas de estilo, importaciones sin usar y errores sencillos antes de integrar el código.
2. **Pruebas automatizadas:** incluí pruebas con `pytest`, entre ellas una para evitar la división entre cero. Estas se ejecutan con `pytest` y me permiten asegurarme de que una modificación no rompa funciones que ya estaban funcionando.
3. **Pull Request y Code Review:** antes de fusionar el proyecto, creé una rama, publiqué los cambios, abrí un PR hacia `main` y dejé un comentario de auto-revisión. Esto ayuda a detectar errores y decisiones incompletas desde una etapa temprana.

Estas prácticas se relacionan con lo visto en clase porque permiten integrar y verificar cambios pequeños de forma continua, evitando el enfoque de "Big Bang", donde todos los cambios se unen al final y los errores terminan generando más retrabajo.

## Comandos de verificación

```bash
ruff check .
ruff format --check .
pytest
```