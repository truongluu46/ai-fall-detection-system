interface AppHeaderProps {
  title: string;
}

export default function AppHeader({ title }: AppHeaderProps) {
  return (
    <header className="panel flex flex-col gap-3 p-5 sm:flex-row sm:items-center sm:justify-between">
      <div>
        <p className="text-sm text-slate-500">Hệ thống giám sát té ngã</p>
        <h2 className="text-xl font-bold text-slate-900">{title}</h2>
      </div>

      <div className="rounded-xl bg-slate-50 px-4 py-2 text-sm text-slate-600">
        Demo frontend React + ATOMIC
      </div>
    </header>
  );
}
