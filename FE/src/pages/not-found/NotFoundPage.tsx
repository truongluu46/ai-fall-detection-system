import { Link } from 'react-router-dom';
import { ROUTES } from '@/constants/routes';

export default function NotFoundPage() {
  return (
    <div className="flex min-h-screen flex-col items-center justify-center gap-4 bg-slate-100 p-4 text-center">
      <h1 className="text-4xl font-bold text-slate-900">404</h1>
      <p className="max-w-md text-slate-600">Trang bạn tìm không tồn tại trong bản React học cơ bản này.</p>
      <Link to={ROUTES.dashboard} className="rounded-xl bg-blue-600 px-4 py-3 font-medium text-white hover:bg-blue-700">
        Quay về dashboard
      </Link>
    </div>
  );
}
