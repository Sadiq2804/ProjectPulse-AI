import {
  Card,
  CardContent,
  Typography,
  Grid
} from "@mui/material";

export default function ProjectCard({ project }) {

  if (!project) return null;

  return (

    <Card
      sx={{
        mt: 4,
        mb: 3,
        borderRadius: 3
      }}
    >

      <CardContent>

        <Typography
          variant="h5"
          gutterBottom
        >
          📁 Project Information
        </Typography>

        <Grid container spacing={2}>

          <Grid item xs={6}>
            <Typography>
              <strong>Name:</strong>
            </Typography>

            <Typography>
              {project.name}
            </Typography>
          </Grid>

          <Grid item xs={6}>
            <Typography>
              <strong>Manager:</strong>
            </Typography>

            <Typography>
              {project.manager}
            </Typography>
          </Grid>

          <Grid item xs={6}>
            <Typography>
              <strong>Start Date:</strong>
            </Typography>

            <Typography>
              {project.start_date}
            </Typography>
          </Grid>

          <Grid item xs={6}>
            <Typography>
              <strong>End Date:</strong>
            </Typography>

            <Typography>
              {project.end_date}
            </Typography>
          </Grid>

        </Grid>

      </CardContent>

    </Card>

  );

}