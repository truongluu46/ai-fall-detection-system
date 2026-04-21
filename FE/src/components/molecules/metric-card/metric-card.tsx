import StatValue from '@/components/atoms/stat-value';

interface MetricCardProps {
  value: string | number;
  label: string;
  helper: string;
}

export default function MetricCard({ value, label, helper }: MetricCardProps) {
  return (
    <article className="panel p-5">
      <div className="space-y-3">
        <StatValue value={value} label={label} />
        <p className="text-sm text-slate-500">{helper}</p>
      </div>
    </article>
  );
}
