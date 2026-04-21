import { NavLink } from 'react-router-dom';
import { cn } from '@/lib/cn';

interface NavItemProps {
  to: string;
  label: string;
}

export default function NavItem({ to, label }: NavItemProps) {
  return (
    <NavLink
      to={to}
      className={({ isActive }) =>
        cn(
          'block rounded-xl px-3 py-2 text-sm font-medium transition',
          isActive ? 'bg-blue-50 text-blue-700' : 'text-slate-600 hover:bg-slate-100 hover:text-slate-900'
        )
      }
    >
      {label}
    </NavLink>
  );
}
