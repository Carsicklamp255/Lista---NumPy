#Crie uma matriz quadrada 3x3 aleatória e calcule seus autovalores e autovetores.

import numpy as np

matriz = np.random.randint(0, 9, size=(3, 3))


autovalores, autovetores = np.linalg.eig(matriz)

print("Matriz:")
print(matriz)
print("\nAutovalores:")
print(autovalores)
print("\nAutovetores:")
print(autovetores)