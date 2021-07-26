import numpy as np

a = np.arange(16).reshape((4, 4))
b = [[value * 4, 1 + value * 4, + 2 + value * 4, 3 + value * 4] for value in range(4)]

def sum_diag_invert_python(m):
    sum = 0
    for i in range(len(m)):
        sum += m[i][-1 - i]

    return sum

def sum_diag_invert_numpy(m):
    m = np.fliplr(m)
    return np.trace(m)

print(f'\nSuma de la diagonal inversa de la matriz: numpy\n{sum_diag_invert_numpy(a)}\n\nSuma de la diagonal inversa de la matriz: python\n{sum_diag_invert_python(b)}\n\n')