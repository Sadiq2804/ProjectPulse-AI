from pathlib import Path

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate


class PDFGenerator:

    def generate(self, project, health, summary, filename):

        output_dir = Path("outputs/reports")
        output_dir.mkdir(parents=True, exist_ok=True)

        pdf_path = output_dir / f"{filename.replace('.xlsx', '')}.pdf"

        doc = SimpleDocTemplate(str(pdf_path))

        styles = getSampleStyleSheet()

        story = []

        story.append(Paragraph("<b>ProjectPulse AI Report</b>", styles["Title"]))

        story.append(
            Paragraph(
                f"<b>Project:</b> {project['project']['name']}",
                styles["Normal"],
            )
        )

        story.append(
            Paragraph(
                f"<b>Manager:</b> {project['project']['manager']}",
                styles["Normal"],
            )
        )

        story.append(
            Paragraph(
                f"<b>Overall Health:</b> {health['overall_health']}",
                styles["Normal"],
            )
        )

        story.append(
            Paragraph(
                f"<b>Health Score:</b> {health['health_score']}",
                styles["Normal"],
            )
        )

        story.append(
            Paragraph(
                f"<b>Progress:</b> {health['progress_percent']}%",
                styles["Normal"],
            )
        )

        story.append(
            Paragraph(
                "<br/><b>Executive Summary</b>",
                styles["Heading2"],
            )
        )

        story.append(
            Paragraph(summary.replace("\n", "<br/>"), styles["BodyText"])
        )

        doc.build(story)

        return str(pdf_path)