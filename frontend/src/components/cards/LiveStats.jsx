import { motion } from "framer-motion";
import {
  HiShieldCheck,
  HiLightningBolt,
  HiClock,
  HiChip,
} from "react-icons/hi";

export default function LiveStats() {

  const cards = [

    {
      title: "Threat Engines",
      value: "5",
      icon: <HiShieldCheck className="text-blue-600 text-3xl" />,
      bg: "bg-blue-50"
    },

    {
      title: "Detection Accuracy",
      value: "99%",
      icon: <HiLightningBolt className="text-green-600 text-3xl" />,
      bg: "bg-green-50"
    },

    {
      title: "Average Scan",
      value: "2.1 sec",
      icon: <HiClock className="text-orange-500 text-3xl" />,
      bg: "bg-orange-50"
    },

    {
      title: "AI Model",
      value: "Gemini",
      icon: <HiChip className="text-purple-600 text-3xl" />,
      bg: "bg-purple-50"
    }

  ];

  return (

    <div className="grid md:grid-cols-2 xl:grid-cols-4 gap-6">

      {cards.map((card) => (

        <motion.div

          key={card.title}

          whileHover={{
            y: -6,
            scale: 1.02
          }}

          transition={{
            duration: .2
          }}

          className="bg-white rounded-3xl shadow-lg border border-slate-200 p-8"

        >

          <div className={`${card.bg} w-16 h-16 rounded-2xl flex items-center justify-center`}>

            {card.icon}

          </div>

          <h2 className="mt-6 text-4xl font-bold text-slate-900">

            {card.value}

          </h2>

          <p className="mt-2 text-slate-500">

            {card.title}

          </p>

        </motion.div>

      ))}

    </div>

  );

}