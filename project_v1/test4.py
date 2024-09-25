import os
import cv2
import numpy as np

input_folder = 'picture'
output_folder = 'rotated_pic'  # Tạo thư mục mới để lưu ảnh đã quay

# Góc quay (độ)
angle_1 = 45  # Quay 45 độ
angle_2 = 90  # Quay 90 độ
angle_3 = 180 # Quay 180 độ

# Kiểm tra và tạo thư mục nếu chưa tồn tại
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Duyệt qua các file ảnh trong thư mục
for filename in os.listdir(input_folder):

    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):

        img_path = os.path.join(input_folder, filename)

        image = cv2.imread(img_path)

        if image is not None:

            cv2.imshow('Original Image', image)

            height, width = image.shape[:2]

            # Xác định tâm ảnh
            center = (width // 2, height // 2)

            # Ma trận quay cho các góc khác nhau
            M_rotate_1 = cv2.getRotationMatrix2D(center, angle_1, 1.0)  # Quay 45 độ
            M_rotate_2 = cv2.getRotationMatrix2D(center, angle_2, 1.0)  # Quay 90 độ
            M_rotate_3 = cv2.getRotationMatrix2D(center, angle_3, 1.0)  # Quay 180 độ

            # Quay ảnh với các góc khác nhau
            rotated_1 = cv2.warpAffine(image, M_rotate_1, (width, height))
            rotated_2 = cv2.warpAffine(image, M_rotate_2, (width, height))
            rotated_3 = cv2.warpAffine(image, M_rotate_3, (width, height))

            # Hiển thị các ảnh đã quay
            cv2.imshow(f'Rotated by {angle_1} degrees', rotated_1)
            cv2.imshow(f'Rotated by {angle_2} degrees', rotated_2)
            cv2.imshow(f'Rotated by {angle_3} degrees', rotated_3)

            cv2.waitKey(0)
            cv2.destroyAllWindows()

            # Lưu các ảnh đã quay vào thư mục đích
            cv2.imwrite(os.path.join(output_folder, f'rotated_{angle_1}deg_' + filename), rotated_1)
            cv2.imwrite(os.path.join(output_folder, f'rotated_{angle_2}deg_' + filename), rotated_2)
            cv2.imwrite(os.path.join(output_folder, f'rotated_{angle_3}deg_' + filename), rotated_3)

            print(f"Đã quay và lưu {filename} với các góc quay {angle_1}, {angle_2}, {angle_3}.")
        else:
            print(f"Không thể đọc ảnh {filename}.")
    else:
        print(f"{filename} không phải là file ảnh.")

print("Hoàn thành việc quay các ảnh.")
