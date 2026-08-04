export default function ReasonList({ reasons }) {
  return (
    <div className="bg-white rounded-3xl shadow-xl border border-slate-200 p-8">

      <h2 className="text-2xl font-bold mb-6">

        Why was this verdict given?

      </h2>

      <div className="space-y-4">

        {reasons.map((reason, index) => (

          <div
            key={index}
            className="border-l-4 border-blue-500 bg-slate-50 rounded-xl p-4"
          >

            {reason}

          </div>

        ))}

      </div>

    </div>
  );
}