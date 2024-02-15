import numpy as np
import cv2


imagem = cv2.imread('gato.jpg')
imagem = cv2.GaussianBlur(imagem, (13,13), 0) #parametros sempre impares!!!

cv2.imshow("Imagem Suavi", imagem)


cv2.waitKey(999)