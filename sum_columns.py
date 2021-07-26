import numpy as np

a = np.arange(16).reshape((4, 4))
b = [[value * 4, 1 + value * 4, + 2 + value * 4, 3 + value * 4] for value in range(4)]

# Sumando los valores de cada columna
def sum_columns_numpy(m):
    # Axis = ejes, el axi 0 es igual a las columnas
    return np.sum(m, axis = 0)

def sum_columns_python(m):
    sum = []
    # De esta manera recorremos toda la matriz
    for i in range(len(m)):
        for j in range(len(m[0])):
            # Si es la primera vuelta, queremos agregar los valores
            # a la lista.
            # Sino, sumamos los valores en la posición j de la lista.
            if i == 0:
                sum.append(m[i][j])
            else:
                sum[j] += m[i][j]

    return sum

print(f'\nSuma de los valores de las columnas: numpy\n{sum_columns_numpy(a)}\n\nSuma de los valores de las columnas: python\n{sum_columns_python(b)}\n\n')