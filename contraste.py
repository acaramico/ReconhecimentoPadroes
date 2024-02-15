from matplotlib import pyplot as plt
import numpy as np
import cv2

imagem = cv2.imread("gato.jpg")
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
contraste = cv2.equalizeHist(imagem)

cv2.imshow("Imagem Equalizada", contraste)
plt.figure()
plt.title("Histograma Equalizado")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.hist(contraste.ravel(), 256, [0,256])
plt.xlim([0,256])
plt.show()


cv2.imshow("Imagem Original", imagem)
plt.figure()
plt.title("Histograma Original")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.hist(imagem.ravel(), 256, [0,256])
plt.xlim([0,256])
plt.show()

