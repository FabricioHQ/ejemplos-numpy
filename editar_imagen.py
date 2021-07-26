import numpy as np
import cv2


path = input('Coloque la ruta de su imagen: ')
print(path)
imagen = cv2.imread(path)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(imagen[0])