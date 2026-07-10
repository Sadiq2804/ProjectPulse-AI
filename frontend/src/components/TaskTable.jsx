import {
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
  Typography,
  Chip,
} from "@mui/material";

export default function TaskTable({ tasks }) {
  if (!tasks || tasks.length === 0) return null;

  const getColor = (rag) => {
    switch ((rag || "").toLowerCase()) {
      case "green":
        return "success";
      case "yellow":
        return "warning";
      case "red":
        return "error";
      default:
        return "default";
    }
  };

  return (
    <Paper sx={{ mt: 4, p: 2 }}>
      <Typography variant="h5" gutterBottom>
        📋 Project Tasks
      </Typography>

      <TableContainer>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell><strong>Task</strong></TableCell>
              <TableCell><strong>Status</strong></TableCell>
              <TableCell><strong>Owner</strong></TableCell>
              <TableCell><strong>Progress</strong></TableCell>
              <TableCell><strong>RAG</strong></TableCell>
            </TableRow>
          </TableHead>

          <TableBody>
            {tasks.slice(0, 10).map((task, index) => (
              <TableRow key={index}>
                <TableCell>{task.task_name}</TableCell>
                <TableCell>{task.status}</TableCell>
                <TableCell>{task.owner || "-"}</TableCell>
                <TableCell>
                  {Math.round((task.percent_complete || 0) * 100)}%
                </TableCell>
                <TableCell>
                  <Chip
                    label={task.rag || "N/A"}
                    color={getColor(task.rag)}
                  />
                </TableCell>
              </TableRow>
            ))}
          </TableBody>

        </Table>
      </TableContainer>
    </Paper>
  );
}