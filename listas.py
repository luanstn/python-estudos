"""
num = [2, 5, 9, 1]
num[2] = 3
num.append(6)
num.sort(reverse = True)
num.insert(2, 7)
if 5 in num:
    num.remove(5)
else:
    print("Não achei o número 5")
print(num)
print(f"essa lista tem {len(num)} elementos")"""

"""
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f"{c}...", end="")
    print(f"Na posição {c} encontrei o valor {v}")
"""
"""
valores = []
for cont in range(0, 5):
    valores.append(int(input("Digite um valor: ")))

for c, v in enumerate(valores):
    print(f"{c}...", end="")
    print(f"Na posição {c} encontrei o valor {v}")
"""
"""

quando modificar, vai modificar as duas por que voce fez uma ligação e não um cópia da lista

a = [2, 3, 4, 5]
b = a
b[2] = 8
print(f"lista {a}")
print(f"lista {b}")
"""
"""
aqui criou um cópia,então quando modificar o B o A não vai ser alterado

a = [2, 3, 4, 5]
b = a[:]
b[2] = 8
print(f"lista {a}")
print(f"lista {b}")
"""
"""
vai pedir para inserir 5 valores e vai colocar em uma lista e dizer qual é o maior e o menor 

numeros = []

for cont in range(0, 5):
    numeros.append(int(input(f"Digite um valor na posição {cont} : ")))

    if cont == 0:
        maior = numeros[0]
        menor = numeros[0]

    if numeros[cont] > maior:
        maior = numeros[cont]
    if numeros[cont] < menor:
        menor = numeros[cont]
print(f"lista: {numeros}")
print(f"O maior é: {maior}, e o menor é: {menor}")
"""
"""
vai pedir para o usuário colocar os numeros na lista e se ele quiser para ou não

lista = []
c = 0
while c == 0:
    numero = int(input("Digite um valor: "))

    if numero in lista:
        print("Esse número já está na lista!")
    if numero not in lista:
        lista.append(numero)

    encerra = input("Deseja continuar? [S/N] ").upper()

    if encerra == "S":
        c = 0
    else:
        print("encerrando...")
        c = c + 1
print(f"sua lista foi: {lista}")
"""
"""
vai pedir um valor e vai add na lista e vai dizer a quantidade, ordem decrescente e se 0 numero 5 aparece

lista = []
c = 0
quant = 0

while c == 0:
    numero = int(input("Digite um balor: "))
    lista.append(numero)
    continua = input("Deseja continuar? [S/N] ").upper()
    quant = quant + 1

    if continua == "N":
        print("Encerrando...")
        c = c + 1
    if continua != "S":
        print("você está digitando a letra errada!")
        c = c + 0



altera = lista.sort(reverse=True)

print(f"a quantidade de números digitados foi: {quant}")
print(f"Lista em ordem decrescente: {lista}")
if 5 in lista:
    print("O número 5 apareceu na lista!")
else:
    print("o número 5 não apareceu na lista!")
"""
"""
vai pedir valores e vai dizer se é impar ou par

lista = []
c = 0

while c == 0:
    numero = int(input("Digite um valor: "))
    lista.append(numero)

    continua = input("Deseja continuar? [S/N] ").upper()

    if continua == "N":
        print("Encerrando...")
        c = c + 1
    if continua != "S":
        print("você digitou errado, tente novamente!")
        c = c + 0

par = []
impar = []

for f in lista:
    if f % 2 == 0:
        par.append(f)
    else:
        impar.append(f)
print(f"A lista completa é: {lista}")
print(f"A lista de pares: {par}")
print(f"A lista de ímpares: {impar}")
"""

"""  --------------------------- LISTAS COMPOSTAS ----------------------------"""
"""
teste = list()
teste.append("Luan")
teste.append(22)
galera = list()
galera.append(teste[:])
teste[0] = "maria"
teste[1] = 22
galera.append(teste[:])
print(galera)
"""
"""
vai pegar só os nomes

galera = [["joaquim", 12], ["Luan", 22], ["Camily", 19], ["Maria", 13]]
for c in galera:
    print(c[0])
    """

"""
vai pegar só a idade 

galera = [["joaquim", 12], ["Luan", 22], ["Camily", 19], ["Maria", 13]]
for c in galera:
    print(c[1])
"""
"""
galera = [["joaquim", 12], ["Luan", 22], ["Camily", 19], ["Maria", 13]]
for c in galera:
    print(f"{c[0]} tem {c[1]} anos de idade")
"""
"""
para armazenar uma lista dentro de outra e voce pode colocar os valores

galera = list()
dado = list()
for c in range(0, 3):
    dado.append(input("Digite seu nome: "))
    dado.append(int(input("Digite sua idade: ")))
    galera.append(dado[:])
    dado.clear()
print(galera)
"""
"""
ler dados que eu colocar e dizer se é maior ou menor de idade

galera = list()
dado = list()
maior = 0
menor = 0
for c in range(0, 3):
    dado.append(input("Digite seu nome: "))
    dado.append(int(input("Digite sua idade: ")))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade")
        maior = maior + 1
    else:
        print(f"{p[0]} é menor de idade")
        menor = menor + 1
"""
"""
galera = list()
dados = list()

c = 0
while c == 0:
    dados.append(input("Digite seu nome: "))
    dados.append(float(input("Digite o seu peso: ")))
    galera.append(dados[:])
    dados.clear()
    escolha = input("Deseja continuar? [S/N] ").upper()

    if escolha == "N":
        print("Encerrando...")
        c = c + 1

maior = galera[0][1]
menor = galera[0][1]
nomesmai = list()
nomesmeno = list()

for p in galera:
    if p[1] > maior:
        maior = p[1]
        nomesmai = [p[0]]
    elif p[1] == maior:
        nomesmai.append(p[0])


    elif p[1] < menor:
        menor = p[1]
        nomesmeno = [p[0]]
    elif p[1] == menor:
        nomesmeno.append(p[0])

print(f"Os maiores peso foram os de {nomesmai} com o peso de {maior} ")
print(f"Os menores pesos foram os de {nomesmeno} com o peso de {menor} ")
print(f"foram colocadas {len(galera)} pessoas")
"""
"""
pessoas = list()

for c in range(0, 3):
    pessoas.append(input("Digite o seu nome: "))

primeiro = (pessoas[0])
ultimo = (pessoas[-1])
vezes = (len(pessoas))

print(f"Foram digitados {vezes} vezes!")
print(f"a primeira pessoa a ser digitada foi {primeiro} e o último foi {ultimo}")
"""
"""
from random import randint
numeros = list()

for c in range(0, 5):
    sorteio = randint(1, 100)
    numeros.append(sorteio)

    if c == 0:
        maior = sorteio
        menor = sorteio
    else:
        if sorteio > maior:
            maior = sorteio
        elif sorteio < menor:
            menor = sorteio

print(f"os numeros sorteadoes foram: {numeros}!")
print(f"o maior valor sortedo foi {maior} e o menor foi {menor}")
"""
"""
pessoas = list()
dados = list()
maiores = 0
menores = 0

for c in range(0, 4):
    dados.append(input("Digite o seu nome: "))
    dados.append(float(input("Digite a sua idade: ")))
    pessoas.append(dados[:])
    dados.clear()
for p in pessoas:
    if p[1] >= 18:
        maiores = maiores + 1
    else:
        menores = menores + 1
print(f"as pessoas cadastradas foram: {pessoas}")
print(f"{maiores} pessoas são maiores de idade")
"""
"""
pessoas = list()
dados = list()
c = 0

while c == 0:
    dados.append(input("Digite o seu nome: "))
    dados.append(float(input("Digite o seu peso: ")))
    pessoas.append(dados[:])
    dados.clear()
    pedido = input("Deseja continuar? [S/N] ").upper()
    if pedido == "N":
        c = c + 1
        print("Encerrando...")

maior = pessoas[0][1]
menor = pessoas[0][1]
maispesados = list()
maisleves = list()

for p in pessoas:

    if p[1] > maior:
        maior = p[1]
        maispesados.append(p[0])
    elif p[1] < menor:
        menor = p[1]
        maisleves.append(p[0])

contagem = len(pessoas)
print(f"As pessoas mais pesadas foram: {maispesados}")
print(f"As mais leves foram: {maisleves}")
print(f"foram cadastradas {contagem} pessoas")
"""
"""

numeros = list()
pares = list()
impares = list()

for c in range (0, 5):
    n = int(input("Digite o seu nome: "))
    numeros.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print(pares)
print(impares)
"""
"""
como fazer uma matriz de 3 colunas e 3 linhas
matriz = []

for c in range(0, 3):
    linha = []
    for j in range(0, 3):
        valor = int(input(f"Digite o valor da linha para {c} e {j}: "))
        linha.append(valor)
    matriz.append(linha)
print(matriz, end=" ")
"""
"""
matriz = []

for c in range(0, 3):
    linha = []
    for l in range (0, 3):
        valor = int(input("Digite um valor: "))
        linha.append(valor)
    matriz.append(linha)

for c in range(0, 3):
    for l in range(0, 3):
        print(matriz[c][l], end=" ")
    print()
"""
"""
cria uma matriz de 3 por 3 e faz a soma de todos os valores que foram colocados
matriz = []
todos = 0
for c in range(0, 3):
    linha = []
    for l in range (0, 3):
        valor = int(input("Digite um valor: "))
        linha.append(valor)
        todos = todos + valor
    matriz.append(linha)
print(todos)
"""
"""
faz uma matriz 3 por 3 e diz a soma dos pares quanto dá
matriz = []
pares = 0

for c in range(0, 3):
    linha = []
    for j in range(0, 3):
        valor = int(input("Digite o valor: "))
        linha.append(valor)
        if valor % 2 == 0:
            pares = pares + valor
    matriz.append(linha)

print(f"A soma dos pares dessa matriz é: {pares}")
"""
"""
vai criar uma matriz de 3 por 3 e vai somar os que estão na terceira coluna

matriz = []
resul = []
n = 0

for c in range(0, 3):
    linha = []
    for j in range(0, 3):
        valor = int(input("Digite o valor: "))
        linha.append(valor)
    matriz.append(linha)
for p in matriz:
    resul.append(p[2])
    n = n + p[2]
print(n)
"""
"""
vai pegar todo o valor da segunda linha, somar e dar o resultado

matriz = []
maior = []
for c in range(0, 3):
    linha = []
    for j in range(0, 3):
        valor = int(input("Digite o valor: "))
        linha.append(valor)
    matriz.append(linha)
    
n = 0
for valor in matriz[1]:
    n = n + valor
    print(n)
"""
"""
vai fazer uma matriz de 3 colunas e 3 linhas e ver a soma de todos os pares, a soma dos valores da terceira
coluna, o maior valor da segunda linha.

matriz = []
matriz = []
pares = 0
terceira = 0
maior = 0


for c in range(0, 3):
    linha = []
    for j in range(0,3):
        numeros = int(input("Digite um número: "))
        linha.append(numeros)
    matriz.append(linha)

for c in range(0, 3):
    for j in range(0, 3):
        if matriz[c][j] % 2 == 0:
            pares = pares + matriz[c][j]
        print(matriz[c][j], end=" ")
    print()

for p in matriz:
    terceira = terceira + p[2]

for p in matriz[1]:
    if p >= maior:
        maior = p

print(f"A soma de todos os valores pares da matriz é: {pares}")
print(f"A soma dos valores da terceira coluna é: {terceira}")
print(f"o maior valor da segunda linha é: {maior}")
"""
"""
sorteia quantos jogos de mega sena voce quer fazer, com números aleatórios
import random
quant = int(input("Quantos jogos deseja fazer? "))
jogos = []

for c in range(0, quant):
    linha = []
    for j in range(0, 6):
        sorteio = random.randint(1, 60)
        if sorteio not in linha:
            linha.append(sorteio)
    jogos.append(linha)

for c in range(0, quant):
    print(f"jogo {c + 1} : ", end = " ")
    for p in jogos[c]:
        print(f"{p},", end = " ")
    print()
"""
"""
aluno = list()
dados = list()
media = list()
c = 0
conta = 0

while c == 0:
   dados.append(input("Nome: "))
   dados.append(float(input("primeira nota: ")))
   dados.append(float(input("segunda nota: ")))
   aluno.append(dados[:])
   dados.clear()

   finaliza = input("Deseja continuar? [s/n]").upper()

   if finaliza == "N":
       c = c + 1
for c in aluno:
    conta = conta + 1
    media = (c[1] + c[2]) /2
    print(f"{conta}  {c[0]}   ------      {media}")

    escolha = int(input(f"qual estudante você deseja ver? (999 para encerrar)"))

    if escolha == 999:
        print("encerrando")
    if 0 <= escolha < len(aluno):
        print(f"Notas de aluno {aluno[escolha][0]}: {aluno[escolha][1]}, {aluno[escolha][2]}")
"""
"""
pessoas = list()
nomes = list()
dados = list()
maiores = 0
menores = 0

for c in range(0, 4):
    dados.append(input("Nome: "))
    dados.append(int(input("sua idade: ")))
    pessoas.append(dados[:])
    dados.clear()
for p in pessoas:
    if p[1] > 18:
        maiores = maiores + 1
    else:
        menores = menores + 1
    nomes.append(p[0])

print(f"as pessoas cadastradas são: {pessoas}")
print(f"de maiores tem: {maiores} e menores: {menores}")
print(nomes)
"""
"""
Maiores de idade em uma lista

Menores de idade em outra
No final, mostre as duas listas separadas.

pessoas = list()
dados = list()
maiores = list()
menores = list()
c = 0
while c == 0:
    dados.append(input("Nome: "))
    dados.append(int(input("Digite sua idade: ")))
    pessoas.append(dados[:])
    dados.clear()

    escolha = input("continuar? [s/n]").upper()
    if escolha == "N":
        c = c + 1

for p in pessoas:
    if p[1] > 18:
        maiores.append(p)
    else:
        menores.append(p)
print(f"as pessoas cadastradas foram: {pessoas}")
print(f"de maiores tem: {maiores}")
print(f"de menores tem: {menores}")
"""
"""

pede o nome e uma nota de vários alunos.
Depois, mostre duas listas:

Uma com os alunos aprovados (nota ≥ 7)

Outra com os reprovados (nota < 7)

alunos = list()
dados = list()
aprovados = list()
reprovados = list()

c = 0
while c == 0:
    dados.append(input("digite o nome: "))
    dados.append(int(input("digite a nota: ")))
    alunos.append(dados[:])
    dados.clear()

    escolha = input("continuar? [s/n]").upper()
    if escolha == "N":
        c = c + 1

for p in alunos:
    if p[1] > 7:
        aprovados.append(p)
    else:
        reprovados.append(p)
print(f"Os alunos cadastrados foram: {alunos}")
print(f"Os alunos que foram aprovados: {aprovados}")
print(f"Os alunos que foram reprovados: {reprovados}")
"""
"""
Cadastro de times
Cadastre o nome de um time e o número de vitórias e derrotas.
Depois, mostre:

O time com mais vitórias
O time com mais derrotas

times = list()
dados = list()
vitorioso = list()
perdedor = list()
c = 0
while c == 0:
    dados.append(input("Digite o nome do time: "))
    dados.append(int(input("quantidade de vitórias: ")))
    dados.append(int(input("quantidade de derrotas")))
    times.append(dados[:])
    dados.clear()
    escolha = input("continuar? [s/n]").upper()

    if escolha == "N":
        print("encerrando")
        c = c + 1
        
mais_vitorios = times[0][0]
mais_derrotas = times[0][0]
maior = times[0][1]
menor = times[0][2]

for p in times:
    if p[1] > maior:
        maior = p[1]
        mais_vitorios = p[0]

    if p[2] > menor:
        menor = p[2]
        mais_derrotas = p[0]

print(f"o time com mais vitórias é: {mais_vitorios} com {maior} jogos ganhos")
print(f"O time mais perdedor é: {mais_derrotas} com {menor} jogos perdidos")
"""
"""
lista = list()
dados = list()
acima = list()
somamedias = 0

while True:
    dados.append(input("Nome: "))
    dados.append(float(input("Digite a primeira nota: ")))
    dados.append(float(input("Digite a segunda nota: ")))
    dados.append(float(input("Digite a terceira nota: ")))
    lista.append(dados[:])
    dados.clear()

    escolha = input("continuar? [s/n]").upper()

    if escolha == "N":
        print("encerrando...\n")
        break


print("Médias individuais: ")
for p in lista:
    media = (p[1] + p[2] + p[3]) / 3
    print(f"{p[0]} - {media:.2f}")

    somamedias = somamedias + media

    if media > 7:
        acima.append([p[0], media])


mediagrl = somamedias / len(lista)
print(f"a média geral da turma é: {mediagrl:.2f}")

print("Alunos acima da média geral:")

for p in acima:
    print(f"{p[0]}  -  {p[1]:.2f}")
"""

"""Cadastro com busca
Peça o nome e a idade de várias pessoas e guarde em uma lista.
Depois, pergunte um nome e mostre se ele está cadastrado ou não.

pessoas = list()
dados = list()

while True:
    dados.append(input("Digite o nome: "))
    dados.append(int(input("Digite a idade: ")))
    pessoas.append(dados[:])
    dados.clear()

    escolha = input("continuar? [s/n]").upper()
    if escolha == "N":
        print("encerrando...")
        break

cadastro = input("digite o nome para ver se essa pessoa está cadastra: ")

for p in pessoas:
    if cadastro == p[0]:
        print(f"{p[0]} já foi cadastrado")
        break
else:
    print("Não foi cadastrado")"""

"""
Maior e menor em sublistas
Crie uma lista composta com várias listas de 3 números cada.
Mostre:

O maior número de cada sublista

O menor número de cada sublista
Exemplo: [[3,5,1],[10,2,8]] → maiores = [5,10], menores = [1,2]"""
"""
Cria uma lista composta com várias listas de 3 números cada.
Mostre:

O maior número de cada sublista

O menor número de cada sublista
Exemplo: [[3,5,1],[10,2,8]] → maiores = [5,10], menores = [1,2]

lista = list()
numeros = list()

while True:
    numeros.append(int(input("Digite o primeiro numero: ")))
    numeros.append(int(input("Digite o segundo numero: ")))
    numeros.append(int(input("Digite o terceiro numero: ")))
    lista.append(numeros[:])
    numeros.clear()

    escolha = input("continuar? [s/n]").upper()

    if escolha == "N":
        print("encerrando...")
        break

maior = lista[0][0]
menor = lista[0][0]
maiorlista = list()
menorlista = list()


for p in range(len(lista)):
    for j in range(len(lista[p])):
        if lista[p][j] > maior:
            maior = lista[p][j]

        if lista[p][j] < menor:
            menor = lista[p][j]

    maiorlista.append(maior)
    menorlista.append(menor)
print(maiorlista)
print(menorlista)
"""""
"""
Matriz simplificada (nível lista composta)
Peça 9 números e monte uma estrutura assim:

[ [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9] ]


Depois, mostre:

Todos os números pares

A soma dos valores da 3ª coluna

O maior valor da 2ª linha


matriz = []

for c in range(0, 3):
    linha = []
    for j in range(0, 3):
        numeros = int(input(f"Digite nove números: "))
        linha.append(numeros)
    matriz.append(linha)


for c in range(0, 3):
    for j in range(0, 3):
        print(f"{matriz[c][j]:^5}", end="")
    print()
"""


"""------------------------------- DICIONÁRIOS ---------------------------------"""

"""
pessoas = {"nome": 'luan', "idade": 22, "sexo": 'M'}
print(pessoas['nome'])
print(f"o {pessoas["nome"]} tem {pessoas["idade"]} anos")
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
"""
"""
        VAI IMPRIMIR A CHAVE
        
pessoas = {"nome": 'luan', "idade": 22, "sexo": 'M'}
for k in pessoas.keys():
    print(k)
"""
"""
      VAI IMPRIMIR A CHAVE E ITENS  
      
pessoas = {"nome": 'luan', "idade": 22, "sexo": 'M'}
for k, v in pessoas.items():
    print(f"{k} = {v}")
"""
"""
        VAI MUDAR O NOME
        
pessoas = {"nome": 'luan', "idade": 22, "sexo": 'M'}
pessoas["nome"] = "raylson"
for k, v in pessoas.items():
    print(f"{k} = {v}")
"""
"""
    ADICIONA ELEMENTOS AO DICIONÁRIO
    
pessoas = {"nome": 'luan', "idade": 22, "sexo": 'M'}
pessoas["peso"] = 91.21
for k, v in pessoas.items():
    print(f"{k} = {v}")
"""
"""

        CRIA UMA LISTA E ADICIONA OS DICIONARIOS
        
brasil = list()
estado = {"uf" : "Rio de janeiro", "sigla" : "RJ"}
estado2 = {"uf" : "Paraíba", "sigla" : "PB"}
brasil.append(estado)
brasil.append(estado2)
print(brasil[1]["sigla"])
"""
"""
estado = dict()
brasil = list()
for c in range(0, 3):
    estado["uf"] = str(input("Unidade Federativa: "))
    estado["sigla"] = str(input("Sigla do Estado: "))
    brasil.append(estado.copy())
print(brasil)
"""
"""
vai criar um dicionario e dizer se está aprovado ou reprovado

alunos = dict()

for c in range(0, 1):
    alunos["nome"] = str(input("Nome: "))
    alunos["media"] = float(input("Media: "))


    if alunos["media"] >= 7:
        alunos["situacao"] = "aprovado"
    if alunos["media"] < 7:
        alunos["situacao"] = "reprovado"
for p, j in alunos.items():
    print(f"{p} é igual a {j}")
"""
"""
faz um sorteio para 4 pessoas e diz o ranking

import random
from operator import itemgetter

jogadores = dict()
for c in range(0, 4):
    nome = "jogador" + str(c+1)
    resultado = random.randint(1, 6)
    jogadores[nome] = resultado
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f"{i+1} lugar: {v[0]} com {v[1]}.")
"""
"""
ele vai pegar nome, pedir a data de nascimento e fazer o calculo da idade, quanto tempo tem de carteira assinada

pessoa = dict()

for c in range(0, 1):
    pessoa["nome"] = str(input("Nome: "))
    anonasc = int(input("Ano de nascimento: "))
    pessoa["idade"] = 2025 - anonasc
    pessoa["carteira"] = int(input("Carteira de trabalho: "))


    if pessoa["carteira"] != 0:
        pessoa["contratacao"] = int(input("Ano de contratacao: "))
        pessoa["salario"] = float(input("Digite o seu salário: "))

        pessoa["aposentadoria"] = (pessoa["contratacao"] - anonasc) + 35

print( "------------------------- SEUS DADOS -------------------------")
for c, k in pessoa.items():
    print(f"{c} tem o valor {k}")
"""
"""
vai pegar o nome do jogador e vai pedir o total de partidas e gols e dizer os gols que fez em cada
partida e o total de gols feitos.

jogador = dict()
jogador["nome"] = str(input("nome do jogador: "))
partidas = int(input("numero de partidas: "))
gols = list()
totalgols = 0

for i in range(0, partidas):
    gols.append(int(input("numero de gols: ")))

    totalgols = totalgols + gols[i]

jogador["gols"] = gols[:]
jogador["total"] = totalgols

for k, y in jogador.items():
    print(f"O campo {k} tem o valor {y}")

for i in range(len(gols)):
    print(f"Na partida {i+1}, ele fez {gols[i]} gols.")
"""
"""
vai pegar o nome, idade, sexo e colocar em um dicionário e o dicionário vai ser colocado em uma lista, depois
vai dizer quantas pessoas foram cadastradas, a media do grupo, quantas mulheres foram cadastradas e quantas
pessoas estão acima da média


pessoas = list()
dados = dict()
idadesjuntos = 0
while True:
    dados["nome"] = str(input("Digite o nome: "))
    dados["sexo"] = str(input("Digite o sexo: ")).upper()
    dados["idade"] = int(input("Digite a idade: "))
    pessoas.append(dados.copy())
    idadesjuntos = idadesjuntos + dados["idade"]

    confirma = str(input("Deseja continuar? [S/N] ")).upper()

    if confirma in "N":
        break

media = idadesjuntos / len(pessoas)
mulheres = list()

for c in pessoas:
    if c["sexo"] == "F":
        mulheres.append(c["nome"])

acimamedia = list()

for c in pessoas:
    if c["idade"] > media:
        acimamedia.append(c["nome"])

print(f"{len(pessoas)} pessoas foram cadastradas!")
print(f"a media de idade é: {media:.2f}")
print(f"as mulheres cadastradas foram: {mulheres}")
print(f"lista das pessoas que estão acima da média: {acimamedia}")
"""
"""
jogador = list()
dados = dict()

while True:
    dados["nome"] = str(input("Digite o nome: "))
    dados["partidas"] = int(input("Digite a quantidade de partidas: "))

    gols = []
    totalgol = 0

    for c in range(0, dados["partidas"]):
       qnt = int(input("Digite a quantidade de gols: "))
       gols.append(qnt)
       totalgol = totalgol + qnt

    dados["gols"] = gols[:]
    dados["total"] = totalgol

    jogador.append(dados.copy())
    dados.clear()

    confirma = str(input("Deseja continuar? [S/N] ")).upper()

    if confirma in "N":
        break
"""