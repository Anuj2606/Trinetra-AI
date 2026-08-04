import {
  LayoutGrid,
  History as HistoryIcon,
  BarChart3,
} from "lucide-react";

import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav className="border-b border-blue-100 bg-gradient-to-r from-blue-50 via-blue-100 to-blue-50 backdrop-blur">
      <div className="mx-auto flex max-w-7xl items-center justify-between px-6 py-4 lg:px-8">

        <Link
          to="/"
          className="flex items-center gap-3 text-2xl font-semibold text-blue-900 transition hover:text-blue-700"
        >
          <span>Trinetra AI</span>
        </Link>

        <div className="flex items-center gap-2 text-sm font-medium text-slate-700">

          <Link
            to="/dashboard"
            className="flex items-center gap-2 rounded-lg px-3 py-2 transition hover:bg-slate-50 hover:text-blue-600"
          >
            <LayoutGrid size={18} />
            Dashboard
          </Link>

          <Link
            to="/history"
            className="flex items-center gap-2 rounded-lg px-3 py-2 transition hover:bg-slate-50 hover:text-blue-600"
          >
            <HistoryIcon size={18} />
            History
          </Link>

          <Link
            to="/analytics"
            className="flex items-center gap-2 rounded-lg px-3 py-2 transition hover:bg-slate-50 hover:text-blue-600"
          >
            <BarChart3 size={18} />
            Analytics
          </Link>

        </div>

      </div>
    </nav>
  );
}