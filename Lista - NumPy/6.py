#Crie um array de números inteiros aleatórios entre 1 e 100 (tamanho 20).
#Substitua todos os valores maiores que 50 por 0.

import numpy as np

arr = np.random.randint(1, 100, size = 20)
filter_arr = arr > 50
newarr = arr[filter_arr]

print(newarr)
