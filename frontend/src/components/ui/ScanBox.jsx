import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { HiSearch, HiShieldCheck } from "react-icons/hi";
import ScanLoader from "./ScanLoader";
import { useNavigate } from "react-router-dom";
import api from "../../services/api";

export default function ScanBox() {

  const navigate = useNavigate()
  
  const [url, setUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [step, setStep] = useState(0);

  const handleScan = async () => {
  if (!url.trim()) {
    alert("Enter URL");
    return;
  }

  try {
    setLoading(true);

    const interval = setInterval(() => {
      setStep((prev) => (prev < 4 ? prev + 1 : prev));
    }, 800);

    const res = await api.post("/scan", {
      url,
    });
    console.log("========== BACKEND RESPONSE ==========");
    console.log(res.data);
    console.log("Providers:", res.data.providers);
    console.log("AI Summary:", res.data.ai_summary);
    console.log("Fraud Analysis:", res.data.fraud_analysis);
    clearInterval(interval);

    setLoading(false);

    navigate("/dashboard", {
      state: res.data,
    });
  } catch (err) {
    console.error(err);
    alert("Scan failed.");
    setLoading(false);
  }
};

  return (
    <motion.div
      initial={{ opacity: 0, y: 25 }}
      animate={{ opacity: 1, y: 0 }}
      className="bg-white rounded-3xl border border-slate-200 shadow-xl p-10"
    >
      {/* Header */}

      <div className="flex items-center gap-4 mb-8">
        <div className="w-16 h-16 rounded-2xl bg-blue-100 flex items-center justify-center">
          <HiShieldCheck className="text-blue-600 text-4xl" />
        </div>

        <div>
          <h2 className="text-3xl font-bold text-slate-900">
            Scan Suspicious URL
          </h2>

          <p className="text-slate-500 mt-1">
            AI-powered fraud detection using multiple threat intelligence
            providers.
          </p>
        </div>
      </div>

      {/* Input */}

      <div className="flex flex-col lg:flex-row gap-4">

        <input
          type="text"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          placeholder="https://example.com"
          className="
          flex-1
          h-16
          rounded-2xl
          border
          border-slate-300
          bg-slate-50
          px-6
          text-lg
          focus:ring-4
          focus:ring-blue-200
          focus:border-blue-500
          outline-none
          transition
          "
        />

        <motion.button
          whileHover={{ scale: 1.03 }}
          whileTap={{ scale: .96 }}
          onClick={handleScan}
          disabled={loading}
          className="
          h-16
          px-10
          rounded-2xl
          bg-gradient-to-r
          from-blue-600
          to-indigo-600
          text-white
          font-semibold
          shadow-lg
          hover:shadow-xl
          disabled:opacity-60
          flex
          items-center
          justify-center
          gap-2
          "
        >
          <HiSearch />

          {loading ? "Analyzing..." : "Analyze URL"}
        </motion.button>

      </div>

      {/* Providers */}

      <div className="grid grid-cols-2 lg:grid-cols-5 gap-4 mt-8">

        {[
          "VirusTotal",
          "Safe Browsing",
          "URLScan",
          "RDAP",
          "Gemini AI",
        ].map((provider) => (
          <motion.div
            key={provider}
            whileHover={{ y: -4 }}
            className="rounded-xl border bg-slate-50 p-4 text-center"
          >
            <p className="font-semibold text-slate-700">{provider}</p>
          </motion.div>
        ))}

      </div>

      {/* Loader */}

      <AnimatePresence>

        {loading && (

          <motion.div
            initial={{ opacity: 0, y: 15 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0 }}
            className="mt-10"
          >
            <ScanLoader step={step} />
          </motion.div>

        )}

      </AnimatePresence>

    </motion.div>
  );
}