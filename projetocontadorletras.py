nome = input("digita uma frase:")

tiraespaco = (nome.replace(" ", ""))
contaletra = len(tiraespaco)

contpalavra = nome.split()
contarpalavras = len(contpalavra)

print(f"A frase tem {contaletra} letras")
print(f"A frase tem {contarpalavras} palavras")