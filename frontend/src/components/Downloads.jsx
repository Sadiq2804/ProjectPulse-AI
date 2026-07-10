import {
Button
} from "@mui/material";

import PictureAsPdfIcon from "@mui/icons-material/PictureAsPdf";

import SlideshowIcon from "@mui/icons-material/Slideshow";

export default function Downloads({filename}){

if(!filename) return null;

return(

<div style={{marginTop:30}}>

<Button

variant="contained"

startIcon={<PictureAsPdfIcon/>}

href={`http://127.0.0.1:8000/report/${filename}`}

>

Download PDF

</Button>

<Button

variant="contained"

color="success"

sx={{ml:2}}

startIcon={<SlideshowIcon/>}

href={`http://127.0.0.1:8000/presentation/${filename}`}

>

Download PPT

</Button>

</div>

);

}