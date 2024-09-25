import cv2
import numpy as np

# Đọc ảnh
image = cv2.imread('picture1.jpg', cv2.IMREAD_GRAYSCALE)

# Áp dụng toán tử Sobel để tính gradient theo trục x và y
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)  # Gradient theo trục x
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)  # Gradient theo trục y

sobel_x = cv2.convertScaleAbs(sobel_x)
sobel_y = cv2.convertScaleAbs(sobel_y)

# Combine the two results
sobel_combined = cv2.bitwise_or(sobel_x, sobel_y)

edges = cv2.Canny(image, 100, 200)


# Hiển thị ảnh
cv2.imshow('Original Image', image)
# cv2.imshow('Sobel X', sobel_x)
# cv2.imshow('Sobel Y', sobel_y)
cv2.imshow('Sobel Combined', sobel_combined)
cv2.imshow('Canny',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
