import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Không thể mở webcam")
    exit()
img_counter1 = 0
img_counter2 = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Không thể nhận khung hình từ webcam")
        break
    cv2.imshow('Webcam', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('c'):
        img_name = f"CVF24B21DCPT218HG{img_counter1}.jpg"
        cv2.imwrite(img_name, frame)
        print(f"Đã chụp và lưu hình ảnh: {img_name}")
        img_counter1 += 1
    if key == ord('t'):
        img_name = f"CVF24B21DCPT218HN{img_counter2}.jpg"
        cv2.imwrite(img_name, frame)
        print(f"Đã chụp và lưu hình ảnh: {img_name}")
        img_counter2 += 1
    elif key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
