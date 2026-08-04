import { motion } from "framer-motion";

const providers = [
  "VirusTotal",
  "Google Safe Browsing",
  "RDAP",
  "URLScan",
  "Gemini AI",
];

export default function ScanLoader({ step = 0 }) {
  return (
    <div className="bg-white rounded-3xl border border-slate-200 shadow-xl p-8">

      <h2 className="text-2xl font-bold mb-8">

        AI Threat Analysis

      </h2>

      {providers.map((provider, index) => (

        <motion.div

          key={provider}

          initial={{ opacity: 0, x: -20 }}

          animate={{
            opacity: 1,
            x: 0,
          }}

          transition={{
            delay: index * .15,
          }}

          className="flex items-center justify-between mb-5"

        >

          <span className="font-medium">

            {provider}

          </span>

          {index < step ? (

            <span className="text-green-600 font-bold">

              ✓ Complete

            </span>

          ) : index === step ? (

            <motion.div

              animate={{
                rotate: 360,
              }}

              transition={{
                repeat: Infinity,
                duration: 1,
                ease: "linear",
              }}

              className="w-5 h-5 border-2 border-blue-600 border-t-transparent rounded-full"

            />

          ) : (

            <span className="text-slate-400">

              Waiting...

            </span>

          )}

        </motion.div>

      ))}

    </div>
  );
}