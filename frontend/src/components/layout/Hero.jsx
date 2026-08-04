import { motion } from "framer-motion";
import { ShieldCheck, Globe2, Activity } from "lucide-react";

export default function Hero() {
  return (
    <section className="overflow-hidden rounded-3xl border border-slate-200 bg-white p-8 shadow-sm lg:p-12">
      <motion.div
        initial={{ opacity: 0, y: 24 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8 }}
        className="grid gap-8 lg:grid-cols-[1.2fr_0.9fr] lg:items-center"
      >
        <div>
          <h1 className="mt-6 text-4xl font-bold tracking-tight text-slate-900 lg:text-5xl">
            Analyze suspicious links in seconds.
          </h1>

          <p className="mt-4 max-w-2xl text-lg leading-8 text-slate-600">
            Trinetra AI helps you check any URL against trusted cybersecurity signals so you can quickly understand whether it is phishing, malicious, or safe.
          </p>

          <p className="mt-3 max-w-2xl text-sm leading-7 text-slate-500">
            Paste a site address, review multi-provider threat evidence, and get a clear risk summary before taking action.
          </p>

          <div className="mt-8 flex flex-col items-center justify-center gap-3 text-sm font-medium text-slate-700 md:flex-row">
            <div className="flex w-full max-w-[220px] items-center justify-center gap-2 rounded-2xl border border-slate-200 bg-white px-4 py-3 text-center">
              Multi-engine detection
            </div>
            <div className="flex w-full max-w-[220px] items-center justify-center gap-2 rounded-2xl border border-slate-200 bg-white px-4 py-3 text-center">
              Global threat visibility
            </div>
            <div className="flex w-full max-w-[220px] items-center justify-center gap-2 rounded-2xl border border-slate-200 bg-white px-4 py-3 text-center">
              Real-time risk signals
            </div>
          </div>
        </div>

        <div className="rounded-[28px] border border-slate-200 bg-gradient-to-br from-slate-900 via-blue-950 to-slate-900 p-[1px] shadow-sm">
          <div className="rounded-[27px] bg-slate-950/95 p-7 text-white">
            <div className="flex items-start justify-between gap-4">
              <div>
                <div className="text-xs font-semibold uppercase tracking-[0.24em] text-blue-200">
                  Trinetra AI
                </div>
                <div className="mt-2 text-2xl font-semibold text-white">
                  URL threat assessment
                </div>
              </div>
              <span className="flex h-12 w-12 items-center justify-center rounded-2xl bg-blue-500/15 text-blue-200">
                <ShieldCheck size={20} />
              </span>
            </div>

            <div className="mt-6 rounded-2xl border border-white/10 bg-white/5 p-5">
              <div className="text-sm font-medium text-slate-200">
                Checks suspicious URLs using multiple security intelligence sources in one place.
              </div>
              <div className="mt-4 space-y-3">
                <div className="rounded-xl bg-white/5 px-4 py-3">
                  <div className="text-xs uppercase tracking-[0.2em] text-slate-300">Signals</div>
                  <div className="mt-2 text-sm font-semibold text-white">VirusTotal • Safe Browsing • RDAP • URLScan</div>
                </div>
                <div className="rounded-xl bg-white/5 px-4 py-3">
                  <div className="text-xs uppercase tracking-[0.2em] text-slate-300">Outcome</div>
                  <div className="mt-2 text-sm font-semibold text-white">Clear verdict in one view</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </motion.div>
    </section>
  );
}