"""
numero = int(input("Escreva o número: "))

base = int(input("escolha a base de conversão( 1 = binário 2 = octal 3 = hexadecimal): "))

if base == 1:
    print(bin(numero))
elif base == 2:
    print(oct(numero))
elif base == 3:
    print(hex(numero))

"""
"""
ler dois numero inteiros e compara e diz qual é o maior

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))

if num1 > num2:
    print(f"O {num1} é o maior valor")
elif num2 > num1:
    print(f"o {num2} é o maior valor")
else:
    print("não existe valor maior, os dois são iguais")
"""
"""
ler ano de nascimento e informa a idade e ver se vai se alistar e etc

anonascimento = int(input("Qual ano você nasceu? "))

compara = 2025 - anonascimento
anosfalta = 18 - compara
passouprazo = compara - 21

if compara < 18:
    print("você ainda vai se alistar")
    print(f"faltam {anosfalta} anos")
elif compara > 21:
    print(f"você passou do tempo de se alistar")
    print(f"você passou do prazo há {passouprazo} anos")
elif compara >= 18:
    print("é hora de se alistar")
"""

"""
programa que calcula a media de aluno

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite dua segunda nota: "))

media = (nota1 + nota2) / 2

if media > 7.0:
    print(f"você foi aprovado com {media:.2f} de media")
elif media < 5.0:
    print(f"Sua media foi {media:.2f}, você foi reprovado")
elif media >= 5.0:
    print(f"você ficou na recuperação com {media:.2f} de media")
"""
"""
ler o nascimento e diz de acordo com a idade qual categoria

nascimento = int(input("Digite seu ano de nascimento: "))

idade = 2025 - nascimento

if idade <= 9:
    print("mirim")
elif idade <= 14:
    print("infantil")
elif idade <= 19:
    print("junior")
elif idade == 20:
    print("senior")
elif idade > 20:
    print("master")
    """
"""
calcula imc de uma pessoa

altura = float(input("Digite sua altura: "))
peso = float(input("Digite o seu peso: "))

imc = peso / (altura * altura)

if imc <= 18.5:
    print("abaixo")
elif imc <= 25:
    print("peso ideal")
elif imc <= 30:
    print("sobrepeso")
elif imc <= 40:
    print("obesidade")
elif imc > 40:
    print("obesidade mórbida")

"""

