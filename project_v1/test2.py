import os
import cv2

input_folder = 'picture'
output_folder = 'resized_pic'  # Tạo thư mục mới để lưu ảnh đã resize

new_width = 700
new_height = 700

# Kiem tra va tao thu muc khi chua ton tai
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Duyet qua file anh trong thu muc
for filename in os.listdir(input_folder):

    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):

        img_path = os.path.join(input_folder, filename)

        image = cv2.imread(img_path)

        if image is not None:

            cv2.imshow('Original Image', image)

            # Resize anh voi noi suy khac nhau
            resized_linear = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)
            resized_cubic = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_CUBIC)
            resized_area = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)

            # Hien thi anh noi suy khac nhau
            cv2.imshow('Resized with INTER_LINEAR', resized_linear)
            cv2.imshow('Resized with INTER_CUBIC', resized_cubic)
            cv2.imshow('Resized with INTER_AREA', resized_area)

            cv2.waitKey(0)
            cv2.destroyAllWindows()

            cv2.imwrite(os.path.join(output_folder, 'linear_' + filename), resized_linear)
            cv2.imwrite(os.path.join(output_folder, 'cubic_' + filename), resized_cubic)
            cv2.imwrite(os.path.join(output_folder, 'area_' + filename), resized_area)

            print(f"Đã resize và lưu {filename} với các phương pháp nội suy khác nhau.")
        else:
            print(f"Không thể đọc ảnh {filename}.")
    else:
        print(f"{filename} không phải là file ảnh.")

print("Hoàn thành việc resize các ảnh.")