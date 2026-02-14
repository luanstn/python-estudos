"""
import random
adivinhar = random.randint(1,5)
tentativa = int(input("escolha um numero de 1 à 5: "))
if adivinhar == tentativa:
    print(f"você acertou!! o numero era {tentativa}")
else:
        print(f"errou!! o numero era {adivinhar}")

     """
"""
velocidade = int(input("velocidade: "))
multa = velocidade - 80
reais = multa * 7

if velocidade > 80:
    print(f"você foi multado no valor de {reais:.2f} reais")
else:
    print("passou de boa!")
"""
"""
numero = int(input("numero: "))

if numero % 2 == 0:
    print(f"o numero {numero} é par")
else :
    print("esse número é impar")
"""
"""
distancia = int(input("qual a distância da viagem que voce deseja fazer? "))

valor1 = distancia * 0.5
valor2 = distancia * 0.45

if distancia  <= 200:
    print(f"o valor será: {valor1:.2f}")
else:
    print(f"0 valor será: {valor2:.2f}")
"""
"""
ano = (int(input("qual ano você está? ")))

verifica = ano % 4 == 0 and ano % 400 == 0

nbissexto = ano % 100 == 0 and ano % 400 != 0


if verifica:
    print("esse ano é bissexto")
else:
    print("esse ano não é bissexto")
"""
"""
num1 = int(input("numero1: "))
num2 = int(input("numero2: "))
num3 = int(input("numero3: "))

maior = num1
if num1 > num2:
    maior = num2
elif num3 > maior:
    maior = num3

menor = num1
if num1 < num2:
    menor = num2
elif num3 < menor:
    menor = num3

print(f"O número maior é {maior} e o menor é {menor}")

"""
"""
salario = float(input("Digite o seu salario: "))

if salario > 1.250:
    aumento = salario * 1.10
    print(f"O salario é de {aumento:.2f}")
else:
    aumento = salario * 1.15
    print(f"o salário é de R$ {aumento:.2f}")
    """

