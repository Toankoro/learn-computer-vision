import cv2
import numpy as np

# Khai báo biến toàn cục để lưu trữ các tọa độ điểm chuột
ref_point = []
cropping = False

def click_and_crop(event, x, y, flags, param):
    global ref_point, cropping

    # Nếu sự kiện chuột là nhấn chuột trái, lưu điểm bắt đầu (x, y)
    if event == cv2.EVENT_LBUTTONDOWN:
        ref_point = [(x, y)]
        cropping = True

    # Khi di chuột và nhấn chuột trái, cập nhật điểm kết thúc (x, y)
    elif event == cv2.EVENT_LBUTTONUP:
        ref_point.append((x, y))
        cropping = False

        # Vẽ hình chữ nhật trên vùng đã chọn
        cv2.rectangle(frame, ref_point[0], ref_point[1], (0, 255, 0), 2)
        cv2.imshow("image", frame)

# Mở webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Không thể mở webcam.")
    exit()

cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop)

while True:
    ret, frame = cap.read()

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
            cv2.imshow("Cropped Image", crop_img)
            cv2.imwrite("cropped_image.jpg", crop_img)
            print("Đã lưu ảnh khoanh vùng.")

# Giải phóng webcam và đóng các cửa sổ
cap.release()
cv2.destroyAllWindows()
