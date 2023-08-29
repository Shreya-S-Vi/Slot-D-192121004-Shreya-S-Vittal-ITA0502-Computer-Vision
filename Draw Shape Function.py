import numpy as np
import cv2

#rectangle
img = np.zeros((400,400,3),dtype="uint8")
cv2.rectangle(img,(30,30),(300,200),(0,255,255),5)

#square
img2 = np.zeros((400,400,3),dtype="uint8")
cv2.rectangle(img2,(30,30),(300,300),(255,255,0),5)

#line
img3 = np.zeros((400,400,3),dtype="uint8")
cv2.line(img3,(20,160),(100,160),(0,255,0),5)

#circle
img4 = np.zeros((400,400,3),dtype="uint8")
cv2.circle(img4,(200,200),80,(255,255,255),5)
cv2.imshow("circle",img4)

cv2.imshow("rectangle",img)
cv2.imshow("square",img2)
cv2.imshow("line",img3)
cv2.imshow("circle",img4)
cv2.waitKey()
