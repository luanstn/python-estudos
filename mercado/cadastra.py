produtos = list()

def ler_dinheiro(valor):
    while True:
        entrada = input(valor).replace(",", ".").strip()
        try:
            valor = float(entrada)
            return valor
        except ValueError:
            print("digite um valor válido")

def cadastrar_produto(a):
    while True:
        dados = dict()
        dados['nome'] = input("Digite o nome do produto: ")
        dados['preco'] = ler_dinheiro("Digite o preco do produto: ")
        dados['estoque'] = int(input("Digite o estoque do produto: "))

        a.append(dados)

        continuar = input("Deseja continuar? [S/N]").upper()
        if continuar == "N":
            break

def mostrar_estoque(estoque):
    total = 0
    for produto in produtos:
        total = total + produto['estoque']
    return "o estoque total é: ", total

def maior_valor(mercadorias):
    if not mercadorias:
        print("Nenhum produto foi encontrado")
    else:
        valor_inicio =  mercadorias[0]['estoque'] * mercadorias[0]['preco']
        maior = valor_inicio
        maior_produto = mercadorias[0]
        for c in mercadorias:
            atual = c['preco'] * c['estoque']
            if atual > maior:
                maior = atual
                maior_produto = c

        print(maior)
        print(maior_produto)

def ler_int(valor):
    while True:
        valor = input(valor)
        try:
            valor = int(valor)
            return valor
        except ValueError:
            print("número invalido")

def atualizar_produto(mercadorias):
    contador = 0
    for c in mercadorias:
        contador = contador + 1
        print(f"{contador} - {c['nome']}, {c['preco']}, {c['estoque']}")
    atualizar = input("Deseja atualizar o valor? [S/N]").upper()
    if atualizar == "N":
        print("okey")
    else:
        valor = ler_int("qual você quer atualizar?")
        indice = valor - 1
        mercadorias[indice]['preco'] = ler_int("Digite o novo preco do produto: ")

def menu(a):
    while True:
        print("1 - cadastrar produtos")
        print("2 - mostrar estoque")
        print("3 - mostrar estoque com maior valor")
        print("4 - atualizar produto")
        print("5 - sair")

        ler = ler_int("selecione uma opção: ")

        if ler == 1:
            cadastrar_produto(produtos)
        elif ler == 2:
            print(mostrar_estoque(produtos))
        elif ler == 3:
            maior_valor(produtos)
        elif ler == 4:
            atualizar_produto(produtos)
        elif ler == 5:
            break

menu(produtos)