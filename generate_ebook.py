"""
Ebook PDF Generator — The Somatic Reset Series & All Series
Generates professional PDFs with Poppins font, cover pages, disclaimers, TOC, chapters.
"""

from reportlab.lib.pagesizes import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    HRFlowable, KeepTogether
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate
from reportlab.pdfgen import canvas
import os

# ── Font Registration ─────────────────────────────────────────────────────────
FONT_DIR = os.path.join(os.path.dirname(__file__), "fonts")

pdfmetrics.registerFont(TTFont("Poppins", os.path.join(FONT_DIR, "Poppins-Regular.ttf")))
pdfmetrics.registerFont(TTFont("Poppins-Bold", os.path.join(FONT_DIR, "Poppins-Bold.ttf")))
pdfmetrics.registerFont(TTFont("Poppins-Italic", os.path.join(FONT_DIR, "Poppins-Italic.ttf")))
pdfmetrics.registerFont(TTFont("Poppins-SemiBold", os.path.join(FONT_DIR, "Poppins-SemiBold.ttf")))
pdfmetrics.registerFont(TTFont("Poppins-Light", os.path.join(FONT_DIR, "Poppins-Light.ttf")))

PAGE_W = 6 * inch
PAGE_H = 9 * inch
MARGIN = 0.85 * inch


# ── Styles ────────────────────────────────────────────────────────────────────
def get_styles(accent_hex):
    accent = colors.HexColor(accent_hex)
    dark   = colors.HexColor("#1A1A2E")
    mid    = colors.HexColor("#4A4A6A")

    return {
        "body": ParagraphStyle(
            "body", fontName="Poppins", fontSize=10.5, leading=18,
            textColor=dark, alignment=TA_JUSTIFY, spaceAfter=10
        ),
        "body_light": ParagraphStyle(
            "body_light", fontName="Poppins-Light", fontSize=10.5, leading=18,
            textColor=dark, alignment=TA_JUSTIFY, spaceAfter=10
        ),
        "h1": ParagraphStyle(
            "h1", fontName="Poppins-Bold", fontSize=22, leading=30,
            textColor=accent, spaceBefore=24, spaceAfter=12, alignment=TA_LEFT
        ),
        "h2": ParagraphStyle(
            "h2", fontName="Poppins-SemiBold", fontSize=15, leading=22,
            textColor=dark, spaceBefore=18, spaceAfter=8, alignment=TA_LEFT
        ),
        "h3": ParagraphStyle(
            "h3", fontName="Poppins-SemiBold", fontSize=12, leading=18,
            textColor=mid, spaceBefore=12, spaceAfter=6, alignment=TA_LEFT
        ),
        "intro": ParagraphStyle(
            "intro", fontName="Poppins-Italic", fontSize=11.5, leading=20,
            textColor=mid, alignment=TA_JUSTIFY, spaceAfter=14
        ),
        "disclaimer": ParagraphStyle(
            "disclaimer", fontName="Poppins", fontSize=9, leading=15,
            textColor=colors.HexColor("#888888"), alignment=TA_JUSTIFY, spaceAfter=8
        ),
        "toc_entry": ParagraphStyle(
            "toc_entry", fontName="Poppins", fontSize=11, leading=22,
            textColor=dark, spaceAfter=4
        ),
        "toc_title": ParagraphStyle(
            "toc_title", fontName="Poppins-Bold", fontSize=18, leading=26,
            textColor=accent, spaceAfter=20, spaceBefore=10
        ),
        "callout": ParagraphStyle(
            "callout", fontName="Poppins-Italic", fontSize=11, leading=18,
            textColor=accent, leftIndent=20, rightIndent=20,
            spaceBefore=12, spaceAfter=12, alignment=TA_CENTER
        ),
        "bullet": ParagraphStyle(
            "bullet", fontName="Poppins", fontSize=10.5, leading=18,
            textColor=dark, leftIndent=18, spaceAfter=5,
            bulletIndent=6, bulletFontName="Poppins"
        ),
    }


# ── Cover Page ────────────────────────────────────────────────────────────────
def draw_cover(c, doc, title, subtitle, series_name, accent_hex, bg_hex):
    w, h = PAGE_W, PAGE_H
    c.saveState()

    # Background
    c.setFillColor(colors.HexColor(bg_hex))
    c.rect(0, 0, w, h, fill=1, stroke=0)

    # Accent block top
    c.setFillColor(colors.HexColor(accent_hex))
    c.rect(0, h - 1.4 * inch, w, 1.4 * inch, fill=1, stroke=0)

    # Accent block bottom
    c.rect(0, 0, w, 0.9 * inch, fill=1, stroke=0)

    # Series name in top block
    c.setFillColor(colors.white)
    c.setFont("Poppins", 10)
    c.drawCentredString(w / 2, h - 0.75 * inch, series_name.upper())

    # Title
    c.setFillColor(colors.HexColor("#1A1A2E"))
    title_lines = wrap_text_to_lines(title, 26)
    y = h - 2.4 * inch
    for line in title_lines:
        c.setFont("Poppins-Bold", 28 if len(title) < 40 else 22)
        c.drawCentredString(w / 2, y, line)
        y -= 38

    # Divider
    c.setStrokeColor(colors.HexColor(accent_hex))
    c.setLineWidth(2)
    c.line(MARGIN, y - 10, w - MARGIN, y - 10)
    y -= 34

    # Subtitle
    if subtitle:
        sub_lines = wrap_text_to_lines(subtitle, 38)
        c.setFillColor(colors.HexColor("#4A4A6A"))
        for line in sub_lines:
            c.setFont("Poppins-Italic", 12)
            c.drawCentredString(w / 2, y, line)
            y -= 20

    # Bottom accent bar text
    c.setFillColor(colors.white)
    c.setFont("Poppins", 9)
    c.drawCentredString(w / 2, 0.34 * inch, "educationalpurposes only  ·  not professional advice")

    c.restoreState()


def wrap_text_to_lines(text, max_chars):
    words = text.split()
    lines, current = [], ""
    for word in words:
        if len(current) + len(word) + 1 <= max_chars:
            current = (current + " " + word).strip()
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


# ── Page Numbers ──────────────────────────────────────────────────────────────
def add_page_number(c, doc):
    c.saveState()
    c.setFont("Poppins", 8)
    c.setFillColor(colors.HexColor("#AAAAAA"))
    c.drawCentredString(PAGE_W / 2, 0.45 * inch, str(doc.page))
    c.restoreState()


# ── Main Generator ────────────────────────────────────────────────────────────
def generate_ebook(output_path, book_data):
    """
    book_data = {
        "title": str,
        "subtitle": str,
        "series_name": str,
        "accent_hex": str,    e.g. "#4FC3F7"
        "bg_hex": str,        e.g. "#F0F8FF"
        "disclaimer": str,
        "chapters": [
            {
                "title": str,
                "intro": str,         (optional italic opener)
                "sections": [
                    {"heading": str, "body": [str, ...]},
                    ...
                ],
                "callout": str,       (optional pull quote)
            },
            ...
        ]
    }
    """
    S = get_styles(book_data["accent_hex"])
    story = []

    # ── COVER (first page drawn via canvas) ───────────────────────────────────
    class CoverDocTemplate(BaseDocTemplate):
        def __init__(self, filename, **kwargs):
            super().__init__(filename, **kwargs)
            frame = Frame(MARGIN, MARGIN, PAGE_W - 2*MARGIN, PAGE_H - 2*MARGIN, id="normal")
            cover_template = PageTemplate(id="Cover", frames=[frame], onPage=self._draw_cover)
            main_template  = PageTemplate(id="Main",  frames=[frame], onPage=add_page_number)
            self.addPageTemplates([cover_template, main_template])

        def _draw_cover(self, c, doc):
            draw_cover(
                c, doc,
                book_data["title"],
                book_data.get("subtitle", ""),
                book_data["series_name"],
                book_data["accent_hex"],
                book_data["bg_hex"]
            )

    doc = CoverDocTemplate(
        output_path,
        pagesize=(PAGE_W, PAGE_H),
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=MARGIN, bottomMargin=MARGIN,
        title=book_data["title"],
    )

    # Cover placeholder — just a page break, canvas draws the cover
    from reportlab.platypus import NextPageTemplate
    story.append(NextPageTemplate("Main"))
    story.append(PageBreak())

    # ── DISCLAIMER PAGE ────────────────────────────────────────────────────────
    story.append(Spacer(1, 1.2 * inch))
    story.append(Paragraph("Disclaimer", S["h2"]))
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#DDDDDD"), spaceAfter=12))
    for para in book_data["disclaimer"].strip().split("\n\n"):
        story.append(Paragraph(para.strip(), S["disclaimer"]))
    story.append(PageBreak())

    # ── TABLE OF CONTENTS ──────────────────────────────────────────────────────
    story.append(Spacer(1, 0.6 * inch))
    story.append(Paragraph("Contents", S["toc_title"]))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor(book_data["accent_hex"]), spaceAfter=16))
    for i, ch in enumerate(book_data["chapters"], 1):
        story.append(Paragraph(f"{i}.  {ch['title']}", S["toc_entry"]))
    story.append(PageBreak())

    # ── CHAPTERS ──────────────────────────────────────────────────────────────
    for ch in book_data["chapters"]:
        story.append(Paragraph(ch["title"], S["h1"]))
        story.append(HRFlowable(width="40%", thickness=2, color=colors.HexColor(book_data["accent_hex"]), spaceAfter=10))

        if ch.get("intro"):
            story.append(Paragraph(ch["intro"], S["intro"]))

        for section in ch.get("sections", []):
            if section.get("heading"):
                story.append(Paragraph(section["heading"], S["h2"]))
            for para in section.get("body", []):
                if para.startswith("• "):
                    story.append(Paragraph(para, S["bullet"]))
                else:
                    story.append(Paragraph(para, S["body"]))

        if ch.get("callout"):
            story.append(Spacer(1, 8))
            story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#EEEEEE")))
            story.append(Paragraph(f'"{ch["callout"]}"', S["callout"]))
            story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#EEEEEE")))
            story.append(Spacer(1, 8))

        story.append(PageBreak())

    doc.build(story)
    print(f"✓ Generated: {os.path.basename(output_path)}")
