from treinochat import operacoes

a = int(input("digite o primeiro valor: "))
b = int(input("digite o segundo valor: "))
print(f"A soma de {a} + {b} é: {operacoes.soma(a, b)}")
print(f"A multiplicação é: {operacoes.multiplicacao(a, b)}")
print(f"A subtração é: {operacoes.subtracao(a, b)}")
print(f"A divisão é: {operacoes.divisao(a, b)}")