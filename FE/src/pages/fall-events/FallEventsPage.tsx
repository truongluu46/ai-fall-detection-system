import PageTitle from '@/components/atoms/page-title';
import SearchInput from '@/components/molecules/search-input';
import EventList from '@/components/organisms/event-list';
import DashboardTemplate from '@/components/templates/dashboard-template';
import { fallEvents } from '@/data/mockData';

export default function FallEventsPage() {
  return (
    <DashboardTemplate title="Fall Events">
      <section className="space-y-4">
        <PageTitle title="Danh sách sự kiện té ngã" description="Bạn có thể thay mock data bằng API thật khi backend FastAPI sẵn sàng." />
        <SearchInput placeholder="Tìm theo camera, trạng thái, thời gian..." />
        <EventList events={fallEvents} />
      </section>
    </DashboardTemplate>
  );
}
