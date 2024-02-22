import cv2


imagem = cv2.imread('seoul.jpg')
cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Aplicar a binarização de Otsu
limiar, binarizada = cv2.threshold(cinza, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

print(limiar)
cv2.imshow('Imagem Binarizada', binarizada)
cv2.waitKey(9999)
