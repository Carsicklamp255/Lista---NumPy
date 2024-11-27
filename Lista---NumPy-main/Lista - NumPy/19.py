import numpy as np

matriz_3x33 = np.random.randint(1, 10, size=(3, 33))

matriz_33x3 = np.random.randint(1, 10, size=(33, 3))

resultado_3x3 = np.dot(matriz_3x33, matriz_33x3)

media_linhas = np.mean(resultado_3x3, axis=1, keepdims=True)

resultado_final = resultado_3x3 - media_linhas

print("Matriz 3x33:")
print(matriz_3x33)
print("\nMatriz 33x3:")
print(matriz_33x3)
print("\nResultado da multiplicação (3x3):")
print(resultado_3x3)
print("\nMédia de cada linha:")
print(media_linhas)
print("\nResultado depois de subtrair a média de cada linha:")
print(resultado_final)