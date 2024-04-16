import cv2

# Leia a imagem
img = cv2.imread("butterfly.jpg")

# Exiba a imagem colorida
cv2.imshow("Imagem Original Colorida",img)

print(img)
# Converta a imagem colorida para escala de cinza
gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) 

# Exiba a imagem em escala de cinza
cv2.imshow("Imagem em escala de cinza",gray_img)


#print(gray_img)

# Mantem a janela aberta por tempo indeterminado
cv2.waitKey()
