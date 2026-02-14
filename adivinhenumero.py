import random

sorteio = random.randint(1, 20)
acertou = False

while not acertou:
    chute = int(input("digite um numero de 1 a 20: "))

    if chute == sorteio:
        print("Você acertou!!")
        acertou = True
    elif chute  > sorteio:
        print("O seu chute foi maior")
    else:
        print("o seu chute foi menor")


