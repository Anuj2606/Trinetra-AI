import {
  HiShieldCheck,
  HiExclamationCircle,
  HiClock,
  HiCheckCircle,
} from "react-icons/hi";

export default function StatsCards({ result }) {
  if (!result) return null;

  const risk = result.risk;

  return (
    <div className="grid lg:grid-cols-4 md:grid-cols-2 gap-6">

      <div className="bg-white rounded-xl shadow p-6 border">
        <HiShieldCheck className="text-blue-600 text-4xl mb-3" />
        <p className="text-gray-500">Risk Score</p>
        <h1 className="text-4xl font-bold">{risk.risk_score}</h1>
      </div>

      <div className="bg-white rounded-xl shadow p-6 border">
        <HiCheckCircle className="text-green-600 text-4xl mb-3" />
        <p className="text-gray-500">Confidence</p>
        <h1 className="text-4xl font-bold">{risk.confidence}%</h1>
      </div>

      <div className="bg-white rounded-xl shadow p-6 border">
        <HiExclamationCircle className="text-red-600 text-4xl mb-3" />
        <p className="text-gray-500">Threat Level</p>
        <h1 className="text-3xl font-bold">
          {risk.risk_level}
        </h1>
      </div>

      <div className="bg-white rounded-xl shadow p-6 border">
        <HiClock className="text-yellow-500 text-4xl mb-3" />
        <p className="text-gray-500">Scan Time</p>
        <h1 className="text-xl font-bold">
          {new Date(result.generated_at).toLocaleTimeString()}
        </h1>
      </div>

    </div>
  );
}