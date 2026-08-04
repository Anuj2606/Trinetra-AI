import {
  HiShieldCheck,
  HiViewGrid,
  HiClock,
  HiInformationCircle,
} from "react-icons/hi";
import { HiChartBar } from "react-icons/hi";

import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav className="bg-slate-950 border-b border-slate-800 shadow-lg">
      <div className="max-w-7xl mx-auto flex items-center justify-between px-8 py-5">

        {/* Logo */}
        <Link
          to="/"
          className="flex items-center gap-3 text-3xl font-bold text-blue-400 hover:text-blue-300 transition"
        >
          <HiShieldCheck size={38} />
          <span>FraudShield AI</span>
        </Link>

        {/* Navigation */}
        <div className="flex items-center gap-8 text-slate-300 font-medium">

          <Link
            to="/dashboard"
            className="flex items-center gap-2 hover:text-blue-400 transition"
          >
            <HiViewGrid size={20} />
            Dashboard
          </Link>

          <Link
            to="/history"
            className="flex items-center gap-2 hover:text-blue-400 transition"
          >
            <HiClock size={20} />
            History
          </Link>

          <Link
            to="/about"
            className="flex items-center gap-2 hover:text-blue-400 transition"
          >
            <HiInformationCircle size={20} />
            About
          </Link>

          <Link
    to="/analytics"
    className="flex items-center gap-2 hover:text-blue-500"
>
    <HiChartBar/>
    Analytics
</Link>

        </div>

      </div>
    </nav>
  );
}