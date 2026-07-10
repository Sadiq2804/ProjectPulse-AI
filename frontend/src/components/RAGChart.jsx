import {
  ResponsiveContainer,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  Cell,
} from "recharts";

export default function RAGChart({ health }) {
  if (!health) return null;

  const data = [
    { name: "Green", value: health.green_tasks, color: "#22c55e" },
    { name: "Yellow", value: health.yellow_tasks, color: "#eab308" },
    { name: "Red", value: health.red_tasks, color: "#ef4444" },
  ];

  return (
    <ResponsiveContainer width="100%" height={320}>
      <BarChart data={data}>
        <CartesianGrid stroke="#444" strokeDasharray="3 3" />
        <XAxis dataKey="name" stroke="#ffffff" />
        <YAxis stroke="#ffffff" />
        <Tooltip />
        <Bar dataKey="value" radius={[8, 8, 0, 0]}>
          {data.map((entry, index) => (
            <Cell key={index} fill={entry.color} />
          ))}
        </Bar>
      </BarChart>
    </ResponsiveContainer>
  );
}