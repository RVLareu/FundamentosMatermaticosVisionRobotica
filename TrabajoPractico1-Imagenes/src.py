%matplotlib inline
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread(’Estrellas.bmp’)

print(’Estructura de la imagen: {}’.format(img.shape))
print(’Cantidad total de pixeles: {}’.format(img.size))
print(’Tipo de dato de cada pixel: {}’.format(img.dtype))

if len(img.shape)==3:
  print(’Imagen COLOR’)
else:
  print(’Imagen BW’)
plt.imshow(img[...,::-1])

imgGray = cv.imread(’Estrellas.bmp’,cv.IMREAD_GRAYSCALE)
plt.imshow(imgGray, cmap=’gray’, vmin=0, vmax=255)
plt.show()

posicionesMaximos = []
maximoValor = 0;

for fila in range(0,img.shape[0]):
  for columna in range (0,img.shape[1]):

    pixel = imgGray.item(fila,columna)

    if (pixel == maximoValor):
      posicion = (fila,columna)
      posicionesMaximos.append(posicion)

    if (pixel > maximoValor):
      maximoValor = pixel;
      posicionesMaximos = []
      posicion = (fila,columna)
      posicionesMaximos.append(posicion)

for posicion in posicionesMaximos:
  cv.circle(img, posicion, 15, (0,0,255), thickness=5, lineType=8)
plt.imshow(img[...,::-1])
