import cv2
import mediapipe as mp
import requests
import time

# Khởi tạo MediaPipe Pose
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Cấu hình Camera và Server
cap = cv2.VideoCapture(0)
API_URL = "http://localhost:8080/fall"
last_status = None
COOLDOWN = 2  # Giây giữa các lần gửi status

def send_status(status):
    try:
        res = requests.post(API_URL, json={
            "status": status,
            "username": "admin"
        }, timeout=2)
        print(f">>> SEND: {status} | CODE: {res.status_code}")
    except Exception as e:
        print(">>> ERROR SENDING TO SERVER:", e)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Chuyển đổi màu từ BGR sang RGB cho MediaPipe
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(image_rgb)

    fall_detected = False

    if results.pose_landmarks:
        # Vẽ các điểm khớp xương lên màn hình để dễ quan sát
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Lấy danh sách các điểm tọa độ
        landmarks = results.pose_landmarks.landmark
        
        # Lấy tọa độ Y của Mũi (Nose) và Hông (Mid Hip - trung bình 2 bên)
        # Lưu ý: Trong MediaPipe, trục Y chạy từ trên xuống (0 là đỉnh, 1 là đáy)
        nose_y = landmarks[mp_pose.PoseLandmark.NOSE].y
        left_hip_y = landmarks[mp_pose.PoseLandmark.LEFT_HIP].y
        right_hip_y = landmarks[mp_pose.PoseLandmark.RIGHT_HIP].y
        avg_hip_y = (left_hip_y + right_hip_y) / 2

        # Logic: Nếu Mũi thấp hơn Hông (tọa độ Y lớn hơn) => FALL
        if nose_y > avg_hip_y:
            fall_detected = True

    # Xử lý trạng thái gửi về Spring Boot
    if fall_detected and last_status != "FALL":
        print("ALERT: FALL DETECTED!")
        send_status("FALL")
        last_status = "FALL"
    elif not fall_detected and last_status != "SAFE":
        print("STATUS: SAFE")
        send_status("SAFE")
        last_status = "SAFE"

    # Hiển thị lên màn hình
    cv2.putText(frame, f"Status: {last_status}", (10, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0) if not fall_detected else (0, 0, 255), 2)
    cv2.imshow("Fall Detection System", frame)

    # Nhấn 'ESC' để thoát
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()