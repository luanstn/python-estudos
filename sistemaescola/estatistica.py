def melhor_media(lista):
    if len(lista) >= 1:
        melhor = lista[0]
        for aluno in lista:
            if aluno['media'] > melhor['media']:
                melhor = aluno
        return melhor
    else:
        print("não existe aluno registrado")


def pior_media(lista):
    if len(lista) >= 1:
        pior = lista[0]
        for aluno in lista:
            if aluno['media'] < pior['media']:
                pior = aluno
    else:
        print("não existe alunos registrados")

    return pior

def quant_aprovados(lista):
    aprovados = 0
    if len(lista) > 1:
        for aluno in lista:
            if aluno['media'] >= 7:
                aprovados = aprovados + 1
    else:
        print("não existe alunos registrados")
    return aprovados

def ler_float(lista):
    while True:
        entrada = input(lista).replace(",", ".").strip()
        try:
            valor = float(entrada)
            return valor
        except ValueError:
            print("Valor invalido")


def buscar_aluno(lista, nome):
    for c in lista:
        if c['nome'].lower() == nome.lower():
            return c
    else:
        return None