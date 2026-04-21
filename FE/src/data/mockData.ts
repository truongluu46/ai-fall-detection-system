import type { Camera } from '@/types/camera';
import type { FallEvent } from '@/types/fall-event';

export const cameras: Camera[] = [
  {
    id: 1,
    name: 'Camera Hành Lang A1',
    location: 'Tầng 1 - Hành lang',
    status: 'active',
    sourceType: 'webcam',
    description: 'Nguồn demo bằng webcam máy tính.',
  },
  {
    id: 2,
    name: 'Camera Phòng Lab',
    location: 'Phòng thực hành',
    status: 'inactive',
    sourceType: 'video_file',
    description: 'Nguồn demo bằng file video té ngã.',
  },
  {
    id: 3,
    name: 'Camera Khu Vực Cửa',
    location: 'Lối vào chính',
    status: 'error',
    sourceType: 'rtsp',
    description: 'Camera IP dự kiến giai đoạn sau.',
  },
];

export const fallEvents: FallEvent[] = [
  {
    id: 101,
    cameraName: 'Camera Hành Lang A1',
    eventTime: '2026-04-21 08:10:15',
    confidenceScore: 0.91,
    status: 'new',
    note: 'Phát hiện tư thế nằm ngang bất thường.',
  },
  {
    id: 102,
    cameraName: 'Camera Phòng Lab',
    eventTime: '2026-04-21 09:35:40',
    confidenceScore: 0.74,
    status: 'reviewed',
    note: 'Đã được người quản trị kiểm tra.',
  },
  {
    id: 103,
    cameraName: 'Camera Hành Lang A1',
    eventTime: '2026-04-21 10:12:08',
    confidenceScore: 0.62,
    status: 'false_alarm',
    note: 'Người ngồi xuống nhanh nhưng không té.',
  },
];

export const dashboardSummary = {
  totalCameras: cameras.length,
  activeCameras: cameras.filter((camera) => camera.status === 'active').length,
  totalEvents: fallEvents.length,
  newEvents: fallEvents.filter((event) => event.status === 'new').length,
};
