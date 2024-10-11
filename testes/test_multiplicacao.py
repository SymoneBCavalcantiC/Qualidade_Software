import pytest
from calculadora import Calculadora

def test_multiplicar():
    # a e b positivos
    assert Calculadora.multiplicar(4, 3) == 12
    # a e b negativos
    assert Calculadora.multiplicar(-4, -3) == 12
    # a negativo e b positivo
    assert Calculadora.multiplicar(-4, 3) == -12
    # a positivo e b negativo
    assert Calculadora.multiplicar(4, -3) == -12
    # a e b decimais
    assert Calculadora.multiplicar(2.5, 4) == 10.0
    # a ou b sendo zero
    assert Calculadora.multiplicar(4, 0) == 0
    assert Calculadora.multiplicar(0, 3) == 0

