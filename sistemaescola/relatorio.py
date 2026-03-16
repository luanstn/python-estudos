def relatorio(lista):
    contador = 0
    for aluno in lista:
        contador = contador + 1
        print(f"{contador} - aluno : {aluno['nome']}; notas : {aluno['nota1']}, {aluno['nota2']}; media : {aluno['media']}")
