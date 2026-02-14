from loja import entrada

def cadastrar_produtos(a):
    while True:
        produtos = dict()
        produtos['nome'] = str(input("digite o nome do produto: "))
        produtos['preco'] = entrada.ler_dinheiro("digite o preco do produto: ")
        a.append(produtos)

        continuar = str(input("Deseja continuar? [S/N] ")).upper()

        if continuar == "N":
            break
    return a

def listar_produtos(a):
    contador = 0
    for c in a:
        contador += 1
        print(f"[{contador}] - nome: {c['nome']}   valor: {c['preco']}")

