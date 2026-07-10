from pydantic import BaseModel
from typing import List


class ProjectInfo(BaseModel):
    name: str | None = None
    manager: str | None = None
    start_date: str | None = None
    end_date: str | None = None


class SummaryMetrics(BaseModel):
    not_started: int = 0
    in_progress: int = 0
    completed: int = 0


class Task(BaseModel):
    task_name: str | None = None
    owner: str | None = None
    status: str | None = None
    schedule_health: str | None = None
    rag: str | None = None
    percent_complete: float | None = None


class Comment(BaseModel):
    comment: str
    author: str | None = None
    date: str | None = None


class ProjectModel(BaseModel):
    project: ProjectInfo
    summary: SummaryMetrics
    tasks: List[Task]
    comments: List[Comment]