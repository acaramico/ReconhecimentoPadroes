import numpy as np
import cv2


imagem = cv2.imread('puffles.png')
(b, g, r) = cv2.split(imagem)
zeros = np.zeros(imagem.shape[:2], dtype = "uint8")

cv2.imshow("Original", imagem)
cv2.imshow("Vermelho", cv2.merge([zeros, zeros, r]))
cv2.imshow("Verde", cv2.merge([zeros, g, zeros]))
cv2.imshow("Azul", cv2.merge([b, zeros, zeros]))
cv2.imshow("Ciano", cv2.merge([b, g, zeros]))
cv2.imshow("Roxo", cv2.merge([b, zeros, r]))
cv2.imshow("Amarelo", cv2.merge([zeros, g, r]))


cv2.waitKey(99999)
