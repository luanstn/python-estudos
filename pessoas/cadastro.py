pessoa = list()


def cadastrar(msg):
    while True:
        dados = dict()
        dados["nome"] = str(input("Nome: "))
        dados["idade"] = int(input("idade: "))
        pessoa.append(dados)

        continuar = input("Deseja continuar? [S/N] ").upper()
        if continuar == "N":
            break

    return pessoa
