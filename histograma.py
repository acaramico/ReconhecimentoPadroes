from matplotlib import pyplot as plt
import cv2

img = cv2.imread(('gato.jpg'))
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.imshow("Imagem RGB", img)

canais = cv2.split(img)
color = ("b", "g", "r")

plt.figure()
plt.title("Histograma RGB")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")


for(canal, cor) in zip(canais, color):
    hist = cv2.calcHist([canal], [0], None, [256], [0, 256])
    plt.plot(hist, color = cor)
    plt.xlim([0, 256])

plt.show()
