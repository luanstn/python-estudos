def calcular_desconto(valor, porcentagem, formato=False):
    desconto = valor - (valor * porcentagem / 100)
    return desconto if formato == False else total_compra

def calcular_aumento(valor, porcentagem, formato=False):
    aumento = valor + (valor * porcentagem / 100)
    return aumento if formato == False else total_compra

def total_compra(carrinho):
    total = 0
    for c in carrinho:
        total = total + c['preco']
    return total

