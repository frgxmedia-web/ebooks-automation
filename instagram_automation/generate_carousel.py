"""
Generates a 6-slide carousel + 1 story image for Instagram.

Carousel structure:
  Slide 1 — Bundle cover: series name + all 10 book titles listed
  Slide 2 — Hook: relatable opening line about the featured book's topic
  Slide 3 — Core insight #1 from the featured book
  Slide 4 — Core insight #2 (a reframe or surprising truth)
  Slide 5 — Real-life scenario (something the reader will recognise)
  Slide 6 — CTA: featured book title + "Part of the [Series] bundle"

Story (1080×1920):
  Adapted from Slide 1 — bundle cover in portrait format
"""

import os
import json
import textwrap
import random
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from groq import Groq

# ── Paths ──────────────────────────────────────────────────────────────────────
FONTS_DIR  = os.path.join(os.path.dirname(__file__), "..", "fonts")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "posts")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Constants ──────────────────────────────────────────────────────────────────
W, H = 1080, 1080          # carousel slide
SW, SH = 1080, 1920        # story

# ── Helpers ────────────────────────────────────────────────────────────────────
def hex_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def load_font(variant="Regular", size=40):
    name_map = {
        "Regular":  "Poppins-Regular.ttf",
        "Bold":     "Poppins-Bold.ttf",
        "SemiBold": "Poppins-SemiBold.ttf",
        "Italic":   "Poppins-Italic.ttf",
        "Light":    "Poppins-Light.ttf",
    }
    path = os.path.join(FONTS_DIR, name_map.get(variant, "Poppins-Regular.ttf"))
    return ImageFont.truetype(path, size)

def draw_text_centered(draw, text, font, y, color, img_w=W):
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    draw.text(((img_w - tw) // 2, y), text, font=font, fill=color)
    return bbox[3] - bbox[1]

def draw_text_wrapped_centered(draw, text, font, y, color, max_w, line_gap=12, img_w=W):
    """Wraps text and draws centered. Returns total height used."""
    avg_char = draw.textbbox((0,0), "A", font=font)[2]
    chars_per_line = max(10, max_w // max(1, avg_char))
    lines = textwrap.wrap(text, width=chars_per_line)
    font_h = draw.textbbox((0,0), "Ag", font=font)[3]
    total = 0
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        lw = bbox[2] - bbox[0]
        draw.text(((img_w - lw) // 2, y + total), line, font=font, fill=color)
        total += font_h + line_gap
    return total

def add_decorative_bg(img, ac, alpha_big=35, alpha_small=25):
    """Adds two faded accent circles to any image."""
    iw, ih = img.size
    layer = Image.new("RGBA", (iw, ih), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    r1 = int(iw * 0.44)
    d.ellipse([iw - 80 - r1, -80 - r1, iw - 80 + r1, -80 + r1], fill=(*ac, alpha_big))
    r2 = int(iw * 0.26)
    d.ellipse([60 - r2, ih + 40 - r2, 60 + r2, ih + 40 + r2], fill=(*ac, alpha_small))
    return Image.alpha_composite(img, layer)

def save_jpg(img, path):
    img.convert("RGB").save(path, "JPEG", quality=95)

# ── Gemini content generation ─────────────────────────────────────────────────
def generate_slide_content(series_config: dict, book: dict) -> dict:
    """
    Generates content for slides 2-6 about one specific book from the series.
    Returns a dict with keys: hook, insight_1, insight_2, scenario, cta_line
    """
    api_key = os.environ.get("GROQ_API_KEY", "")
    if not api_key:
        raise ValueError("GROQ_API_KEY not set")

    client = Groq(api_key=api_key)

    prompt = f"""
You're writing copy for an Instagram carousel post promoting an ebook.

Series: {series_config['name']}
Featured Book: "{book['title']}" — {book['subtitle']}
Overall series niche: {series_config['niche']}

The tone must feel like a knowledgeable friend sharing something they genuinely believe in. Not a marketer. Not a textbook. Short sentences. Real talk.

Return ONLY valid JSON with these exact keys:

"hook": One sentence (max 14 words) that opens a loop — something relatable that makes the reader go "that's me." No questions. A statement. Start with something they feel, not something generic.

"insight_1": A bold, counterintuitive truth related to this book's topic. 2–3 sentences. Concrete. Something they haven't heard phrased this way before. No fluff.

"insight_2": A second insight or reframe. 2–3 sentences. Could be a mindset shift, an overlooked fact, or a practical truth. Still warm, not clinical.

"scenario": A 2–3 sentence real-life scene — paint a picture of someone's day or moment that this book directly speaks to. The reader should see themselves in it.

"cta_line": One punchy sentence (max 12 words) that positions this book as the answer. Don't say "buy now" or "check out." Make it feel like a natural recommendation from a friend.

"caption": A complete Instagram caption for this post. 4–6 sentences. Human voice, a couple of natural emojis, no AI-speak. End with a line like "Grab the full bundle — link in bio." No hashtags.

Rules: No em-dashes. No "I" or "we". Nothing that sounds like it was generated. Short punchy sentences. Return ONLY the JSON.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.85,
        response_format={"type": "json_object"},
    )
    raw = response.choices[0].message.content.strip()
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
        raw = raw.strip()

    return json.loads(raw)


# ── SLIDE 1: Bundle cover ─────────────────────────────────────────────────────
def make_slide_bundle_cover(series_config: dict, img_w=W, img_h=H) -> Image.Image:
    """
    Cover slide: Series name + tagline + all 10 book titles listed in two columns.
    """
    ac  = hex_rgb(series_config["accent_hex"])
    bg  = (12, 12, 28)
    books = series_config["books"]

    img  = Image.new("RGBA", (img_w, img_h), (*bg, 255))
    img  = add_decorative_bg(img, ac, alpha_big=28, alpha_small=20)
    draw = ImageDraw.Draw(img)

    # Top accent bar
    bar_h = int(img_h * 0.095)
    draw.rectangle([0, 0, img_w, bar_h], fill=(*ac, 255))
    f_series = load_font("Regular", int(img_h * 0.030))
    draw_text_centered(draw, series_config["name"].upper(), f_series,
                       (bar_h - int(img_h * 0.030)) // 2, (255, 255, 255, 255), img_w)

    # "COMPLETE BUNDLE" badge
    y = bar_h + int(img_h * 0.038)
    f_badge = load_font("SemiBold", int(img_h * 0.024))
    draw_text_centered(draw, "✦  COMPLETE BUNDLE  ✦", f_badge, y, (*ac, 220), img_w)
    y += int(img_h * 0.040)

    # Tagline
    f_tag = load_font("Italic", int(img_h * 0.034))
    tag_h = draw_text_wrapped_centered(draw, f'"{series_config["bundle_tagline"]}"',
                                       f_tag, y, (220, 220, 240, 255),
                                       int(img_w * 0.78), line_gap=8, img_w=img_w)
    y += tag_h + int(img_h * 0.030)

    # Divider line
    draw.rectangle([int(img_w * 0.12), y, int(img_w * 0.88), y + 2], fill=(*ac, 140))
    y += int(img_h * 0.030)

    # 10 books — two columns
    col_x = [int(img_w * 0.06), int(img_w * 0.54)]
    f_num  = load_font("SemiBold", int(img_h * 0.022))
    f_book = load_font("Regular",  int(img_h * 0.022))
    row_gap = int(img_h * 0.051)

    for i, book in enumerate(books):
        col  = i % 2
        row  = i // 2
        bx   = col_x[col]
        by   = y + row * row_gap

        # Accent number
        num_label = f"{book['num']:02d}"
        draw.text((bx, by), num_label, font=f_num, fill=(*ac, 255))
        num_bbox = draw.textbbox((0,0), num_label, font=f_num)
        nw = num_bbox[2] - num_bbox[0] + 10

        # Title — trim if too long for column
        title = book["title"]
        max_chars = 26 if img_w == W else 22
        if len(title) > max_chars:
            title = title[:max_chars - 1] + "…"
        draw.text((bx + nw, by), title, font=f_book, fill=(230, 230, 245, 255))

    y += 5 * row_gap + int(img_h * 0.012)

    # Bottom bar
    bot_bar = int(img_h * 0.080)
    draw.rectangle([0, img_h - bot_bar, img_w, img_h], fill=(*ac, 255))
    f_handle = load_font("SemiBold", int(img_h * 0.026))
    handle = f"@{series_config['ig_page_username']}  ·  link in bio"
    draw_text_centered(draw, handle, f_handle,
                       img_h - bot_bar + (bot_bar - int(img_h * 0.026)) // 2,
                       (255, 255, 255, 255), img_w)

    return img


# ── SLIDE 2: Hook ──────────────────────────────────────────────────────────────
def make_slide_hook(book: dict, content: dict, series_config: dict) -> Image.Image:
    ac   = hex_rgb(series_config["accent_hex"])
    bg   = (12, 12, 28)
    img  = Image.new("RGBA", (W, H), (*bg, 255))
    img  = add_decorative_bg(img, ac)
    draw = ImageDraw.Draw(img)

    # Top accent bar — book number
    bar_h = 85
    draw.rectangle([0, 0, W, bar_h], fill=(*ac, 255))
    f_bar = load_font("Regular", 26)
    label = f"Book {book['num']} of 10  ·  {series_config['name'].upper()}"
    draw_text_centered(draw, label, f_bar, (bar_h - 26) // 2, (255, 255, 255, 255))

    # Opening mark
    f_quote = load_font("Bold", 130)
    draw.text((60, 80), "“", font=f_quote, fill=(*ac, 60))

    # Hook text — large, centred
    hook = content["hook"]
    f_hook = load_font("Bold", 68)
    # Measure and fit
    words = hook.split()
    if len(words) <= 4:
        f_hook = load_font("Bold", 86)
        wrap_w = 16
    elif len(words) <= 8:
        wrap_w = 20
    else:
        f_hook = load_font("Bold", 56)
        wrap_w = 24

    lines = textwrap.wrap(hook, width=wrap_w)
    fh = 68 if len(words) > 4 else 86
    f_hook = load_font("Bold", fh)
    line_h = fh + 16
    total_h = len(lines) * line_h
    y = (H - total_h) // 2 - 30

    for line in lines:
        bb = draw.textbbox((0,0), line, font=f_hook)
        lw = bb[2] - bb[0]
        # Shadow
        draw.text(((W - lw) // 2 + 2, y + 2), line, font=f_hook, fill=(0,0,0,100))
        draw.text(((W - lw) // 2, y), line, font=f_hook, fill=(255,255,255,255))
        y += line_h

    # Swipe hint at bottom
    y = H - 110
    draw.rectangle([0, H - 90, W, H], fill=(*ac, 255))
    f_swipe = load_font("Light", 28)
    draw_text_centered(draw, "swipe to see what changed →", f_swipe, H - 66, (255,255,255,220))

    return img


# ── SLIDE 3 & 4: Insight slides ────────────────────────────────────────────────
def make_slide_insight(book: dict, insight_text: str, slide_num: int,
                       series_config: dict) -> Image.Image:
    ac   = hex_rgb(series_config["accent_hex"])
    bg   = (12, 12, 28)
    img  = Image.new("RGBA", (W, H), (*bg, 255))
    img  = add_decorative_bg(img, ac, alpha_big=28, alpha_small=20)
    draw = ImageDraw.Draw(img)

    # Slide counter top-right
    f_counter = load_font("Light", 30)
    counter_text = f"{slide_num} / 6"
    bb = draw.textbbox((0,0), counter_text, font=f_counter)
    draw.text((W - (bb[2]-bb[0]) - 50, 44), counter_text,
              font=f_counter, fill=(*ac, 180))

    # Accent vertical stripe left edge
    draw.rectangle([0, 0, 7, H], fill=(*ac, 255))

    # Insight text — centred
    f_ins = load_font("Regular", 46)
    lines = textwrap.wrap(insight_text, width=30)
    line_h = 58
    total_h = len(lines) * line_h
    y = (H - total_h) // 2 - 20

    for line in lines:
        bb = draw.textbbox((0,0), line, font=f_ins)
        lw = bb[2] - bb[0]
        draw.text(((W - lw) // 2, y), line, font=f_ins, fill=(235,235,250,255))
        y += line_h

    # Book title watermark bottom
    f_wm = load_font("Light", 24)
    wm = f"{book['title']}  ·  Book {book['num']}"
    bb = draw.textbbox((0,0), wm, font=f_wm)
    draw.text(((W - (bb[2]-bb[0])) // 2, H - 60), wm,
              font=f_wm, fill=(*ac, 130))

    return img


# ── SLIDE 5: Scenario ─────────────────────────────────────────────────────────
def make_slide_scenario(book: dict, scenario_text: str,
                        series_config: dict) -> Image.Image:
    ac   = hex_rgb(series_config["accent_hex"])
    bg   = (18, 18, 36)          # slightly lighter bg for variation
    img  = Image.new("RGBA", (W, H), (*bg, 255))
    img  = add_decorative_bg(img, ac, alpha_big=22, alpha_small=18)
    draw = ImageDraw.Draw(img)

    # Label
    y = 90
    f_label = load_font("SemiBold", 28)
    draw_text_centered(draw, "SOUND FAMILIAR?", f_label, y, (*ac, 230))
    y += 55

    # Divider
    draw.rectangle([W//2 - 80, y, W//2 + 80, y + 3], fill=(*ac, 160))
    y += 40

    # Scenario text
    f_sc = load_font("Italic", 42)
    lines = textwrap.wrap(f'"{scenario_text}"', width=30)
    line_h = 56
    total_h = len(lines) * line_h
    start_y = y + max(0, (H - y - 140 - total_h) // 2)

    for line in lines:
        bb = draw.textbbox((0,0), line, font=f_sc)
        lw = bb[2] - bb[0]
        draw.text(((W - lw) // 2, start_y), line, font=f_sc,
                  fill=(220, 220, 240, 255))
        start_y += line_h

    # Bottom
    draw.rectangle([0, H - 90, W, H], fill=(*ac, 255))
    f_bot = load_font("Regular", 26)
    draw_text_centered(draw, "There's a whole book on exactly this.", f_bot,
                       H - 60, (255,255,255,220))

    return img


# ── SLIDE 6: CTA ───────────────────────────────────────────────────────────────
def make_slide_cta(book: dict, cta_line: str, series_config: dict) -> Image.Image:
    ac   = hex_rgb(series_config["accent_hex"])
    bg   = (12, 12, 28)
    img  = Image.new("RGBA", (W, H), (*bg, 255))
    img  = add_decorative_bg(img, ac, alpha_big=40, alpha_small=30)
    draw = ImageDraw.Draw(img)

    # Top bar
    bar_h = 90
    draw.rectangle([0, 0, W, bar_h], fill=(*ac, 255))
    f_bar = load_font("Regular", 26)
    draw_text_centered(draw, series_config["name"].upper(), f_bar,
                       (bar_h - 26) // 2, (255,255,255,255))

    # Book number badge
    y = bar_h + 60
    f_badge = load_font("Light", 32)
    draw_text_centered(draw, f"Book {book['num']} of 10", f_badge, y, (*ac, 200))
    y += 55

    # Book title — big
    f_title = load_font("Bold", 72 if len(book["title"]) < 20 else 58)
    lines = textwrap.wrap(book["title"], width=18)
    line_h = int(f_title.size * 1.25)
    total_title_h = len(lines) * line_h

    # Subtitle
    f_sub = load_font("Italic", 38)
    sub_lines = textwrap.wrap(book["subtitle"], width=30)
    sub_line_h = 50
    total_sub_h = len(sub_lines) * sub_line_h

    divider_gap = 50
    cta_h = 80
    total_block = total_title_h + divider_gap + total_sub_h + 40 + cta_h
    y = bar_h + 60 + 55 + max(20, (H - (bar_h + 60 + 55) - 130 - total_block) // 2)

    for line in lines:
        bb = draw.textbbox((0,0), line, font=f_title)
        lw = bb[2] - bb[0]
        draw.text(((W - lw) // 2 + 2, y + 2), line, font=f_title, fill=(0,0,0,110))
        draw.text(((W - lw) // 2, y), line, font=f_title, fill=(255,255,255,255))
        y += line_h

    y += 18
    draw.rectangle([W//2 - 120, y, W//2 + 120, y + 2], fill=(*ac, 180))
    diamond = 9
    draw.polygon([(W//2, y - diamond), (W//2 + diamond, y),
                  (W//2, y + diamond), (W//2 - diamond, y)], fill=(*ac, 255))
    y += diamond + 22

    for s_line in sub_lines:
        bb = draw.textbbox((0,0), s_line, font=f_sub)
        lw = bb[2] - bb[0]
        draw.text(((W - lw) // 2, y), s_line, font=f_sub, fill=(*ac, 230))
        y += sub_line_h

    y += 28
    # CTA line
    f_cta = load_font("SemiBold", 34)
    cta_lines = textwrap.wrap(cta_line, width=32)
    for c_line in cta_lines:
        bb = draw.textbbox((0,0), c_line, font=f_cta)
        lw = bb[2] - bb[0]
        draw.text(((W - lw) // 2, y), c_line, font=f_cta, fill=(255,255,255,220))
        y += 44

    # Bottom bar
    draw.rectangle([0, H - 90, W, H], fill=(*ac, 255))
    f_bot = load_font("SemiBold", 28)
    draw_text_centered(draw, "Full bundle  ·  link in bio", f_bot, H - 60,
                       (255,255,255,255))

    return img


# ── STORY (1080×1920): bundle cover portrait ─────────────────────────────────
def make_story_slide(series_config: dict) -> Image.Image:
    """
    Portrait story version of the bundle cover.
    Same visual language, extra vertical space used for a tagline + CTA.
    """
    ac   = hex_rgb(series_config["accent_hex"])
    bg   = (12, 12, 28)
    books = series_config["books"]

    img  = Image.new("RGBA", (SW, SH), (*bg, 255))
    img  = add_decorative_bg(img, ac, alpha_big=30, alpha_small=22)
    draw = ImageDraw.Draw(img)

    # Top bar
    bar_h = 130
    draw.rectangle([0, 0, SW, bar_h], fill=(*ac, 255))
    f_series = load_font("Regular", 36)
    draw_text_centered(draw, series_config["name"].upper(), f_series,
                       (bar_h - 36) // 2, (255,255,255,255), SW)

    # Badge
    y = bar_h + 55
    f_badge = load_font("SemiBold", 30)
    draw_text_centered(draw, "✦  COMPLETE 10-BOOK BUNDLE  ✦", f_badge, y, (*ac, 220), SW)
    y += 58

    # Tagline
    f_tag = load_font("Italic", 40)
    tag_h = draw_text_wrapped_centered(draw, f'"{series_config["bundle_tagline"]}"',
                                       f_tag, y, (210, 210, 240, 255),
                                       int(SW * 0.76), line_gap=10, img_w=SW)
    y += tag_h + 50

    # Divider
    draw.rectangle([int(SW * 0.1), y, int(SW * 0.9), y + 2], fill=(*ac, 130))
    y += 40

    # All 10 books — single column in story format (portrait has the height)
    f_num  = load_font("SemiBold", 30)
    f_book = load_font("Regular",  30)
    row_gap = 68

    for book in books:
        num_label = f"{book['num']:02d}  "
        bb = draw.textbbox((0,0), num_label, font=f_num)
        nw = bb[2] - bb[0]
        x_start = int(SW * 0.10)
        draw.text((x_start, y), num_label, font=f_num, fill=(*ac, 255))
        title = book["title"]
        if len(title) > 34:
            title = title[:33] + "…"
        draw.text((x_start + nw, y), title, font=f_book, fill=(230,230,245,255))
        y += row_gap

    # Bottom CTA bar
    cta_h = 150
    draw.rectangle([0, SH - cta_h, SW, SH], fill=(*ac, 255))
    f_cta_big = load_font("Bold", 38)
    f_cta_sub = load_font("Regular", 28)
    draw_text_centered(draw, "Get the full bundle", f_cta_big,
                       SH - cta_h + 28, (255,255,255,255), SW)
    draw_text_centered(draw, f"@{series_config['ig_page_username']}  ·  link in bio",
                       f_cta_sub, SH - cta_h + 86, (255,255,255,200), SW)

    return img


# ── Main: generate full carousel + story ─────────────────────────────────────
def generate_carousel(series_config: dict, book_num: int = None) -> dict:
    """
    Picks a book, generates content, creates all 6 slides + 1 story.
    Returns:
    {
        "slide_paths": [str × 6],
        "story_path": str,
        "caption": str,
        "book_title": str,
        "book_num": int,
    }
    """
    books = series_config["books"]
    if book_num is None:
        book = random.choice(books)
    else:
        book = next((b for b in books if b["num"] == book_num), books[0])

    print(f"  Generating carousel — {series_config['name']} | Book {book['num']}: {book['title']}")

    # Generate Gemini content
    content = generate_slide_content(series_config, book)

    # Timestamps for unique filenames
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    sid = series_config["series_id"]
    bnum = book["num"]
    prefix = f"s{sid:02d}_b{bnum:02d}_{ts}"

    # Build all slides
    slides_data = [
        ("cover",    make_slide_bundle_cover(series_config)),
        ("hook",     make_slide_hook(book, content, series_config)),
        ("insight1", make_slide_insight(book, content["insight_1"], 3, series_config)),
        ("insight2", make_slide_insight(book, content["insight_2"], 4, series_config)),
        ("scenario", make_slide_scenario(book, content["scenario"], series_config)),
        ("cta",      make_slide_cta(book, content["cta_line"], series_config)),
    ]

    slide_paths = []
    for label, slide_img in slides_data:
        path = os.path.join(OUTPUT_DIR, f"{prefix}_{label}.jpg")
        save_jpg(slide_img, path)
        slide_paths.append(path)
        print(f"    ✓ slide_{label}: {os.path.basename(path)}")

    # Story slide
    story_img  = make_story_slide(series_config)
    story_path = os.path.join(OUTPUT_DIR, f"{prefix}_story.jpg")
    save_jpg(story_img, story_path)
    print(f"    ✓ story: {os.path.basename(story_path)}")

    # Caption
    hashtags = " ".join(random.sample(series_config["hashtags"],
                                      min(11, len(series_config["hashtags"]))))
    caption = f"{content['caption']}\n\n{hashtags}"

    return {
        "slide_paths": slide_paths,
        "story_path":  story_path,
        "caption":     caption,
        "book_title":  book["title"],
        "book_num":    book["num"],
        "series_name": series_config["name"],
    }


# ── Quick test ─────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    from config import SERIES_PAGES
    result = generate_carousel(SERIES_PAGES[0], book_num=1)
    print(f"\nSlides: {[os.path.basename(p) for p in result['slide_paths']]}")
    print(f"Story:  {os.path.basename(result['story_path'])}")
    print(f"Caption preview:\n{result['caption'][:300]}...")
