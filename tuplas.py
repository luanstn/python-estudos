"""
lanche = ("hamburguer", "suco", "pizza", "pudim")
print(lanche[-3:])
"""
"""
ele vai printar um por um dos elementos na tupla
lanche = ("hamburguer", "suco", "pizza", "pudim")
for c in lanche:
    print(f"eu vou comer {c}")
print("comi para caramba")
"""
"""
outra maneira de fazer
lanche = ("hamburguer", "suco", "pizza", "pudim")

for cont in range (0, len(lanche)):
    print(lanche[cont])
print("comi para caramba")
"""
"""
lanche = ("hamburguer", "suco", "pizza", "pudim")
for cont in range (0, len(lanche)):
    print(f"eu vou comer o lanche {lanche[cont]} na posicao {cont}")
print("comi para caramba")
"""
"""
também pode ser assim

lanche = ("hamburguer", "suco", "pizza", "pudim")
for pos, comida in enumerate(lanche):
    print(f"eu vou comer {comida} na posicao {pos}")
print("comi para caramba")
"""
"""
vai pedir o nuemro entre 0 e dez, caso acertar vai mostrar escrito senão vai pedir para colocar de novo

numero = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez")
c = 1
while c != 0:
    pedido = (int(input("Digite o numero: ")))

    if pedido > 10:
        print("entre 0 e 10, tente novamente!")
        c = c + 1
    else:
        print(numero[pedido])

    c = c - 1
"""
"""
mostra os 5 primeiros, os 4 ultimos, em ordem alfabetica e em que lugar está um time

campeonato = (
    "Flamengo", "Cruzeiro", "Palmeiras", "Mirassol", "Botafogo",
    "Bahia", "São Paulo", "Fluminense", "Red Bull Bragantino", "Corinthians",
    "Ceará", "Grêmio", "Internacional", "Santos", "Atlético Mineiro",
    "Vasco da Gama", "Vitória", "Juventude", "Fortaleza", "Sport"
)



primeiros = campeonato[:5]
ultimos = campeonato[-4:]
alfabetica = sorted(campeonato)
posicao = campeonato.index("Juventude")

print(f"os 5 primeiros são {primeiros}")
print(f"os 4 últimos são: {ultimos}")
print(f"ordem alfabetica {alfabetica}")
print(f"o juventude está em {posicao} lugar")

"""
"""
vai colocar 5 números aleatórios dentro de uma tupla e vai dizer qual o maior e o menor

import random

salva = ()

for c in range(0, 5):
    numero = random.randint(1, 100)
    if c == 0:
        maior = numero
        menor = numero

    salva = salva + (numero,)

    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print(salva)
print(f"o maior número é: {maior}")
print(f"o menor número é: {menor}")
"""
"""
vai pedir 4 valores e vai ver quantas vezes o 9 apareceu, qual posição o 3 aparece caso tiver sido digitado
e quantos pares foram inseridos


salva = ()
pares = ()
for c in range (0, 4):
    numero = int(input("Digite um número: "))
    salva = salva + (numero,)

    if numero % 2 == 0:
        pares = pares + (numero,)


if 9 in salva:
    print(f"o valor 9 apareceu {salva.count(9)} vezes")
else:
    print("o número 9 não foi digitado nenhuma vez!")
if 3 in salva:
    print(f"o valor 3 apareceu na {salva.index(3+1)} posição")
else:
    print(f"não tem 3 na tupla!")
if len(pares) > 0:
    print(f"os números pares que foram digitados são: ", *pares)
else:
    print("não foi digitado nenhum número par")
"""
"""
vai fazer uma tabela com produtos e o preço, aqui aprende a separa os valores em uma tupla só

produtos = ("Arroz", 20.0,"Feijão", 8.5, "Macarrão", 5.0, "Leite", 4.5, "Pão", 3.0, "Ovo", 12.0, "Açúcar", 6.0)

for c in range(0, len(produtos), 2):
    nome = produtos[c]
    valor = produtos[c + 1]
    if c == 0:
        print("---------TABELA DE PREÇOS-----------")
    print(f"{nome} ------------------------{valor}")
"""
"""
vai mostrar o produto, valor, quantidade e o aumento de 10%

produtos = ("Arroz", 20.0, 5,"Feijão", 8.5, 10,"Macarrão", 5.0, 7,"Leite", 4.5, 12,"Pão", 3.0, 20)

for c in range(0, len(produtos), 3):
    produto = produtos[c]
    valor = produtos[c + 1]
    quantidade = produtos[c + 2]

    aumento = valor * 1.10

    print(f"NOME: {produto}")
    print(f"VALOR: R${valor}")
    print(f"QUANTIDADE: {quantidade}")
    print(f"NOVO PREÇO COM 10% DE AUMENTO: {aumento:.2f}")
    print("-------------------------------------------------")
"""

