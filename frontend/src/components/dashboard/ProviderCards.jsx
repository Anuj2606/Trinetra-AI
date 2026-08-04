import {
  HiShieldCheck,
  HiGlobe,
  HiPhotograph,
  HiDatabase,
} from "react-icons/hi";

export default function ProviderCards({ providers = {} }) {

  const vt = providers?.virustotal || {};
  const sb = providers?.safe_browsing || {};
  const rdap = providers?.rdap || {};
  const urlscan = providers?.urlscan || {};

  return (
    <div>

      <h2 className="text-3xl font-bold text-slate-900 mb-6">
        Threat Intelligence Providers
      </h2>

      <div className="grid lg:grid-cols-2 gap-6">

        {/* VirusTotal */}

        <div className="bg-white rounded-3xl border border-slate-200 shadow-lg p-7">

          <div className="flex items-center gap-3 mb-6">

            <HiShieldCheck className="text-blue-600 text-4xl" />

            <div>

              <h3 className="font-bold text-xl">
                VirusTotal
              </h3>

              <p className={vt.success ? "text-green-600" : "text-red-500"}>
                {vt.success ? "Connected" : "Unavailable"}
              </p>

            </div>

          </div>

          <div className="space-y-3">

            <div className="flex justify-between">
              <span>Malicious</span>
              <span className="font-bold text-red-600">
                {vt.malicious ?? 0}
              </span>
            </div>

            <div className="flex justify-between">
              <span>Suspicious</span>
              <span className="font-bold text-orange-500">
                {vt.suspicious ?? 0}
              </span>
            </div>

            <div className="flex justify-between">
              <span>Harmless</span>
              <span className="font-bold text-green-600">
                {vt.harmless ?? 0}
              </span>
            </div>

          </div>

        </div>

        {/* Safe Browsing */}

        <div className="bg-white rounded-3xl border border-slate-200 shadow-lg p-7">

          <div className="flex items-center gap-3 mb-6">

            <HiGlobe className="text-green-600 text-4xl" />

            <div>

              <h3 className="font-bold text-xl">
                Google Safe Browsing
              </h3>

              <p className={sb.success ? "text-green-600" : "text-red-500"}>
                {sb.success ? "Connected" : "Unavailable"}
              </p>

            </div>

          </div>

          <div className="flex justify-between">

            <span>Status</span>

            <span className={sb.unsafe ? "text-red-600 font-bold" : "text-green-600 font-bold"}>

              {sb.unsafe ? "Unsafe" : "Safe"}

            </span>

          </div>

        </div>

        {/* RDAP */}

        <div className="bg-white rounded-3xl border border-slate-200 shadow-lg p-7">

          <div className="flex items-center gap-3 mb-6">

            <HiDatabase className="text-purple-600 text-4xl" />

            <div>

              <h3 className="font-bold text-xl">
                Domain Information
              </h3>

              <p className={rdap.success ? "text-green-600" : "text-red-500"}>
                {rdap.success ? "Available" : "Unavailable"}
              </p>

            </div>

          </div>

          {rdap.success ? (

            <div className="space-y-3">

              <div className="flex justify-between">

                <span>Domain Age</span>

                <span className="font-bold">

                  {rdap.age_days ?? "-"} days

                </span>

              </div>

              <div className="flex justify-between">

                <span>Registrar</span>

                <span className="font-bold">

                  {rdap.registrar ?? "-"}

                </span>

              </div>

            </div>

          ) : (

            <p className="text-red-500">
              Domain information unavailable
            </p>

          )}

        </div>

        {/* URLScan */}

        <div className="bg-white rounded-3xl border border-slate-200 shadow-lg p-7">

          <div className="flex items-center gap-3 mb-6">

            <HiPhotograph className="text-orange-500 text-4xl" />

            <div>

              <h3 className="font-bold text-xl">
                URLScan
              </h3>

              <p className={urlscan.success ? "text-green-600" : "text-orange-500"}>

                {urlscan.success ? "Completed" : "Pending / Unavailable"}

              </p>

            </div>

          </div>

          {urlscan.success ? (

            <>

              <div className="flex justify-between mb-3">

                <span>Country</span>

                <span className="font-bold">

                  {urlscan.country ?? "-"}

                </span>

              </div>

              <div className="flex justify-between mb-5">

                <span>Server</span>

                <span className="font-bold">

                  {urlscan.server ?? "-"}

                </span>

              </div>

              {urlscan.screenshot ? (

                <a
                  href={urlscan.screenshot}
                  target="_blank"
                  rel="noreferrer"
                  className="inline-block bg-blue-600 hover:bg-blue-700 text-white px-5 py-3 rounded-xl"
                >
                  View Screenshot
                </a>

              ) : (

                <p className="text-slate-500">
                  Screenshot unavailable
                </p>

              )}

            </>

          ) : (

            <p className="text-slate-500">
              URLScan is still processing or unavailable.
            </p>

          )}

        </div>

      </div>

    </div>
  );
}