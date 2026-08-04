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

    <div className="grid gap-4 md:grid-cols-2 xl:grid-cols-4">

      {cards.map((card) => (

        <motion.div

          key={card.title}

          whileHover={{
            y: -4,
            scale: 1.01
          }}

          transition={{
            duration: .2
          }}

          className="flex min-h-[180px] flex-col justify-between rounded-2xl border border-slate-200 bg-white p-5 shadow-sm"

        >

          <div className={`${card.bg} flex h-14 w-14 items-center justify-center rounded-xl`}>

            {card.icon}

          </div>

          <div>
            <h2 className="text-2xl font-bold text-slate-900">

              {card.value}

            </h2>

            <p className="mt-1 text-sm font-medium text-slate-500">

              {card.title}

            </p>
          </div>

        </motion.div>

      ))}

    </div>

  );

}