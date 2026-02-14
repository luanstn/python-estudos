def leiaint(a):

    while True:
        valor = input(a)

        try:
            valor = int(valor)
            return valor
        except ValueError:
            print(f"o valor não é inteiro, tente novamente.")

def leiafloat(b):
    while True:
        valor = input(b).replace(',', '.')

        try:
            valor = float(valor)
            return valor

        except ValueError:
            print("o valor não é decimal, tente novamente.")
