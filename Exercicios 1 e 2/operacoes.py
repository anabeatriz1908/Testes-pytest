import math

def somar(a,b):
    resultado = a + b
    return resultado

def subtrair(a, b):
    resultado = a -b
    return resultado

def multiplicar(a, b):
    resultado = a * b
    return resultado

def dividir(a, b):
    if b == 0:
        raise ValueError("Erro! Não é possível realizar divisão por zero")
    else:
        resultado = a/b
        return resultado

def raiz_quadrada(numero):
    if numero < 0:
        raise ValueError("Erro! Números negativos não possuem raiz quadrada")
    else:
        resultado = math.sqrt(numero)
        return resultado

def calcular_media(lista_numeros):
    count = len(lista_numeros)

    if count <= 0:
        raise ValueError("Lista vazia")
    else:
        resultado = sum(lista_numeros) / count
        return resultado

def numero_eh_positivo_ou_eh_negativo(numero):
    if numero >= 0:
        return True
    else:
        return False

