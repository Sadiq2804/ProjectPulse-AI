import {
Card,
CardContent,
Typography,
LinearProgress
} from "@mui/material";

export default function ProgressCard({health}){

if(!health) return null;

return(

<Card sx={{mt:4}}>

<CardContent>

<Typography variant="h6">

Overall Progress

</Typography>

<LinearProgress
variant="determinate"
value={health.progress_percent}
sx={{
height:15,
borderRadius:5,
mt:2
}}
/>

<Typography sx={{mt:2}}>

{health.progress_percent}%

</Typography>

</CardContent>

</Card>

);

}