import cv2
import matplotlib.pyplot as plt

imageObj = cv2.imread(r"C:/Users/vitta/Desktop/Bird.jpg")
plt.axis("off")
plt.title("Original image")
plt.imshow(cv2.cvtColor(imageObj,cv2.COLOR_BGR2RGB))
plt.show()

blue_color = cv2.calcHist([imageObj],[0],None,[256],[0,256])
red_color = cv2.calcHist([imageObj],[1],None,[256],[0,256])
green_color = cv2.calcHist([imageObj],[2],None,[256],[0,256])

plt.subplot(3,1,1)
plt.title("Histogram of Blue")
plt.hist(blue_color,color="blue")

plt.subplot(3,1,2)
plt.title("Histogram of Green")
plt.hist(green_color,color="green")

plt.subplot(3,1,3)
plt.title("Histogram of Red")
plt.hist(red_color,color="red")

plt.tight_layout()
plt.show()

plt.title("Histogram of all RGB colors")
plt.hist(blue_color,color="blue")
plt.hist(green_color,color="green")
plt.hist(red_color,color="red")
plt.show()

