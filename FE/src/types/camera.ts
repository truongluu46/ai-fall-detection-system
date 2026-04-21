export type CameraStatus = 'active' | 'inactive' | 'error';

export interface Camera {
  id: number;
  name: string;
  location: string;
  status: CameraStatus;
  sourceType: 'webcam' | 'video_file' | 'rtsp';
  description: string;
}
