nome = input("Digite uma palavra: ")

tiraespaco = nome.replace(" ", "")
ler = len(tiraespaco)

inverter = tiraespaco[::-1]

if nome == inverter:
    print(f"a frase {nome} é um polindromo")
else:
    print(f"a frase {nome} não é um polindromo")
