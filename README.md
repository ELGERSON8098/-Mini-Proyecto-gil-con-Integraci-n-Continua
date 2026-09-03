# Calculadora basica

Programa en Python con operaciones de suma, resta, multiplicacion y division.

## Uso

```python
from calculadora import dividir, sumar

print(sumar(8, 2))
print(dividir(8, 2))
```

## Practicas de calidad aplicadas

1. **Coding standards:** se configuro `ruff` como linter y formateador en `pyproject.toml`. Se ejecuta con `ruff check .` y `ruff format --check .`. Esta practica detecta problemas de estilo, importaciones sin usar y errores simples antes de integrar codigo.
2. **Pruebas automatizadas:** se incluyeron pruebas con `pytest`, incluso para impedir la division entre cero. Se ejecutan con `pytest` y evitan que una modificacion rompa funciones ya realizadas.
3. **Pull Request y Code Review:** se debe crear una rama, publicar el proyecto, abrir un PR hacia `main` y dejar un comentario de auto-revision antes de fusionarlo. La revision detecta errores y decisiones incompletas temprano.

Estas practicas se relacionan con lo discutido en clase porque integran y verifican cambios pequenos de manera continua. Asi se evita el enfoque de "Big Bang", en el que todos los cambios se unen al final y los errores producen mas retrabajo.

## Comandos de verificacion

```bash
ruff check .
ruff format --check .
pytest
```