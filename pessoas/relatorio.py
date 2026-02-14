from pessoas.cadastro import pessoa

def total():
    return len(pessoa)

def media():
    total = 0
    for c in pessoa:
        total = total + c["idade"]
    return total / len(pessoa)

def velho():
    maisvelho = pessoa[0]

    for c in pessoa:
        if c["idade"] > maisvelho["idade"]:
            maisvelho = c

    return maisvelho["nome"]

def novo():
    maisnovo = pessoa[0]

    for c in pessoa:
        if c["idade"] < maisnovo["idade"]:
            maisnovo = c

    return maisnovo["nome"]