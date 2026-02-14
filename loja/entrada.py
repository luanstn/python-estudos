def ler_dinheiro(valor):
    while True:
        entrada = input(valor).replace(",", ".").strip()
        try:
            valor = float(entrada)
            return valor
        except ValueError:
            print(f"você digitou errado, tente novamente")


