import Navbar from "../components/layout/Navbar";
import Hero from "../components/layout/Hero";
import LiveStats from "../components/cards/LiveStats";
import ScanBox from "../components/ui/ScanBox";

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-b from-slate-50 via-white to-slate-100">

      {/* Navbar */}
      <Navbar />

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-6 lg:px-8 py-10 space-y-14">

        {/* Hero Section */}
        <Hero />

        {/* Live Statistics */}
        <LiveStats />

        {/* Scan Box */}
        <ScanBox />

      </main>

    </div>
  );
}