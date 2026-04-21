import type { PropsWithChildren } from 'react';
import AppSidebar from '@/components/organisms/app-sidebar';
import AppHeader from '@/components/organisms/app-header';

interface DashboardTemplateProps extends PropsWithChildren {
  title: string;
}

export default function DashboardTemplate({ title, children }: DashboardTemplateProps) {
  return (
    <div className="min-h-screen bg-slate-50">
      <div className="page-shell lg:flex lg:items-start lg:gap-6">
        <AppSidebar />
        <main className="mt-6 min-w-0 flex-1 space-y-6 lg:mt-0">
          <AppHeader title={title} />
          {children}
        </main>
      </div>
    </div>
  );
}
