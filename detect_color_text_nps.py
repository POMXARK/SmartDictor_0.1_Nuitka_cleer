import cv2
import numpy as np

img = cv2.imread("HZ3Te.jpg")
imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 255, 255])
mask_blue = cv2.inRange(imghsv, lower_blue, upper_blue)
contours, _ = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
im = np.copy(img)
cv2.drawContours(im, contours, -1, (0, 255, 0), 1)
cv2.imwrite("contours_blue.png", im)

pc = (40, 0, 165), (255, 255, 255)  # голубой текст
npc = (0, 70, 135), (61, 225, 240)  # желтый текст
