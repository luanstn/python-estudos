from sistemaescola import cadastrar
from sistemaescola import relatorio
from sistemaescola import estatistica

listaalunos = list()

while True:
    print("SISTEMA DE CADASTRO E RELATÓRIO DOS ALUNOS")
    print("1 - cadastrar aluno")
    print("2 - relatorio dos alunos")
    print("3 - estatísticas dos alunos")
    print("4 - sair")

    ler = int(input("escolha uma opção: "))

    if ler == 1:
        cadastrar.cadastrar(listaalunos)
    elif ler == 2:
        relatorio.relatorio(listaalunos)
    elif ler == 3:
        while True:
            print("1 - aluno com maior média")
            print("2 - aluno com menor média")
            print("3 - quantidade de alunos aprovados")
            print("4 - buscar aluno")
            print("5 - sair")

            opcao = int(input("escolha: "))

            if opcao == 1:
                if len(listaalunos) == 0:
                    print("nenhum aluno cadastrado")
                else:
                    melhor_aluno = estatistica.melhor_media(listaalunos)
                    print(f"o aluno com melhor média é {melhor_aluno['nome']}, com {melhor_aluno['media']}")
            elif opcao == 2:
                if len(listaalunos) == 0:
                    print("nenhum aluno cadastrado")
                else:
                    pior_aluno = estatistica.pior_media(listaalunos)
                    print(f"o aluno com pior média é {pior_aluno['nome']}, com {pior_aluno['media']}")
            elif opcao == 3:
                if len(listaalunos) == 0:
                    print("nenhum aluno cadastrado")
                else:
                    aprovados = estatistica.quant_aprovados(listaalunos)
                    print(f"tinha um total de {len(listaalunos)} alunos, e foram aprovados: {aprovados}")
            elif opcao == 4:
                nome = input("digite o nome: ").strip()
                busca = estatistica.buscar_aluno(listaalunos, nome)
                if busca:
                    print("O aluno foi encontrado!")
                    print(f"nome : {busca['nome']}")
                    print(f"nota : {busca['nota1']}")
                    print(f"nota 2 : {busca['nota2']}")
                    print(f"média : {busca['media']}")
                else:
                    print("o aluno não foi encontrado")
            elif opcao == 5:
                break
    elif ler == 4:
        print("saindo...")
        break