from loja import entrada
from loja import financeiro
from loja import produtos

lista_produtos = list()
carrinho = list()

lista = produtos.cadastrar_produtos(lista_produtos)

while True:
    print("LISTA DE PRODUTOS")
    produtos.listar_produtos(lista)

    while True:
        try:
            indice = int(input("Digite o numero do produto: "))
            indice_real = indice - 1
            produto_escolhido = lista[indice_real]
            carrinho.append(produto_escolhido)
            break
        except ValueError:
            print("Digite um numero inteiro")
        except IndexError:
            print("Digite um numero inteiro")

    confirmar = input("Deseja continuar? [s/n] ").upper()
    if confirmar == "N":
        break

calcula_carrinho = financeiro.total_compra(carrinho)

while True:
    try:
        forma = int(input("forma de pagamento [1 - A vista |2 - Cartão]:  "))

        if forma not in (1, 2):
            raise ValueError("Forma de pagamento invalida")
        break
    except ValueError:
        print("Digite apenas 1 ou 2")

if forma == 1:
    total = financeiro.calcular_desconto(calcula_carrinho, 10)
    print(f"Total de compras = {total}")
elif forma == 2:
    total = financeiro.calcular_aumento(calcula_carrinho, 10)
    print(f"Aumento de compra = {total}")
