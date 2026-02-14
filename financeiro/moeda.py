def metade(a, formato=False):
    metades = a/2
    return metades if formato == False else traducao(metades)

def dobro(a, formato=False):
    dobros = a*2
    return dobros if formato == False else traducao(dobros)

def aumentar(a, porcentagem, formato=False):
    aumento = a + (a * porcentagem / 100)
    return aumento if formato == False else traducao(aumento)

def diminuir(a, porcentagem, formato=False):
    diminui = a - (a * porcentagem / 100)
    return diminui if formato == False else traducao(diminui)

def traducao(a):
    return f"R${a:.2f}"

def resumo(a, aumento, reducao):
    print('-'*30)
    print('RESUMO DO VALOR')
    print('-'*30)

    print(f"preço analisado: {traducao(a)}")
    print(f"Dobro analisado: {dobro(a, True)}")
    print(f"metade analisado: {metade(a, True)}")
    print(f"aumento de {aumento}%: {aumentar(a, aumento, True)}")
    print(f"diminui de {reducao}%: {diminuir(a, reducao, True)}")
    print("-"*30)
