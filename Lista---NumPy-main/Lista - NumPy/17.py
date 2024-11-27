#.Crie uma matriz quadrada 3×3 aleatória. Calcule o determinante e, se
#possível, a inversa dessa matriz
import numpy as np

matriz = np.random.randint(1, 10, size=(3, 3))

determinante = np.linalg.det(matriz)

if determinante != 0:
    inversa = np.linalg.inv(matriz)
else:
    inversa = False

print("Matriz:")
print(matriz)
print("\nDeterminante:", determinante)

if inversa is not None:
    print("\nInversa da matriz:")
    print(inversa)
else:
    print("\nA matriz inversa não esxiste pois o determinante é zero.")