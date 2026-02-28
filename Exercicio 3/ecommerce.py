

def calcular_preco_final(preco_base, cupom=None, frete_gratis=False):
    novo_preco = preco_base
    if preco_base <= 0:
        raise ValueError("Produto com preço inválido.")

    if cupom != None and "promo" in cupom.lower():
        desconto = "".join([char for char in cupom if char.isdigit()])
        if not desconto:
            raise ValueError("Cupom Inválido.")
        
        else:
            novo_preco -= preco_base * (int(desconto) / 100)
    
    if frete_gratis == True or novo_preco>500:
        return novo_preco
    else:
        novo_preco += 20.00
        return novo_preco
        
