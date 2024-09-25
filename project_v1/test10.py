import cv2
import numpy as np

# Khai báo biến toàn cục để lưu trữ các tọa độ điểm chuột
ref_point = []
cropping = False
crop_img = np.zeros((480, 640, 3), dtype=np.uint8)
text = ''
objects_info = []
count=0
name=''
def click_and_crop(event, x, y, flags, param):
    global ref_point, cropping, frame_copy

    # Nếu sự kiện chuột là nhấn chuột trái, lưu điểm bắt đầu (x, y)
    if event == cv2.EVENT_LBUTTONDOWN:
        ref_point = [(x, y)]
        cropping = True

    # Khi di chuột và đang nhấn chuột trái, cập nhật điểm kết thúc (x, y) và vẽ hình chữ nhật tạm thời
    elif event == cv2.EVENT_MOUSEMOVE:
        if cropping:
            frame_copy = frame.copy()  # Sao chép khung hình để vẽ tạm
            cv2.rectangle(frame_copy, ref_point[0], (x, y), (0, 255, 0), 2)
            cv2.imshow("image", frame_copy)

    # Khi thả chuột trái, cập nhật điểm kết thúc và vẽ hình chữ nhật cố định
    elif event == cv2.EVENT_LBUTTONUP:
        ref_point.append((x, y))
        cropping = False
        cv2.rectangle(frame, ref_point[0], ref_point[1], (0, 255, 0), 2)
        cv2.imshow("image", frame)


# Tải ảnh từ file thay vì từ webcam
image_path = "pictest.jpg"  # Đường dẫn tới ảnh của bạn
frame = cv2.imread(image_path)

if frame is None:
    print("Không thể tải ảnh.")
    exit()

cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop)

# Hiển thị ảnh đã tải
while True:

    cv2.imshow("image", frame)
    key = cv2.waitKey(1) & 0xFF

    # Nhấn 'q' để thoát khỏi vòng lặp
    if key == ord('q'):
        break

    # Nhấn 'c' để cắt ảnh từ vùng đã chọn và lưu lại
    if len(ref_point) == 2 and not text:
        # Đảm bảo tọa độ nằm trong phạm vi ảnh
        x1, y1 = ref_point[0]
        x2, y2 = ref_point[1]

        # Giới hạn tọa độ trong kích thước của ảnh
        x1 = max(0, min(x1, frame.shape[1] - 1))
        y1 = max(0, min(y1, frame.shape[0] - 1))
        x2 = max(0, min(x2, frame.shape[1] - 1))
        y2 = max(0, min(y2, frame.shape[0] - 1))

        # Đảm bảo rằng điểm bắt đầu nhỏ hơn điểm kết thúc
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)

        # Kiểm tra kích thước vùng cắt, bỏ qua nếu vùng cắt trống
        if x2 - x1 > 0 and y2 - y1 > 0:
            crop_img = frame[y1:y2, x1:x2]

            # Kiểm tra xem vùng cắt có hợp lệ không trước khi lưu
            if crop_img.size != 0:  # Kiểm tra nếu vùng ảnh cắt không trống
                text = ''
                label = ''
        if key == ord('h'):
            text = 'con nguoi'
            name = 'HH'
        elif key == ord('x'):
            text = 'xe may'
            name = 'HX'
        elif key == ord('o'):
            text = 'o to'
            name='HO'
        elif key == ord('m'):
            text = 'meo'
            name='HM'
        elif key == ord('n'):
            text = 'nha'
            name = 'HN'
        if text:
            label = text
            obj_info = {
                "label": label,
                "position": {
                    "x1": x1,
                    "y1": y1,
                    "x2": x2,
                    "y2": y2
                }
            }
            objects_info.append(obj_info)

            # Tính toán chiều cao của ảnh đã cắt
            height, width, _ = crop_img.shape
            font_scale = height / 5 / 30
            # Đặt các thuộc tính văn bản
            font = cv2.FONT_HERSHEY_SIMPLEX
            text_size = cv2.getTextSize(text, font, font_scale, 2)[0]

            # Đặt vị trí của văn bản, canh chỉnh văn bản ở giữa ảnh cắt
            text_x = (crop_img.shape[1] - text_size[0]) // 2
            text_y = (crop_img.shape[0] + text_size[1]) // 2
            # Vẽ văn bản lên ảnh cắt
            cv2.putText(crop_img, text, (text_x, text_y), font, font_scale, (255, 255, 255), 2, cv2.LINE_AA)

            # Hiển thị ảnh đã chèn văn bản và lưu lại
            count=count+1
            cv2.imwrite(f"{name}{count}.jpg", crop_img)
            print("Đã lưu ảnh có văn bản.")
            text=''
with open('data.txt', 'w') as f:  # Sử dụng 'w' để ghi đè file
    for obj in objects_info:
        f.write(f"Tên file ảnh gốc: {image_path}\n")
        f.write(f"Loại đối tượng: {obj['label']}\n")
        f.write(f"Vị trí đối tượng: {obj['position']['x1']}, {obj['position']['y1']} -> {obj['position']['x2']}, {obj['position']['y2']}\n")
        f.write("\n")
# Đóng các cửa sổ
cv2.destroyAllWindows()
