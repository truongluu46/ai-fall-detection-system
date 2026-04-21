# React Atomic Fall Detection

Dự án **Camera AI báo cáo người bị ngã**.

## Stack
- React + Vite + TypeScript
- React Router DOM
- Tailwind CSS
- Atomic Design

## Mục tiêu học
Bản này giúp bạn luyện:
- component
- props
- layout
- route cơ bản
- chia folder chuẩn ATOMIC
- mock data trước khi nối backend FastAPI

## Cách chạy
```bash
npm install
npm run dev
```

## Route hiện có
- `/` dashboard
- `/cameras`
- `/fall-events`
- `/notifications`
- `/login`

## Tư duy ATOMIC trong project này
- `atoms`: thành phần nhỏ nhất như badge, title, stat value
- `molecules`: ghép vài atom, ví dụ metric-card, search-input
- `organisms`: khối UI lớn hơn như sidebar, header, list
- `templates`: khung trang
- `pages`: màn hình hoàn chỉnh

## Khi nào chuyển sang Next.js
Sau khi bạn đã hiểu:
- component là gì
- props hoạt động ra sao
- route frontend hoạt động thế nào
- cách chia UI theo ATOMIC

