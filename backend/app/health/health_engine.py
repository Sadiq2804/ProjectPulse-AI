from collections import Counter


class HealthEngine:

    def __init__(self, project_data: dict):
        self.data = project_data


    def calculate(self):

        tasks = self.data.get("tasks", [])
        summary = self.data.get("summary", {})


        rag_counter = Counter()


        completed = 0
        in_progress = 0
        not_started = 0

        overdue = 0
        critical = 0

        total_progress = 0


        # -----------------------------
        # Task Analysis
        # -----------------------------

        for task in tasks:

            rag = (
                task.get("rag") or ""
            ).strip().lower()


            if rag:
                rag_counter[rag] += 1



            progress = (
                task.get("percent_complete", 0)
                or 0
            )

            total_progress += progress



            status = (
                task.get("status") or ""
            ).lower()


            if "completed" in status:
                completed += 1


            elif "progress" in status:
                in_progress += 1


            elif "not" in status:
                not_started += 1



            schedule = (
                task.get("schedule_health")
                or ""
            ).lower()


            if "red" in schedule:
                overdue += 1



            task_name = (
                task.get("task_name")
                or ""
            ).lower()


            if "critical" in task_name:
                critical += 1



        # -----------------------------
        # Progress Calculation
        # -----------------------------

        avg_progress = (

            round(
                (total_progress / len(tasks)),
                2
            )

            if tasks else 0

        )


        # -----------------------------
        # Additional Indicators
        # -----------------------------

        budget_status = (
            self.data.get("budget_status")
        )


        milestone_health = (
            self.data.get("milestone_health")
        )


        stakeholder_sentiment = (
            self.data.get(
                "stakeholder_sentiment"
            )
        )


        blockers = (
            self.data.get(
                "blockers",
                []
            )
        )



        # -----------------------------
        # Dynamic RAG Score
        # -----------------------------

        score = 100


        factors_used = []



        # Schedule factor

        factors_used.append(
            "schedule"
        )

        score -= (
            rag_counter["red"] * 5
        )

        score -= (
            overdue * 2
        )



        # Progress factor

        factors_used.append(
            "progress"
        )


        if avg_progress < 30:

            score -= 15


        elif avg_progress < 60:

            score -= 8



        # Milestone factor
        if milestone_health:

            factors_used.append(
                "milestone"
            )


            if str(
                milestone_health
            ).lower() == "red":

                score -= 10



        # Budget factor

        if budget_status:

            factors_used.append(
                "budget"
            )


            if str(
                budget_status
            ).lower() == "red":

                score -= 10



        # Blocker factor

        if blockers:

            factors_used.append(
                "blockers"
            )

            score -= (
                len(blockers) * 3
            )



        # Sentiment factor

        if stakeholder_sentiment:

            factors_used.append(
                "sentiment"
            )


            sentiment = (
                str(
                    stakeholder_sentiment
                ).lower()
            )


            if "negative" in sentiment:

                score -= 5



        score = max(
            score,
            0
        )



        # -----------------------------
        # Final RAG
        # -----------------------------

        if score >= 80:

            health = "Green"


        elif score >= 60:

            health = "Amber"


        else:

            health = "Red"



        return {


            "overall_health":
                health,


            "health_score":
                score,


            "progress_percent":
                avg_progress,


            "green_tasks":
                rag_counter["green"],


            "yellow_tasks":
                rag_counter["yellow"],


            "red_tasks":
                rag_counter["red"],


            "completed_tasks":
                summary.get(
                    "completed",
                    completed
                ),


            "in_progress_tasks":
                summary.get(
                    "in_progress",
                    in_progress
                ),


            "not_started_tasks":
                summary.get(
                    "not_started",
                    not_started
                ),


            "critical_tasks":
                critical,


            "overdue_tasks":
                overdue,


            # New assignment fields

            "budget_status":
                budget_status
                if budget_status
                else "Not Available",


            "milestone_health":
                milestone_health
                if milestone_health
                else "Not Available",


            "stakeholder_sentiment":
                stakeholder_sentiment
                if stakeholder_sentiment
                else "Not Available",


            "blockers":
                blockers,


            "scoring_factors_used":
                factors_used,

        }