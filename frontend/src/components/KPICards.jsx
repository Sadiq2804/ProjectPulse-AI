import {
  Card,
  CardContent,
  Grid,
  Typography
} from "@mui/material";

import MonitorHeartIcon from "@mui/icons-material/MonitorHeart";
import TrendingUpIcon from "@mui/icons-material/TrendingUp";
import WarningAmberIcon from "@mui/icons-material/WarningAmber";
import ReportProblemIcon from "@mui/icons-material/ReportProblem";

export default function KPICards({ health }) {

  if (!health) return null;

  const cards = [

    {
      title: "Health Score",
      value: health.health_score,
      icon: <MonitorHeartIcon fontSize="large"/>,
      color:"#2e7d32"
    },

    {
      title:"Progress %",
      value:health.progress_percent,
      icon:<TrendingUpIcon fontSize="large"/>,
      color:"#1565c0"
    },

    {
      title:"Overdue",
      value:health.overdue_tasks,
      icon:<WarningAmberIcon fontSize="large"/>,
      color:"#ef6c00"
    },

    {
      title:"Overall",
      value:health.overall_health,
      icon:<ReportProblemIcon fontSize="large"/>,
      color:"#c62828"
    }

  ];

  return(

    <Grid container spacing={3} sx={{mb:4}}>

      {cards.map((card,index)=>(

        <Grid item xs={12} md={3} key={index}>

          <Card
            sx={{
              background:card.color,
              color:"white",
              borderRadius:3,
              boxShadow:6
            }}
          >

            <CardContent>

              {card.icon}

              <Typography
                variant="h6"
                sx={{mt:1}}
              >
                {card.title}
              </Typography>

              <Typography
                variant="h3"
                fontWeight="bold"
              >
                {card.value}
              </Typography>

            </CardContent>

          </Card>

        </Grid>

      ))}

    </Grid>

  );

}