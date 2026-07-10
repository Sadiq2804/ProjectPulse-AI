from pathlib import Path

import pandas as pd

from app.models.project_model import (
    Comment,
    ProjectInfo,
    ProjectModel,
    SummaryMetrics,
    Task,
)


def find_column(df, possible_names):
    """
    Finds the first matching column from a list of possible names.
    """

    columns = {}

    for col in df.columns:
        columns[str(col).strip().lower()] = col

    for possible in possible_names:

        for column in columns:

            if possible.lower() == column:
                return columns[column]

            if possible.lower() in column:
                return columns[column]

    return None


class ProjectExtractor:

    def __init__(self, filepath: str):
        self.filepath = Path(filepath)

    def extract(self):

        workbook = pd.ExcelFile(self.filepath)

        # -----------------------------
        # Detect Sheets Automatically
        # -----------------------------

        project_df = None
        summary_df = pd.DataFrame()
        comments_df = pd.DataFrame()

        for sheet in workbook.sheet_names:

            df = pd.read_excel(workbook, sheet_name=sheet)

            cols = [str(c).strip().lower() for c in df.columns]

            if (
                "task name" in cols
                or "status" in cols
                or "owner" in cols
                or "assigned to" in cols
            ):
                project_df = df

            elif (
                "project name" in cols
                or "unnamed: 1" in cols
            ):
                summary_df = df

            elif "comment" in sheet.lower():
                comments_df = df

        if project_df is None:
            raise Exception("Project task sheet not found.")

        # -----------------------------
        # Detect Columns Automatically
        # -----------------------------

        task_col = find_column(
            project_df,
            [
                "Task Name",
                "Task",
                "Activity",
                "Work Item",
            ],
        )

        owner_col = find_column(
            project_df,
            [
                "Owner",
                "Assigned To",
                "Resource",
            ],
        )

        status_col = find_column(
            project_df,
            [
                "Status",
                "Task Status",
            ],
        )

        health_col = find_column(
            project_df,
            [
                "Schedule Health",
                "Health",
                "Schedule",
            ],
        )

        rag_col = find_column(
            project_df,
            [
                "RAG",
                "Traffic Light",
                "Health",
            ],
        )

        progress_col = find_column(
            project_df,
            [
                "% Complete",
                "Progress",
                "% Done",
            ],
        )

        # -----------------------------
        # Project Information
        # -----------------------------

        project = ProjectInfo()

        for _, row in summary_df.iterrows():

            values = row.fillna("").tolist()

            if len(values) < 2:
                continue

            key = str(values[0]).strip()
            value = values[1]

            if key == "Project Manager":
                project.manager = str(value)

            elif key == "Project Start Date":
                project.start_date = str(value)

            elif key == "Project End Date":
                project.end_date = str(value)

        if task_col:

            names = project_df[task_col].dropna()

            if not names.empty:
                project.name = str(names.iloc[0])
            else:
                project.name = "Unknown Project"

        # -----------------------------
        # Summary
        # -----------------------------

        summary = SummaryMetrics()

        for _, row in summary_df.iterrows():

            values = row.fillna("").tolist()

            if len(values) < 2:
                continue

            key = str(values[0]).strip()
            value = values[1]

            try:

                if key == "Not Started":
                    summary.not_started = int(value)

                elif key == "In Progress":
                    summary.in_progress = int(value)

                elif key == "Completed":
                    summary.completed = int(value)

            except:
                pass

        # -----------------------------
        # Tasks
        # -----------------------------

        tasks = []

        for _, row in project_df.iterrows():

            if progress_col:
                percent = row.get(progress_col)
            else:
                percent = 0

            if pd.isna(percent):
                percent = 0

            tasks.append(

                Task(

                    task_name=""
                    if task_col is None or pd.isna(row.get(task_col))
                    else str(row.get(task_col)),

                    owner=""
                    if owner_col is None or pd.isna(row.get(owner_col))
                    else str(row.get(owner_col)),

                    status=""
                    if status_col is None or pd.isna(row.get(status_col))
                    else str(row.get(status_col)),

                    schedule_health=""
                    if health_col is None or pd.isna(row.get(health_col))
                    else str(row.get(health_col)),

                    rag=""
                    if rag_col is None or pd.isna(row.get(rag_col))
                    else str(row.get(rag_col)),

                    percent_complete=float(percent),

                )

            )

        # -----------------------------
        # Comments
        # -----------------------------

        comments = []

        if not comments_df.empty:

            for _, row in comments_df.iterrows():

                values = row.fillna("").tolist()

                if len(values) >= 4:

                    comments.append(

                        Comment(

                            comment=str(values[1]),

                            author=str(values[2]),

                            date=str(values[3]),

                        )

                    )

        # -----------------------------
        # Return Model
        # -----------------------------

        model = ProjectModel(

            project=project,

            summary=summary,

            tasks=tasks,

            comments=comments,

        )

        return model.model_dump(mode="json")


def extract_project_summary(filename: str):

    filepath = f"uploads/{filename}"

    extractor = ProjectExtractor(filepath)

    return extractor.extract()