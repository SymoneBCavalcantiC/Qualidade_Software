import pytest
from Calculadora import Calculadora

def test_adicionar():
    # a e b positivos
    assert Calculadora.adicionar(2, 3) == 5
    # a e b negativos
    assert Calculadora.adicionar(-2, -3) == -5
    # a negativo e b positivo
    assert Calculadora.adicionar(-2, 3) == 1
    # a positivo e b negativo
    assert Calculadora.adicionar(2, -3) == -1
    # a e b decimais
    assert Calculadora.adicionar(2.5, 3.5) == 6.0
    # a ou b sendo zero
    assert Calculadora.adicionar(2, 0) == 2
    assert Calculadora.adicionar(0, 3) == 3

