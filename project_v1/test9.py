import cv2
import numpy as np

# Khai báo biến toàn cục để lưu trữ các tọa độ điểm chuột
ref_point = []
cropping = False


def click_and_crop(event, x, y, flags, param):
    global ref_point, cropping, frame_copy

    # Nếu sự kiện chuột là nhấn chuột trái, lưu điểm bắt đầu (x, y)
    if event == cv2.EVENT_LBUTTONDOWN:
        ref_point = [(x, y)]
        cropping = True

    # Khi di chuột và đang nhấn chuột trái, cập nhật điểm kết thúc (x, y) và vẽ hình chữ nhật
    elif event == cv2.EVENT_MOUSEMOVE:
        if cropping:
            frame_copy = frame.copy()
            cv2.rectangle(frame_copy, ref_point[0], (x, y), (0, 255, 0), 2)
            cv2.imshow("image", frame_copy)

    # Khi thả chuột trái, cập nhật điểm kết thúc và vẽ hình chữ nhật cố định
    elif event == cv2.EVENT_LBUTTONUP:
        ref_point.append((x, y))
        cropping = False
        cv2.rectangle(frame, ref_point[0], ref_point[1], (0, 255, 0), 2)


# Mở webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Không thể mở webcam.")
    exit()

cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop)

while True:
    ret, frame = cap.read()
    frame_copy = frame.copy()

    if not ret:
        print("Không thể nhận được khung hình.")
        break

    cv2.imshow("image", frame)

    key = cv2.waitKey(1) & 0xFF

    # Nhấn 'q' để thoát khỏi vòng lặp
    if key == ord('q'):
        break

    # Nhấn 'c' để chụp ảnh từ vùng đã khoanh và lưu lại
    if key == ord('c'):
        if len(ref_point) == 2:
            crop_img = frame[ref_point[0][1]:ref_point[1][1], ref_point[0][0]:ref_point[1][0]]

            # Sau khi chọn vùng, yêu cầu nhập văn bản
            text = input("Nhập văn bản cần chèn: ")
            height, width, _ = crop_img.shape
            font_scale = height / 10 / 30
            # Đặt các thuộc tính văn bản
            font = cv2.FONT_HERSHEY_SIMPLEX
            text_size = cv2.getTextSize(text, font, font_scale, 2)[0]

            # Đặt vị trí của văn bản, canh chỉnh văn bản ở giữa ảnh cắt
            text_x = (crop_img.shape[1] - text_size[0]) // 2
            text_y = (crop_img.shape[0] + text_size[1]) // 2

            # Vẽ văn bản lên ảnh cắt
            cv2.putText(crop_img, text, (text_x, text_y), font, font_scale, (255, 255, 255), 2, cv2.LINE_AA)

            # Hiển thị ảnh đã chèn văn bản và lưu lại
            cv2.imshow(f"Image with {text} ", crop_img)
            cv2.imwrite(f"image_with_{text}.jpg", crop_img)
            print("Đã lưu ảnh có văn bản.")

# Giải phóng webcam và đóng các cửa sổ
cap.release()
cv2.destroyAllWindows()
