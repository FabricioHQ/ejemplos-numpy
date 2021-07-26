import numpy as np

# Crea un array bidimensional 5x5 con todos los valores
# cero. Usando el indexado de arrays, asigna 1 a todos
# los elementos de la última fila y 5 a todos los elementos
# de la primera columna. Finalmente, asigna el valor 100 a
# todos los elementos del subarray central 3x3 de la matriz
# de 5x5.

# Creamos el array de 5x5 de 0.
array = np.zeros((5, 5), dtype = int)

print(f'\n{array}')

# Reemplazamos la última fila con 1.
array[-1:,:] = 1

print(f'{array}')
# Reemplazamos la primera fila con 5
array[:1,:] = 5

print(f'{array}')
# Reemplazamos el subarray central 3x3 con 100.
# Este código reemplaza el centro de toda matriz
array[1:-1,1:-1] = 100

print(f'{array}')
# print(f'\n{array}\n')