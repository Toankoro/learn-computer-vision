import os
import cv2
import numpy as np

input_folder = 'picture'
output_folder = 'perspective_transformed_pic'  # Tạo thư mục mới để lưu ảnh sau khi biến đổi phối cảnh

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

            # Điểm gốc trên ảnh gốc (theo chiều trái trên, phải trên, trái dưới, phải dưới)
            pts1 = np.float32([[100, 100], [300, 100], [100, 300], [300, 300]])

            # Điểm đích trên ảnh mới (theo chiều tương ứng với pts1 nhưng ở các vị trí khác)
            pts2 = np.float32([[0, 50], [350, 50], [100, 350], [300, 350]])

            # Tạo ma trận biến đổi phối cảnh
            M_perspective = cv2.getPerspectiveTransform(pts1, pts2)

            # Áp dụng phép biến đổi phối cảnh
            perspective_transformed = cv2.warpPerspective(image, M_perspective, (width, height))

            # Hiển thị ảnh đã biến đổi phối cảnh
            cv2.imshow('Perspective Transformed Image', perspective_transformed)

            cv2.waitKey(0)
            cv2.destroyAllWindows()

            # Lưu ảnh sau khi biến đổi phối cảnh
            cv2.imwrite(os.path.join(output_folder, 'perspective_' + filename), perspective_transformed)

            print(f"Đã áp dụng phép biến đổi phối cảnh và lưu {filename}.")
        else:
            print(f"Không thể đọc ảnh {filename}.")
    else:
        print(f"{filename} không phải là file ảnh.")

print("Hoàn thành việc áp dụng phép biến đổi phối cảnh cho các ảnh.")
