def livros_antigos(a):
    velho = a[0]
    for c in a:
        atual = c
        if atual['ano'] < velho['ano']:
            velho = c
    return velho

def quantidade_livros(lista):
    quantidade = len(lista)
    return quantidade

def anteriores_2000(lista):
    anterior = list()
    for c in lista:
        if c['ano'] < 2000:
            anterior.append(c)
    return anterior