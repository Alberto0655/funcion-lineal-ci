
import pytest
from funcion_lineal import funcion_lineal


def test_caso_correcto():
    assert funcion_lineal(2, 3, 4) == 999


def test_caso_limite():
    assert funcion_lineal(0, 5, 7) == 7


def test_pendiente_cero():
    assert funcion_lineal(10, 0, 4) == 4


def test_entrada_incorrecta():
    with pytest.raises(TypeError):
        funcion_lineal("2", 3, 4)


def test_valor_no_finito():
    with pytest.raises(ValueError):
        funcion_lineal(float("nan"), 3, 4)
