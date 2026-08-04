import {
  HiShieldCheck,
  HiExclamationCircle,
  HiCheckCircle,
} from "react-icons/hi";
import { motion } from "framer-motion";

export default function RiskOverview({ result }) {
  const risk = result.risk;
  const fraud = result.fraud_analysis;

  const levelColor = {
    SAFE: "bg-green-100 text-green-700",
    LOW: "bg-yellow-100 text-yellow-700",
    MEDIUM: "bg-orange-100 text-orange-700",
    HIGH: "bg-red-100 text-red-700",
    CRITICAL: "bg-red-600 text-white",
  };

  return (
    <motion.div
      initial={{ opacity: 0, y: 25 }}
      animate={{ opacity: 1, y: 0 }}
      className="grid lg:grid-cols-4 gap-6"
    >
      {/* Risk Score */}

      <div className="bg-white rounded-3xl shadow-lg border border-slate-200 p-8">

        <HiShieldCheck className="text-blue-600 text-5xl mb-5" />

        <p className="text-slate-500 text-sm uppercase tracking-wide">
          Risk Score
        </p>

        <h1 className="text-6xl font-black mt-3 text-slate-900">
          {risk.risk_score}
        </h1>

      </div>

      {/* Threat Level */}

      <div className="bg-white rounded-3xl shadow-lg border border-slate-200 p-8">

        <HiExclamationCircle className="text-red-500 text-5xl mb-5" />

        <p className="text-slate-500 text-sm uppercase tracking-wide">
          Threat Level
        </p>

        <div
          className={`inline-block mt-5 px-5 py-3 rounded-full font-bold ${
            levelColor[risk.risk_level]
          }`}
        >
          {risk.risk_level}
        </div>

      </div>

      {/* Confidence */}

      <div className="bg-white rounded-3xl shadow-lg border border-slate-200 p-8">

        <HiCheckCircle className="text-green-500 text-5xl mb-5" />

        <p className="text-slate-500 text-sm uppercase tracking-wide">
          Confidence
        </p>

        <h2 className="text-5xl font-bold mt-4 text-slate-900">
          {risk.confidence}%
        </h2>

      </div>

      {/* Attack */}

      <div className="bg-white rounded-3xl shadow-lg border border-slate-200 p-8">

        <p className="text-slate-500 text-sm uppercase tracking-wide">
          Attack Type
        </p>

        <h2 className="mt-4 text-2xl font-bold text-slate-900">
          {fraud.attack_type}
        </h2>

        <div className="mt-6">

          <span
            className={`px-4 py-2 rounded-full font-semibold ${
              levelColor[fraud.severity]
            }`}
          >
            {fraud.severity}
          </span>

        </div>

      </div>

    </motion.div>
  );
}