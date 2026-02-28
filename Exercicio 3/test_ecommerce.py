import pytest
from ecommerce import calcular_preco_final

##################################
# Sem cupom
##################################
def test_preco_sem_cupom_com_frete():
    resultado = calcular_preco_final(100, None, False)
    assert resultado == 120

def test_preco_sem_cupom_frete_gratis():
    resultado = calcular_preco_final(100, None, frete_gratis=True)
    assert resultado == 100

def test_preco_sem_cupom_frete_gratis_acima_500():
    resultado = calcular_preco_final(600)
    assert resultado == 600

##################################
# Casos com cupom
##################################
def test_preco_com_cupom_10():
    resultado = calcular_preco_final(200, cupom="PROMO10", frete_gratis=False)
    assert resultado == pytest.approx(200)

def test_preco_com_cupom_20():
    resultado = calcular_preco_final(300, cupom="PROMO20", frete_gratis=False)
    assert resultado == pytest.approx(260)

def test_preco_com_cupom_e_frete_gratis():
    resultado = calcular_preco_final(200, cupom="PROMO10", frete_gratis=True)
    assert resultado == pytest.approx(180)

def test_preco_com_cupom_e_frete_gratis_por_valor():
    resultado = calcular_preco_final(600, cupom="PROMO10")
    assert resultado == pytest.approx(540)

def test_cupom_valido():
    resultado = calcular_preco_final(100, cupom="PROMO10")
    assert resultado == 110.0

##################################
# Cupom inválido
##################################
def test_cupom_invalido():
    resultado = calcular_preco_final(100, cupom="ABC123")
    assert resultado == 120

def test_cupom_invalido_sem_numero():
    with pytest.raises(ValueError):
        calcular_preco_final(100, cupom="PROMO")

def test_cupom_sem_promo_nao_aplica_desconto():
    resultado = calcular_preco_final(100, cupom="DESCONTO10")
    assert resultado == 120.0

##################################
# Preço inválido
##################################d
def test_preco_zero():
    with pytest.raises(ValueError):
        calcular_preco_final(0)

def test_preco_negativo():
    with pytest.raises(ValueError):
        calcular_preco_final(-50)

##################################
# FRETE
##################################
def test_frete_gratis_true():
    resultado = calcular_preco_final(100, frete_gratis=True)
    assert resultado == 100.0

def test_valor_menor_500_com_frete():
    resultado = calcular_preco_final(200)
    assert resultado == 220.0

def test_valor_acima_500_sem_frete():
    resultado = calcular_preco_final(600)
    assert resultado == 600.0



