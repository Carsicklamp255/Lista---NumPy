#Crie uma matriz 5×5 contendo os números inteiros de 1 a 25. Extraia a
#submatriz formada pelas linhas 2 a 4 e pelas colunas 2 a 4.
import numpy as np

matriz_5x5 = np.arange(1, 26).reshape(5, 5)
print("Matriz 5x5:\n", matriz_5x5)

submatriz = matriz_5x5[1:4, 1:4]  
print("\nSubmatriz:\n", submatriz)