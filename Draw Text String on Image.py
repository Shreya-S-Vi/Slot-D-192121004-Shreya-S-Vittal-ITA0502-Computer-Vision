import cv2
image = cv2.imread("C:/USers/vitta/Desktop/Bird.jpg")
text = "Bird"
coordinates = (50,50)
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
color = (255,0,0)
thickness = 2
image = cv2.putText(image,text,coordinates,font,fontScale,color,thickness,cv2.LINE_AA)
cv2.imshow("Text",image)
