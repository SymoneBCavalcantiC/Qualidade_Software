import pytest
from calculadora import Calculadora

def test_potencia():
    # a e b positivos
    assert Calculadora.potencia(2, 3) == 8
    # a e b negativos
    assert Calculadora.potencia(-2, -3) == -0.125
    # a negativo e b positivo
    assert Calculadora.potencia(-2, 3) == -8
    # a positivo e b negativo
    assert Calculadora.potencia(2, -3) == 0.125
    # a e b decimais
    assert Calculadora.potencia(2.5, 2) == 6.25
    # a ou b sendo zero
    assert Calculadora.potencia(0, 3) == 0
    assert Calculadora.potencia(3, 0) == 1

