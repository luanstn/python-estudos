from utils import moeda
from utils import validacao
from utils import numeros
from utils import texto

numero = validacao.leiaint("digite o número: ")
dobro = numeros.dobro(numero)
dobro_formatado = moeda.moeda(dobro)
print(dobro_formatado)

print(f"dobro formatado: {moeda.moeda(numeros.dobro(numero))}")