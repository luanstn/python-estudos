valorcasa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o seu salário: "))
anos = int(input("Digite em quantos anos você pagaria: "))

meses = anos * 12

mensal = valorcasa / meses


if mensal < salario * 0.3:
    print("Seu emprestimo foi aprovado!")
elif mensal > salario * 0.3:
    print("seu emprestimo foi negado!")

print(f"você terá que pagar: {mensal:.2f} reais")

