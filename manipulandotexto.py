'''
para dividir a frase com split e pegar só a frase de acordo com o número que voce colocar

frase = "curso em video para python"
dividido = frase.split()
print(dividido[2])
'''
from os.path import split
'''
nome = input("digite o seu nome: ")

print(nome.upper())
print(nome.lower())

sem_espacos = nome.replace(" ", "" )
print(len(sem_espacos))

nomeprimeiro = nome.split(" ")[0]
print(nomeprimeiro)
'''

""""
num = str(input("digite um nome de 0 a 9999"))

unidade = num[0]
dezena = num[1]
centena = num[2]
milhar = num[3]

print(unidade)
print(dezena)
print(centena)
print(milhar)
"""
"""
cidade = input("digite o nome da sua cidade")

print("santo" in cidade)
"""
"""
nome = input("digite o seu nome: ")

semespaco = nome.replace(" ", "")
print("silva" in semespaco)
"""
"""
nome = input("digite uma frase: ")

contador = nome.count("a")

primeirapos = nome.find("a")

ultimapos = nome.rfind("a")

print(contador)
print(primeirapos)
print(ultimapos)

"""
""""
nome = input("digite o seu nome: ")

primeiro = nome.split()[0]

ultimo = nome.split()[-1]

print(primeiro)
print(ultimo)

"""
"""
frase = input("digite uma frase: ")

contacaracter = frase.replace(" ", "")
print(len(contacaracter))

quantos_a = frase.count("a")

print(quantos_a)
"""
"""
nome = input("digite o seu nome: ")

ultimaletra = nome.rfind("a")

primeiraletra = nome.find("a")

print(primeiraletra)
print(ultimaletra)
"""

