import pytest
from calculadora import Calculadora

def test_dividir():
    # a e b positivos
    assert Calculadora.dividir(10, 2) == 5
    # a e b negativos
    assert Calculadora.dividir(-10, -2) == 5
    # a negativo e b positivo
    assert Calculadora.dividir(-10, 2) == -5
    # a positivo e b negativo
    assert Calculadora.dividir(10, -2) == -5
    # a e b decimais
    assert Calculadora.dividir(7.5, 2.5) == 3.0
    # a ou b sendo zero
    assert Calculadora.dividir(0, 3) == 0
    with pytest.raises(ValueError, match="Divisão por zero não é permitida"):
        Calculadora.dividir(3, 0)

