export default function RiskCards({ risk }) {
  if (!risk) return null;

  const levelColor = {
    SAFE: "text-green-400",
    LOW: "text-yellow-400",
    MEDIUM: "text-orange-400",
    HIGH: "text-red-400",
    CRITICAL: "text-red-600",
  };

  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-10">

      <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-lg">
        <p className="text-slate-400 text-sm">Risk Score</p>

        <h1 className="text-5xl font-bold mt-3 text-blue-400">
          {risk.risk_score}
        </h1>
      </div>

      <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-lg">
        <p className="text-slate-400 text-sm">Confidence</p>

        <h1 className="text-5xl font-bold mt-3 text-green-400">
          {risk.confidence}%
        </h1>
      </div>

      <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-lg">
        <p className="text-slate-400 text-sm">Threat Level</p>

        <h1
          className={`text-4xl font-bold mt-3 ${
            levelColor[risk.risk_level]
          }`}
        >
          {risk.risk_level}
        </h1>
      </div>

    </div>
  );
}