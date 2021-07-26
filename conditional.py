import numpy as np

# Crea un array de 100 números aleatorios con valores de
# -100 a +100. Usando arrays de booleanos crea otros arrays
# que contengan los positivos, los negativos y los mayores
# de 50 de ese array.

# Creamos el array de 100 elementos de entre -100 hasta 100.
array = np.linspace(-100, 100, 100)
print(array)

# Usamos una condicional. No devolverá un array booleano
mayores50 = array > 50
print(f'\n{mayores50}')
positivos = array >= 0
print(f'\n{positivos}')
negativos = array < 0
print(f'\n{negativos}')