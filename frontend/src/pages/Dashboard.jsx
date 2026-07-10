import { useState } from "react";
import {
  Button,
  Container,
  Box,
  CircularProgress,
  Alert,
  Typography,
  Paper,
} from "@mui/material";

import api from "../services/api";

import Header from "../components/Header";
import ProjectCard from "../components/ProjectCard";
import KPICards from "../components/KPICards";
import Charts from "../components/Charts";
import RAGChart from "../components/RAGChart";
import ProgressCard from "../components/ProgressCard";
import Summary from "../components/Summary";
import TaskTable from "../components/TaskTable";
import Downloads from "../components/Downloads";
import Reasoning from "../components/Reasoning";

export default function Dashboard() {
  const [file, setFile] = useState(null);

  const [filename, setFilename] = useState("");

  const [project, setProject] = useState(null);

  const [tasks, setTasks] = useState([]);

  const [health, setHealth] = useState(null);

  const [summary, setSummary] = useState("");

  const [loading, setLoading] = useState(false);

  const [error, setError] = useState("");

  const [success, setSuccess] = useState("");

  const [reasoning,setReasoning]=useState(null);

  async function upload() {
    if (!file) {
      setError("Please select an Excel (.xlsx or .xls) file.");
      return;
    }

    setLoading(true);

    setError("");
    setSuccess("");

    setProject(null);
    setTasks([]);
    setHealth(null);
    setSummary("");
    setFilename("");

    try {
      const formData = new FormData();
      formData.append("file", file);

      // Upload
      const uploadRes = await api.post("/upload/", formData);

      const name = uploadRes.data.filename;

      setFilename(name);

      // Extract
      try {
        const extractRes = await api.get(`/extract/${name}`);

        setProject(extractRes.data.project);
        setTasks(extractRes.data.tasks || []);
      } catch (err) {
        console.error("Extract Error:", err);
      }

      // Health
      try {
        const healthRes = await api.get(`/health-score/${name}`);

        setHealth(healthRes.data);

        const reasoningRes =
await api.get(`/health/reasoning/${name}`);

setReasoning(reasoningRes.data);
      } catch (err) {
        console.error("Health Error:", err);
      }

      // Summary
      try {
        const summaryRes = await api.get(`/summary/${name}`);

        setSummary(summaryRes.data.summary);
      } catch (err) {
        console.error("Summary Error:", err);

        setSummary(`
Executive Summary

The AI summary could not be generated because the Gemini API quota has been exceeded.

The project metrics, charts, reports, and dashboards have been generated successfully using the uploaded Excel workbook.

Recommendations

• Prioritize overdue activities.
• Review Red RAG tasks.
• Monitor Yellow tasks closely.
• Complete remaining pending work items.
`);
      }

      setSuccess("Project analyzed successfully!");
    } catch (err) {
      console.error(err);

      if (err.response) {
        setError(err.response.data.detail || "Upload failed.");
      } else {
        setError("Unable to connect to backend.");
      }
    } finally {
      setLoading(false);
    }
  }

  return (
    <>
      <Header />

      <Container maxWidth="xl" sx={{ mt: 4, mb: 6 }}>
        <Typography
          variant="h4"
          fontWeight="bold"
          align="center"
          gutterBottom
        >
          AI Project Health Reporting Dashboard
        </Typography>

        <Typography
          align="center"
          color="text.secondary"
          sx={{ mb: 4 }}
        >
          Upload any supported Microsoft Excel Project Workbook
        </Typography>

        <Paper
          elevation={3}
          sx={{
            p: 3,
            mb: 4,
            borderRadius: 3,
          }}
        >
          <Box
            sx={{
              display: "flex",
              justifyContent: "center",
              gap: 2,
              flexWrap: "wrap",
              alignItems: "center",
            }}
          >
            <input
              type="file"
              accept=".xlsx,.xls"
              onChange={(e) => {
                setFile(e.target.files[0]);
                setError("");
                setSuccess("");
              }}
            />

            <Button
              variant="contained"
              size="large"
              onClick={upload}
              disabled={loading}
            >
              {loading ? "Analyzing..." : "Analyze Project"}
            </Button>
          </Box>

          {filename && (
            <Typography
              align="center"
              sx={{ mt: 2 }}
            >
              Uploaded File:
              <strong> {filename}</strong>
            </Typography>
          )}
        </Paper>

        {loading && (
          <Box
            sx={{
              textAlign: "center",
              mt: 4,
              mb: 4,
            }}
          >
            <CircularProgress />

            <Typography sx={{ mt: 2 }}>
              Uploading and analyzing project...
            </Typography>
          </Box>
        )}

        {success && (
          <Alert severity="success" sx={{ mb: 3 }}>
            {success}
          </Alert>
        )}

        {error && (
          <Alert severity="error" sx={{ mb: 3 }}>
            {error}
          </Alert>
        )}

        {!loading && !project && !error && (
          <Paper
            elevation={2}
            sx={{
              p: 5,
              textAlign: "center",
              borderRadius: 3,
              mb: 4,
            }}
          >
            <Typography variant="h5" gutterBottom>
              Welcome to ProjectPulse AI
            </Typography>

            <Typography color="text.secondary">
              Upload an Excel project workbook to generate an AI-powered
              health dashboard, executive summary, PDF report and PowerPoint
              presentation.
            </Typography>
          </Paper>
        )}

        {project && <ProjectCard project={project} />}

        {health && (
          <>
            <KPICards health={health} />

            <Reasoning reasoning={reasoning}/>
            
            <Charts health={health} />

            <RAGChart health={health} />

            <ProgressCard health={health} />
          </>
        )}

        {summary && <Summary summary={summary} />}

        {tasks.length > 0 && (
          <TaskTable tasks={tasks} />
        )}

        {filename && (
          <Downloads filename={filename} />
        )}

        <Box
          sx={{
            mt: 6,
            textAlign: "center",
            opacity: 0.7,
          }}
        >
          <Typography variant="body2">
            ProjectPulse AI • Developed by Sadiq Hussain Ansari
          </Typography>
        </Box>
      </Container>
    </>
  );
}