import cv2
import numpy as np
img = cv2.imread(r"C:/Users/vitta/Desktop/Bird.jpg",0)
equ = cv2.equalizeHist(img)
res = np.hstack((img, equ))
cv2.imshow('img', res)
cv2.waitKey(0)
