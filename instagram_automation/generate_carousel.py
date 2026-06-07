"""
Instagram carousel + story generator.
Apex-style: dark, bold, human. All 10 improvement fixes applied.
"""

import os
import json
import textwrap
import random
import re
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from groq import Groq

FONTS_DIR  = os.path.join(os.path.dirname(__file__), "..", "fonts")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "posts")
os.makedirs(OUTPUT_DIR, exist_ok=True)

W, H   = 1080, 1080
SW, SH = 1080, 1920

# Slightly different dark tones per slide for variation
BG_TONES = [
    (10, 10, 14),
    (12, 11, 18),
    (10, 13, 16),
    (14, 10, 16),
    (11, 11, 20),
]

# Day-based content themes (Monday=0 ... Sunday=6)
DAY_THEMES = {
    0: ("myth-busting", "Start with something most people get wrong. Then correct it clearly."),
    1: ("real talk", "Be blunt. Say the uncomfortable truth most people avoid."),
    2: ("mini story", "Frame everything as a 3rd-person story — someone the reader will recognise."),
    3: ("practical", "Focus on what to actually do. Specific steps, not concepts."),
    4: ("mindset shift", "Challenge how the reader sees this topic. Flip their assumption."),
    5: ("deep insight", "Go deeper than surface level. Share something that takes a moment to absorb."),
    6: ("reflection", "Reflective tone. Make the reader pause and think about their own situation."),
}

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

def subtle_bg(img, ac, tone_idx=0, intensity=18):
    iw, ih = img.size
    layer = Image.new("RGBA", (iw, ih), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    r = int(iw * 0.55)
    d.ellipse([iw - r, -r//2, iw + r//2, r], fill=(*ac, intensity))
    r2 = int(iw * 0.3)
    d.ellipse([-r2//2, ih - r2//2, r2//2, ih + r2//2], fill=(*ac, max(6, intensity - 8)))
    return Image.alpha_composite(img, layer)

def thin_line(draw, y, img_w=W, ac=(255,255,255), alpha=60, margin=80):
    draw.rectangle([margin, y, img_w - margin, y + 1], fill=(*ac, alpha))

def clean(text):
    """Strip markdown, emojis, and junk from AI output."""
    text = text.replace("**", "").replace("*", "").replace("_", "")
    text = re.sub(r'[^\x00-\x7FÀ-ɏ‘’“”–—]', '', text)
    text = text.strip()
    return text

def save_jpg(img, path):
    img.convert("RGB").save(path, "JPEG", quality=96)


# ── AI Content Generation ──────────────────────────────────────────────────────
def generate_slide_content(series_config: dict, book: dict) -> dict:
    api_key = os.environ.get("GROQ_API_KEY", "")
    if not api_key:
        raise ValueError("GROQ_API_KEY not set")

    client = Groq(api_key=api_key)

    day = datetime.utcnow().weekday()
    theme_name, theme_instruction = DAY_THEMES[day]

    prompt = f"""
You write Instagram carousel copy. Tone: real, sharp, human. Like a knowledgeable friend texting you.

Series: {series_config['name']}
Book: "{book['title']}" — {book['subtitle']}
Niche: {series_config['niche']}
Today's content angle: {theme_name} — {theme_instruction}

Return ONLY valid JSON with these exact keys:

"hook": One statement. MAX 9 words. Stops the scroll. No question marks. Should feel like something the reader already thinks but never saw written this way. Raw, personal, specific. Bad example: "Trauma lives in your body." Good example: "You fixed your life on paper. Still exhausted."

"p1_head": 3-5 words. Clean truth or surprising fact. No hype.
"p1_sub": 2 sentences. Specific and grounded. Conversational, not clinical.

"p2_head": 3-5 words. A reframe — shifts how they think about this.
"p2_sub": 2 sentences. Concrete. Something they can relate to immediately.

"p3_head": 3-5 words. Something from real life they will recognise.
"p3_sub": 2 sentences. Paint a scene. Third-person is fine. Make them feel seen.

"p4_head": 3-5 words. What actually helps. Practical, warm, not preachy.
"p4_sub": 2 sentences. Actionable. End with something that feels like hope, not a command.

"save_line": One short sentence (max 8 words) that makes someone want to screenshot this slide. Like "Save this for when it gets heavy." or "Come back to this on a hard day."

"caption": 3-4 sentences. Written like a real person, not a brand. Warm, specific to the topic. End with a question that gets people to comment — something they can actually answer in 1-2 words. No URLs. No em-dashes. 1-2 emojis placed naturally. No hashtags.

STRICT RULES:
- Zero asterisks (* or **). Zero underscores.
- No exclamation marks anywhere.
- No "I" or "we". No "dive into", "delve", "game-changer", "journey", "unlock", "empower".
- No AI-sounding phrases. Write like a human.
- Return ONLY the JSON object.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.9,
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
    ac  = hex_rgb(series_config["accent_hex"])
    img = Image.new("RGBA", (W, H), (*BG_TONES[0], 255))
    img = subtle_bg(img, ac, intensity=22)
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
    y = (H - total) // 2 - 30

    for line in lines:
        bb = draw.textbbox((0,0), line, font=f)
        lw = bb[2] - bb[0]
        draw.text(((W - lw) // 2 + 3, y + 3), line, font=f, fill=(0, 0, 0, 80))
        draw.text(((W - lw) // 2, y), line, font=f, fill=(255, 255, 255, 255))
        y += lh

    # Accent bottom bar
    draw.rectangle([0, H - 6, W, H], fill=(*ac, 255))
    f_s = load_font("Light", 24)
    draw_centered(draw, "swipe", f_s, H - 52, (*ac, 200))

    return img


# ── SLIDES 2-5: Numbered Point ────────────────────────────────────────────────
def make_slide_point(num: int, headline: str, subtext: str,
                     series_config: dict, save_line: str = "") -> Image.Image:
    ac   = hex_rgb(series_config["accent_hex"])
    tone = BG_TONES[num % len(BG_TONES)]
    img  = Image.new("RGBA", (W, H), (*tone, 255))
    img  = subtle_bg(img, ac, tone_idx=num, intensity=16)
    draw = ImageDraw.Draw(img)

    # Left accent stripe
    draw.rectangle([0, 0, 5, H], fill=(*ac, 255))

    # Big accent number
    f_num = load_font("Bold", 120)
    num_label = f"{num:02d}."
    draw.text((72, 90), num_label, font=f_num, fill=(*ac, 255))

    num_bb = draw.textbbox((0,0), num_label, font=f_num)
    num_bottom = 90 + (num_bb[3] - num_bb[1])
    thin_line(draw, num_bottom + 55, ac=ac, alpha=80, margin=72)

    # Headline
    words = headline.split()
    fsize = 72 if len(words) <= 5 else 60
    f_head = load_font("Bold", fsize)
    lines = textwrap.wrap(headline, width=20)
    lh = fsize + 16
    y = num_bottom + 85

    for line in lines:
        draw.text((72, y), line, font=f_head, fill=(255, 255, 255, 255))
        y += lh

    y += 18

    # Subtext
    f_sub = load_font("Regular", 40)
    sub_lines = textwrap.wrap(subtext, width=30)
    for s in sub_lines:
        draw.text((72, y), s, font=f_sub, fill=(185, 185, 210, 255))
        y += 56

    # "Save this" line on slide 3 (fix #6 — screenshottable moment)
    if num == 3 and save_line:
        save_clean = clean(save_line)
        f_save = load_font("Italic", 26)
        save_bb = draw.textbbox((0,0), save_clean, font=f_save)
        sw = save_bb[2] - save_bb[0]
        sx = (W - sw) // 2
        # pill background
        pad = 18
        draw.rounded_rectangle([sx - pad, H - 130, sx + sw + pad, H - 90],
                                radius=20, fill=(*ac, 40))
        draw.text((sx, H - 126), save_clean, font=f_save, fill=(*ac, 220))

    # Bottom bar
    draw.rectangle([0, H - 72, W, H], fill=(*ac, 255))
    f_bot = load_font("Light", 22)
    draw_centered(draw, series_config["name"].upper(), f_bot, H - 46,
                  (255, 255, 255, 190))

    return img


# ── SLIDE 6: CTA ──────────────────────────────────────────────────────────────
def make_slide_cta(book: dict, series_config: dict) -> Image.Image:
    ac   = hex_rgb(series_config["accent_hex"])
    img  = Image.new("RGBA", (W, H), (*BG_TONES[0], 255))
    img  = subtle_bg(img, ac, intensity=28)
    draw = ImageDraw.Draw(img)

    # Top bar
    bar_h = 88
    draw.rectangle([0, 0, W, bar_h], fill=(*ac, 255))
    f_bar = load_font("SemiBold", 26)
    draw_centered(draw, series_config["name"].upper(), f_bar,
                  (bar_h - 26) // 2, (255, 255, 255, 255))

    y = bar_h + 55

    # Soft recommendation line (fix #4 — less product-focused)
    f_rec = load_font("Italic", 30)
    draw_centered(draw, "if this resonated, there is a full book on it.", f_rec,
                  y, (180, 180, 210, 255))
    y += 50

    thin_line(draw, y, ac=(255,255,255), alpha=30)
    y += 28

    # Book number
    f_booknum = load_font("Light", 30)
    draw_centered(draw, f"Book {book['num']} of 10", f_booknum, y, (*ac, 200))
    y += 48

    # Book title
    fsize = 76 if len(book["title"]) < 18 else 60
    f_title = load_font("Bold", fsize)
    t_lines = textwrap.wrap(book["title"], width=16)
    for line in t_lines:
        bb = draw.textbbox((0,0), line, font=f_title)
        lw = bb[2] - bb[0]
        draw.text(((W - lw) // 2 + 2, y + 2), line, font=f_title, fill=(0,0,0,90))
        draw.text(((W - lw) // 2, y), line, font=f_title, fill=(255,255,255,255))
        y += fsize + 12

    y += 8
    f_sub = load_font("Italic", 32)
    sub_lines = textwrap.wrap(book["subtitle"], width=30)
    for s in sub_lines:
        bb = draw.textbbox((0,0), s, font=f_sub)
        lw = bb[2] - bb[0]
        draw.text(((W - lw) // 2, y), s, font=f_sub, fill=(*ac, 210))
        y += 44

    y += 14
    # Gumroad URL
    gumroad = series_config.get("gumroad_link", "link in bio")
    f_link = load_font("Bold", 26)
    draw_centered(draw, gumroad, f_link, y, (*ac, 240))

    # Bottom bar
    draw.rectangle([0, H - 80, W, H], fill=(*ac, 255))
    f_bot = load_font("SemiBold", 26)
    draw_centered(draw, "Full 10-book bundle  ·  link in bio", f_bot,
                  H - 54, (255, 255, 255, 255))

    return img


# ── STORY (1080×1920) ─────────────────────────────────────────────────────────
def make_story_slide(hook_text: str, caption_question: str,
                     series_config: dict) -> Image.Image:
    """Story with hook + engagement question (fix #9)."""
    ac   = hex_rgb(series_config["accent_hex"])
    img  = Image.new("RGBA", (SW, SH), (*BG_TONES[0], 255))
    img  = subtle_bg(img, ac, intensity=24)
    draw = ImageDraw.Draw(img)

    # Top bar
    bar_h = 120
    draw.rectangle([0, 0, SW, bar_h], fill=(*ac, 255))
    f_bar = load_font("Regular", 34)
    draw_centered(draw, series_config["name"].upper(), f_bar,
                  (bar_h - 34) // 2, (255,255,255,255), SW)

    # Hook text
    words = hook_text.split()
    fsize = 96 if len(words) <= 5 else (78 if len(words) <= 8 else 64)
    wrap_w = 14 if len(words) <= 5 else (18 if len(words) <= 8 else 22)
    f_hook = load_font("Bold", fsize)
    lines  = textwrap.wrap(hook_text, width=wrap_w)
    lh     = fsize + 22
    total  = len(lines) * lh
    y      = bar_h + (int(SH * 0.48) - bar_h - total) // 2

    for line in lines:
        bb = draw.textbbox((0,0), line, font=f_hook)
        lw = bb[2] - bb[0]
        draw.text(((SW - lw) // 2 + 3, y + 3), line, font=f_hook, fill=(0,0,0,80))
        draw.text(((SW - lw) // 2, y), line, font=f_hook, fill=(255,255,255,255))
        y += lh

    thin_line(draw, int(SH * 0.55), img_w=SW, ac=ac, alpha=100, margin=100)

    # Engagement question (fix #9 — story has a real question)
    q_y = int(SH * 0.57)
    f_qlabel = load_font("SemiBold", 28)
    draw_centered(draw, "tell me in the comments", f_qlabel, q_y, (*ac, 200), SW)
    q_y += 48

    # Extract just the question from caption
    question = caption_question if caption_question else "does this sound familiar to you?"
    f_q = load_font("Bold", 44)
    q_lines = textwrap.wrap(question, width=22)
    for ql in q_lines:
        bb = draw.textbbox((0,0), ql, font=f_q)
        lw = bb[2] - bb[0]
        draw.text(((SW - lw) // 2, q_y), ql, font=f_q, fill=(255,255,255,255))
        q_y += 58

    q_y += 20
    f_link = load_font("Regular", 28)
    draw_centered(draw, "Full bundle — link in bio", f_link, q_y,
                  (200,200,220,220), SW)

    # Bottom bar
    cta_h = 120
    draw.rectangle([0, SH - cta_h, SW, SH], fill=(*ac, 255))
    f_cta = load_font("Bold", 34)
    draw_centered(draw, "Get the Full Bundle", f_cta, SH - cta_h + 22,
                  (255,255,255,255), SW)
    f_handle = load_font("Regular", 24)
    draw_centered(draw, f"@{series_config['ig_page_username']}",
                  f_handle, SH - cta_h + 72, (255,255,255,190), SW)

    return img


# ── Hashtag improvement (fix #7 — niche + smaller tags mixed in) ──────────────
SMALL_TAGS = [
    "#selfhealingjourney", "#quietstruggles", "#realtalkonline",
    "#mentalhealthreality", "#healingisnotlinear", "#bookrecommendations",
    "#ebooksforwomen", "#selfhelpbooks", "#personaldevelopmentbooks",
]

def build_hashtags(series_config: dict) -> str:
    series_tags = random.sample(series_config["hashtags"],
                                min(8, len(series_config["hashtags"])))
    extra = random.sample(SMALL_TAGS, 3)
    all_tags = series_tags + extra
    random.shuffle(all_tags)
    return " ".join(all_tags)


# ── Caption engagement question extraction ────────────────────────────────────
def extract_question(caption: str) -> str:
    """Pull the question from the caption for the story slide."""
    sentences = re.split(r'(?<=[.!?])\s+', caption.strip())
    for s in reversed(sentences):
        if "?" in s:
            return s.strip()
    return "does this sound familiar to you?"


# ── Main ──────────────────────────────────────────────────────────────────────
def generate_carousel(series_config: dict, book_num: int = None) -> dict:
    books = series_config["books"]
    book  = random.choice(books) if book_num is None else \
            next((b for b in books if b["num"] == book_num), books[0])

    print(f"  Generating carousel — {series_config['name']} | Book {book['num']}: {book['title']}")

    content = generate_slide_content(series_config, book)

    # Clean all text fields
    for k in ["hook", "p1_head", "p1_sub", "p2_head", "p2_sub",
              "p3_head", "p3_sub", "p4_head", "p4_sub", "save_line"]:
        if k in content:
            content[k] = clean(content[k])

    ts     = datetime.now().strftime("%Y%m%d_%H%M%S")
    sid    = series_config["series_id"]
    bnum   = book["num"]
    prefix = f"s{sid:02d}_b{bnum:02d}_{ts}"
    hook   = content["hook"]
    save_line = content.get("save_line", "")

    slides_data = [
        ("hook",   make_slide_hook(hook, series_config)),
        ("point1", make_slide_point(1, content["p1_head"], content["p1_sub"], series_config)),
        ("point2", make_slide_point(2, content["p2_head"], content["p2_sub"], series_config)),
        ("point3", make_slide_point(3, content["p3_head"], content["p3_sub"], series_config, save_line)),
        ("point4", make_slide_point(4, content["p4_head"], content["p4_sub"], series_config)),
        ("cta",    make_slide_cta(book, series_config)),
    ]

    slide_paths = []
    for label, slide_img in slides_data:
        path = os.path.join(OUTPUT_DIR, f"{prefix}_{label}.jpg")
        save_jpg(slide_img, path)
        slide_paths.append(path)
        print(f"    ✓ slide_{label}: {os.path.basename(path)}")

    # Caption (fix #10 — ends with engagement question)
    caption_text = content.get("caption", "")
    caption_text = re.sub(r'https?://\S+', '', caption_text).strip()
    caption_text = re.sub(r'\w+\.gumroad\.com\S*', '', caption_text).strip()
    caption_text = clean(caption_text)

    hashtags = build_hashtags(series_config)
    caption  = f"{caption_text}\n\n{hashtags}"

    # Extract question for story
    story_question = extract_question(caption_text)

    story_img  = make_story_slide(hook, story_question, series_config)
    story_path = os.path.join(OUTPUT_DIR, f"{prefix}_story.jpg")
    save_jpg(story_img, story_path)
    print(f"    ✓ story: {os.path.basename(story_path)}")

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
    print(f"\nCaption:\n{result['caption'][:500]}...")
