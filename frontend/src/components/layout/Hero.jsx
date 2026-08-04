import { motion } from "framer-motion";
import {
  HiShieldCheck,
  HiSparkles,
  HiGlobeAlt,
} from "react-icons/hi";

export default function Hero() {
  return (
    <section className="relative overflow-hidden rounded-3xl bg-gradient-to-r from-slate-900 via-blue-900 to-slate-900 text-white p-16">

      {/* Background blur */}
      <div className="absolute -top-24 -right-24 w-96 h-96 bg-blue-500/20 rounded-full blur-3xl"></div>
      <div className="absolute -bottom-32 left-0 w-96 h-96 bg-cyan-400/10 rounded-full blur-3xl"></div>

      <motion.div
        initial={{ opacity: 0, y: 35 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: .8 }}
        className="relative z-10"
      >

        <span className="inline-flex items-center gap-2 bg-blue-500/20 border border-blue-400/30 px-5 py-2 rounded-full text-sm font-semibold">

          <HiSparkles />

          AI Powered Threat Intelligence

        </span>

        <h1 className="mt-8 text-6xl font-extrabold leading-tight">

          Detect Fraud

          <br />

          Before It Happens

        </h1>

        <p className="mt-6 text-xl text-slate-300 max-w-3xl leading-9">

          Analyze suspicious URLs using Artificial Intelligence,
          VirusTotal, Google Safe Browsing,
          URLScan and RDAP to detect phishing,
          malware and online fraud in real time.

        </p>

        <div className="flex gap-8 mt-12">

          <div className="flex items-center gap-3">

            <HiShieldCheck className="text-emerald-400 text-2xl"/>

            Multi Engine Detection

          </div>

          <div className="flex items-center gap-3">

            <HiGlobeAlt className="text-cyan-400 text-2xl"/>

            Global Threat Intelligence

          </div>

        </div>

      </motion.div>

    </section>
  );
}