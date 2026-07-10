import {
  AppBar,
  Toolbar,
  Typography,
  Box
} from "@mui/material";

import DashboardIcon from "@mui/icons-material/Dashboard";

export default function Header() {
  return (
    <AppBar
      position="static"
      sx={{
        mb: 4,
        borderRadius: 2,
        background:
          "linear-gradient(90deg,#1565c0,#1976d2,#42a5f5)"
      }}
    >
      <Toolbar>

        <DashboardIcon sx={{ mr: 2 }} />

        <Typography
          variant="h5"
          sx={{ flexGrow: 1 }}
        >
          ProjectPulse AI
        </Typography>

        <Typography>
          AI Project Health Reporting Agent
        </Typography>

      </Toolbar>
    </AppBar>
  );
}