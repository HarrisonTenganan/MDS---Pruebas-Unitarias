## Harrison Tenganan Colorado
## Archivo de pruebas unitarias

import pytest

from main import sumar, restar, multiplicar, dividir

# Pruebas por cada operación

def test_sumar():
    assert sumar(5, 2) == 7
    assert sumar(-2, -2) == -4

def test_restar():
    assert restar(10, 3) == 7
    assert restar(-4, 3) == -7

def test_multiplicar():
    assert multiplicar(2, 4) == 8
    assert multiplicar(3, -4) == -12

def test_dividir():
    assert dividir(18, 2) == 9
    assert dividir(-10, -2) == 5
    with pytest.raises(ValueError):
        dividir(5, 0)
