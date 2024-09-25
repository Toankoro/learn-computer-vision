import os
import cv2
import numpy as np

input_folder = 'picture'
output_folder = 'affine_transformed_pic'  # Tạo thư mục mới để lưu ảnh sau khi biến đổi affine

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

            # Điểm ban đầu trên ảnh gốc
            pts1 = np.float32([[50, 50], [200, 50], [50, 200]])

            # Điểm biến đổi đích trên ảnh mới
            pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

            # Tạo ma trận biến đổi affine
            M_affine = cv2.getAffineTransform(pts1, pts2)

            # Áp dụng phép biến đổi affine
            affine_transformed = cv2.warpAffine(image, M_affine, (width, height))

            # Hiển thị ảnh đã biến đổi affine
            cv2.imshow('Affine Transformed Image', affine_transformed)

            cv2.waitKey(0)
            cv2.destroyAllWindows()

            # Lưu ảnh sau khi biến đổi affine
            cv2.imwrite(os.path.join(output_folder, 'affine_' + filename), affine_transformed)

            print(f"Đã áp dụng phép biến đổi affine và lưu {filename}.")
        else:
            print(f"Không thể đọc ảnh {filename}.")
    else:
        print(f"{filename} không phải là file ảnh.")

print("Hoàn thành việc áp dụng phép biến đổi affine cho các ảnh.")
