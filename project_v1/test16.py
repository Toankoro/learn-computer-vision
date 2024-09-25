import cv2
import numpy as np
import matplotlib.pyplot as plt

# Bước 1: Đọc ảnh và chuyển sang ảnh xám
img = cv2.imread('images.jpg', 0)  # Đọc ảnh đầu vào, 0 để chuyển ảnh sang ảnh xám

# Bước 2: Áp dụng biến đổi Fourier
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)  # Dịch chuyển các tần số thấp vào trung tâm

# Tính magnitude spectrum (phổ biên độ) để hiển thị
magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))

# Bước 3: Tạo mặt nạ lọc thông thấp hoặc thông cao
rows, cols = img.shape
crow, ccol = rows // 2, cols // 2  # Tọa độ trung tâm

# Tạo mặt nạ thông thấp, giữ lại các tần số thấp xung quanh tâm ảnh
mask = np.zeros((rows, cols, 2), np.uint8)
mask[crow-30:crow+30, ccol-30:ccol+30] = 1  # Khu vực giữ lại tần số thấp

# Áp dụng mặt nạ lên ảnh DFT đã shift
fshift = dft_shift * mask

# Bước 4: Biến đổi ngược Fourier để đưa ảnh về miền không gian
f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

# Bước 5: Hiển thị ảnh gốc, phổ biên độ và ảnh sau khi lọc
plt.figure(figsize=(12, 6))

plt.subplot(131), plt.imshow(img, cmap='gray')
plt.title('Ảnh gốc'), plt.axis('off')

plt.subplot(132), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Phổ biên độ'), plt.axis('off')

plt.subplot(133), plt.imshow(img_back, cmap='gray')
plt.title('Ảnh sau khi lọc thông thấp'), plt.axis('off')

plt.show()
