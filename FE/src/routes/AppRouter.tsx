import { Navigate, Route, Routes } from 'react-router-dom';
import { ROUTES } from '@/constants/routes';
import DashboardPage from '@/pages/dashboard/DashboardPage';
import CamerasPage from '@/pages/cameras/CamerasPage';
import FallEventsPage from '@/pages/fall-events/FallEventsPage';
import NotificationsPage from '@/pages/notifications/NotificationsPage';
import LoginPage from '@/pages/login/LoginPage';
import NotFoundPage from '@/pages/not-found/NotFoundPage';

export default function AppRouter() {
  return (
    <Routes>
      <Route path={ROUTES.dashboard} element={<DashboardPage />} />
      <Route path={ROUTES.cameras} element={<CamerasPage />} />
      <Route path={ROUTES.fallEvents} element={<FallEventsPage />} />
      <Route path={ROUTES.notifications} element={<NotificationsPage />} />
      <Route path={ROUTES.login} element={<LoginPage />} />
      <Route path="/home" element={<Navigate to={ROUTES.dashboard} replace />} />
      <Route path="*" element={<NotFoundPage />} />
    </Routes>
  );
}
