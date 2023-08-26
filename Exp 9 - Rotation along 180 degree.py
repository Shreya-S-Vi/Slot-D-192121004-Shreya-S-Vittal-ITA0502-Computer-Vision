import cv2
path = r"C:/Users/vitta/Desktop/Bird.jpg"
src = cv2.imread(path)
window_name = 'Image rotated along 180 degrees'
image = cv2.rotate(src, cv2.ROTATE_180)
cv2.imshow(window_name, image)
cv2.waitKey(0)
