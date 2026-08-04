import { HiSparkles } from "react-icons/hi";

export default function AICard({ summary }) {

  if (!summary) return null;

  return (

    <div className="bg-white rounded-xl shadow border p-8">

      <div className="flex items-center gap-3 mb-5">

        <HiSparkles className="text-purple-600 text-3xl" />

        <h2 className="text-2xl font-bold">

          AI Analysis

        </h2>

      </div>

      <div className="whitespace-pre-wrap leading-8 text-gray-700">

        {summary}

      </div>

    </div>

  );

}