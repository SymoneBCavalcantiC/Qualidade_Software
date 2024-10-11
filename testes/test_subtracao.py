import pytest
from Calculadora import Calculadora

def test_subtrair():
    # a e b positivos
    assert Calculadora.subtrair(5, 3) == 2
    # a e b negativos
    assert Calculadora.subtrair(-5, -3) == -2
    # a negativo e b positivo
    assert Calculadora.subtrair(-5, 3) == -8
    # a positivo e b negativo
    assert Calculadora.subtrair(5, -3) == 8
    # a e b decimais
    assert Calculadora.subtrair(5.5, 3.5) == 2.0
    # a ou b sendo zero
    assert Calculadora.subtrair(5, 0) == 5
    assert Calculadora.subtrair(0, 3) == -3

