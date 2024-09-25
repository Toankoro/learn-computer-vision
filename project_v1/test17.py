import cv2
import numpy as np

# Bước 1: Đọc ảnh và chuyển sang ảnh xám
img = cv2.imread('picture2.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Bước 2: Làm mờ ảnh để giảm nhiễu
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Bước 3: Ngưỡng hóa ảnh để chuyển thành ảnh nhị phân
_, thresh = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)

# Bước 4: Phát hiện đường bao
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Bước 5: Vẽ các đường bao trên ảnh gốc
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)  # Vẽ tất cả đường bao với màu xanh lá

# Hiển thị kết quả
cv2.imshow('Contours', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
