import MetricCard from '@/components/molecules/metric-card';

interface DashboardStatsProps {
  totalCameras: number;
  activeCameras: number;
  totalEvents: number;
  newEvents: number;
}

export default function DashboardStats(props: DashboardStatsProps) {
  return (
    <section className="grid gap-4 md:grid-cols-2 xl:grid-cols-4">
      <MetricCard value={props.totalCameras} label="Tổng camera" helper="Số lượng nguồn vào đã cấu hình" />
      <MetricCard value={props.activeCameras} label="Camera hoạt động" helper="Nguồn đang sẵn sàng để xử lý" />
      <MetricCard value={props.totalEvents} label="Sự kiện té ngã" helper="Tổng event đã ghi nhận" />
      <MetricCard value={props.newEvents} label="Event mới" helper="Các event cần người quản trị xem lại" />
    </section>
  );
}
