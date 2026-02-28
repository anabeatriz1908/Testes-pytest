from operacoes import *
import pytest

##################################
# TESTE SOMA
##################################
def test_somar_inteiros():
    assert somar(2, 3) == 5
    
def test_somar_float():
    assert somar(2.1, 1.2) == pytest.approx(3.3)

##################################
# TESTE SUBTRAIR
##################################
def test_subtrair():
    assert subtrair(10, 1) == 9

def test_subtrair_float():
    assert subtrair(4.6, 2.5) == pytest.approx(2,1)

##################################
# TESTE MULTIPLICAR
##################################
def test_multiplicar_int():
    assert multiplicar(10, 3) == 30

def test_multiplicar_float():
    assert multiplicar(6.4, 5.7) == pytest.approx(36.48)

##################################
# TESTE DIVIDIR
##################################
def test_dividir_int():
    assert dividir(6, 2) == 3

def test_dividir_float():
    assert dividir(5, 2) == pytest.approx(2.5)

def test_dividir_zero():
    with pytest.raises(ValueError):
        dividir(1,0)

##################################
# TESTE RAIZ QUADRADA
##################################
def test_raiz_quadrada_numero_negativo():
    with pytest.raises(ValueError):
        raiz_quadrada(-4)
    
def test_raiz_quadrada_valores_inteiros():
    assert raiz_quadrada(4) == 2

def test_raiz_quadrada_valores_float():
    assert raiz_quadrada(7.5) == pytest.approx(2.7386127875258306)

##################################
# TESTE MÉDIA
##################################
def test_calcular_media_inteiros():
    assert calcular_media([2, 4, 6]) == 4

def test_calcular_media_floats():
    assert calcular_media([0.1, 0.2, 0.3]) == pytest.approx(0.2)
    
def test_calcular_media_lista_vazia():
    with pytest.raises(ValueError):
        calcular_media([])

##################################
# NUMEROS POSITIVOS E NEGATIVOS
##################################
def test_numero_eh_positivo():
    assert numero_eh_positivo_ou_eh_negativo(10) is True

def test_numero_eh_negativo():
    assert numero_eh_positivo_ou_eh_negativo(-5) is False


