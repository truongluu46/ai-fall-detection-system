import NavItem from '@/components/atoms/nav-item';
import { ROUTES } from '@/constants/routes';

export default function AppSidebar() {
  return (
    <aside className="w-full rounded-2xl border border-slate-200 bg-white p-4 shadow-panel lg:w-72 lg:min-h-[calc(100vh-3rem)]">
      <div className="mb-6 space-y-1 px-2">
        <p className="text-xs font-semibold uppercase tracking-[0.2em] text-blue-600">AI Project</p>
        <h2 className="text-lg font-bold text-slate-900">Fall Detection Dashboard</h2>
      </div>

      <nav className="space-y-2">
        <NavItem to={ROUTES.dashboard} label="Dashboard" />
        <NavItem to={ROUTES.cameras} label="Cameras" />
        <NavItem to={ROUTES.fallEvents} label="Fall Events" />
        <NavItem to={ROUTES.notifications} label="Notifications" />
        <NavItem to={ROUTES.login} label="Login" />
      </nav>
    </aside>
  );
}
