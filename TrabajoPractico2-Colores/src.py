%matplotlib inline
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img_color = cv.imread('arandelas.bmp')
imgRGB = cv.cvtColor(img_color, cv.COLOR_BGR2RGB)

plt.figure(0)
plt.imshow(imgRGB)
plt.show()

img_muestra_marron = imgRGB[2120:2170,1370:1420,:]
img_muestra_azul = imgRGB[2230:2270,740:770,:]
img_muestra_celeste = imgRGB[1180:1230,870:910,:]
img_muestra_rojo = imgRGB[1400:1440,1610:1640,:]

lista_arandelas=[img_muestra_marron,img_muestra_azul,img_muestra_celeste,img_muestra_rojo]

for i in range(1,5):
    plt.figure(i)
    plt.imshow(lista_arandelas[i-1])
plt.show()

color_mean_marron, color_std_marron = cv.meanStdDev(img_muestra_marron)
color_mean_azul, color_std_azul = cv.meanStdDev(img_muestra_azul)
color_mean_celeste, color_std_celeste = cv.meanStdDev(img_muestra_celeste)
color_mean_rojo, color_std_rojo = cv.meanStdDev(img_muestra_rojo)

#mascara marron
mask = cv.inRange(imgRGB, color_mean_marron-color_std_marron*18,  color_mean_marron+color_std_marron*18)
img_segmentada_marron = cv.bitwise_and(imgRGB, imgRGB, mask=mask)

plt.figure(6)
plt.imshow(img_segmentada_marron)
plt.show()

#mascara azul
mask = cv.inRange(imgRGB, color_mean_azul-color_std_azul*12,  color_mean_azul+color_std_azul*12)
img_segmentada_azul = cv.bitwise_and(imgRGB, imgRGB, mask=mask)

plt.figure(7)
plt.imshow(img_segmentada_azul)
plt.show()

#mascara celeste
mask = cv.inRange(imgRGB, color_mean_celeste-color_std_celeste*13,  color_mean_celeste+color_std_celeste*13)
img_segmentada_celeste = cv.bitwise_and(imgRGB, imgRGB, mask=mask)

plt.figure(8)
plt.imshow(img_segmentada_celeste)
plt.show()

#mascara roja
mask = cv.inRange(imgRGB, color_mean_rojo-color_std_rojo*14,  color_mean_rojo+color_std_rojo*14)
img_segmentada_rojo = cv.bitwise_and(imgRGB, imgRGB, mask=mask)

plt.figure(9)
plt.imshow(img_segmentada_rojo)
plt.show()

img_HSV = cv.cvtColor(img_color, cv.COLOR_BGR2HSV)
plt.figure(10)
plt.imshow(img_HSV)

#mascara marron HSV
color_l_marron = (13,100,100)
color_u_marron = (15,255,255)

mask_marron = cv.inRange(img_HSV, color_l_marron,  color_u_marron)
img_segmentada_marron = cv.bitwise_and(imgRGB, imgRGB, mask=mask_marron)

plt.figure(11)
plt.imshow(img_segmentada_marron)
plt.show()

#mascara azul HSV
color_l_azul = (109,100,100)
color_u_azul = (118,255,255)

mask_azul = cv.inRange(img_HSV, color_l_azul,  color_u_azul)
img_segmentada_azul = cv.bitwise_and(imgRGB, imgRGB, mask=mask_azul)

plt.figure(12)
plt.imshow(img_segmentada_azul)
plt.show()

#mascara celeste HSV
color_l_celeste = (106,100,100)
color_u_celeste = (108,255,255)

mask_celeste = cv.inRange(img_HSV, color_l_celeste,  color_u_celeste)
img_segmentada_celeste = cv.bitwise_and(imgRGB, imgRGB, mask=mask_celeste)

plt.figure(13)
plt.imshow(img_segmentada_celeste)
plt.show()

#mascara roja HSV
color_l_rojo = (176,100,100)
color_u_rojo = (182,255,255)

mask_rojo = cv.inRange(img_HSV, color_l_rojo,  color_u_rojo)
img_segmentada_roja = cv.bitwise_and(imgRGB, imgRGB, mask=mask_rojo)

plt.figure(14)
plt.imshow(img_segmentada_roja)
plt.show()

#mascara azul ajustando S y V
color_l_azul_ajustada = (109,150,130)
color_u_azul_ajustada = (118,210,180)

mask_azul_ajustada = cv.inRange(img_HSV, color_l_azul_ajustada,  color_u_azul_ajustada)
img_segmentada_azul_ajustada = cv.bitwise_and(imgRGB, imgRGB, mask=mask_azul_ajustada)

plt.figure(16)
plt.imshow(img_segmentada_azul_ajustada)
plt.show()

#mascara celeste ajustando S y V
color_l_celeste_ajustada = (106,180,165)
color_u_celeste_ajustada = (108,230,225)

mask_celeste_ajustada = cv.inRange(img_HSV, color_l_celeste_ajustada,  color_u_celeste_ajustada)
img_segmentada_celeste_ajustada = cv.bitwise_and(imgRGB, imgRGB, mask=mask_celeste_ajustada)

plt.figure(15)
plt.imshow(img_segmentada_celeste_ajustada)
plt.show()
