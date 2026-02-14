"""
enquanto for 0 menor que 10 vai continuar
c = 1
while c < 10:
    print(c)
    c = c + 1
print("fim")
"""
"""
enquanto s for inserido vai pedir o número

n = "s"
while n == "s":
    numero = int(input("Digite um numero: "))
    n = str(input("quer continuar? [S/N] "))
print("fim")
"""
"""

n = 1)
par = 0
impar = 0

while n != 0:
    n = int(input("Digite um numero: "))
    if n % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1

print(f"você digitou  {par} números pares e {impar} impares")
"""
"""
caso você digitar f ou m o programa chega ao fim

c = 0
while c == 0:
    sexo = str(input("Digite o sexo: ")).upper()
    if sexo == "F":
        c = c + 1
    if sexo == "M":
        c = c + 1
print("FIM")
"""
"""
programa que define qual a função que você vai escolher dependendo do numero que você colocar

c = 0

while c == 0:
    num1 = int(input("Digite um numero: "))
    num2 = int(input("Digite outro numero: "))

    escolha = int(input("[1] somar [2] multiplicar [3] maior [4] novos numeros [5] sair do programa: "))

    if escolha == 1:
        soma = num1 + num2
        print(f" A soma dos dois números foi: {soma}")

    if escolha == 2:
        mult = num1 * num2
        print(f" a multiplicação dos valores foi: {mult}")

    maior = num1
    if  escolha == 3:
        if num2 > maior:
            maior = num2
            print(f"o maior é {maior}")
        else:
            print(f"o maior é {num1}" )

    if escolha == 4:
        c = c - 1


    elif escolha == 5:
        c = c + 1

    c = c + 1
print("FIM")

"""
"""
vai calcular o fatorial

num = int(input("escolha um número: "))
fatorial = 1
c = num

while c > 1:
    fatorial = fatorial * c
    c = c - 1

print(fatorial)
"""

