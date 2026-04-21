import type { PropsWithChildren } from 'react';

export default function AuthTemplate({ children }: PropsWithChildren) {
  return (
    <div className="flex min-h-screen items-center justify-center bg-slate-100 p-4">
      <div className="w-full max-w-md rounded-3xl border border-slate-200 bg-white p-8 shadow-panel">
        {children}
      </div>
    </div>
  );
}
