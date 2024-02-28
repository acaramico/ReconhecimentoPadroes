import cv2
import numpy as np


imagem = cv2.imread('Tomates.jpg')
cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(cinza, (11,11), 0)

limiar, binarizada = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

bordas = cv2.Canny(binarizada, 70, 120)

contornos, hierarquia = cv2.findContours(bordas, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(imagem, contornos, -1, (0, 255, 0), 2)

ladoalado = np.vstack([
    np.hstack([cinza, blur]),
    np.hstack([binarizada, bordas])
])

cv2.imshow("passo a passo" + str(len(contornos)), ladoalado)
cv2.imshow("objetos encontrados na foto = " + str(len(contornos)), imagem)
cv2.waitKey(99999)

