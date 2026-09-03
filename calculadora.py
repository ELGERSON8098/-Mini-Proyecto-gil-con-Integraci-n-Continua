"""Operaciones aritmeticas basicas para una calculadora sencilla."""


def sumar(primer_numero: float, segundo_numero: float) -> float:
    """Devuelve la suma de dos numeros."""
    return primer_numero + segundo_numero


def restar(primer_numero: float, segundo_numero: float) -> float:
    """Devuelve la resta de dos numeros."""
    return primer_numero - segundo_numero


def multiplicar(primer_numero: float, segundo_numero: float) -> float:
    """Devuelve el producto de dos numeros."""
    return primer_numero * segundo_numero


def dividir(dividendo: float, divisor: float) -> float:
    """Devuelve el cociente y evita la division entre cero."""
    if divisor == 0:
        raise ValueError("No se puede dividir entre cero.")
    return dividendo / divisor