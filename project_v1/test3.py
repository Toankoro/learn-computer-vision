import os
import cv2
import numpy as np

input_folder = 'picture'
output_folder = 'shifted_pic'  # Tạo thư mục mới để lưu ảnh đã dịch chuyển

# Các giá trị dịch chuyển theo trục x và y
shift_x = 100  # Dịch sang phải 100 pixel
shift_y = 50   # Dịch xuống dưới 50 pixel

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

            # Ma trận dịch chuyển cho các hướng khác nhau
            M_shift_x = np.float32([[1, 0, shift_x], [0, 1, 0]])  # Dịch theo trục x
            M_shift_y = np.float32([[1, 0, 0], [0, 1, shift_y]])  # Dịch theo trục y
            M_shift_xy = np.float32([[1, 0, shift_x], [0, 1, shift_y]])  # Dịch theo cả trục x và y

            # Dịch chuyển ảnh theo trục x, y, và cả x, y
            shifted_x = cv2.warpAffine(image, M_shift_x, (width, height))
            shifted_y = cv2.warpAffine(image, M_shift_y, (width, height))
            shifted_xy = cv2.warpAffine(image, M_shift_xy, (width, height))

            # Hiển thị các ảnh đã dịch chuyển
            cv2.imshow('Shifted along X', shifted_x)
            cv2.imshow('Shifted along Y', shifted_y)
            cv2.imshow('Shifted along X and Y', shifted_xy)

            cv2.waitKey(0)
            cv2.destroyAllWindows()

            # Lưu các ảnh đã dịch chuyển vào thư mục đích
            cv2.imwrite(os.path.join(output_folder, 'shifted_x_' + filename), shifted_x)
            cv2.imwrite(os.path.join(output_folder, 'shifted_y_' + filename), shifted_y)
            cv2.imwrite(os.path.join(output_folder, 'shifted_xy_' + filename), shifted_xy)

            print(f"Đã dịch chuyển và lưu {filename} với các phương pháp dịch chuyển khác nhau.")
        else:
            print(f"Không thể đọc ảnh {filename}.")
    else:
        print(f"{filename} không phải là file ảnh.")

print("Hoàn thành việc dịch chuyển các ảnh.")
