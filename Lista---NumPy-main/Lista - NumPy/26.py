#Crie um array com 30 números inteiros aleatórios entre 0 e 10. Identifique os
#valores únicos e conte a frequência de cada valor
import numpy as np

arr = np.random.randint(0, 11, size = 30)
print("array:", arr)

valor_unico,valor_frequente = np.unique(arr, return_counts= True)

valores_unicos = valor_unico[valor_frequente == 1]
print("valores únicos: ", valores_unicos)
print("Valores Frenquentes: ", valor_frequente)
