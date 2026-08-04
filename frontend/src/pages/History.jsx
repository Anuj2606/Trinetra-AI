import { useEffect, useState } from "react";
import Navbar from "../components/layout/Navbar";
import api from "../services/api";

export default function History() {

    const [history, setHistory] = useState([]);
    const [search, setSearch] = useState("");

    useEffect(() => {

        api.get("/history")

        .then(res => setHistory(res.data))

        .catch(console.error);

    }, []);

    const filtered = history.filter(item =>
        item.url.toLowerCase().includes(search.toLowerCase())
    );

    return (

        <div className="min-h-screen bg-slate-100">

            <Navbar/>

            <div className="max-w-7xl mx-auto py-10">

                <h1 className="text-4xl font-bold mb-8">

                    Scan History

                </h1>

                <input

                    placeholder="Search URL..."

                    value={search}

                    onChange={(e)=>setSearch(e.target.value)}

                    className="w-full mb-8 rounded-xl border p-4"

                />

                <div className="bg-white rounded-3xl shadow">

                    <table className="w-full">

                        <thead className="bg-slate-50">

                            <tr>

                                <th className="p-5 text-left">URL</th>

                                <th>Risk</th>

                                <th>Level</th>

                                <th>Attack</th>

                                <th>Date</th>

                            </tr>

                        </thead>

                        <tbody>

                            {filtered.map(scan=>(

                                <tr
                                    key={scan.id}
                                    className="border-t hover:bg-slate-50"
                                >

                                    <td className="p-5">

                                        {scan.url}

                                    </td>

                                    <td>

                                        {scan.risk_score}

                                    </td>

                                    <td>

                                        {scan.risk_level}

                                    </td>

                                    <td>

                                        {scan.attack_type}

                                    </td>

                                    <td>

                                        {new Date(scan.created_at).toLocaleString()}

                                    </td>

                                </tr>

                            ))}

                        </tbody>

                    </table>

                </div>

            </div>

        </div>

    );

}