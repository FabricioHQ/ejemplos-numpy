import numpy as np

# Red convolucional numpy de 50x50 con un keernel de 3x3.
# Librería por defecto de python que para generar núemros aleatorios.
import random as rand

# Matriz numpy aleatorio de 50x50
I = np.array([[rand.randrange(2) for i in range(50)] for j in range(50)])
print(f'\n  Matriz base\n{I}')

# Matriz numpy aleatorio de 3x3
K = np.array([[rand.randrange(2) for i in range(3)] for j in range(3)])
print(f'\n\n  Kernel (Filtro)\n{K}')

def conv(matriz, kernel):
    # Creamos una matriz de 48x48 para la salida con 0.
    IK = np.zeros((matriz[0].size - kernel[0].size + 1,matriz[0].size - kernel[0].size + 1))
    print(f'{IK}')

    # Recorremos las matriz vacía y obtenemos sus posiciones.
    for i in range(IK[0].size):
        for j in range(IK[0].size):
            # Obetenemos la suma de la multiplicación con el kernel
            value = np.sum(matriz[i:i+3, j: j+3] * kernel)
            
            # Asignamos el valor en la posición i, j de la solución.
            IK[i,j] = value
    return IK

print(f'\n\n  Matriz resultante\n{conv(I, K)}\n')