import StatusBadge from '@/components/atoms/status-badge';
import type { FallEvent } from '@/types/fall-event';

interface EventCardProps {
  event: FallEvent;
}

function mapEventStatus(status: FallEvent['status']) {
  switch (status) {
    case 'new':
      return { label: 'Mới', variant: 'danger' as const };
    case 'reviewed':
      return { label: 'Đã xem', variant: 'success' as const };
    case 'false_alarm':
      return { label: 'Báo giả', variant: 'warning' as const };
    case 'confirmed':
      return { label: 'Đã xác nhận', variant: 'success' as const };
    default:
      return { label: status, variant: 'neutral' as const };
  }
}

export default function EventCard({ event }: EventCardProps) {
  const badge = mapEventStatus(event.status);

  return (
    <article className="panel p-5">
      <div className="flex items-start justify-between gap-4">
        <div>
          <h3 className="text-lg font-semibold text-slate-900">{event.cameraName}</h3>
          <p className="mt-1 text-sm text-slate-500">{event.eventTime}</p>
        </div>
        <StatusBadge label={badge.label} variant={badge.variant} />
      </div>

      <div className="mt-4 grid gap-3 text-sm text-slate-600 sm:grid-cols-2">
        <p><span className="font-medium">Độ tin cậy:</span> {Math.round(event.confidenceScore * 100)}%</p>
        <p><span className="font-medium">Ghi chú:</span> {event.note}</p>
      </div>
    </article>
  );
}
