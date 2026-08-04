import { HiExclamationTriangle } from "react-icons/hi2";

export default function FraudCard({ fraud }) {

  if (!fraud) return null;

  return (

    <div className="bg-white rounded-xl shadow border p-8">

      <div className="flex items-center gap-3">

        <HiExclamationTriangle className="text-red-500 text-3xl"/>

        <h2 className="text-2xl font-bold">

          Fraud Analysis

        </h2>

      </div>

      <div className="mt-6 space-y-3">

        <p>

          <b>Attack Type:</b>

          {fraud.attack_type}

        </p>

        <p>

          <b>Severity:</b>

          {fraud.severity}

        </p>

        <p>

          <b>Recommendation:</b>

          {fraud.recommendation}

        </p>

      </div>

    </div>

  );

}