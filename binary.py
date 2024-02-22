import numpy as np
import cv2
#import mahotas


imagem = cv2.imread('gato.jpg')
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
imagemNova = imagem.copy()

#thresholder fixo
ret, bin = cv2.threshold(imagem, 160, 255, cv2.THRESH_BINARY)
cv2.imshow("Binarização de imagem por thresholder", bin)

#OTSU
T = mahotas.thresholding.otsu(imagemNova)
print(T)
binNova = imagemNova.copy()
binNova[binNova > T] = 255
binNova[binNova < 255] = 0


cv2.waitKey(9999)