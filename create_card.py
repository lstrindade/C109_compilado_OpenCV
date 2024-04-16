import cv2

img = cv2.imread("poster.jpg")

rocket = img[120:360, 400:500]

img[0:240, 500:600] = rocket

text_to_show = "Houston we have a problem..."




cv2.imshow("resultado",img)

###### ATIVIDADE ADICIONAL ####

# cv2.imwrite("Greetings.jpg",img)

###############################

cv2.waitKey(0)
