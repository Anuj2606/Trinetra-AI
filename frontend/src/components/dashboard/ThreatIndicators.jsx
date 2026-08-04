import {
  HiExclamationCircle,
  HiShieldCheck,
  HiInformationCircle,
} from "react-icons/hi";

export default function ThreatIndicators({ reasons = [], indicators = [] }) {
  const allIndicators = [...new Set([...reasons, ...indicators])];

  const getStyle = (text) => {
    const value = text.toLowerCase();

    if (
      value.includes("malicious") ||
      value.includes("phishing") ||
      value.includes("critical")
    ) {
      return {
        bg: "bg-red-50",
        border: "border-red-300",
        text: "text-red-700",
        icon: <HiExclamationCircle className="text-red-600 text-xl" />,
      };
    }

    if (
      value.includes("suspicious") ||
      value.includes("keyword") ||
      value.includes("redirect") ||
      value.includes("hyphen")
    ) {
      return {
        bg: "bg-yellow-50",
        border: "border-yellow-300",
        text: "text-yellow-700",
        icon: <HiInformationCircle className="text-yellow-600 text-xl" />,
      };
    }

    return {
      bg: "bg-green-50",
      border: "border-green-300",
      text: "text-green-700",
      icon: <HiShieldCheck className="text-green-600 text-xl" />,
    };
  };

  return (
    <div className="bg-white rounded-3xl shadow-lg border border-slate-200 p-8">

      <div className="flex items-center justify-between mb-8">

        <div>

          <h2 className="text-3xl font-bold text-slate-900">
            Threat Indicators
          </h2>

          <p className="text-slate-500 mt-1">
            Key findings detected during analysis
          </p>

        </div>

        <span className="bg-blue-100 text-blue-700 px-4 py-2 rounded-full font-semibold">
          {allIndicators.length} Findings
        </span>

      </div>

      {allIndicators.length === 0 ? (
        <div className="bg-green-50 border border-green-300 rounded-2xl p-6 text-center">
          <HiShieldCheck className="mx-auto text-5xl text-green-600 mb-4" />

          <h3 className="text-xl font-bold text-green-700">
            No Threat Indicators
          </h3>

          <p className="text-green-600 mt-2">
            The scanned URL appears clean.
          </p>
        </div>
      ) : (
        <div className="grid md:grid-cols-2 gap-5">

          {allIndicators.map((item, index) => {
            const style = getStyle(item);

            return (
              <div
                key={index}
                className={`${style.bg} ${style.border} border rounded-2xl p-5 flex items-start gap-4 hover:shadow-md transition`}
              >
                <div>{style.icon}</div>

                <div>

                  <p className={`font-semibold ${style.text}`}>
                    {item}
                  </p>

                </div>
              </div>
            );
          })}

        </div>
      )}

    </div>
  );
}