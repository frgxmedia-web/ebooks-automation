"""
Generates a 6-slide carousel + 1 story image for Instagram.
Apex-style: dark backgrounds, bold white text, accent-colored numbers.

Carousel structure:
  Slide 1 — Hook: one powerful statement, nothing else
  Slide 2 — Point 01: bold headline + subtitle (insight)
  Slide 3 — Point 02: bold headline + subtitle (reframe)
  Slide 4 — Point 03: bold headline + subtitle (scenario)
  Slide 5 — Point 04: bold headline + subtitle (tip)
  Slide 6 — CTA: bundle reveal + Gumroad link

Story (1080×1920): portrait hook + CTA
"""

import os
import json
import textwrap
import random
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from groq import Groq

FONTS_DIR  = os.path.join(os.path.dirname(__file__), "..", "fonts")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "posts")
os.makedirs(OUTPUT_DIR, exist_ok=True)

W, H   = 1080, 1080
SW, SH = 1080, 1920

BG_DARK  = (10, 10, 14)
BG_DARK2 = (14, 14, 20)

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

def draw_centered(draw, text, font, y, color, img_w=W):
    bb = draw.textbbox((0, 0), text, font=font)
    tw = bb[2] - bb[0]
    draw.text(((img_w - tw) // 2, y), text, font=font, fill=color)
    return bb[3] - bb[1]

def draw_wrapped_centered(draw, text, font, y, color, max_w, line_gap=14, img_w=W):
    avg = max(1, draw.textbbox((0,0), "A", font=font)[2])
    chars = max(8, max_w // avg)
    lines = textwrap.wrap(text, width=chars)
    lh = draw.textbbox((0,0), "Ag", font=font)[3]
    total = 0
    for line in lines:
        bb = draw.textbbox((0,0), line, font=font)
        lw = bb[2] - bb[0]
        draw.text(((img_w - lw) // 2, y + total), line, font=font, fill=color)
        total += lh + line_gap
    return total

def subtle_noise(img, ac, intensity=18):
    """Adds a very faint vignette + accent glow at top-right corner."""
    iw, ih = img.size
    layer = Image.new("RGBA", (iw, ih), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    r = int(iw * 0.55)
    d.ellipse([iw - r, -r//2, iw + r//2, r], fill=(*ac, intensity))
    r2 = int(iw * 0.3)
    d.ellipse([-r2//2, ih - r2//2, r2//2, ih + r2//2], fill=(*ac, intensity - 6))
    return Image.alpha_composite(img, layer)

def save_jpg(img, path):
    img.convert("RGB").save(path, "JPEG", quality=96)

def thin_line(draw, y, img_w=W, ac=(255,255,255), alpha=60, margin=80):
    draw.rectangle([margin, y, img_w - margin, y + 1], fill=(*ac, alpha))


# ── AI Content Generation ──────────────────────────────────────────────────────
def generate_slide_content(series_config: dict, book: dict) -> dict:
    api_key = os.environ.get("GROQ_API_KEY", "")
    if not api_key:
        raise ValueError("GROQ_API_KEY not set")

    client = Groq(api_key=api_key)

    prompt = f"""
You write copy for Instagram carousels. Apex-style: sharp, real, no fluff.

Series: {series_config['name']}
Book: "{book['title']}" — {book['subtitle']}
Niche: {series_config['niche']}

Return ONLY valid JSON with these exact keys:

"hook": One punchy statement. MAX 10 words. Dark, relatable, stops the scroll. No question marks. Like: "Your nervous system has been running on panic mode." or "Most people never fix this because nobody told them." Start with something they FEEL.

"p1_head": 4-6 word bold headline for point 01. A truth or fact that surprises.
"p1_sub": 1-2 sentences expanding p1_head. Specific. No filler.

"p2_head": 4-6 word bold headline for point 02. A reframe or shift in thinking.
"p2_sub": 1-2 sentences expanding p2_head.

"p3_head": 4-6 word bold headline for point 03. Real-life situation they recognise.
"p3_sub": 1-2 sentences. Paint the picture.

"p4_head": 4-6 word bold headline for point 04. Practical — what to actually do.
"p4_sub": 1-2 sentences. Actionable.

"caption": Full Instagram caption. 3-5 sentences. Human voice. No AI-speak. No em-dashes. End with: "Full 10-book bundle — link in bio." Include 2-3 natural emojis mid-text, not at start. No hashtags in caption.

Rules: No em-dashes. No "I" or "we". Short punchy sentences. Return ONLY the JSON.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.88,
        response_format={"type": "json_object"},
    )
    raw = response.choices[0].message.content.strip()
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
        raw = raw.strip()
    return json.loads(raw)


# ── SLIDE 1: Hook ─────────────────────────────────────────────────────────────
def make_slide_hook(hook_text: str, series_config: dict) -> Image.Image:
    """Pure dark slide — huge bold hook, nothing else."""
    ac  = hex_rgb(series_config["accent_hex"])
    img = Image.new("RGBA", (W, H), (*BG_DARK, 255))
    img = subtle_noise(img, ac, intensity=22)
    draw = ImageDraw.Draw(img)

    words = hook_text.split()
    if len(words) <= 5:
        fsize, wrap_w = 100, 14
    elif len(words) <= 8:
        fsize, wrap_w = 82, 18
    else:
        fsize, wrap_w = 68, 22

    f = load_font("Bold", fsize)
    lines = textwrap.wrap(hook_text, width=wrap_w)
    lh = fsize + 20
    total = len(lines) * lh
    y = (H - total) // 2 - 20

    for line in lines:
        bb = draw.textbbox((0,0), line, font=f)
        lw = bb[2] - bb[0]
        # subtle shadow
        draw.text(((W - lw) // 2 + 3, y + 3), line, font=f, fill=(0, 0, 0, 80))
        draw.text(((W - lw) // 2, y), line, font=f, fill=(255, 255, 255, 255))
        y += lh

    # Thin accent line at bottom
    draw.rectangle([0, H - 6, W, H], fill=(*ac, 255))

    # Swipe nudge
    f_s = load_font("Light", 24)
    draw_centered(draw, "swipe →", f_s, H - 52, (*ac, 200))

    return img


# ── SLIDE 2-5: Numbered Point ─────────────────────────────────────────────────
def make_slide_point(num: int, headline: str, subtext: str,
                     series_config: dict) -> Image.Image:
    """Apex-style: big accent number, bold headline, lighter subtext."""
    ac  = hex_rgb(series_config["accent_hex"])
    img = Image.new("RGBA", (W, H), (*BG_DARK2, 255))
    img = subtle_noise(img, ac, intensity=16)
    draw = ImageDraw.Draw(img)

    # Left accent stripe
    draw.rectangle([0, 0, 5, H], fill=(*ac, 255))

    # Big accent number top-left
    f_num = load_font("Bold", 120)
    num_label = f"{num:02d}."
    draw.text((72, 100), num_label, font=f_num, fill=(*ac, 255))

    # Divider below number
    num_bb = draw.textbbox((0,0), num_label, font=f_num)
    num_bottom = 100 + (num_bb[3] - num_bb[1])
    thin_line(draw, num_bottom + 30, ac=ac, alpha=80, margin=72)

    # Headline — bold white, large
    words = headline.split()
    fsize = 72 if len(words) <= 5 else 60
    f_head = load_font("Bold", fsize)
    lines = textwrap.wrap(headline, width=20)
    lh = fsize + 16
    y = num_bottom + 60

    for line in lines:
        bb = draw.textbbox((0,0), line, font=f_head)
        lw = bb[2] - bb[0]
        draw.text((72, y), line, font=f_head, fill=(255, 255, 255, 255))
        y += lh

    y += 18

    # Subtext — lighter, smaller
    f_sub = load_font("Regular", 36)
    sub_lines = textwrap.wrap(subtext, width=34)
    for s in sub_lines:
        draw.text((72, y), s, font=f_sub, fill=(185, 185, 210, 255))
        y += 50

    # Bottom accent bar
    draw.rectangle([0, H - 72, W, H], fill=(*ac, 255))
    f_bot = load_font("Light", 24)
    series_short = series_config["name"].upper()
    draw_centered(draw, series_short, f_bot, H - 48, (255, 255, 255, 200))

    return img


# ── SLIDE 6: CTA + Bundle ─────────────────────────────────────────────────────
def make_slide_cta(book: dict, series_config: dict) -> Image.Image:
    """Final slide: featured book + bundle name + Gumroad link."""
    ac    = hex_rgb(series_config["accent_hex"])
    img   = Image.new("RGBA", (W, H), (*BG_DARK, 255))
    img   = subtle_noise(img, ac, intensity=28)
    draw  = ImageDraw.Draw(img)

    # Top bar
    bar_h = 88
    draw.rectangle([0, 0, W, bar_h], fill=(*ac, 255))
    f_bar = load_font("SemiBold", 26)
    draw_centered(draw, series_config["name"].upper(), f_bar,
                  (bar_h - 26) // 2, (255, 255, 255, 255))

    # Featured book title
    y = bar_h + 60
    f_booknum = load_font("Light", 30)
    draw_centered(draw, f"Book {book['num']} of 10", f_booknum, y, (*ac, 200))
    y += 48

    fsize = 80 if len(book["title"]) < 18 else 62
    f_title = load_font("Bold", fsize)
    t_lines = textwrap.wrap(book["title"], width=16)
    for line in t_lines:
        bb = draw.textbbox((0,0), line, font=f_title)
        lw = bb[2] - bb[0]
        draw.text(((W - lw) // 2 + 2, y + 2), line, font=f_title, fill=(0,0,0,100))
        draw.text(((W - lw) // 2, y), line, font=f_title, fill=(255,255,255,255))
        y += fsize + 14

    # Subtitle
    y += 10
    f_sub = load_font("Italic", 34)
    sub_lines = textwrap.wrap(book["subtitle"], width=32)
    for s in sub_lines:
        bb = draw.textbbox((0,0), s, font=f_sub)
        lw = bb[2] - bb[0]
        draw.text(((W - lw) // 2, y), s, font=f_sub, fill=(*ac, 220))
        y += 46

    # Divider + "Part of the bundle"
    y += 16
    thin_line(draw, y, ac=(255,255,255), alpha=40)
    y += 22
    f_bundle = load_font("Regular", 28)
    draw_centered(draw, f"Part of the {series_config['name']}", f_bundle,
                  y, (180, 180, 210, 255))
    y += 46

    # Gumroad link — prominent
    gumroad = series_config.get("gumroad_link", "link in bio")
    f_link = load_font("Bold", 32)
    draw_centered(draw, f"mindshiftbooks1.gumroad.com", f_link, y, (*ac, 255))

    # Bottom bar
    draw.rectangle([0, H - 80, W, H], fill=(*ac, 255))
    f_bot = load_font("SemiBold", 28)
    draw_centered(draw, "Full 10-book bundle  ·  link in bio", f_bot, H - 54,
                  (255, 255, 255, 255))

    return img


# ── STORY (1080×1920) ─────────────────────────────────────────────────────────
def make_story_slide(hook_text: str, series_config: dict) -> Image.Image:
    ac    = hex_rgb(series_config["accent_hex"])
    img   = Image.new("RGBA", (SW, SH), (*BG_DARK, 255))
    img   = subtle_noise(img, ac, intensity=24)
    draw  = ImageDraw.Draw(img)

    # Top bar
    bar_h = 120
    draw.rectangle([0, 0, SW, bar_h], fill=(*ac, 255))
    f_bar = load_font("Regular", 34)
    draw_centered(draw, series_config["name"].upper(), f_bar,
                  (bar_h - 34) // 2, (255,255,255,255), SW)

    # Hook — centered vertically in upper 60% of image
    words = hook_text.split()
    fsize = 96 if len(words) <= 5 else (78 if len(words) <= 8 else 64)
    wrap_w = 14 if len(words) <= 5 else (18 if len(words) <= 8 else 22)
    f_hook = load_font("Bold", fsize)
    lines  = textwrap.wrap(hook_text, width=wrap_w)
    lh     = fsize + 22
    total  = len(lines) * lh
    y      = bar_h + (int(SH * 0.55) - bar_h - total) // 2

    for line in lines:
        bb = draw.textbbox((0,0), line, font=f_hook)
        lw = bb[2] - bb[0]
        draw.text(((SW - lw) // 2 + 3, y + 3), line, font=f_hook, fill=(0,0,0,80))
        draw.text(((SW - lw) // 2, y), line, font=f_hook, fill=(255,255,255,255))
        y += lh

    # Divider
    thin_line(draw, int(SH * 0.60), img_w=SW, ac=ac, alpha=100, margin=100)

    # "10 books on this" section
    y = int(SH * 0.62)
    f_sub = load_font("SemiBold", 36)
    draw_centered(draw, "10 books on this topic.", f_sub, y, (*ac, 220), SW)
    y += 58
    f_link = load_font("Regular", 30)
    draw_centered(draw, "Full bundle — link in bio", f_link, y, (200,200,220,255), SW)

    # Bottom CTA bar
    cta_h = 130
    draw.rectangle([0, SH - cta_h, SW, SH], fill=(*ac, 255))
    f_cta = load_font("Bold", 36)
    draw_centered(draw, "Get the Full Bundle", f_cta, SH - cta_h + 24,
                  (255,255,255,255), SW)
    f_handle = load_font("Regular", 26)
    draw_centered(draw, f"@{series_config['ig_page_username']}",
                  f_handle, SH - cta_h + 76, (255,255,255,200), SW)

    return img


# ── Main ──────────────────────────────────────────────────────────────────────
def generate_carousel(series_config: dict, book_num: int = None) -> dict:
    books = series_config["books"]
    book  = random.choice(books) if book_num is None else \
            next((b for b in books if b["num"] == book_num), books[0])

    print(f"  Generating carousel — {series_config['name']} | Book {book['num']}: {book['title']}")

    content = generate_slide_content(series_config, book)

    ts     = datetime.now().strftime("%Y%m%d_%H%M%S")
    sid    = series_config["series_id"]
    bnum   = book["num"]
    prefix = f"s{sid:02d}_b{bnum:02d}_{ts}"

    hook = content["hook"]

    slides_data = [
        ("hook",     make_slide_hook(hook, series_config)),
        ("point1",   make_slide_point(1, content["p1_head"], content["p1_sub"], series_config)),
        ("point2",   make_slide_point(2, content["p2_head"], content["p2_sub"], series_config)),
        ("point3",   make_slide_point(3, content["p3_head"], content["p3_sub"], series_config)),
        ("point4",   make_slide_point(4, content["p4_head"], content["p4_sub"], series_config)),
        ("cta",      make_slide_cta(book, series_config)),
    ]

    slide_paths = []
    for label, slide_img in slides_data:
        path = os.path.join(OUTPUT_DIR, f"{prefix}_{label}.jpg")
        save_jpg(slide_img, path)
        slide_paths.append(path)
        print(f"    ✓ slide_{label}: {os.path.basename(path)}")

    story_img  = make_story_slide(hook, series_config)
    story_path = os.path.join(OUTPUT_DIR, f"{prefix}_story.jpg")
    save_jpg(story_img, story_path)
    print(f"    ✓ story: {os.path.basename(story_path)}")

    # Caption with Gumroad link
    gumroad = series_config.get("gumroad_link", "link in bio")
    hashtags = " ".join(random.sample(series_config["hashtags"],
                                      min(11, len(series_config["hashtags"]))))
    caption_text = content["caption"]
    # Ensure Gumroad link is in caption
    if "gumroad" not in caption_text.lower() and gumroad != "link in bio":
        caption_text = caption_text.rstrip() + f"\n\nGet the full bundle: {gumroad}"

    caption = f"{caption_text}\n\n{hashtags}"

    return {
        "slide_paths": slide_paths,
        "story_path":  story_path,
        "caption":     caption,
        "book_title":  book["title"],
        "book_num":    book["num"],
        "series_name": series_config["name"],
    }


if __name__ == "__main__":
    from config import SERIES_PAGES
    result = generate_carousel(SERIES_PAGES[0], book_num=1)
    print(f"\nSlides: {[os.path.basename(p) for p in result['slide_paths']]}")
    print(f"Caption:\n{result['caption'][:400]}...")
