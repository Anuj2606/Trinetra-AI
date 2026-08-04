import { useEffect, useState } from "react";
import api from "../services/api";
import Navbar from "../components/layout/Navbar";

import {
    PieChart,
    Pie,
    Cell,
    Tooltip,
    ResponsiveContainer,
    BarChart,
    Bar,
    XAxis,
    YAxis
} from "recharts";

const COLORS = [
    "#10B981",
    "#EF4444",
    "#F59E0B",
    "#3B82F6",
    "#8B5CF6"
];

export default function Analytics() {

    const [data, setData] = useState(null);

    useEffect(() => {

        api.get("/analytics")

            .then(res => setData(res.data))

            .catch(console.error);

    }, []);

    if (!data)

        return (
            <div className="p-10">

                Loading...

            </div>
        );

    return (

        <div className="min-h-screen bg-slate-100">

            <Navbar/>

            <div className="max-w-7xl mx-auto py-10">

                <h1 className="text-4xl font-bold mb-10">

                    Security Analytics

                </h1>

                <div className="grid lg:grid-cols-3 gap-6 mb-8">

                    <div className="bg-white rounded-3xl p-8 shadow">

                        <h3>Total Scans</h3>

                        <h1 className="text-5xl font-bold mt-4">

                            {data.total}

                        </h1>

                    </div>

                    <div className="bg-white rounded-3xl p-8 shadow">

                        <h3>Safe URLs</h3>

                        <h1 className="text-5xl font-bold text-green-600 mt-4">

                            {data.safe}

                        </h1>

                    </div>

                    <div className="bg-white rounded-3xl p-8 shadow">

                        <h3>Malicious URLs</h3>

                        <h1 className="text-5xl font-bold text-red-600 mt-4">

                            {data.malicious}

                        </h1>

                    </div>

                </div>

                <div className="grid lg:grid-cols-2 gap-8">

                    <div className="bg-white rounded-3xl shadow p-8">

                        <h2 className="font-bold text-2xl mb-6">

                            Safe vs Malicious

                        </h2>

                        <ResponsiveContainer width="100%" height={300}>

                            <PieChart>

                                <Pie
                                    data={[
                                        {
                                            name: "Safe",
                                            value: data.safe
                                        },
                                        {
                                            name: "Malicious",
                                            value: data.malicious
                                        }
                                    ]}
                                    dataKey="value"
                                >

                                    {COLORS.map((c, i) => (

                                        <Cell key={i} fill={c}/>

                                    ))}

                                </Pie>

                                <Tooltip/>

                            </PieChart>

                        </ResponsiveContainer>

                    </div>

                    <div className="bg-white rounded-3xl shadow p-8">

                        <h2 className="font-bold text-2xl mb-6">

                            Risk Distribution

                        </h2>

                        <ResponsiveContainer width="100%" height={300}>

                            <BarChart data={data.risk_levels}>

                                <XAxis dataKey="name"/>

                                <YAxis/>

                                <Tooltip/>

                                <Bar dataKey="value"/>

                            </BarChart>

                        </ResponsiveContainer>

                    </div>

                </div>

            </div>

        </div>

    );

}