import PageTitle from '@/components/atoms/page-title';
import SearchInput from '@/components/molecules/search-input';
import CameraGrid from '@/components/organisms/camera-grid';
import DashboardTemplate from '@/components/templates/dashboard-template';
import { cameras } from '@/data/mockData';

export default function CamerasPage() {
  return (
    <DashboardTemplate title="Cameras">
      <section className="space-y-4">
        <PageTitle title="Danh sách camera" description="Giai đoạn đầu có thể dùng webcam máy tính hoặc file video thay cho camera IP thật." />
        <SearchInput placeholder="Tìm camera theo tên hoặc vị trí..." />
        <CameraGrid cameras={cameras} />
      </section>
    </DashboardTemplate>
  );
}
