import { useLocation, Navigate } from "react-router-dom";
import Navbar from "../components/layout/Navbar";

import RiskOverview from "../components/dashboard/RiskOverview";
import ProviderCards from "../components/dashboard/ProviderCards";
import ThreatIndicators from "../components/dashboard/ThreatIndicators";
import RecommendationCard from "../components/dashboard/RecommendationCard";
import AICard from "../components/dashboard/AICard";

import api from "../services/api";

export default function Dashboard() {

    const location = useLocation();

    const result = location.state;
    console.log(result);
    console.log(result.providers);
    console.log(result.providers.urlscan);
    if (!result) {
        return <Navigate to="/" replace />;
    }

    const downloadReport = async () => {

        try {

            const response = await api.post(
                "/report",
                result,
                {
                    responseType: "blob",
                }
            );

            const blob = new Blob(
                [response.data],
                {
                    type: "application/pdf",
                }
            );

            const url = window.URL.createObjectURL(blob);

            const link = document.createElement("a");

            link.href = url;

            link.download = "FraudShield_Report.pdf";

            document.body.appendChild(link);

            link.click();

            link.remove();

            window.URL.revokeObjectURL(url);

        } catch (error) {

            console.error(error);

            alert("Unable to generate PDF report.");

        }

    };

    return (

        <div className="min-h-screen bg-slate-100">

            <Navbar />

            <div className="max-w-7xl mx-auto px-8 py-10">

                {/* Header */}

                <div className="flex justify-between items-center mb-8">

                    <div>

                        <h1 className="text-4xl font-bold">

                            Fraud Detection Report

                        </h1>

                        <p className="text-slate-500 mt-2">

                            AI Threat Intelligence Report

                        </p>

                    </div>

                    <button

                        onClick={downloadReport}

                        className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-xl font-semibold shadow-lg"

                    >

                        Export PDF Report

                    </button>

                </div>

                {/* URL */}

                <div className="bg-white rounded-3xl shadow border border-slate-200 p-6 mb-8">

                    <p className="text-slate-500">

                        Scanned URL

                    </p>

                    <h2 className="text-xl font-semibold mt-2 break-all">

                        {result.url}

                    </h2>

                </div>

                {/* Risk Overview */}

                <RiskOverview result={result} />

                {/* Providers */}

                <div className="mt-8">

                    <ProviderCards providers={result.providers} />

                </div>

                {/* Threat Indicators */}

                <div className="mt-8">

                    <ThreatIndicators
                        reasons={result.risk.reasons}
                        indicators={result.fraud_analysis.indicators}
                    />

                </div>

                {/* Gemini AI */}

                <div className="mt-8">

                    <AICard
                        summary={result.ai_summary}
                    />

                </div>

                {/* Recommendation */}

                <div className="mt-8">

                    <RecommendationCard
                        recommendation={result.fraud_analysis.recommendation}
                    />

                </div>

            </div>

        </div>

    );

}