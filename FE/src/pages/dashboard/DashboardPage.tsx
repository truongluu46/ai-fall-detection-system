import PageTitle from '@/components/atoms/page-title';
import DashboardStats from '@/components/organisms/dashboard-stats';
import EventList from '@/components/organisms/event-list';
import DashboardTemplate from '@/components/templates/dashboard-template';
import { dashboardSummary, fallEvents } from '@/data/mockData';

export default function DashboardPage() {
  return (
    <DashboardTemplate title="Dashboard">
      <section className="space-y-4">
        <PageTitle
          title="Tổng quan hệ thống"
          description="Bản React cơ bản để học composition theo chuẩn Atomic Design trước khi chuyển sang Next.js."
        />
        <DashboardStats {...dashboardSummary} />
      </section>

      <section className="space-y-4">
        <PageTitle title="Sự kiện gần đây" description="Dữ liệu đang là mock data để bạn tập trung học UI, props, state và chia component." />
        <EventList events={fallEvents.slice(0, 2)} />
      </section>
    </DashboardTemplate>
  );
}
