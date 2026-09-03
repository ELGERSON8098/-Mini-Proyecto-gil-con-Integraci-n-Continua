import pytest

from calculadora import dividir, multiplicar, restar, sumar


def test_suma() -> None:
    assert sumar(8, 2) == 10


def test_resta() -> None:
    assert restar(8, 2) == 6


def test_multiplicacion() -> None:
    assert multiplicar(8, 2) == 16


def test_division() -> None:
    assert dividir(8, 2) == 4


def test_division_entre_cero() -> None:
    with pytest.raises(ValueError, match="No se puede dividir entre cero"):
        dividir(8, 0)