from pathlib import Path

from pptx import Presentation
from pptx.util import Inches, Pt


class PPTGenerator:

    def generate(self, project, health, summary, filename):

        output_dir = Path("outputs/presentations")
        output_dir.mkdir(parents=True, exist_ok=True)

        ppt_path = output_dir / f"{filename.replace('.xlsx', '')}.pptx"

        prs = Presentation()

        # -------------------------
        # Slide 1
        # -------------------------

        slide = prs.slides.add_slide(prs.slide_layouts[0])

        slide.shapes.title.text = "ProjectPulse AI"

        slide.placeholders[1].text = (
            "AI Project Health Report\n\n"
            f"{project['project']['name']}"
        )

        # -------------------------
        # Slide 2
        # -------------------------

        slide = prs.slides.add_slide(prs.slide_layouts[5])

        title = slide.shapes.title

        title.text = "Project Overview"

        textbox = slide.shapes.add_textbox(
            Inches(0.7),
            Inches(1.2),
            Inches(8),
            Inches(5),
        )

        frame = textbox.text_frame

        p = frame.add_paragraph()
        p.text = f"Project : {project['project']['name']}"
        p.font.size = Pt(22)

        p = frame.add_paragraph()
        p.text = f"Manager : {project['project']['manager']}"

        p = frame.add_paragraph()
        p.text = f"Health : {health['overall_health']}"

        p = frame.add_paragraph()
        p.text = f"Progress : {health['progress_percent']} %"

        # -------------------------
        # Slide 3
        # -------------------------

        slide = prs.slides.add_slide(prs.slide_layouts[5])

        slide.shapes.title.text = "AI Executive Summary"

        textbox = slide.shapes.add_textbox(
            Inches(0.6),
            Inches(1),
            Inches(8.5),
            Inches(5.5),
        )

        textbox.text_frame.text = summary

        prs.save(ppt_path)

        return str(ppt_path)