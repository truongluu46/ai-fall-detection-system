import PageTitle from '@/components/atoms/page-title';
import DashboardTemplate from '@/components/templates/dashboard-template';

const items = [
  'Có 1 cảnh báo mới từ Camera Hành Lang A1',
  'Sự kiện #101 đang chờ người quản trị xem lại',
  'Mô hình fall_detector_v1 đã được load thành công',
];

export default function NotificationsPage() {
  return (
    <DashboardTemplate title="Notifications">
      <section className="space-y-4">
        <PageTitle title="Thông báo hệ thống" description="Trang này sau này có thể nối với polling hoặc WebSocket từ backend." />
        <div className="panel p-5">
          <ul className="space-y-3 text-sm text-slate-700">
            {items.map((item) => (
              <li key={item} className="rounded-xl bg-slate-50 px-4 py-3">{item}</li>
            ))}
          </ul>
        </div>
      </section>
    </DashboardTemplate>
  );
}
