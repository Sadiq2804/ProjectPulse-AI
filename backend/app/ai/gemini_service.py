def generate_summary(project_data, health_data):

    prompt = f"""

You are a Senior PMO Consultant.

Analyze the project health data below.

Project Information:
{project_data}


Health Assessment:
{health_data}


Generate an executive project health report.

Include:

1. Executive Summary
- Explain current project status.

2. RAG Reasoning
- Explain why the project is Green, Amber, or Red.
- Mention the factors affecting the score.

3. Key Risks
- Identify schedule risks.
- Identify blockers.
- Identify critical activities.

4. Positive Highlights
- Mention completed progress.
- Mention areas performing well.

5. Recommendations
- Provide actionable steps for leadership.


Important:

If data is unavailable, clearly mention:
"Information not available in the project plan"


Keep the response under 300 words.

"""

    try:

        response = model.generate_content(
            prompt
        )

        return response.text


    except Exception as e:

        print(
            "Gemini Error:",
            e
        )


        return f"""

Executive Summary

The project has an overall health score of:

{health_data.get('health_score')}%


Current RAG Status:

{health_data.get('overall_health')}


Reasoning:

The health score was calculated using:

- Schedule performance
- Task completion progress
- RAG task distribution
- Overdue activities


Available Indicators:

Budget:
{health_data.get('budget_status')}


Milestones:
{health_data.get('milestone_health')}


Stakeholder Sentiment:
{health_data.get('stakeholder_sentiment')}


Risks:

- Red Tasks:
{health_data.get('red_tasks')}

- Yellow Tasks:
{health_data.get('yellow_tasks')}

- Overdue Tasks:
{health_data.get('overdue_tasks')}


Recommendations:

• Monitor delayed activities.
• Review critical tasks.
• Improve milestone tracking.
• Communicate risks with stakeholders.

"""