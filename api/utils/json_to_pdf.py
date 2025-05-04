from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas

def generate_pdf_from_json(cv_json: dict, filename: str):
    c = canvas.Canvas(filename, pagesize=LETTER)
    width, height = LETTER
    y = height - 40

    for section, content in cv_json.items():
        c.setFont("Helvetica-Bold", 14)
        c.drawString(40, y, section.capitalize())
        y -= 20

        c.setFont("Helvetica", 12)
        for line in content.split('\n'):
            if y < 50:
                c.showPage()
                y = height - 40
            c.drawString(60, y, line.strip())
            y -= 15

        y -= 20

    c.save()
