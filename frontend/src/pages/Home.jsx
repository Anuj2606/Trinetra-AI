import Navbar from "../components/layout/Navbar";
import Hero from "../components/layout/Hero";
import LiveStats from "../components/cards/LiveStats";
import ScanBox from "../components/ui/ScanBox";

export default function Home() {
  return (
    <div className="min-h-screen bg-slate-50 text-slate-900">

      {/* Navbar */}
      <Navbar />

      {/* Main Content */}
      <main className="mx-auto max-w-7xl space-y-14 px-6 py-10 lg:px-8">

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