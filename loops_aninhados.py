
linha = int(input("Digite quantidade de linha"))
coluna = int(input("Digite quantidade de coluna"))
caractere = input("Digite o caractere")

for i in range(linha):
    for j in range(coluna):
        print(caractere, end="")
    print()