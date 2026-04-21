import AuthTemplate from '@/components/templates/auth-template';

export default function LoginPage() {
  return (
    <AuthTemplate>
      <div className="space-y-6">
        <div className="space-y-2 text-center">
          <p className="text-sm font-semibold uppercase tracking-[0.2em] text-blue-600">React Basic</p>
          <h1 className="text-2xl font-bold text-slate-900">Đăng nhập hệ thống</h1>
          <p className="text-sm text-slate-500">Màn hình này chỉ để bạn học React UI cơ bản trước khi sang Next.js.</p>
        </div>

        <form className="space-y-4">
          <div className="space-y-2">
            <label className="block text-sm font-medium text-slate-700">Username</label>
            <input className="w-full rounded-xl border border-slate-200 px-4 py-3 outline-none focus:border-blue-400" placeholder="admin" />
          </div>

          <div className="space-y-2">
            <label className="block text-sm font-medium text-slate-700">Password</label>
            <input type="password" className="w-full rounded-xl border border-slate-200 px-4 py-3 outline-none focus:border-blue-400" placeholder="••••••••" />
          </div>

          <button type="button" className="w-full rounded-xl bg-blue-600 px-4 py-3 font-semibold text-white transition hover:bg-blue-700">
            Login Demo
          </button>
        </form>
      </div>
    </AuthTemplate>
  );
}
