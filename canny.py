import numpy as np
import cv2


imagem = cv2.imread('gato.jpg')
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(imagem, (11,11), 0)

cannyA = cv2.Canny(blur, 20, 120)
cannyB = cv2.Canny(blur, 70, 200)

final = np.vstack([
    np.hstack([cannyA, cannyB]),
    np.hstack([imagem, blur])
])

cv2.imshow("Detector de bordas canny", final)
cv2.waitKey(99999)