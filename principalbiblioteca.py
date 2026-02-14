from sistemabiblioteca import cadastra
from sistemabiblioteca import listar
from sistemabiblioteca import estatistica

lista = list()

def menu(lista):
    while True:
        print("1 - cadastrar livros")
        print("2 - listar todos os livros")
        print("3 - Mostrar as estatísticas")
        print("4 - sair")

        ler = cadastra.ler_int("escolha uma opção")

        if ler == 1:
            cadastra.cadastrar_livro(lista)
            print(f"cadastrado com sucesso!")
        elif ler == 2:
            organizando = listar.listar_livros(lista)
        elif ler == 3:
            while True:
                print("1 - livro mais antigo")
                print("2 - quantidade de livros")
                print("3 - livros anteriores a 2000")
                print("4 - sair")
                escolha = cadastra.ler_int("escolha uma opção: ")

                if escolha == 1:
                    maisantigo = estatistica.livros_antigos(lista)
                    print(f"O livro mais antigo é: {maisantigo['nome']}, ele foi criado em {maisantigo['ano']}")
                elif escolha == 2:
                    quantidade = estatistica.quantidade_livros(lista)
                    print(f"quantidade total de livros é: {quantidade}")
                elif escolha == 3:
                    anteriores = estatistica.anteriores_2000(lista)
                    print(f"os livros que são anteriores a 2000:")
                    for c in anteriores:
                        print(f"{c['nome']} - {c['ano']}")
                elif escolha == 4:
                    break
        elif ler == 4:
            break

menu(lista)