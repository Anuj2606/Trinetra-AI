import {
    Activity,
    ArrowDown,
    Check,
    Database,
    FileText,
    Globe2,
    Lock,
    Search,
    Server,
    Shield,
    ShieldCheck,
} from "lucide-react";

import Navbar from "../components/layout/Navbar";

const features = [
    {
        title: "Multi-source Threat Intelligence",
        icon: Globe2,
    },
    {
        title: "VirusTotal Integration",
        icon: Search,
    },
    {
        title: "Google Safe Browsing",
        icon: ShieldCheck,
    },
    {
        title: "URLScan.io",
        icon: Activity,
    },
    {
        title: "RDAP Lookup",
        icon: Database,
    },
    {
        title: "AI Security Summary",
        icon: FileText,
    },
    {
        title: "Unified Risk Score",
        icon: Lock,
    },
    {
        title: "Dashboard Analytics",
        icon: Activity,
    },
    {
        title: "Scan History",
        icon: Server,
    },
    {
        title: "PDF Report Generation",
        icon: FileText,
    },
];

const technologies = [
    "React",
    "FastAPI",
    "Python",
    "PostgreSQL",
    "Tailwind CSS",
    "VirusTotal API",
    "Google Safe Browsing",
    "URLScan.io",
    "RDAP",
    "Google Gemini AI",
];

const missionPoints = [
    "Improve cybersecurity awareness",
    "Detect phishing websites",
    "Simplify threat analysis",
    "Provide explainable security assessments",
];

const workflow = [
    "User submits URL",
    "Threat Intelligence APIs",
    "Risk Assessment Engine",
    "Gemini AI Summary",
    "Dashboard & PDF Report",
];

export default function About() {
    return (
        <div className="min-h-screen bg-white text-slate-900">
            <Navbar />

            <main className="mx-auto max-w-6xl px-4 py-10 sm:px-6 lg:px-8 lg:py-14">
                <section className="grid gap-6 lg:grid-cols-[1.15fr_0.85fr] lg:items-stretch">
                    <div className="rounded-3xl border border-slate-200 bg-white p-8 shadow-sm transition duration-300 hover:shadow-md sm:p-10">
                        <div className="inline-flex items-center gap-2 rounded-full bg-blue-50 px-3 py-1.5 text-sm font-semibold text-blue-700">
                            <ShieldCheck size={16} />
                            About Trinetra AI
                        </div>

                        <h1 className="mt-6 text-4xl font-bold tracking-tight text-slate-900 sm:text-5xl">
                            Trinetra AI
                        </h1>

                        <p className="mt-2 text-base font-medium text-blue-700 sm:text-lg">
                            AI-Powered Threat Detection System
                        </p>

                        <p className="mt-5 max-w-2xl text-base leading-7 text-slate-600 sm:text-lg">
                            Trinetra AI analyzes suspicious URLs using multiple cybersecurity
                            intelligence providers and Artificial Intelligence to help users
                            identify malicious websites.
                        </p>

                        <div className="mt-7 flex flex-wrap gap-3">
                            <span className="rounded-full border border-slate-200 bg-slate-50 px-3 py-1.5 text-sm font-medium text-slate-700">
                                Multi-source analysis
                            </span>
                            <span className="rounded-full border border-slate-200 bg-slate-50 px-3 py-1.5 text-sm font-medium text-slate-700">
                                Evidence-backed assessment
                            </span>
                        </div>
                    </div>

                    <div className="rounded-3xl border border-slate-200 bg-slate-50 p-8 shadow-sm transition duration-300 hover:shadow-md sm:p-10">
                        <div className="flex items-center justify-center rounded-2xl bg-white p-6 shadow-sm ring-1 ring-slate-200">
                            <div className="flex h-24 w-24 items-center justify-center rounded-full bg-blue-50 text-blue-700">
                                <Shield size={44} strokeWidth={1.7} />
                            </div>
                        </div>

                        <div className="mt-6 space-y-3">
                            <div className="flex items-center gap-3 rounded-2xl bg-white px-4 py-3 ring-1 ring-slate-200">
                                <ShieldCheck className="text-blue-700" size={18} />
                                <span className="text-sm font-medium text-slate-700">Security-first URL review</span>
                            </div>
                            <div className="flex items-center gap-3 rounded-2xl bg-white px-4 py-3 ring-1 ring-slate-200">
                                <Search className="text-blue-700" size={18} />
                                <span className="text-sm font-medium text-slate-700">Threat signals pulled from trusted providers</span>
                            </div>
                            <div className="flex items-center gap-3 rounded-2xl bg-white px-4 py-3 ring-1 ring-slate-200">
                                <FileText className="text-blue-700" size={18} />
                                <span className="text-sm font-medium text-slate-700">Readable security summary and report output</span>
                            </div>
                        </div>
                    </div>
                </section>

                <section className="mt-8 rounded-3xl border border-slate-200 bg-slate-50 p-6 shadow-sm transition duration-300 hover:shadow-md sm:p-8">
                    <div className="flex items-center gap-2 text-sm font-semibold uppercase tracking-[0.18em] text-blue-700">
                        <ShieldCheck size={16} />
                        Mission
                    </div>

                    <div className="mt-4 grid gap-4 md:grid-cols-2 xl:grid-cols-4">
                        {missionPoints.map((item) => (
                            <div key={item} className="rounded-2xl border border-slate-200 bg-white p-4">
                                <div className="flex items-start gap-3">
                                    <span className="mt-0.5 flex h-8 w-8 items-center justify-center rounded-lg bg-blue-50 text-blue-700">
                                        <Check size={16} />
                                    </span>
                                    <p className="text-sm leading-6 text-slate-700">{item}</p>
                                </div>
                            </div>
                        ))}
                    </div>
                </section>

                <section className="mt-8">
                    <div className="mb-4 flex items-center gap-2 text-sm font-semibold uppercase tracking-[0.18em] text-blue-700">
                        <Search size={16} />
                        Key Features
                    </div>

                    <div className="grid gap-4 sm:grid-cols-2 xl:grid-cols-4">
                        {features.map((item) => {
                            const Icon = item.icon;

                            return (
                                <div
                                    key={item.title}
                                    className="rounded-2xl border border-slate-200 bg-slate-50 p-5 shadow-sm transition duration-300 hover:-translate-y-0.5 hover:shadow-md"
                                >
                                    <div className="flex h-11 w-11 items-center justify-center rounded-xl bg-white text-blue-700 ring-1 ring-slate-200">
                                        <Icon size={18} />
                                    </div>
                                    <p className="mt-4 text-sm font-semibold text-slate-900">{item.title}</p>
                                </div>
                            );
                        })}
                    </div>
                </section>

                <section className="mt-8 rounded-3xl border border-slate-200 bg-white p-6 shadow-sm transition duration-300 hover:shadow-md sm:p-8">
                    <div className="flex items-center gap-2 text-sm font-semibold uppercase tracking-[0.18em] text-blue-700">
                        <Activity size={16} />
                        How It Works
                    </div>

                    <div className="mt-6 flex flex-col items-stretch gap-3 xl:flex-row xl:items-center xl:justify-between">
                        {workflow.map((step, index) => (
                            <div key={step} className="flex flex-1 items-center gap-3">
                                <div className="rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3 text-center text-sm font-semibold text-slate-800">
                                    {step}
                                </div>
                                {index < workflow.length - 1 ? (
                                    <div className="hidden text-blue-700 xl:block">
                                        <ArrowDown size={18} />
                                    </div>
                                ) : null}
                            </div>
                        ))}
                    </div>

                    <div className="mt-4 flex items-center justify-center text-blue-700 xl:hidden">
                        <ArrowDown size={18} />
                    </div>
                </section>

                <section className="mt-8 rounded-3xl border border-slate-200 bg-slate-50 p-6 shadow-sm transition duration-300 hover:shadow-md sm:p-8">
                    <div className="flex items-center gap-2 text-sm font-semibold uppercase tracking-[0.18em] text-blue-700">
                        <Server size={16} />
                        Technologies Used
                    </div>

                    <div className="mt-5 grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
                        {technologies.map((tech) => (
                            <div
                                key={tech}
                                className="rounded-2xl border border-slate-200 bg-white px-4 py-3 text-sm font-medium text-slate-700 shadow-sm"
                            >
                                {tech}
                            </div>
                        ))}
                    </div>
                </section>

                <footer className="mt-8 rounded-3xl border border-slate-200 bg-white px-6 py-6 text-center shadow-sm sm:px-8">
                    <p className="text-lg font-semibold text-slate-900">Trinetra AI</p>
                    <p className="mt-1 text-sm text-blue-700">AI-Powered Threat Detection System</p>
                    <p className="mt-3 text-sm leading-6 text-slate-600">
                        Developed as a cybersecurity research project.
                    </p>
                </footer>
            </main>
        </div>
    );
}