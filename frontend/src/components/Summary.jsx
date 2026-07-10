import {
    Paper,
    Typography
} from "@mui/material";

export default function Summary({ summary }){

    if(!summary) return null;

    return(

        <Paper sx={{p:3,mt:4}}>

            <Typography
                variant="h5"
            >

                AI Executive Summary

            </Typography>

            <Typography
                sx={{whiteSpace:"pre-wrap"}}
            >

                {summary}

            </Typography>

        </Paper>

    );

}