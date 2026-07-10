# Project Health Reporting Agent — RAG Methodology

## 1. Approach

RAG status is produced by a deterministic, weighted rules engine (not an LLM judgment call).

Gemini is used only to narrate the score in business language and interpret unstructured comments.

---

## 2. Scoring Pillars & Weights

| Pillar | Weight | Signals Used |
|---|---|---|
| Schedule Health | 40% | Progress, delays, overdue tasks |
| Execution & Blockers | 25% | On Hold tasks, critical blockers |
| Milestone Health | 20% | Phase and milestone RAG |
| Stakeholder Sentiment | 15% | Comments and feedback |
| Budget Burn | Placeholder | Enabled when budget data exists |

---

## 3. Thresholds

Green ≥ 75

Amber 50–74

Red < 50

---

## 4. Handling Missing Data

The system handles:

- Missing dates
- Missing RAG values
- Missing comments

Reports include:

- Confidence score
- Assumptions made
- Data limitations

---

## 5. Output

Every report provides:

- Health score
- RAG status
- Reasoning
- Risks
- Recommendations