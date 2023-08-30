import cv2
image = cv2.imread(r"C:/Users/vitta/Downloads/RGB.jpeg")
B,G,R = cv2.split(image)
cv2.imshow("Original",image)
cv2.imshow("Blue",B)
cv2.imshow("Green",G)
cv2.imshow("Red",R)
cv2.waitKey()
