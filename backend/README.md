# Backend - Fall Detection API

Backend scaffold cho dự án **Camera AI báo cáo người bị ngã**.

## 1) Khuyên dùng môi trường nào?
### Khuyên dùng nhất cho dự án này
- **Python 3.11 + venv**
- Lý do:
  - nhẹ hơn Conda
  - dễ deploy FastAPI hơn
  - đơn giản cho sinh viên
  - đủ tốt cho stack hiện tại: FastAPI + OpenCV + MediaPipe + scikit-learn

### Khi nào dùng Conda?
Conda có ích hơn nếu bạn:
- làm deep learning nặng
- có nhiều xung đột binary package
- muốn quản lý môi trường data science theo kiểu notebook/ML riêng

Với dự án này:
- **venv là lựa chọn chính**
- **Conda là lựa chọn phụ**, nên mình vẫn kèm `environment.yml`

> Mình **không đóng gói sẵn thư mục môi trường ảo** vì nó rất nặng, không portable, và thường lỗi khi chuyển máy.  
> Chuẩn nhất là gửi **file mô tả môi trường** (`requirements.txt`, `environment.yml`) rồi tạo môi trường ở máy của bạn.

---

## 2) Setup nhanh bằng venv
```bash
cd backend
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# CMD:
# .venv\Scripts\activate.bat

pip install -r requirements.txt
copy .env.example .env
```

## 3) Setup nhanh bằng Conda
```bash
cd backend
conda env create -f environment.yml
conda activate fall-detection-ml
copy .env.example .env
```

## 4) Tạo database PostgreSQL
Tạo database:
```sql
CREATE DATABASE fall_detection_db;
```

Cập nhật `DATABASE_URL` trong `.env` nếu cần.

## 5) Khởi tạo model file mock
Script này tạo ra một mô hình Random Forest đơn giản để bạn có thể chạy inference ngay:
```bash
python scripts/train_mock_model.py
```

## 6) Khởi tạo schema DB
### Cách nhanh để demo ngay
```bash
python scripts/init_db.py
```

### Cách chuẩn bằng Alembic
```bash
alembic revision --autogenerate -m "initial schema"
alembic upgrade head
```

## 7) Chạy server
```bash
uvicorn app.main:app --reload
```

Swagger:
- `http://127.0.0.1:8000/docs`

## 8) Endpoint chính
- `GET /api/v1/health`
- `POST /api/v1/cameras`
- `GET /api/v1/cameras`
- `POST /api/v1/model-versions`
- `GET /api/v1/model-versions`
- `POST /api/v1/fall-events`
- `GET /api/v1/fall-events`
- `POST /api/v1/processing/upload-video`
- `POST /api/v1/processing/from-camera/{camera_id}`

## 9) Gợi ý lộ trình dev
1. Chạy `init_db.py`
2. Chạy `train_mock_model.py`
3. Tạo 1 camera kiểu `webcam`
4. Dùng webcam hoặc upload video để test inference
5. Khi pipeline ổn thì thay mock model bằng model train thật

## 10) Source input gợi ý
- ban đầu: webcam laptop hoặc file video
- sau đó: camera IP/RTSP trong LAN
