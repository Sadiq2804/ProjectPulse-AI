import os

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")


def generate_summary(project_data, health_data):
    prompt = f"""
You are a Senior PMO consultant.

Analyze this project.

Project:
{project_data}

Health:
{health_data}

Generate:
1. Executive Summary
2. Key Risks
3. Positive Highlights
4. Recommendations

Maximum 250 words.
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        print("Gemini Error:", e)

        return f"""
Executive Summary

The project currently has an overall health score of {health_data['health_score']}.

Current Progress:
- Completed Tasks: {health_data['completed_tasks']}
- In Progress: {health_data['in_progress_tasks']}
- Not Started: {health_data['not_started_tasks']}

Key Risks:
- Red Tasks: {health_data['red_tasks']}
- Yellow Tasks: {health_data['yellow_tasks']}
- Overdue Tasks: {health_data['overdue_tasks']}

Recommendations:
• Prioritize overdue tasks.
• Review high-risk activities.
• Increase monitoring of delayed milestones.
"""