import {
    PieChart,
    Pie,
    Cell,
    Tooltip
} from "recharts";

export default function Charts({ health }) {

    if (!health) return null;

    const data = [

        {
            name:"Completed",
            value:health.completed_tasks
        },

        {
            name:"In Progress",
            value:health.in_progress_tasks
        },

        {
            name:"Not Started",
            value:health.not_started_tasks
        }

    ];

    return(

        <div style={{marginTop:40}}>

            <PieChart
                width={500}
                height={300}
            >

                <Pie

                    data={data}

                    dataKey="value"

                    outerRadius={100}

                    label

                >

                    <Cell fill="#4caf50"/>

                    <Cell fill="#ff9800"/>

                    <Cell fill="#f44336"/>

                </Pie>

                <Tooltip/>

            </PieChart>

        </div>

    );

}