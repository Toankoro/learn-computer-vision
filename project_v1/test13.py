import cv2
import numpy as np
import matplotlib.pyplot as plt

# Đọc ảnh màu
image_color = cv2.imread('anh.jpg')

# Chuyển đổi ảnh từ không gian màu BGR sang YUV
image_yuv = cv2.cvtColor(image_color, cv2.COLOR_BGR2YUV)

# Cân bằng lược đồ trên kênh Y (kênh độ sáng)
image_yuv[:, :, 0] = cv2.equalizeHist(image_yuv[:, :, 0])

# Chuyển đổi lại sang không gian màu BGR
equalized_image_color = cv2.cvtColor(image_yuv, cv2.COLOR_YUV2BGR)

# Tính lược đồ tần suất của kênh độ sáng trước và sau khi cân bằng
hist_original = cv2.calcHist([image_color], [0], None, [256], [0, 256])
hist_equalized = cv2.calcHist([equalized_image_color], [0], None, [256], [0, 256])

# Tạo cửa sổ hiển thị
plt.figure(figsize=(12, 8))

# Ảnh gốc
plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(image_color, cv2.COLOR_BGR2RGB))
plt.title('Ảnh gốc')
plt.axis('off')

# Lược đồ tần suất kênh độ sáng ảnh gốc
plt.subplot(2, 2, 2)
plt.plot(hist_original, color='black')
plt.title('Lược đồ tần suất - Ảnh gốc')
plt.xlim([0, 256])

# Ảnh sau khi cân bằng
plt.subplot(2, 2, 3)
plt.imshow(cv2.cvtColor(equalized_image_color, cv2.COLOR_BGR2RGB))
plt.title('Ảnh sau khi cân bằng')
plt.axis('off')

# Lược đồ tần suất kênh độ sáng ảnh sau khi cân bằng
plt.subplot(2, 2, 4)
plt.plot(hist_equalized, color='black')
plt.title('Lược đồ tần suất - Ảnh đã cân bằng')
plt.xlim([0, 256])

# Hiển thị tất cả trên cùng một cửa sổ
plt.tight_layout()
plt.show()
