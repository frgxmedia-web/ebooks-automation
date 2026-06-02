"""
Generate Instagram post image + caption using Gemini 2.0 Flash
Produces a 1080x1080 quote/tip card (Pillow) + caption text
"""

import os
import json
import textwrap
import random
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import google.generativeai as genai

# ── Paths ──────────────────────────────────────────────────────────────────────
FONTS_DIR = os.path.join(os.path.dirname(__file__), "..", "fonts")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "posts")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Font loader ────────────────────────────────────────────────────────────────
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

# ── Hex to RGB ─────────────────────────────────────────────────────────────────
def hex_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

# ── Gemini content generation ─────────────────────────────────────────────────
def generate_content(series_config: dict, post_type: str) -> dict:
    """
    Returns: {
        "headline": "short punchy text for the card (max 12 words)",
        "subtext": "1-2 sentence supporting text for the card",
        "caption": "Instagram caption with emojis, call to action",
    }
    """
    api_key = os.environ.get("GEMINI_API_KEY", "")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not set")

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name="gemini-2.0-flash")

    post_type_instructions = {
        "quote": "Write an original, insightful quote related to this topic. Not clichéd.",
        "tip":   "Write one practical, actionable tip someone can use today.",
        "preview": "Write a compelling teaser — something that makes people want to learn more.",
        "question": "Write a thought-provoking question that makes people reflect on their life.",
        "stat":  "Write a surprising but plausible fact or insight about this topic.",
    }

    prompt = f"""
You are a social media content creator for a wellness and self-development brand.

Series: {series_config['name']}
Niche: {series_config['niche']}
Post type: {post_type} — {post_type_instructions[post_type]}

Generate a social media post. Return ONLY valid JSON with these exact keys:
- "headline": Max 10 words. Bold, punchy, no quotes around it.
- "subtext": 1–2 sentences expanding on the headline. Warm, human, not clinical.
- "caption": Full Instagram caption (3–5 sentences). Include 1–2 relevant emojis naturally. End with a soft CTA like "Save this post." or "Which one resonates?" Do NOT include hashtags here.

Rules:
- Do NOT sound like AI
- Do NOT use em-dashes
- Do NOT say "I" or "we"
- Write like a knowledgeable friend, not a textbook
- Return ONLY the JSON object, nothing else
"""

    response = model.generate_content(prompt)
    raw = response.text.strip()

    # Strip markdown code block if present
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
        raw = raw.strip()

    return json.loads(raw)


# ── Post image generator ───────────────────────────────────────────────────────
def make_post_image(content: dict, series_config: dict, post_type: str) -> str:
    """
    Creates a 1080x1080 Instagram post image.
    Returns the file path of the saved image.
    """
    W, H = 1080, 1080
    ac = hex_rgb(series_config["accent_hex"])
    bg = (12, 12, 28)  # deep navy (matches ebook covers)

    # ── Base ──────────────────────────────────────────────────────────────────
    img = Image.new("RGBA", (W, H), (*bg, 255))

    # ── Decorative background elements ────────────────────────────────────────
    # Large faded circle top-right
    circle_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    cd = ImageDraw.Draw(circle_layer)
    cr = 480
    cx, cy = W - 80, -80
    cd.ellipse([cx - cr, cy - cr, cx + cr, cy + cr], fill=(*ac, 35))
    img = Image.alpha_composite(img, circle_layer)

    # Medium circle bottom-left
    circle_layer2 = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    cd2 = ImageDraw.Draw(circle_layer2)
    cr2 = 280
    cx2, cy2 = 60, H + 40
    cd2.ellipse([cx2 - cr2, cy2 - cr2, cx2 + cr2, cy2 + cr2], fill=(*ac, 28))
    img = Image.alpha_composite(img, circle_layer2)

    draw = ImageDraw.Draw(img)

    # ── Top bar ────────────────────────────────────────────────────────────────
    bar_h = 100
    draw.rectangle([0, 0, W, bar_h], fill=(*ac, 255))

    font_series = load_font("Regular", 32)
    series_label = series_config["name"].upper()
    bbox = draw.textbbox((0, 0), series_label, font=font_series)
    tw = bbox[2] - bbox[0]
    draw.text(((W - tw) // 2, (bar_h - 32) // 2), series_label,
              font=font_series, fill=(255, 255, 255, 255))

    # ── Post type badge ────────────────────────────────────────────────────────
    badge_labels = {
        "quote":    "✦  QUOTE",
        "tip":      "✦  TODAY'S TIP",
        "preview":  "✦  BOOK PREVIEW",
        "question": "✦  THINK ABOUT THIS",
        "stat":     "✦  DID YOU KNOW",
    }
    font_badge = load_font("Light", 28)
    badge_text = badge_labels.get(post_type, "✦  POST")
    badge_bbox = draw.textbbox((0, 0), badge_text, font=font_badge)
    bw = badge_bbox[2] - badge_bbox[0]
    draw.text(((W - bw) // 2, bar_h + 50), badge_text,
              font=font_badge, fill=(*ac, 200))

    # ── Headline ───────────────────────────────────────────────────────────────
    headline = content.get("headline", "")
    words = headline.split()
    # Dynamic sizing based on length
    if len(words) <= 4:
        font_size = 88
        wrap_w = 18
    elif len(words) <= 7:
        font_size = 72
        wrap_w = 22
    else:
        font_size = 58
        wrap_w = 28

    font_headline = load_font("Bold", font_size)
    lines = textwrap.wrap(headline, width=wrap_w)

    # Measure headline block
    line_gap = int(font_size * 0.25)
    headline_h = len(lines) * font_size + (len(lines) - 1) * line_gap

    # Measure subtext block
    subtext = content.get("subtext", "")
    font_sub = load_font("Regular", 36)
    sub_lines = textwrap.wrap(subtext, width=42)
    sub_line_gap = 14
    sub_h = len(sub_lines) * 36 + (len(sub_lines) - 1) * sub_line_gap

    # Total content height
    divider_space = 60
    total_h = headline_h + divider_space + sub_h

    # Vertical center in available area
    top_zone = bar_h + 110
    bot_zone = H - 130
    available = bot_zone - top_zone
    start_y = top_zone + max(0, (available - total_h) // 2)

    # Draw shadow + headline lines
    y = start_y
    for line in lines:
        bbox_l = draw.textbbox((0, 0), line, font=font_headline)
        lw = bbox_l[2] - bbox_l[0]
        x = (W - lw) // 2
        # shadow
        draw.text((x + 2, y + 2), line, font=font_headline, fill=(0, 0, 0, 120))
        draw.text((x, y), line, font=font_headline, fill=(255, 255, 255, 255))
        y += font_size + line_gap

    # ── Divider ────────────────────────────────────────────────────────────────
    y += 20
    line_y = y + 10
    draw.rectangle([120, line_y, W - 120, line_y + 2], fill=(*ac, 160))
    # Diamond
    dm = 10
    draw.polygon([(W // 2, line_y - dm), (W // 2 + dm, line_y),
                  (W // 2, line_y + dm), (W // 2 - dm, line_y)],
                 fill=(*ac, 255))
    y = line_y + dm + 18

    # ── Subtext ────────────────────────────────────────────────────────────────
    for s_line in sub_lines:
        bbox_s = draw.textbbox((0, 0), s_line, font=font_sub)
        sw = bbox_s[2] - bbox_s[0]
        draw.text(((W - sw) // 2, y), s_line,
                  font=font_sub, fill=(210, 210, 230, 255))
        y += 36 + sub_line_gap

    # ── Bottom bar ─────────────────────────────────────────────────────────────
    bot_bar_h = 90
    draw.rectangle([0, H - bot_bar_h, W, H], fill=(*ac, 255))

    font_handle = load_font("SemiBold", 30)
    handle = f"@{series_config['ig_page_username']}"
    hbbox = draw.textbbox((0, 0), handle, font=font_handle)
    hw = hbbox[2] - hbbox[0]
    draw.text(((W - hw) // 2, H - bot_bar_h + (bot_bar_h - 30) // 2),
              handle, font=font_handle, fill=(255, 255, 255, 255))

    # ── Save ───────────────────────────────────────────────────────────────────
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    fname = f"post_series{series_config['series_id']}_{post_type}_{ts}.jpg"
    out_path = os.path.join(OUTPUT_DIR, fname)
    img.convert("RGB").save(out_path, "JPEG", quality=95)
    return out_path


# ── Caption builder ────────────────────────────────────────────────────────────
def build_caption(content: dict, series_config: dict) -> str:
    caption = content.get("caption", "")
    hashtags = " ".join(random.sample(series_config["hashtags"],
                                      min(12, len(series_config["hashtags"]))))
    return f"{caption}\n\n{hashtags}"


# ── Main entry ────────────────────────────────────────────────────────────────
def generate_post(series_config: dict, post_type: str = None) -> dict:
    """
    Full pipeline: generate content → create image → build caption
    Returns: {"image_path": str, "caption": str}
    """
    if post_type is None:
        post_type = random.choice(["quote", "tip", "preview", "question", "stat"])

    print(f"  Generating {post_type} post for: {series_config['name']}")
    content = generate_content(series_config, post_type)
    image_path = make_post_image(content, series_config, post_type)
    caption = build_caption(content, series_config)

    print(f"  ✓ Image: {image_path}")
    return {
        "image_path":  image_path,
        "caption":     caption,
        "headline":    content.get("headline"),
        "series_name": series_config["name"],
        "post_type":   post_type,
    }


if __name__ == "__main__":
    # Quick local test — needs GEMINI_API_KEY set
    from config import SERIES_PAGES
    result = generate_post(SERIES_PAGES[0], post_type="quote")
    print(f"\nHeadline: {result['headline']}")
    print(f"Caption preview:\n{result['caption'][:300]}...")
