import {
    Card,
    CardContent,
    Typography,
    List,
    ListItem
} from "@mui/material";


export default function Reasoning({reasoning}){


    if(!reasoning)
        return null;


    return (

        <Card sx={{mt:3}}>

            <CardContent>

                <Typography variant="h5">
                    Why this Health Status?
                </Typography>


                <Typography sx={{mt:2}}>
                    Status:
                    <b> {reasoning.health_status}</b>
                </Typography>


                <Typography sx={{mt:2}}>
                    Key Reasons
                </Typography>


                <List>

                {
                    reasoning.reasons.map(
                        (item,index)=>(

                        <ListItem key={index}>
                            • {item}
                        </ListItem>

                        )
                    )
                }

                </List>


                <Typography>
                    Recommended Actions
                </Typography>


                <List>

                {
                    reasoning.recommendations.map(
                        (item,index)=>(

                        <ListItem key={index}>
                            • {item}
                        </ListItem>

                        )
                    )
                }

                </List>


            </CardContent>

        </Card>

    );

}
