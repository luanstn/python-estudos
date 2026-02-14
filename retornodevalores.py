"""
def soma(a = 0, b = 0, c = 0):
    s = a + b + c
    return s

r1 = soma(5, 2, 3)
r2 = soma(2, 2)
r3 = soma(6)

print(f"os resultados foram {r1}, {r2}, {r3}")
"""
"""
def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input("Digite um número:"))
print(f"o fatorial de {n} é igual a {fatorial(n)}")

f1 = fatorial(7)
f2 = fatorial(5)
f3 = fatorial()
"""
"""
def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

f1 = fatorial(4)
f2 = fatorial(5)
f3 = fatorial()
print(f"Os resultados foram {f1}, {f2}, {f3}")
"""
"""
def par(n = 0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input("Digite um numero:"))
if par(num):
    print("é par!")
else:
    print("não é par!")
"""
"""
RETORNA A IDADE DE ACORDO COM O ANO DE NASCIMENTO E DIZ SE PODE VOTAR OU NÃO

def voto(ano):
    idade = 2025 - ano
    return idade

n = int(input("Digite o ano de nascimento:"))
idade = voto(n)

if idade < 18:
    print("não vota")
elif idade >= 18 and idade < 65:
    print("voto obrigatorio")
elif idade >= 65:
    print("voto opcional")
"""
"""
def fatorial(n = 1, show = False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print(" x ", end=' ')
            else:
                print(" = ", end=' ')
        f *= c
    return f

print(fatorial(5, True))

"""

def ficha(jogador = "<desconhecido>", gols = 0):
    ficha = print(f"O jogador {jogador} fez {gols} gol(s) no campeonato.")

n = str(input("Digite o nome do jogador: "))
s = str(input("Digite a quantidade de gols: "))

if s.isnumeric():
    gols = int(s)
else:
    s = 0

if n.strip() == '':
    ficha(gols = s)
else:
    ficha(n, s)