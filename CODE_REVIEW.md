# Auto-revision del Pull Request

## Cambio revisado

Se agrego una calculadora basica, pruebas automatizadas y configuracion de `ruff`.

## Comentario de revision

**Aprobado con observacion:** la funcion `dividir` valida correctamente el divisor igual a cero y cuenta con una prueba para ese caso. Antes de fusionar, se deben ejecutar `ruff check .`, `ruff format --check .` y `pytest` en un equipo con Python instalado.

## Resultado

El cambio queda aprobado cuando las tres verificaciones finalicen sin errores.