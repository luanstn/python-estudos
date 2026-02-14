"""
for c in range(10, 0-1, -1):
    print(c)
"""
"""
c = 10
while c > 0:
    c = c - 1
    print(c)
"""
"""
lista = list()
acumula = 0
for c in range(0, 5):
    numero = int(input("Digite 5 números: "))
    lista.append(numero)
    acumula = acumula + numero

    media = acumula / 5

maior = 0
menor = 0
for c in lista:
    if c > maior:
        maior = c
        menor = c
    if c < menor:
        menor = c
        
print(lista)
print(maior, menor)
print(media)
"""
"""
lista = list()
impar = list()
pares = list()

for c in range(0, 10):
    numero = int(input("coloque 10 números: " ))
    lista.append(numero)

    if numero % 2 == 0:
        pares.append(numero)
    else:
        impar.append(numero)
print(impar)
print(pares)
"""
"""
dados = dict()

dados["nome"] = str(input("Digite o seu nome: "))
dados["idade"] = int(input("Digite sua idade: "))

for c, k in dados.items():
    print(f"{c} : {k}")
"""
"""
dados = dict()

dados["nome"] = str(input("digite o nome do aluno: "))
dados["nota1"] = float(input("digite a primeira nota: "))
dados["nota2"] = float(input("digite a segunda nota: "))

print(" ------ BOLETIM DO ALUNO ------- ")
for c, k in dados.items():
    print(f"{c} : {k}")
    media = (dados["nota1"] + dados["nota2"]) / 2

print(media)

if media >= 7:
    print("aprovado")
else:
    print("reprovado")
"""
"""
alunos = list()

while True:
    dados = dict()
    dados["nome"] = str(input("Digite o nome do aluno: "))
    dados["media"] = float(input("digite a media: "))

    alunos.append(dados)

    continuar = str(input("Deseja continuar? [S/N] ")).upper()

    if continuar == "N":
        break

total = 0

for alunos in alunos:
    total = total + alunos["media"]

mediattl = total / len(alunos)
print(mediattl)

maior = alunos[0]["media"]
menor = alunos[0]["media"]

for aluno in alunos:
    if alunos["media"] > maior:
        maior = alunos["media"]

    if alunos["media"] < menor:
        menor = alunos["media"]
print(maior)
print(menor)
"""