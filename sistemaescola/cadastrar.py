from sistemaescola import estatistica

def cadastrar(lista):
    while True:
        dados = dict()
        dados['nome'] = input("nome: ")
        dados['nota1'] = estatistica.ler_float("primeira nota: ")
        dados['nota2'] = estatistica.ler_float("segunda nota: ")

        media = (dados['nota1'] + dados['nota2']) / 2
        dados['media'] = media

        lista.append(dados)

        continuar = input("Deseja continuar? [s/n] ").upper()
        if continuar == "N":
            break
