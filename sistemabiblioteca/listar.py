def listar_livros(lista):
    contador = 0
    print("LISTA DE LIVROS")
    for livro in lista:
        contador += 1
        print(f"{contador} - nome: {livro['nome']} , autor: {livro['autor']}, ano: {livro['ano']}")