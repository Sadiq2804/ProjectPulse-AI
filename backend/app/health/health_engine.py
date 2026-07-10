from collections import Counter


class HealthEngine:

    def __init__(self, project_data: dict):
        self.data = project_data

    def calculate(self):

        tasks = self.data["tasks"]
        summary = self.data["summary"]

        rag_counter = Counter()

        completed = 0
        in_progress = 0
        not_started = 0
        overdue = 0
        critical = 0

        total_progress = 0

        for task in tasks:

            rag = (task.get("rag") or "").strip().lower()

            if rag:
                rag_counter[rag] += 1

            progress = task.get("percent_complete", 0) or 0
            total_progress += progress

            status = (task.get("status") or "").lower()

            if "completed" in status:
                completed += 1

            elif "progress" in status:
                in_progress += 1

            elif "not" in status:
                not_started += 1

            schedule = (task.get("schedule_health") or "").lower()

            if "red" in schedule:
                overdue += 1

            if "critical" in task.get("task_name", "").lower():
                critical += 1

        avg_progress = (
            round((total_progress / len(tasks)) * 100, 2)
            if tasks else 0
        )

        score = 100

        score -= rag_counter["red"] * 5
        score -= rag_counter["yellow"] * 2
        score -= overdue * 2

        score = max(score, 0)

        if score >= 80:
            health = "Green"
        elif score >= 60:
            health = "Amber"
        else:
            health = "Red"

        return {

            "overall_health": health,

            "health_score": score,

            "progress_percent": avg_progress,

            "green_tasks": rag_counter["green"],

            "yellow_tasks": rag_counter["yellow"],

            "red_tasks": rag_counter["red"],

            "completed_tasks": summary["completed"],

            "in_progress_tasks": summary["in_progress"],

            "not_started_tasks": summary["not_started"],

            "critical_tasks": critical,

            "overdue_tasks": overdue,
        }