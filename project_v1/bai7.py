import cv2
import numpy as np
img = cv2.imread('pic.png')
cv2.imshow('Original Image', img)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV Image', img_hsv)
cv2.imwrite('HSV Image.png', img_hsv)
b, g, r = cv2.split(img)
blue_img = cv2.merge([b, np.zeros_like(b), np.zeros_like(b)])

green_img = cv2.merge([np.zeros_like(g), g, np.zeros_like(g)])

red_img = cv2.merge([np.zeros_like(r), np.zeros_like(r), r])

cv2.imshow('Blue Channel', blue_img)
cv2.imshow('Green Channel', green_img)
cv2.imshow('Red Channel', red_img)
cv2.imwrite('blue_channel.png', blue_img)
cv2.imwrite('green_channel.png', green_img)
cv2.imwrite('red_channel.png', red_img)
h, s, v = cv2.split(img_hsv)
increase_value = 20
v = cv2.add(v, increase_value)

img_hsv_modified = cv2.merge([h, s, v])

img_bgr_modified = cv2.cvtColor(img_hsv_modified, cv2.COLOR_HSV2BGR)

cv2.imshow('Modified Image', img_bgr_modified)
cv2.imwrite('Modified Image.png', img_bgr_modified)
cv2.waitKey(0)
cv2.destroyAllWindows()


