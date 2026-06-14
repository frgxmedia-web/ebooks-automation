"""
Instagram carousel + story generator — 6-Beat Framework
Beats: Cold Open → Mirror → Point → Rhythm Flip → Turn → Payoff → CTA
Visuals: Pexels photo backgrounds (optional) + enhanced gradients
"""

import os
import io
import json
import textwrap
import random
import re
import urllib.request
import urllib.error
import urllib.parse
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from groq import Groq

FONTS_DIR  = os.path.join(os.path.dirname(__file__), "..", "fonts")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "posts")
os.makedirs(OUTPUT_DIR, exist_ok=True)

W, H   = 1080, 1080
SW, SH = 1080, 1920

# Pexels search terms per series
NICHE_KEYWORDS = {
    1:  "meditation forest calm nature",
    2:  "healthy food nutrition lifestyle",
    3:  "creative workspace focus desk",
    4:  "finance money growth minimal",
    5:  "women wellness yoga health",
    6:  "technology digital laptop future",
    7:  "peaceful sunset nature healing",
    8:  "professional career city office",
    9:  "couple connection hands love",
    10: "family children parent home",
}

# Day-based themes
DAY_THEMES = {
    0: ("myth-busting",   "Challenge something most people believe is true. Correct it with specifics."),
    1: ("real talk",      "Say the uncomfortable truth most people avoid. Be blunt, not harsh."),
    2: ("mini story",     "Frame everything as a third-person scene the reader will recognise in themselves."),
    3: ("practical",      "Focus on what to actually do. Specific steps, not abstract concepts."),
    4: ("mindset shift",  "Flip how the reader sees this topic. Reframe their core assumption."),
    5: ("deep insight",   "Go beneath the surface. Share something that takes a moment to absorb."),
    6: ("reflection",     "Reflective tone. Make them pause and think about their own situation."),
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

def clean(text):
    text = text.replace("**", "").replace("*", "").replace("_", "")
    text = re.sub(r'[^\x00-\x7FÀ-ɏ‘’“”–—]', '', text)
    return text.strip()

def save_jpg(img, path):
    img.convert("RGB").save(path, "JPEG", quality=96)

def thin_line(draw, y, img_w=W, ac=(255,255,255), alpha=60, margin=80):
    draw.rectangle([margin, y, img_w - margin, y + 1], fill=(*ac, alpha))


# ── Photo Fetching (Pexels) ───────────────────────────────────────────────────
def fetch_pexels_photo(keyword: str, size: tuple = (W, H)) -> Image.Image | None:
    api_key = os.environ.get("UNSPLASH_ACCESS_KEY", "")
    if not api_key:
        return None
    try:
        req = urllib.request.Request(
            f"https://api.unsplash.com/photos/random?query={urllib.parse.quote(keyword)}&orientation=squarish&content_filter=high",
            headers={"Authorization": f"Client-ID {api_key}"}
        )
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read())
        img_url = data.get("urls", {}).get("regular") or data.get("urls", {}).get("full")
        if not img_url:
            return None
        with urllib.request.urlopen(img_url, timeout=15) as r:
            img = Image.open(io.BytesIO(r.read())).convert("RGBA")
        img = img.resize(size, Image.LANCZOS)
        return img
    except Exception as e:
        print(f"    ~ Unsplash error: {e}")
        return None


# ── Background Builders ───────────────────────────────────────────────────────
def make_dark_gradient(w: int, h: int, ac: tuple, intensity: int = 22) -> Image.Image:
    """Radial gradient from corner — dark with accent glow."""
    base = (10, 10, 14)
    img  = Image.new("RGBA", (w, h), (*base, 255))
    layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    r = int(w * 0.65)
    d.ellipse([w - r, -r//2, w + r//2, r], fill=(*ac, intensity))
    r2 = int(w * 0.35)
    d.ellipse([-r2//2, h - r2//2, r2//2, h + r2//2], fill=(*ac, max(6, intensity - 10)))
    return Image.alpha_composite(img, layer)

def make_accent_bg(w: int, h: int, ac: tuple) -> Image.Image:
    """Solid accent colour background with subtle dark vignette."""
    img   = Image.new("RGBA", (w, h), (*ac, 255))
    layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    r = int(w * 0.8)
    d.ellipse([(w - r)//2, (h - r)//2, (w + r)//2, (h + r)//2],
              fill=(0, 0, 0, 60))
    return Image.alpha_composite(img, layer)

def make_light_bg(w: int, h: int, ac: tuple) -> Image.Image:
    """Off-white background with faint accent tint."""
    base = (245, 244, 240)
    img  = Image.new("RGBA", (w, h), (*base, 255))
    layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    r = int(w * 0.6)
    d.ellipse([w//2 - r//2, -r//4, w//2 + r//2, h//2], fill=(*ac, 14))
    return Image.alpha_composite(img, layer)

def apply_photo_bg(photo: Image.Image, overlay_color: tuple = (0,0,0),
                   overlay_alpha: int = 140) -> Image.Image:
    """Darken photo for text legibility."""
    photo = photo.convert("RGBA")
    overlay = Image.new("RGBA", photo.size, (*overlay_color, overlay_alpha))
    return Image.alpha_composite(photo, overlay)


# ── AI Content (6-Beat Framework) ────────────────────────────────────────────
def generate_slide_content(series_config: dict, book: dict) -> dict:
    api_key = os.environ.get("GROQ_API_KEY", "")
    if not api_key:
        raise ValueError("GROQ_API_KEY not set")

    client = Groq(api_key=api_key)
    day = datetime.utcnow().weekday()
    theme_name, theme_instruction = DAY_THEMES[day]

    prompt = f"""
You write Instagram carousel copy using a 6-beat storytelling framework. Tone: real, sharp, human. Like a knowledgeable friend texting you — not a brand, not a guru.

Series: {series_config['name']}
Book: "{book['title']}" — {book['subtitle']}
Niche: {series_config['niche']}
Today's angle: {theme_name} — {theme_instruction}

THE 6-BEAT FRAMEWORK — follow this exactly:

BEAT 1 — COLD OPEN (cold_open):
Drop them at the most interesting moment. Don't introduce the topic — drop them inside it.
Max 9 words. Specific to this book's topic. Feels like a cliff edge.
NOT: "Still feeling stuck." YES: "Still exhausted after fixing everything?"
NOT: "Trauma lives in your body." YES: "Your thyroid is what nobody checked."

BEAT 2 — MIRROR (mirror_text):
Say the sentence they have thought but never admitted out loud.
When they read it, they should stop scrolling and feel seen.
1-2 sentences. No questions. State it as fact about them.
Example: "You know exactly what to do. You just can't do it when it matters."

BEAT 3 — SPINE POINT (p1_head + p1_sub):
First practical insight. 3-5 word headline. 2 grounded, specific sentences.
Every sentence must earn the next one — make them need to swipe.

BEAT 4 — RHYTHM FLIP (p2_head + p2_sub):
A reframe — flip how they think about this topic.
3-5 word headline. 2 concrete sentences. This is the colour-flip slide — make it feel different.

BEAT 5 — THE TURN (turn_admission + turn_lesson):
turn_admission: A small, honest admission. 1 sentence. Something like "Most people already know this part."
turn_lesson: Rewrite rule — never "here's what I learned." Always "so you can ___."
1 sentence starting with "So you can" or "Which means you can" — give them the takeaway as a gift to them.
This is the slide people screenshot. Make it the sharpest line in the set.

BEAT 6 — THE PAYOFF (payoff_belief + payoff_action):
payoff_belief: Flip their core belief about this topic. 1 sentence. Bold, final, true.
payoff_action: One specific next action. NOT "follow for more." Give them something real they can do TODAY.

Also return:
"save_line": Max 8 words. Makes someone want to screenshot. "Save this for when it gets heavy."
"caption": 3-4 sentences. Warm, real, specific. End with a comment-bait question (1-2 word answer). No URLs. No em-dashes. 1-2 emojis natural. No hashtags.

STRICT RULES:
- Zero asterisks or underscores
- No exclamation marks
- No "I" or "we"
- No: dive into, delve, game-changer, journey, unlock, empower, resonate
- Return ONLY valid JSON with keys: cold_open, mirror_text, p1_head, p1_sub, p2_head, p2_sub, turn_admission, turn_lesson, payoff_belief, payoff_action, save_line, caption
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


# ── SLIDE 1: Cold Open ────────────────────────────────────────────────────────
def make_slide_cold_open(hook: str, series_config: dict,
                          photo: Image.Image | None = None) -> Image.Image:
    ac = hex_rgb(series_config["accent_hex"])

    if photo:
        img = apply_photo_bg(photo, overlay_color=(5, 5, 10), overlay_alpha=150)
    else:
        img = make_dark_gradient(W, H, ac, intensity=28)

    draw = ImageDraw.Draw(img)

    words = hook.split()
    fsize = 100 if len(words) <= 5 else (82 if len(words) <= 8 else 66)
    wrap_w = 14 if len(words) <= 5 else (18 if len(words) <= 8 else 22)

    f = load_font("Bold", fsize)
    lines = textwrap.wrap(hook, width=wrap_w)
    lh = fsize + 22
    total = len(lines) * lh
    y = (H - total) // 2 - 40

    for line in lines:
        bb = draw.textbbox((0, 0), line, font=f)
        lw = bb[2] - bb[0]
        draw.text(((W - lw) // 2 + 3, y + 3), line, font=f, fill=(0, 0, 0, 90))
        draw.text(((W - lw) // 2, y), line, font=f, fill=(255, 255, 255, 255))
        y += lh

    # Accent bottom bar
    draw.rectangle([0, H - 8, W, H], fill=(*ac, 255))
    f_s = load_font("Light", 26)
    draw_centered(draw, "swipe  →", f_s, H - 56, (*ac, 210))

    return img


# ── SLIDE 2: Mirror ───────────────────────────────────────────────────────────
def make_slide_mirror(mirror_text: str, series_config: dict) -> Image.Image:
    """Light bg — visual contrast from dark slide 1. Single bold statement."""
    ac   = hex_rgb(series_config["accent_hex"])
    img  = make_light_bg(W, H, ac)
    draw = ImageDraw.Draw(img)

    # Accent left stripe
    draw.rectangle([0, 0, 6, H], fill=(*ac, 255))

    # Small label
    f_label = load_font("Light", 26)
    draw.text((72, 90), "this is you", font=f_label, fill=(*ac, 180))

    thin_line(draw, 136, ac=ac, alpha=60, margin=72)

    # Mirror statement — large, dark text on light bg
    dark = (18, 18, 28)
    words = mirror_text.split()
    fsize = 68 if len(words) <= 12 else 54
    f = load_font("Bold", fsize)
    lines = textwrap.wrap(mirror_text, width=22)
    lh = fsize + 18
    y = 180

    for line in lines:
        draw.text((72, y), line, font=f, fill=(*dark, 255))
        y += lh

    y += 24
    # Accent underline
    draw.rectangle([72, y, 72 + 80, y + 4], fill=(*ac, 255))

    # Bottom
    draw.rectangle([0, H - 72, W, H], fill=(*ac, 255))
    f_bot = load_font("Light", 22)
    draw_centered(draw, series_config["name"].upper(), f_bot, H - 46,
                  (255, 255, 255, 190))

    return img


# ── SLIDE 3: Spine Point (dark) ───────────────────────────────────────────────
def make_slide_point_dark(num: int, headline: str, subtext: str,
                           series_config: dict, save_line: str = "") -> Image.Image:
    ac   = hex_rgb(series_config["accent_hex"])
    img  = make_dark_gradient(W, H, ac, intensity=16)
    draw = ImageDraw.Draw(img)

    draw.rectangle([0, 0, 6, H], fill=(*ac, 255))

    f_num = load_font("Bold", 120)
    num_label = f"{num:02d}."
    draw.text((72, 90), num_label, font=f_num, fill=(*ac, 255))

    num_bb = draw.textbbox((0, 0), num_label, font=f_num)
    num_bottom = 90 + (num_bb[3] - num_bb[1])
    thin_line(draw, num_bottom + 55, ac=ac, alpha=80, margin=72)

    words = headline.split()
    fsize = 72 if len(words) <= 5 else 58
    f_head = load_font("Bold", fsize)
    lines = textwrap.wrap(headline, width=20)
    lh = fsize + 16
    y = num_bottom + 85

    for line in lines:
        draw.text((72, y), line, font=f_head, fill=(255, 255, 255, 255))
        y += lh

    y += 18
    f_sub = load_font("Regular", 40)
    for s in textwrap.wrap(subtext, width=30):
        draw.text((72, y), s, font=f_sub, fill=(185, 185, 210, 255))
        y += 56

    if save_line:
        f_save = load_font("Italic", 26)
        save_bb = draw.textbbox((0, 0), save_line, font=f_save)
        sw = save_bb[2] - save_bb[0]
        sx = (W - sw) // 2
        pad = 18
        draw.rounded_rectangle([sx - pad, H - 130, sx + sw + pad, H - 90],
                                radius=20, fill=(*ac, 40))
        draw.text((sx, H - 126), save_line, font=f_save, fill=(*ac, 220))

    draw.rectangle([0, H - 72, W, H], fill=(*ac, 255))
    f_bot = load_font("Light", 22)
    draw_centered(draw, series_config["name"].upper(), f_bot, H - 46,
                  (255, 255, 255, 190))

    return img


# ── SLIDE 4: Rhythm Flip (accent bg) ─────────────────────────────────────────
def make_slide_rhythm_flip(headline: str, subtext: str,
                            series_config: dict) -> Image.Image:
    """Accent colour background — visual rhythm break."""
    ac   = hex_rgb(series_config["accent_hex"])
    img  = make_accent_bg(W, H, ac)
    draw = ImageDraw.Draw(img)

    # White left stripe
    draw.rectangle([0, 0, 6, H], fill=(255, 255, 255, 200))

    f_label = load_font("Light", 26)
    draw.text((72, 90), "flip the script", font=f_label, fill=(255, 255, 255, 160))
    thin_line(draw, 136, ac=(255, 255, 255), alpha=80, margin=72)

    words = headline.split()
    fsize = 76 if len(words) <= 5 else 62
    f_head = load_font("Bold", fsize)
    lines = textwrap.wrap(headline, width=20)
    lh = fsize + 18
    y = 180

    for line in lines:
        draw.text((72, y), line, font=f_head, fill=(255, 255, 255, 255))
        y += lh

    y += 24
    f_sub = load_font("Regular", 40)
    for s in textwrap.wrap(subtext, width=30):
        draw.text((72, y), s, font=f_sub, fill=(255, 255, 255, 210))
        y += 56

    # Bottom bar — white on accent
    draw.rectangle([0, H - 72, W, H], fill=(255, 255, 255, 40))
    f_bot = load_font("Light", 22)
    draw_centered(draw, series_config["name"].upper(), f_bot, H - 46,
                  (255, 255, 255, 200))

    return img


# ── SLIDE 5: The Turn ─────────────────────────────────────────────────────────
def make_slide_turn(admission: str, lesson: str, series_config: dict,
                     photo: Image.Image | None = None) -> Image.Image:
    """The screenshot slide — sharpest line in the set."""
    ac = hex_rgb(series_config["accent_hex"])

    if photo:
        img = apply_photo_bg(photo, overlay_color=(8, 8, 16), overlay_alpha=160)
    else:
        img = make_dark_gradient(W, H, ac, intensity=20)

    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, 6, H], fill=(*ac, 255))

    # Small admission (honest, soft)
    f_adm = load_font("Italic", 32)
    adm_lines = textwrap.wrap(admission, width=34)
    y = 120
    for line in adm_lines:
        draw.text((72, y), line, font=f_adm, fill=(185, 185, 210, 220))
        y += 46

    thin_line(draw, y + 20, ac=ac, alpha=60, margin=72)
    y += 52

    # The lesson — large, white, bold
    f_lesson = load_font("Bold", 66)
    lesson_lines = textwrap.wrap(lesson, width=22)
    lh = 66 + 16
    for line in lesson_lines:
        draw.text((72, y), line, font=f_lesson, fill=(255, 255, 255, 255))
        y += lh

    y += 16
    # Accent underline under lesson
    draw.rectangle([72, y, 72 + 120, y + 5], fill=(*ac, 255))

    # Save nudge
    f_save = load_font("Italic", 26)
    save = "save this."
    draw.text((72, H - 130), save, font=f_save, fill=(*ac, 200))

    draw.rectangle([0, H - 72, W, H], fill=(*ac, 255))
    f_bot = load_font("Light", 22)
    draw_centered(draw, series_config["name"].upper(), f_bot, H - 46,
                  (255, 255, 255, 190))

    return img


# ── SLIDE 6: Payoff ───────────────────────────────────────────────────────────
def make_slide_payoff(belief: str, action: str, series_config: dict) -> Image.Image:
    """Belief flip + one specific action. Closes the story."""
    ac   = hex_rgb(series_config["accent_hex"])
    dark = (6, 6, 10)
    img  = Image.new("RGBA", (W, H), (*dark, 255))
    draw = ImageDraw.Draw(img)

    # Full accent top bar
    bar_h = 10
    draw.rectangle([0, 0, W, bar_h], fill=(*ac, 255))

    # Belief flip — centered, large
    f_belief = load_font("Bold", 66)
    belief_lines = textwrap.wrap(belief, width=22)
    lh = 66 + 18
    total = len(belief_lines) * lh
    y = (H // 2) - (total // 2) - 60

    for line in belief_lines:
        bb = draw.textbbox((0, 0), line, font=f_belief)
        lw = bb[2] - bb[0]
        draw.text(((W - lw) // 2 + 2, y + 2), line, font=f_belief, fill=(0, 0, 0, 80))
        draw.text(((W - lw) // 2, y), line, font=f_belief, fill=(255, 255, 255, 255))
        y += lh

    y += 24
    thin_line(draw, y, ac=ac, alpha=100)
    y += 32

    # Action — accent coloured, smaller
    f_action = load_font("SemiBold", 38)
    action_lines = textwrap.wrap(action, width=28)
    for line in action_lines:
        bb = draw.textbbox((0, 0), line, font=f_action)
        lw = bb[2] - bb[0]
        draw.text(((W - lw) // 2, y), line, font=f_action, fill=(*ac, 240))
        y += 52

    # Bottom bar
    draw.rectangle([0, H - 80, W, H], fill=(*ac, 255))
    f_bot = load_font("Light", 22)
    draw_centered(draw, "full book — link in bio", f_bot, H - 54,
                  (255, 255, 255, 200))

    return img


# ── SLIDE 7: CTA ──────────────────────────────────────────────────────────────
def make_slide_cta(book: dict, series_config: dict) -> Image.Image:
    ac   = hex_rgb(series_config["accent_hex"])
    img  = make_dark_gradient(W, H, ac, intensity=28)
    draw = ImageDraw.Draw(img)

    bar_h = 88
    draw.rectangle([0, 0, W, bar_h], fill=(*ac, 255))
    f_bar = load_font("SemiBold", 26)
    draw_centered(draw, series_config["name"].upper(), f_bar,
                  (bar_h - 26) // 2, (255, 255, 255, 255))

    y = bar_h + 55
    f_rec = load_font("Italic", 30)
    draw_centered(draw, "there is a full book on exactly this.", f_rec,
                  y, (180, 180, 210, 255))
    y += 50

    thin_line(draw, y, ac=(255,255,255), alpha=30)
    y += 28

    f_booknum = load_font("Light", 30)
    draw_centered(draw, f"Book {book['num']} of 10", f_booknum, y, (*ac, 200))
    y += 48

    fsize = 76 if len(book["title"]) < 18 else 60
    f_title = load_font("Bold", fsize)
    for line in textwrap.wrap(book["title"], width=16):
        bb = draw.textbbox((0, 0), line, font=f_title)
        lw = bb[2] - bb[0]
        draw.text(((W - lw) // 2 + 2, y + 2), line, font=f_title, fill=(0,0,0,90))
        draw.text(((W - lw) // 2, y), line, font=f_title, fill=(255,255,255,255))
        y += fsize + 12

    y += 8
    f_sub = load_font("Italic", 32)
    for s in textwrap.wrap(book["subtitle"], width=30):
        bb = draw.textbbox((0, 0), s, font=f_sub)
        lw = bb[2] - bb[0]
        draw.text(((W - lw) // 2, y), s, font=f_sub, fill=(*ac, 210))
        y += 44

    y += 14
    gumroad = series_config.get("gumroad_link", "link in bio")
    f_link = load_font("Bold", 26)
    draw_centered(draw, gumroad, f_link, y, (*ac, 240))

    draw.rectangle([0, H - 80, W, H], fill=(*ac, 255))
    f_bot = load_font("SemiBold", 26)
    draw_centered(draw, "Full 10-book bundle  ·  link in bio", f_bot,
                  H - 54, (255, 255, 255, 255))

    return img


# ── Story Slide ───────────────────────────────────────────────────────────────
def make_story_slide(hook_text: str, caption_question: str,
                     series_config: dict,
                     photo: Image.Image | None = None) -> Image.Image:
    ac = hex_rgb(series_config["accent_hex"])

    if photo:
        story_photo = photo.resize((SW, SH), Image.LANCZOS)
        img = apply_photo_bg(story_photo, overlay_color=(5, 5, 12), overlay_alpha=155)
    else:
        img = Image.new("RGBA", (SW, SH), (10, 10, 14, 255))
        layer = Image.new("RGBA", (SW, SH), (0, 0, 0, 0))
        d = ImageDraw.Draw(layer)
        r = int(SW * 0.65)
        d.ellipse([SW - r, -r//2, SW + r//2, r], fill=(*ac, 22))
        img = Image.alpha_composite(img, layer)

    draw = ImageDraw.Draw(img)

    bar_h = 120
    draw.rectangle([0, 0, SW, bar_h], fill=(*ac, 255))
    f_bar = load_font("Regular", 34)
    draw_centered(draw, series_config["name"].upper(), f_bar,
                  (bar_h - 34) // 2, (255, 255, 255, 255), SW)

    words = hook_text.split()
    fsize = 96 if len(words) <= 5 else (78 if len(words) <= 8 else 64)
    wrap_w = 14 if len(words) <= 5 else (18 if len(words) <= 8 else 22)
    f_hook = load_font("Bold", fsize)
    lines = textwrap.wrap(hook_text, width=wrap_w)
    lh = fsize + 22
    total = len(lines) * lh
    y = bar_h + (int(SH * 0.48) - bar_h - total) // 2

    for line in lines:
        bb = draw.textbbox((0, 0), line, font=f_hook)
        lw = bb[2] - bb[0]
        draw.text(((SW - lw) // 2 + 3, y + 3), line, font=f_hook, fill=(0, 0, 0, 80))
        draw.text(((SW - lw) // 2, y), line, font=f_hook, fill=(255, 255, 255, 255))
        y += lh

    thin_line(draw, int(SH * 0.55), img_w=SW, ac=ac, alpha=100, margin=100)

    q_y = int(SH * 0.57)
    f_qlabel = load_font("SemiBold", 28)
    draw_centered(draw, "tell me in the comments", f_qlabel, q_y, (*ac, 200), SW)
    q_y += 48

    question = caption_question or "does this sound familiar to you?"
    f_q = load_font("Bold", 44)
    for ql in textwrap.wrap(question, width=22):
        bb = draw.textbbox((0, 0), ql, font=f_q)
        lw = bb[2] - bb[0]
        draw.text(((SW - lw) // 2, q_y), ql, font=f_q, fill=(255, 255, 255, 255))
        q_y += 58

    q_y += 20
    f_link = load_font("Regular", 28)
    draw_centered(draw, "Full bundle — link in bio", f_link, q_y,
                  (200, 200, 220, 220), SW)

    cta_h = 120
    draw.rectangle([0, SH - cta_h, SW, SH], fill=(*ac, 255))
    f_cta = load_font("Bold", 34)
    draw_centered(draw, "Get the Full Bundle", f_cta, SH - cta_h + 22,
                  (255, 255, 255, 255), SW)
    f_handle = load_font("Regular", 24)
    draw_centered(draw, f"@{series_config['ig_page_username']}",
                  f_handle, SH - cta_h + 72, (255, 255, 255, 190), SW)

    return img


# ── Hashtags ──────────────────────────────────────────────────────────────────
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

def extract_question(caption: str) -> str:
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
    for k in ["cold_open", "mirror_text", "p1_head", "p1_sub", "p2_head", "p2_sub",
              "turn_admission", "turn_lesson", "payoff_belief", "payoff_action", "save_line"]:
        if k in content:
            content[k] = clean(content[k])

    # Fetch photo (optional — needs PEXELS_API_KEY)
    keyword = NICHE_KEYWORDS.get(series_config["series_id"], "nature minimal")
    photo = fetch_pexels_photo(keyword)
    if photo:
        print(f"    ✓ Photo fetched for '{keyword}'")
    else:
        print(f"    ~ No photo (Pexels key not set or unavailable) — using gradient")

    ts     = datetime.now().strftime("%Y%m%d_%H%M%S")
    sid    = series_config["series_id"]
    bnum   = book["num"]
    prefix = f"s{sid:02d}_b{bnum:02d}_{ts}"

    slides_data = [
        ("hook",    make_slide_cold_open(content["cold_open"], series_config, photo)),
        ("mirror",  make_slide_mirror(content["mirror_text"], series_config)),
        ("point1",  make_slide_point_dark(1, content["p1_head"], content["p1_sub"], series_config)),
        ("flip",    make_slide_rhythm_flip(content["p2_head"], content["p2_sub"], series_config)),
        ("turn",    make_slide_turn(content["turn_admission"], content["turn_lesson"], series_config, photo)),
        ("payoff",  make_slide_payoff(content["payoff_belief"], content["payoff_action"], series_config)),
        ("cta",     make_slide_cta(book, series_config)),
    ]

    slide_paths = []
    for label, slide_img in slides_data:
        path = os.path.join(OUTPUT_DIR, f"{prefix}_{label}.jpg")
        save_jpg(slide_img, path)
        slide_paths.append(path)
        print(f"    ✓ slide_{label}: {os.path.basename(path)}")

    caption_text = content.get("caption", "")
    caption_text = re.sub(r'https?://\S+', '', caption_text).strip()
    caption_text = re.sub(r'\w+\.gumroad\.com\S*', '', caption_text).strip()
    caption_text = clean(caption_text)

    hashtags = build_hashtags(series_config)
    caption  = f"{caption_text}\n\n{hashtags}"
    story_question = extract_question(caption_text)

    story_img  = make_story_slide(content["cold_open"], story_question, series_config, photo)
    story_path = os.path.join(OUTPUT_DIR, f"{prefix}_story.jpg")
    save_jpg(story_img, story_path)
    print(f"    ✓ story: {os.path.basename(story_path)}")

    return {
        "slide_paths":  slide_paths,
        "story_path":   story_path,
        "caption":      caption,
        "book_title":   book["title"],
        "book_num":     book["num"],
        "series_name":  series_config["name"],
    }


if __name__ == "__main__":
    from config import SERIES_PAGES
    result = generate_carousel(SERIES_PAGES[0], book_num=1)
    print(f"\nCaption:\n{result['caption'][:500]}...")
