interface SearchInputProps {
  placeholder?: string;
}

export default function SearchInput({ placeholder = 'Tìm kiếm...' }: SearchInputProps) {
  return (
    <input
      type="text"
      placeholder={placeholder}
      className="w-full rounded-xl border border-slate-200 bg-white px-4 py-2.5 text-sm outline-none transition focus:border-blue-400 focus:ring-4 focus:ring-blue-50"
    />
  );
}
