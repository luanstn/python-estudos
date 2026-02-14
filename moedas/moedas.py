def metade(valor, formato=False):
    metades = valor / 2
    return metades if formato == False else moeda(metades)


def dobro(valor, formato=False):
    dobros = valor * 2

    return dobros if formato == False else moeda(dobros)


def aumentar(valor, aumento =0, formato=False):
    aumento = valor + (valor * aumento / 100)
    return aumento if formato == False else moeda(aumento)


def diminui(valor, desconto=0, formato=False):
    diminuir = valor - (valor * desconto / 100)

    return diminuir if formato == False else moeda(diminuir)

def moeda(valor):
    return f"R$ {valor:.2f}"

def resumo(valor, aumento, desconto):
    print("-"*20)
    print("RESUMO DO VALOR")
    print("-"*20)

    print(f"Preço analisado:    {moeda(valor)}")
    print(f"Dobro analisado:    {dobro(valor, True)}")
    print(f"metade do preço:    {metade(valor, True)}")
    print(f"{aumento}% de aumento:  {aumentar(valor, aumento, True)}")
    print(f"{desconto}$ de redução: {diminui(valor, desconto, True)}")

