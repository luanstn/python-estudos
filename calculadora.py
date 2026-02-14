import math

num1 = float(input("digite um numero: "))
operacao = input("digite subtração = +, divisão = / ,subtrair = -, multiplicar = * ")
num2 = float(input("digite um numero: "))

if operacao == "+":
    print(num1 + num2)
elif operacao == "-":
    print(num1 - num2)
elif operacao == "*":
    print(num1 * num2)
elif operacao == "/":
    print(num1 / num2 )
