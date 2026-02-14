"""
numeros = int(input("Digite um número: "))

if numeros % 2 == 0:
    print(f"{numeros} é par")
else:
    print(f"{numeros} é impar")
"""
"""
num = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))

print(f"a soma deles é {num + num2}")
print(f"a subtração deles é {num - num2}")
print(f"a multiplicação deles é {num * num2}")
print(f"a divisão deles é {num / num2}")
"""
"""
nome = input("Digite seu nome: ")

maiuscula = nome.upper()
minuscula = nome.lower()

tiraespaco = nome.replace(" ", "")
contaletra = len(tiraespaco)

print(maiuscula)
print(minuscula)
print(contaletra)
"""
"""
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("voce é maior de idade")
else:
    print("você é menor de idade")
"""
"""
c = 1
adicao = 0
cont = 0

while c != 0:
    numero = int(input("Digite um numero: "))

    adicao = adicao + numero
    cont = cont + 1

    escolha = int(input("Digite 1 para adicionar mais numeros e 0 para pausar: "))

    if escolha == 0:
        c = c - 1

print(f" o total da adição dos números foi : {adicao}")
print(f"foram feitas {cont} adições")
"""
"""
import random

sorteio = random.randint(1, 10)
adivinha = int(input(f"tente adivinhar o número: "))

if adivinha != sorteio:
    print(f"você errou! o número sorteado foi {sorteio}")
else:
    print("você acertou!")
"""
"""
lista = list()

for c in range(0, 5):
    numeros = int(input("Digite 5 numeros: "))
    lista.append(numeros)

maior = lista[0]
menor = lista[0]

for numeros in lista:
    if numeros > maior:
        maior = numeros
    if numeros < menor:
        menor = numeros

print(lista)
print(maior, menor)
"""
"""
Crie uma função mensagem() que:
não receba parâmetros
imprima: "Bem-vindo ao mundo Python!"

def mensagem():
    print("Bem vindo ao mundo python!")

mensagem()
"""
"""

def soma(a, b):
    soma = (a + b)
    print(soma)

soma(88, 22)
"""
"""
Crie uma função area(largura, comprimento=1) que:
calcule a área
se o comprimento não for passado, use 1

def calcula(largura, altura= 1):
    calc = largura * altura
    print(calc)

calcula(5, )
"""
"""
aqui vai aceitar o tanto de parametros que voce quiser

def contador(*num):
    contador = 0
    print(num)

contador(2, 1, 7)
"""
"""
Crie uma lista com 5 números inteiros.
mostre:
o maior
o menor
a média

lista = list()
maior = 0
menor = 0
cont = 0

for c in range(0, 5):
    numeros = int(input("Digite um numero: "))
    lista.append(numeros)
    cont = cont + numeros
    media = cont / 5

    if c == 0:
        maior = numeros
        menor = numeros

    if numeros > maior:
        maior = numeros
    if numeros < menor:
        menor = numeros


print(f"a lista foi: {lista}")
print(f"o maior número foi: {maior}")
print(f"O menor número foi: {menor}")
print(f" A media foi: {media}")

"""
"""
lista = list()

for c in range(0, 5):
    dados = int(input("Digite um numero: "))
    lista.append(dados)

print(lista)
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)
"""
"""
dada a lista:

numeros = [2, 7, 4, 9, 10, 15, 8]


Crie uma nova lista só com os números pares.

numeros = [2, 7, 4, 9, 10, 15, 8]
pares = list()

for c in numeros:
    if c % 2 == 0:
        pares.append(c)

print(pares)
print(numeros)
"""
"""
nomes = ["Luan", "rafael", "Raylson", "micla"]


print("Primeiro nome: ", nomes[0])
print("ultimo nome: ", nomes[-1])
"""
"""
upla com números Dada a tupla: valores = (3, 5, 7, 9, 11, 13) Mostre:quantos números existem a soma
se o número 7 está na tupla

valores = (3, 5, 7, 9, 11, 13)
soma = 0
for c in valores:
    soma = soma + c

print(soma)
print(len(valores))

if 7 in valores:
    print("o 7 está nos valores")
else:
    print("o else não está nos valores")
"""

"""
alunos = list()

while True:

    aluno = dict()
    aluno["nome"] = str(input("Nome: "))
    aluno["idade"] = int(input("Idade: "))
    aluno["nota"] = float(input("Nota: "))
    alunos.append(aluno)

    continuar = input("Continuar? [S/N] ").upper()
    if continuar == "N":
        break
print(alunos)
"""
"""
aqui mostra a chave e o valor e como funcionam, tô pegando os dois:

aluno = {
    "nome": "Luan",
    "idade": 18,
    "nota": 8.5
}
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")

AQUI PEGA SÓ AS CHAVES

for chave in aluno.keys():
    print(chave)

AQUI MOSTRA OS VALORES:

for valor in aluno.values():
    print(valor)
"""
"""
pessoas = list()

while True:
    dados = dict()
    dados["nome"] = str(input("nome: "))
    dados["idade"] = int(input("idade: "))
    dados["sexo"] = str(input("sexo: [F/M]: ")).upper()
    pessoas.append(dados)

    continuar = input("Continuar? [S/N] ").upper()

    if continuar == "N":
        break

mulheres = list()
contador = 0

for pessoa in pessoas:
    if pessoa["sexo"] == "F":
        mulheres.append(pessoa["nome"])

    contador = contador + pessoa["idade"]

media = contador / len(pessoas)

print(f"foram cadastradas {len(pessoas)} pessoas")
print(f"as mulheres que foram cadastradas: {mulheres}")
print(f"A média das pessoas cadastradas foi: {media:.2f}")
print("PESSOAS ACIMA DA MÉDIA")
for pessoa in pessoas:
    if pessoa['idade'] > media:
        print(f"nome: {pessoa['nome']} | idade : {pessoa['idade']}")
"""
"""
def cadastra_pessoa(nome, idade):
    dados = dict()
    dados["nome"] = nome
    dados["idade"] = idade

    if idade > 18:
        dados["status"] = "maior de idade"
    else:
        dados["status"] = "menor de idade"

    return dados

pessoas = list()
while True:
    nome = str(input("nome: "))
    idade = int(input("idade: "))

    pessoa = cadastra_pessoa(nome, idade)
    pessoas.append(pessoa)

    continuar = input("Continuar? [S/N] ").upper()
    if continuar == "N":
        break

print("pessoas cadastradas")

for p in pessoas:
    print(f"nome = {p['nome']} | idade = {p['idade']} | status = {p['status']}")
"""
"""
def dobro(n):
    return n * 2

print(dobro(5))
"""
"""
def maior(a, b):
    if a > b:
        return a
    else:
        return b

print(maior(5, 2))
"""
"""
def par_impar(num):
    if num % 2 == 0:
        return f"par"
    else:
        return "impar"

def mensagem(num):
    tipo = par_impar(num)
    return f"O número é {tipo}"

print(par_impar(5))
"""

"""
def analisar_lista(lista):
    quantidade = len(lista)
    maior = lista[0]
    menor = lista[0]
    contador = 0
    for c in lista:
        if c > maior:
            maior = c
        if c < menor:
            menor = c
        contador = contador + c
    media = contador / quantidade
    return quantidade, maior, menor, media

lista = list()
while True:
    numeros = int(input("numeros: "))
    lista.append(numeros)

    continuar = input("Continuar? [S/N] ").upper()
    if continuar == "N":
        break

def mostrar_relatorio(quantidade, maior, menor, media):
    print("RELATORIO")
    print(f"quantidade: {quantidade}")
    print(f"maior: {maior}")
    print(f"menor: {menor}")
    print(f"media: {media:.2f}")

dados = analisar_lista(lista)
mostrar_relatorio(*dados)
"""
"""
def leiaInt(num):
    ok = False
    while True:
        n = str(input(num))
        if n.isnumeric():
            valor = int(n)
        else:
            print("\033[31m ERRO! Digite novamente\033[m")
        if ok:
            break
    return valor

n = leiaInt("Digite um número: ")
print(f"o valor que você digitou é {n}")

"""
"""
def leiaint(msg):
    while True:
        n = input(msg)
        if n.isnumeric():
            return int(n)
        print("\033[31m ERRO! Digite novamente\033[m")

idade = leiaint("Digite sua idade: ")
print(f"idade: {idade}")
"""
"""
def notas(*n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)

    if sit:
        if r['media'] > 7:
            r['sit'] = 'boa'
        if r['media'] < 7:
            r['sit'] = 'ruim'

    return r

resp = notas(2, 5.3, 9, 8.5)
print(resp)

"""
"""
def cadastro(nome, *notas, sit=False):
    dici = dict()
    dici["nome"] = nome
    dici["lista de notas"] = notas
    dici["media"] = sum(notas) / len(notas)

    if sit:
        if dici["media"] >= 7:
            dici["situação"] = "aprovado"
        elif dici["media"] >= 5:
            dici["situação"] = "recuperação"
        else:
            dici["situação"] = "reprovado"

    return dici


avaliar = cadastro("luan", 8, 7.5, 6, sit=True)
print(avaliar)

"""
"""
A função conta altera o saldo de acordo com o tipo de operação (saque ou depósito)
, mas só permite sacar se houver saldo suficiente.

def conta(saldo, valor, tipo):
    if tipo == "sacar":
        if saldo >= valor:
            saldo = saldo - valor
        else:
            print("saldo insuficiente")
    elif tipo == "depositar":
        saldo = saldo + valor
    return saldo

usuario = conta(2000, 2100, "sacar")
print(usuario)
"""
"""
def analisar(*numeros):
    dici = dict()
    dici["quantidade"] = len(numeros)
    dici["maior"] = max(numeros)
    dici["menor"] = min(numeros)
    dici["media"] = sum(numeros) / len(numeros)

    return dici

resp = analisar( 8, 7.5, 22, 1)
print(resp)
"""
"""
Filtro de pessoas com idade maior do que 18 anos


def filtrar_maiores(lista):
    maiores = list()
    for n in lista:
        if n["idade"] > 18:
            maiores.append(n["nome"])
    return maiores

lista = list()
while True:
    dados = dict()
    dados["nome"] = str(input("nome: "))
    dados["idade"] = int(input("idade: "))
    lista.append(dados.copy())

    continuar = input("Continuar? [S/N] ").upper()
    if continuar == "N":
        break

pessoas = filtrar_maiores(lista)

print("MAIORES DE IDADE")
for n in pessoas:
    print(n)
"""
"""
def conta(saldo, valor, tipo):
    if tipo == "sacar":
        if saldo >= valor:
            saldo = saldo - valor
        else:
            print("saldo insuficiente")
    elif tipo == "depositar":
        saldo = saldo + valor

    return saldo

pessoa = conta(2000, 1400, "sacar")
print(pessoa)
"""
"""
def remover_duplicados(lista):
    nova = list()
    for c in lista:
        if c not in nova:
            nova.append(c)

    return nova

numeros = [1, 2, 3, 4, 4, 5]
print(remover_duplicados(numeros))
"""
"""
def carrinho(*precos):
    if len(precos) == 0:
        return {"total": 0, "media": 0, "maiscaro": 0}

    dados = dict()
    dados["total"] = sum(precos)
    dados["media"] = sum(precos) / len(precos)
    dados["maiscaro"] = max(precos)

    return dados

precos = []
print(carrinho(*precos))

"""
"""
Analisador de texto
def analisar_texto(texto):
Retorne:
quantidade de palavras
quantidade de letras
palavra mais longa

def analisar_texto(texto):
    divide = texto.split()
    quanpala = len(divide)

    tiraespaco = texto.replace(" ", "")
    quantidade = len(tiraespaco)

    maior = divide[0]
    for c in divide:
        if len(c) > len(maior):
            maior = c

    return quantidade, quanpala, maior


texto = "meu nome é luan tenho 22 anos palavragrande"
print(analisar_texto(texto))    
"""
"""
def relatorio_pessoas(lista):
    dici = dict()
    dici["quantidade"] = len(lista)

    soma = 0
    for n in lista:
        soma = soma + n["idade"]

    dici["media"] = soma / len(lista)

    mulheres = list()
    for c in lista:
        if c["sexo"] == "F":
            mulheres.append(c["nome"])

    maisvelho = lista[0]
    maisnovo = lista[0]
    for y in lista:
        if y["idade"] > maisvelho["idade"]:
           maisvelho = y
        elif y["idade"] < maisnovo["idade"]:
            maisnovo = y

    dici["maisvelho"] = maisvelho["nome"]
    dici["maisnovo"] = maisnovo["nome"]

    return dici, mulheres

def mostra_resultado(dici, mulheres):
    print("------------- RELATÓRIO -------------------")

    print(f"O total de pessoas cadastradas foi {dici['quantidade']}")
    print(f"a média de pessoas foi {dici['media']:.2f} anos")

    print("lista de mulheres que foram cadastradas")
    if len(mulheres) == 0:
        print("nenhuma mulher foi cadastrada")
    else:
        print(mulheres)

    print(f"a pessoa mais velha foi: {dici['maisvelho']}")
    print(f"a pessoa mais nova foi: {dici['maisnovo']}")

lista = list()
while True:
    dados = dict()
    dados["nome"] = str(input("nome: "))
    dados["idade"] = int(input("idade: "))
    dados["sexo"] = str(input("sexo: [M/F]: ")).upper()
    lista.append(dados.copy())

    continuar = input("Continuar? [S/N] ").upper()
    if continuar == "N":
        break

dici, mulheres = relatorio_pessoas(lista)
mostra_resultado(dici, mulheres)
"""
"""
c =('\033[m', #sem cores
    '\033[0;30;41m', #1 - vermelho
    '\033[0;30;42m', #2 - verde
    '\033[0;30;43m', #3 - amarelo
    '\033[0;30;44m', #4 - azul
    '\033[0;30;45m', #5 - roxo
    '\033[7;30m' #6 - branco
    );

def ajuda(com):
    titulo(f"acessando o manual do comando \'{com}\'", 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print("~" * tam)
    print(f"   {msg}")
    print("~" * tam)
    print(c[0], end='')

comando = ''
while True:
    titulo("SISTEMA DE AJUDA PYHELP!", 2)
    comando = str(input("função ou biblioteca: "))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)
titulo("ATÉ LOGO", 1)
"""
"""
from uteis import numeros

num = int(input("digite um valor: "))
fat = numeros.fatorial(num)
print(f"O fatorial de {num} é {fat}")
print(f"O dobro de {num} é {numeros.dobro(num)}")
print(f"o triplo de {num} é {numeros.triplo(num)}")
"""
