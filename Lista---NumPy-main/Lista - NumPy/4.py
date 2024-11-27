#Crie um array de 20 números aleatórios entre 0 e 1. Calcule a média, o
#desvio padrão, o valor máximo e o mínimo desse array.
import numpy as np
def calculos(array):

    media = np.mean(array)
    desvio_padrao = np.std(array)
    valor_maximo = np.max(array)
    valor_minimo = np.min(array)
    return media, desvio_padrao, valor_maximo, valor_minimo

array = np.random.randint(0, 2, size=20)
media, desvio_padrao, valor_maximo, valor_minimo = calculos(array)

print("Array:", array)
print("Média:", media)
print("Desvio padrão:", desvio_padrao)
print("Valor máximo:", valor_maximo)
print("Valor mínimo:", valor_minimo)
