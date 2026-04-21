interface StatValueProps {
  value: string | number;
  label: string;
}

export default function StatValue({ value, label }: StatValueProps) {
  return (
    <div className="space-y-1">
      <p className="text-3xl font-bold text-slate-900">{value}</p>
      <p className="text-sm text-slate-500">{label}</p>
    </div>
  );
}
