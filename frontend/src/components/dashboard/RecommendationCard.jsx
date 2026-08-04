import {
  HiShieldCheck,
  HiLockClosed,
  HiBan,
  HiDocumentDownload,
  HiBell,
} from "react-icons/hi";

export default function RecommendationCard({ recommendation }) {
  return (
    <div className="bg-white rounded-3xl shadow-lg border border-slate-200 p-8">

      <div className="flex items-center gap-3 mb-8">

        <HiShieldCheck className="text-blue-600 text-4xl" />

        <div>

          <h2 className="text-3xl font-bold text-slate-900">

            Recommended Actions

          </h2>

          <p className="text-slate-500">

            Suggested response based on AI analysis

          </p>

        </div>

      </div>

      <div className="bg-blue-50 border border-blue-200 rounded-2xl p-5 mb-8">

        <p className="text-lg font-medium text-slate-700">

          {recommendation}

        </p>

      </div>

      <div className="grid md:grid-cols-2 xl:grid-cols-4 gap-5">

        <div className="bg-red-50 rounded-2xl border border-red-200 p-5">

          <HiBan className="text-red-600 text-4xl mb-4"/>

          <h3 className="font-bold">

            Block URL

          </h3>

          <p className="text-sm text-slate-600 mt-2">

            Prevent users from accessing the website.

          </p>

        </div>

        <div className="bg-yellow-50 rounded-2xl border border-yellow-200 p-5">

          <HiLockClosed className="text-yellow-600 text-4xl mb-4"/>

          <h3 className="font-bold">

            Reset Credentials

          </h3>

          <p className="text-sm text-slate-600 mt-2">

            Reset passwords if credentials may have been exposed.

          </p>

        </div>

        <div className="bg-green-50 rounded-2xl border border-green-200 p-5">

          <HiBell className="text-green-600 text-4xl mb-4"/>

          <h3 className="font-bold">

            Notify Security Team

          </h3>

          <p className="text-sm text-slate-600 mt-2">

            Inform SOC analysts for further investigation.

          </p>

        </div>

        <div className="bg-purple-50 rounded-2xl border border-purple-200 p-5">

          <HiDocumentDownload className="text-purple-600 text-4xl mb-4"/>

          <h3 className="font-bold">

            Export Report

          </h3>

          <p className="text-sm text-slate-600 mt-2">

            Generate PDF/JSON report for incident documentation.

          </p>

        </div>

      </div>

    </div>
  );
}