import pytest
from calculadora import Calculadora

def test_fatorial():
    # a positivo
    assert Calculadora.fatorial(5) == 120
    # a zero
    assert Calculadora.fatorial(0) == 1
    # a negativo
    with pytest.raises(ValueError, match="Fatorial de número negativo não é permitido"):
        Calculadora.fatorial(-5)
