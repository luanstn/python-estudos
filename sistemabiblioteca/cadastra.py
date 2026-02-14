def ler_int(a):
    while True:
        corrige = input(a)
        try:
            corrige = int(corrige)
            return corrige
        except ValueError:
            print("O valor está incorreto.")


def cadastrar_livro(livro):
    while True:
        dados = dict()
        dados['nome'] = input("nome do livro para cadastrar: ")
        dados['autor'] = input("autor do livro: ")
        dados['ano'] = ler_int("ano do livro: ")
        livro.append(dados)

        continuar = input("continuar? [s/n] ").upper()
        if continuar == "N":
            break

    return livro
