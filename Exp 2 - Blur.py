import cv2
path=r"C:/Users/vitta/Desktop/Bird.jpg"
img=cv2.imread(path)
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(7,7),0)
cv2.imshow("img Blur",imgBlur)
cv2.waitKey(0)
