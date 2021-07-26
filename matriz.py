import numpy as np

# Creación de matrices en Numpy y Python

matriz_numpy = np.arange(16).reshape((4, 4))
matriz_python = [[value * 4, 1 + value * 4, + 2 + value * 4, 3 + value * 4] for value in range(4)]

print(f'\nMatriz con Numpy\n{matriz_numpy}\n')
print(f'\nMatriz con Python\n{matriz_python}\n')