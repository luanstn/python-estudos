nome = input("Digite o seu nome: ")

minusculas = nome.lower()
maiusculas = nome.upper()

tiraespaco = nome.replace(" ", "")
contaletra = len(tiraespaco)

divide = nome.split()
primeironome = divide[0]

print(minusculas)
print(maiusculas)
print(contaletra)
print(primeironome) 