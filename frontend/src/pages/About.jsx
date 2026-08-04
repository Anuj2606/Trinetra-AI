import Navbar from "../components/layout/Navbar";

export default function About() {

    return (

        <div className="min-h-screen bg-slate-100">

            <Navbar />

            <div className="max-w-5xl mx-auto py-20">

                <h1 className="text-5xl font-bold">

                    About FraudShield AI

                </h1>

                <p className="text-slate-600 mt-6 leading-8">

                    FraudShield AI is an AI-powered fraud detection
                    platform that analyzes suspicious URLs using
                    multiple threat intelligence providers including
                    VirusTotal, Google Safe Browsing,
                    URLScan, RDAP and Generative AI.

                </p>

            </div>

        </div>

    );

}