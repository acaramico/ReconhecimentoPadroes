import numpy as np
import cv2
import matplotlib as plt
#%matplotlib inline

imagem = cv2.imread('selecao.jpg')
imagemGray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

face_frontal = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

face_recon = face_frontal.detectMultiScale(imagemGray, scaleFactor = 1.3, minNeighbors = 1)

for(x, y, w, h) in face_recon:
    cv2.rectangle(imagem, (x,y), (x+w, y+h), (0, 255, 0), 4)

cv2.imshow("Rostos Encontrados", imagem)

cv2.waitKey(9999)