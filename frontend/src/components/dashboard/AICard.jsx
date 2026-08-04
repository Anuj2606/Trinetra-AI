export default function AICard({ summary }) {

  return (

    <div className="bg-white rounded-3xl shadow-xl border border-slate-200 p-8">

      <h2 className="text-2xl font-bold mb-5">

        Gemini AI Security Assessment

      </h2>

      <div className="leading-8 whitespace-pre-wrap text-slate-700">

        {summary}

      </div>

    </div>

  );

}