from moedas import moedas

p = float(input("Digite o preço R$: "))
print(f"A metade de {p} é {moedas.metade(p, True)}")
print(f"O dobro de {p} é {moedas.dobro(p, True)}")
print(f"O aumento de {p} em 10% da o valor {moedas.aumentar(p,10, True)}")
print(f"A diminuição de {p} em 10% da o valor {moedas.diminui(p,10, True)}")