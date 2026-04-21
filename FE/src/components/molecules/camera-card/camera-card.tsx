import StatusBadge from '@/components/atoms/status-badge';
import type { Camera } from '@/types/camera';

interface CameraCardProps {
  camera: Camera;
}

function mapStatus(camera: Camera) {
  if (camera.status === 'active') return { label: 'Đang hoạt động', variant: 'success' as const };
  if (camera.status === 'inactive') return { label: 'Tạm dừng', variant: 'warning' as const };
  return { label: 'Lỗi kết nối', variant: 'danger' as const };
}

export default function CameraCard({ camera }: CameraCardProps) {
  const status = mapStatus(camera);

  return (
    <article className="panel p-5">
      <div className="flex items-start justify-between gap-4">
        <div className="space-y-2">
          <h3 className="text-lg font-semibold text-slate-900">{camera.name}</h3>
          <p className="text-sm text-slate-500">{camera.location}</p>
        </div>
        <StatusBadge label={status.label} variant={status.variant} />
      </div>

      <div className="mt-4 space-y-2 text-sm text-slate-600">
        <p><span className="font-medium">Nguồn:</span> {camera.sourceType}</p>
        <p>{camera.description}</p>
      </div>
    </article>
  );
}
