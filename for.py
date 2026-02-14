'''
n = int(input())
for c in range(0, n):
    print(c)
print("fim")
'''

"""
i = int(input("início: "))
f = int(input("fim: "))
p = int(input("Passo: "))
for c in range(i, f+1, p):
    print(c)
print("fim")
"""
"""
s = 0
for c in range(0, 4):
    n = int(input("Digite um valor: "))
    s = s + n
print(f"o somatório de todos os valores foi: {s}")
"""
"""
fazer uma contagem regressiva de 10 até 0 com time de 1 segundos
import time

for c in range(10, 0-1, -1):
    time.sleep(1)
    print(c)
print(" estouro de fogos!!!"s)
"""
"""
pega todos os números pares de 0 até 50
for c in range (0, 50, 2):
    print(c)
"""
"""
ver a soma de todos os numeros divisiveis por 3 entre 1 e 500
n = 0
for c in range(0, 500, 3):
    n = n + c
print(f"A soma dos numeros impares que são divisiveis por 3 é: {n}")
"""
"""
faz a tabuada de 9 ou de qualquer um que você colocar

for c in range(0 ,10):
    valor = 9 * c
    print(f" {c} * 9 = {valor}")
"""
"""
num = int(input("Digite um valor da tabuada que você quer: "))

for c in range(0, 10):
    valor = num * c
    print(f" {num} * {c} = {valor}")
"""
"""
pede para colocar 6 números e soma só os pares
num = 0
for c in range(0, 7):
    veri = int(input("Digite um valor: "))
    if veri % 2 == 0:
        num = num + veri
print(f"a soma dos números pares que você colocou é: {num}")
"""

"""
verifica se é um palindromo
for c in range(0, 3):
    a = str(input("Digite algo: "))
    tiraes = a.replace(" ", "")
    ler = len(tiraes)
    inverter = tiraes[::-1]
    if a == inverter:
        print(f"{a} é um palindromo")
    else:
        print("Não é um palindromo")
print("FIM")

"""
"""
pede 7 datas de nascimentos e verifica se é maior de idade ou não

f = 0
n = 0
for c in range(0, 7):
    idade = int(input("Digite o ano do seu nascimento: "))
    verifica = 2025 - idade
    if verifica < 18:
        f = f + 1
    else:
        n = n + 1
print(f" {f} pessoas ainda não atingiram a maioridade")
print(f" {n} pessoas atingiram a maioridade")
"""

"""
ler peso de cinco pessoas e ver qual é o maior e o menor

for c in range(0, 5):
    peso = float(input("digite o seu peso: "))
    if c == 0:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print(f" o maior dos pesos foi {maior}, e o menor foi {menor}")

"""
"""
pede o nome, idade e sexo e diz qual homem mais velho, qual a média de idade do grupo e a mulher que tem idade abaixo de 20

n = 0

for c in range(0, 5):
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Digite seu sexo(M ou F): ").strip().upper())

    if c == 0:
        maior = idade
        nome2 = nome
        mulher = 0

    elif idade > maior and sexo == "M":
        nome2 = nome


    if idade < 20 and sexo == "F":
        mulher = mulher + 1

    n = n + idade


print(f"o nome do homem mais velho é: {nome2}")
print(f"a média de idade do grupo é {n/4}")
print(f"{mulher} mulheres tem menos de 20 anos")
"""
"""
programa que vai pedir inicio e final e vai contar de 5 em 5
inicio = int(input("Digite o inicio:"))
fim = int(input("Digite o fim: "))

for c in range(inicio, fim+5, 5):
    print(c)
"""
"""
fazer tabuada de o numero que voce colocar * 20
numero = int(input("Digite um número: "))

for c in range(0, 21):
    resultado = numero * c
    print(f"{numero} * {c} = {resultado}")
"""
"""
pede 5 notas e faz a media delas e diz qual foi a maior e a menor
cont = 0

for c in range(0, 5):
    nota1 = float(input("Digite a sua nota: "))

    if c == 0:
        maior = nota1
        menor = nota1

    elif nota1 > maior:
        maior = nota1
    elif nota1 < menor:
        menor = nota1

    cont = cont + nota1
media = cont / 5

print(f"A média das suas notas é {media:.2f}")
print(f"A maior nota foi: {maior:.2f}")
print(f"A menor nota foi: {menor:.2f}")
"""
""""
pede a frase e vai mostrar o total de letras, quantidade de frases, vezes que A aparece, primeira e ultima vez que 
o A aparece


palavra = str(input("Digite uma frase: "))
confrase = palavra.split()

for c in palavra:

    palavra = palavra.replace(" ",  "")
    contaletra = len(palavra)

    contfrase = len(confrase)

    qtd = palavra.count(c)

    ultima = palavra.rfind("a")
    primeira = palavra.find("a")


print(f" o total de letras é: {contaletra}")
print(f"a quantidade de frses é: {contfrase}")
print(f"a quantidade de vezes que a letra A aparece é {qtd}")
print(f"primeira vez que o A aparece é: {primeira}")
print(f"última vez que a letra Aparece é: {ultima}")

"""
"""

numero = str(input("Digite um número: "))

for c in range(0, 1):
    unidade = numero[0]
    dezena = numero[0:2]
    centena = numero[0:3]
    milhar = numero[0:4]

print(unidade)
print(dezena)
print(centena)
print(milhar)

"""
"""
Digamos que o número de chinchilas de uma fazenda triplica a cada
 ano, após o primeiro ano. Elaborar um programa que leia o número inicial
 de chinchilas e anos e informe ano a ano o número médio previsto de
 chinchilas da fazenda. O número inicial de chinchilas deve ser maior ou
 igual a 2 (um casal). A Figura 5.16 exibe a página com um exemplo de
 saída do programa

chinchilas = int(input("Diga quantas chinchilas tem: "))
anos = int(input("Diga quantas anos tem: "))

for c in range(0, anos):

    chinchilas = chinchilas * 3

    print(c+1, chinchilas)
"""
"""
pede o nome, idade e sexo e diz qual homem mais velho, qual a média de idade do grupo e a mulher que tem idade abaixo de 20

n = 0

for c in range (0, 4):
    nome = input("Digite o nome: ")
    idade = int(input("Digite a sua idade: "))
    sexo = str(input("Digite o sexo(F = feminino M = masculino): ")).upper()


    if c == 0:
        maior = idade
        nome2 = nome
        mulher = 0

    if idade > maior and sexo == "M":
        maior = idade
        nome2 = nome

    if sexo == "F" and idade < 20:
        mulher = mulher + 1

    n = n + idade

    media = n / 4

print(f"o homem mais velho do grupo é: {nome2}")
print(f"{mulher} mulheres tem menos de 20 anos")
print(f"a media de idade do grupo é: {media}")
"""
"""
programa que pede a quantidade de alunos e faz a media das notas e mostra a situação

quantidade = int(input("Digite a quantidade de alunos: "))

media = 0
lista = []


for c in range(0, quantidade):
    nome = input("Digite o nome: ")
    nota1 = float(input("Digite sua nota 1: "))
    nota2 = float(input("Digite sua nota 2: "))
    nota3 = float(input("Digite sua nota 3: "))

    if c == 0:
        nomes = nome

    media = (nota1 + nota2 + nota3) / 3

    if media >= 7:
       situacao = "Aprovado"
    elif media < 7:
       situacao = "Reprovado"

    print("------ Situação do aluno --------")
    print(f"aluno: {nome}")
    print(f"notas: {nota1 , nota2 , nota3}")
    print(f"média: {media} - {situacao}")

"""

