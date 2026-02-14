"""
def meunome():
    print("luan santos de santana")

meunome()
"""
"""
vai mudar o que ta no d, no meio da função

def mensagem(d):
    print("----------------------")
    print(d)
    print("----------------------")
    
mensagem("o nome luan")
"""
"""
def calcula(a, b):
    soma = (a + b)
    print(soma)


calcula(1, 4)
"""
"""
def contador(*num):
    print(num)


contador(1, 2)
contador(2, 3, 9, 0)
"""
"""
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] = lst[pos] * 2
        pos = pos + 1

valores = [10, 20, 30, 40, 50]
dobra(valores)
print(valores)
"""
"""
def soma(* numeros):
    s = 0
    for n in numeros:
        s = s + n
    print(f"soma dos valores {numeros} temos {s}")

soma(1, 8, 3)
soma(9, 3)
"""
"""
def terreno(a, b):
    area = a * b
    print(f"A área do terreno {a}x{b} é de {area}")

print(" CONTROLE DE TERRENOS")
print(" -" *20)
x = float(input("Digite um valor: "))
y = float(input("Digite outro valor: "))

terreno(x, y)
"""
"""
def escrever(a):
    print("-" * len(a))
    print(a)
    print("-" * len(a))


escrever("oi!")
escrever("a linha vai acompanhar independente do tanto de palavras que eu colocar")
escrever("eu sei fazer isso")
"""
"""
import time

def linha():
    print("-" * 30)

def contador(inicio, fim, passo):

    print(f"contagem de {inicio} até {fim} em {passo}")
    for j in range(inicio, fim+passo, passo):
        print(j, end=" ")
    print("FIM!")


for c in range(0, 1):
    linha()
    print("contagem de 1 até 10 de 1 em 1")
    for n in range(0, 10):
        print(n, end=" ")
        time.sleep(0.5)
    print("FIM!")
    linha()
    print("contagem de 10 até 0 de 2 em 2")
    for c in range(10, 0 - 1, -2):
        print(c, end=" ")
        time.sleep(0.5)
    print("FIM!")
    linha()
    print("Agora é sua vez de personalizar a contagem!")

    inicio = int(input("Digite o inicio: "))
    fim = int(input("Digite o fim: "))
    passo = int(input("Digite o passo: "))

    if passo == 0:
        passo = 1

    contador(inicio, fim, passo)
"""
"""
vai pegar os valores e dizer o maior que foi informado

def linha():
    print("-" * 30)

def maior(* num):
    linha()
    print("analisando os valores passados...")
    for n in num:
        print(n, end=" ")
    print(f" foram informados, {len(num)} valores ao todo")
    nmrmaior = 0
    for n in num:
        if n > nmrmaior:
            nmrmaior = n
    print(f"o maior valor informado foi: {nmrmaior}")
    linha()

maior(0, 10, 5, 7, 19, 29, 3,)
maior( 9, 19, 43, 7, 8, 22, 45, 55)
"""
"""
def dobro(n):
    print(n + n)
dobro(5)
"""
"""
def area_retangulo(base, altura):
    area = base * altura
    print(f"o valor da area foi de {area}")

base = float(input("Digite o base: "))
altura = float(input("Digite altura: "))
area_retangulo(base, altura)
"""
"""
def maior(a, b):
    if a > b:
        print(f"{a} é o maior")
    else:
        print(f"{b} é o maior")

maior(7, 5)
"""
"""
def somalista(dados):
    soma = 0
    for d in dados:
        soma = soma + d
    print(soma)

dados = list()

while True:
    numeros = int(input("Digite os dados que quer somar: "))
    dados.append(numeros)


    continuar = input("Deseja continuar? [S/N] ").upper()
    if continuar in "N":
        break

print(dados)
somalista(dados)
"""
"""
def contarvogais(texto):
    contador = 0
    vogais = "aeiouAEIOU"

    for c in texto:
        if c in vogais:
            contador = contador + 1
    print(contador)


texto = input("Digite algo: ")
contarvogais(texto)
"""
"""
def inverterstring(palavra):
    palavra = input("Digite algo: ")
    inverter = palavra[::-1]
    print(inverter)

palavra = input("Digite algo: ")

inverterstring(palavra)
"""
"""
def media(*numeros):
    contador = 0
    for c in numeros:
        contador = contador + c
    print(contador / len(numeros))

media(5, 5, 10)
"""
"""
def palindromo(palavra):
    tiraespaco = palavra.replace(" ", "")
    inverte = tiraespaco[::-1]

    if tiraespaco == inverte:
        print(f"{palavra} é um palindromo")
    else:
        print(f"{palavra} não é um palindromo")

palavra = input("Digite algo: ")
palindromo(palavra)
"""
"""
def ordenarlista(lista):
    lista.sort()
    print(lista)

lista = list()

while True:
    lista.append(input("digite uma valor"))

    continuar = input("Deseja continuar? [S/N] ").upper()

    if continuar in "N":
        break

ordenarlista(lista)
"""
