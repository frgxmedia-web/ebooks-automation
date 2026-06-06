"""
Generates ONE bundle cover per series (10 total).
Size: 1600x2400px — works for Gumroad, Payhip, Etsy, Ko-fi
Design: Bold series name, "Complete 10-Book Bundle", all 10 titles listed.
Output: /bundles/covers/somatic_bundle_cover.jpg etc.
"""

import os
import textwrap
from PIL import Image, ImageDraw, ImageFont

FONTS_DIR  = "/Users/shivaadinath/Desktop/ebooks/fonts"
OUTPUT_DIR = "/Users/shivaadinath/Desktop/ebooks/bundles/covers"
os.makedirs(OUTPUT_DIR, exist_ok=True)

W, H = 1600, 2400

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
    return ImageFont.truetype(os.path.join(FONTS_DIR, name_map[variant]), size)

def draw_centered(draw, text, font, y, color, w=W):
    bb = draw.textbbox((0,0), text, font=font)
    x = (w - (bb[2]-bb[0])) // 2
    draw.text((x, y), text, font=font, fill=color)
    return bb[3] - bb[1]

def make_bundle_cover(series: dict) -> str:
    ac  = hex_rgb(series["accent_hex"])
    bg  = (10, 10, 24)
    books = series["books"]

    img  = Image.new("RGBA", (W, H), (*bg, 255))

    # ── Decorative circles ────────────────────────────────────────────────────
    for layer_data in [
        (W - 60, -60, 600, 38),
        (80, H + 60, 380, 28),
        (W // 2, H // 2, 900, 8),
    ]:
        cx, cy, r, alpha = layer_data
        circle = Image.new("RGBA", (W, H), (0,0,0,0))
        cd = ImageDraw.Draw(circle)
        cd.ellipse([cx-r, cy-r, cx+r, cy+r], fill=(*ac, alpha))
        img = Image.alpha_composite(img, circle)

    draw = ImageDraw.Draw(img)

    # ── Top accent bar ────────────────────────────────────────────────────────
    bar_h = 160
    draw.rectangle([0, 0, W, bar_h], fill=(*ac, 255))

    f_series = load_font("Regular", 44)
    draw_centered(draw, series["name"].upper(), f_series,
                  (bar_h - 44) // 2, (255, 255, 255, 255))

    # ── COMPLETE BUNDLE badge ─────────────────────────────────────────────────
    y = bar_h + 55
    f_badge = load_font("SemiBold", 34)
    draw_centered(draw, "✦   COMPLETE 10-BOOK BUNDLE   ✦", f_badge, y, (*ac, 220))
    y += 62

    # ── Tagline ───────────────────────────────────────────────────────────────
    f_tag = load_font("Italic", 46)
    tagline = f'"{series["bundle_tagline"]}"'
    lines = textwrap.wrap(tagline, width=34)
    for line in lines:
        h_used = draw_centered(draw, line, f_tag, y, (210, 210, 235, 255))
        y += h_used + 12
    y += 30

    # ── Divider ───────────────────────────────────────────────────────────────
    draw.rectangle([int(W*0.08), y, int(W*0.92), y+3], fill=(*ac, 150))
    dm = 14
    draw.polygon([(W//2, y-dm), (W//2+dm, y), (W//2, y+dm), (W//2-dm, y)],
                 fill=(*ac, 255))
    y += dm + 40

    # ── Book list (single column, clean) ─────────────────────────────────────
    f_num   = load_font("SemiBold", 34)
    f_title = load_font("Regular",  34)
    f_sub   = load_font("Light",    26)
    row_gap = 100

    for book in books:
        num_label = f"{book['num']:02d}"
        bb = draw.textbbox((0,0), num_label, font=f_num)
        nw = bb[2] - bb[0]

        x_num   = int(W * 0.09)
        x_title = x_num + nw + 18

        draw.text((x_num, y),   num_label,      font=f_num,   fill=(*ac, 255))
        draw.text((x_title, y), book["title"],  font=f_title, fill=(235, 235, 250, 255))
        draw.text((x_title, y + 38), book["subtitle"], font=f_sub, fill=(160, 160, 185, 255))
        y += row_gap

    y += 10

    # ── Bottom bar ────────────────────────────────────────────────────────────
    bot_h = 130
    draw.rectangle([0, H - bot_h, W, H], fill=(*ac, 255))
    f_bot = load_font("SemiBold", 36)
    draw_centered(draw, "PDF  ·  Instant Download  ·  All 10 Books Included",
                  f_bot, H - bot_h + (bot_h - 36) // 2, (255,255,255,255))

    # ── Save ──────────────────────────────────────────────────────────────────
    slug = series["name"].lower().replace(" ", "_").replace("the_", "")
    out_path = os.path.join(OUTPUT_DIR, f"{slug}bundle_cover.jpg")
    img.convert("RGB").save(out_path, "JPEG", quality=96)
    return out_path


SERIES = [
    {
        "name": "The Somatic Reset Series",
        "accent_hex": "#1ABC9C",
        "bundle_tagline": "Reset your nervous system. Reclaim your body.",
        "books": [
            {"num": 1,  "title": "The Vagus Nerve Reset",         "subtitle": "Rewire Your Nervous System for Calm"},
            {"num": 2,  "title": "Trauma Stored in the Body",      "subtitle": "Understanding Somatic Memory"},
            {"num": 3,  "title": "The Freeze Response",            "subtitle": "Why You Shut Down and How to Thaw"},
            {"num": 4,  "title": "Breathwork for Survival Mode",   "subtitle": "Breathe Your Way Out of Stress"},
            {"num": 5,  "title": "Grounding When the World Spins", "subtitle": "Embodied Techniques for Anxiety"},
            {"num": 6,  "title": "The Tension Release Method",     "subtitle": "Let Go of What the Body Holds"},
            {"num": 7,  "title": "Somatic Boundaries",             "subtitle": "Feeling Safe in Your Own Skin"},
            {"num": 8,  "title": "The Gut-Brain Reset",            "subtitle": "How Your Belly Holds Your Emotions"},
            {"num": 9,  "title": "Sleep and the Nervous System",   "subtitle": "Why You Can't Switch Off at Night"},
            {"num": 10, "title": "Living Regulated",               "subtitle": "A Life Beyond Survival Mode"},
        ],
    },
    {
        "name": "The GLP-1 Lifestyle Series",
        "accent_hex": "#3498DB",
        "bundle_tagline": "Everything you need to know about GLP-1 — in one bundle.",
        "books": [
            {"num": 1,  "title": "GLP-1 Explained",                "subtitle": "What These Medications Actually Do"},
            {"num": 2,  "title": "Eating on GLP-1",                "subtitle": "Nutrition That Works With the Medication"},
            {"num": 3,  "title": "Managing Side Effects",          "subtitle": "Nausea, Fatigue, and What's Normal"},
            {"num": 4,  "title": "The Muscle Question",            "subtitle": "Preserving Strength While Losing Weight"},
            {"num": 5,  "title": "Mental Shifts on GLP-1",         "subtitle": "When Food No Longer Controls You"},
            {"num": 6,  "title": "Exercise and GLP-1",             "subtitle": "Moving Your Body at Every Stage"},
            {"num": 7,  "title": "Coming Off GLP-1",               "subtitle": "Transitioning Without Gaining It Back"},
            {"num": 8,  "title": "GLP-1 for Type 2 Diabetes",      "subtitle": "Beyond Weight Loss"},
            {"num": 9,  "title": "The Emotional Weight",           "subtitle": "Body Image, Identity, and the Scale"},
            {"num": 10, "title": "Sustaining the Results",         "subtitle": "Life After the Medication"},
        ],
    },
    {
        "name": "The ADHD Blueprint Series",
        "accent_hex": "#E67E22",
        "bundle_tagline": "10 books. One complete ADHD operating manual.",
        "books": [
            {"num": 1,  "title": "How the ADHD Brain Works",        "subtitle": "Finally, an Explanation That Makes Sense"},
            {"num": 2,  "title": "The Executive Function Playbook", "subtitle": "Systems for the Systemless Mind"},
            {"num": 3,  "title": "ADHD and Emotions",               "subtitle": "Rejection, Rage, and Riding the Waves"},
            {"num": 4,  "title": "Focus on Demand",                 "subtitle": "Getting Things Done Without Willpower"},
            {"num": 5,  "title": "ADHD at Work",                    "subtitle": "Thriving in Environments Built for Others"},
            {"num": 6,  "title": "ADHD in Relationships",           "subtitle": "When One Partner Has ADHD"},
            {"num": 7,  "title": "ADHD and Sleep",                  "subtitle": "Why Your Brain Won't Shut Up at Night"},
            {"num": 8,  "title": "Women and ADHD",                  "subtitle": "The Late Diagnosis No One Saw Coming"},
            {"num": 9,  "title": "Medication Questions Answered",   "subtitle": "The Honest Guide to ADHD Meds"},
            {"num": 10, "title": "Building Your ADHD Life",         "subtitle": "A System That Actually Fits You"},
        ],
    },
    {
        "name": "The Money Healing Series",
        "accent_hex": "#F7B731",
        "bundle_tagline": "Money isn't just math. It's deeply personal.",
        "books": [
            {"num": 1,  "title": "The Scarcity Mindset Fix",        "subtitle": "Why You Never Feel Like You Have Enough"},
            {"num": 2,  "title": "Debt Without Shame",              "subtitle": "A Compassionate Path to Paying It Off"},
            {"num": 3,  "title": "First-Generation Wealth",         "subtitle": "Building What Nobody Taught You"},
            {"num": 4,  "title": "The Emotional Spender",           "subtitle": "What's Really Behind the Impulse Buy"},
            {"num": 5,  "title": "Side Income Without Burnout",     "subtitle": "Earning More Without Losing Yourself"},
            {"num": 6,  "title": "Money and Mental Health",         "subtitle": "The Anxiety-Finance Connection"},
            {"num": 7,  "title": "Negotiating Your Worth",          "subtitle": "Ask for More Without the Guilt"},
            {"num": 8,  "title": "The Minimalist Budget",           "subtitle": "Spend Less on What Doesn't Matter"},
            {"num": 9,  "title": "Investing for the Skeptic",       "subtitle": "For People Who Don't Trust the Market"},
            {"num": 10, "title": "Couples and Money",               "subtitle": "Having the Conversation That Changes Everything"},
        ],
    },
    {
        "name": "The Hormone Reset Series",
        "accent_hex": "#9B59B6",
        "bundle_tagline": "Your hormones aren't broken — they're trying to tell you something.",
        "books": [
            {"num": 1,  "title": "Cortisol and the Body Under Stress","subtitle": "Why You're Wired and Tired at Once"},
            {"num": 2,  "title": "Estrogen in Balance",             "subtitle": "What Too Much or Too Little Really Means"},
            {"num": 3,  "title": "Thyroid Health Simplified",       "subtitle": "The Gland Everyone Ignores Until It Breaks"},
            {"num": 4,  "title": "Perimenopause Without Panic",     "subtitle": "What's Happening and What to Do About It"},
            {"num": 5,  "title": "Insulin Resistance Explained",    "subtitle": "The Hidden Driver Behind So Many Symptoms"},
            {"num": 6,  "title": "Testosterone for Women",          "subtitle": "Why You Need It and How to Support It"},
            {"num": 7,  "title": "Gut Hormones and the Hunger Code","subtitle": "Why Willpower Has Nothing to Do With It"},
            {"num": 8,  "title": "Cycle Syncing",                   "subtitle": "Working With Your Hormones, Not Against Them"},
            {"num": 9,  "title": "Men's Hormonal Health",           "subtitle": "Testosterone, Stress, and the Silent Decline"},
            {"num": 10, "title": "Hormones After 50",               "subtitle": "The Second Chapter Nobody Prepared You For"},
        ],
    },
    {
        "name": "The AI Professional Series",
        "accent_hex": "#2D9CDB",
        "bundle_tagline": "AI isn't replacing you. Someone using AI will.",
        "books": [
            {"num": 1,  "title": "AI for the Overwhelmed Professional","subtitle": "Where to Start When Everything Feels Like Too Much"},
            {"num": 2,  "title": "Prompt Engineering for Non-Coders","subtitle": "Get 10x Better Results From Any AI Tool"},
            {"num": 3,  "title": "AI for Freelancers",              "subtitle": "Charge More, Do More, Work Less"},
            {"num": 4,  "title": "AI Writing for Content Creators", "subtitle": "Your Voice, Amplified"},
            {"num": 5,  "title": "AI for Small Business Owners",    "subtitle": "The Tools That Actually Save You Time"},
            {"num": 6,  "title": "AI Ethics for Everyday Users",    "subtitle": "What You Should Actually Be Concerned About"},
            {"num": 7,  "title": "The AI Job Search",               "subtitle": "Find Work Faster in a Competitive Market"},
            {"num": 8,  "title": "AI for Educators and Trainers",   "subtitle": "Teaching Smarter in the Age of AI"},
            {"num": 9,  "title": "AI Tools Compared",               "subtitle": "Honest Breakdown of What's Worth Your Time"},
            {"num": 10, "title": "Future-Proofing Your Career",     "subtitle": "Stay Relevant When Everything Keeps Changing"},
        ],
    },
    {
        "name": "The Inner Healing Series",
        "accent_hex": "#E17055",
        "bundle_tagline": "You can't think your way out of what you felt your way into.",
        "books": [
            {"num": 1,  "title": "Healing After Childhood Wounds",  "subtitle": "What You Carried Into Adulthood"},
            {"num": 2,  "title": "The Boundaries Blueprint",        "subtitle": "Saying No Without Guilt or Explanation"},
            {"num": 3,  "title": "Self-Compassion in Practice",     "subtitle": "Being as Kind to Yourself as You Are to Others"},
            {"num": 4,  "title": "Anger",                           "subtitle": "Understanding the Fire Within"},
            {"num": 5,  "title": "Loneliness and Connection",       "subtitle": "Finding Your People in an Isolated World"},
            {"num": 6,  "title": "The Highly Sensitive Person",     "subtitle": "A Guide to Thriving, Not Just Surviving"},
            {"num": 7,  "title": "Forgiveness Is for You",          "subtitle": "Letting Go Without Letting Them Off the Hook"},
            {"num": 8,  "title": "Emotional Intelligence",          "subtitle": "At Work, at Home, and in the Mirror"},
            {"num": 9,  "title": "Finding Purpose After Loss",      "subtitle": "When Everything Falls Apart"},
            {"num": 10, "title": "The Anxiety Reset",               "subtitle": "Breaking the Cycle From the Inside Out"},
        ],
    },
    {
        "name": "The Career Reset Series",
        "accent_hex": "#27AE60",
        "bundle_tagline": "Burned out, stuck, or starting over — this series is for you.",
        "books": [
            {"num": 1,  "title": "Burned Out and Starting Over",    "subtitle": "What to Do When Work Has Taken Everything"},
            {"num": 2,  "title": "The Introverted Professional",    "subtitle": "Thriving Without Pretending to Be an Extrovert"},
            {"num": 3,  "title": "Negotiating at Every Career Stage","subtitle": "How to Ask — and Actually Get It"},
            {"num": 4,  "title": "Remote Work Mastery",             "subtitle": "Productivity, Boundaries, and Visibility from Home"},
            {"num": 5,  "title": "The Career in Your 40s",          "subtitle": "It's Not Too Late to Change Everything"},
            {"num": 6,  "title": "Building a Personal Brand",       "subtitle": "That Actually Works and Doesn't Feel Fake"},
            {"num": 7,  "title": "Difficult Conversations at Work", "subtitle": "Say the Hard Thing Without Burning Bridges"},
            {"num": 8,  "title": "Leadership Without Authority",    "subtitle": "Influence Without the Title"},
            {"num": 9,  "title": "The Consultant Mindset",          "subtitle": "Think Like a Freelancer, Even as an Employee"},
            {"num": 10, "title": "Work-Life Integration",           "subtitle": "Because Balance Was Always a Lie"},
        ],
    },
    {
        "name": "The Relationship Reset Series",
        "accent_hex": "#E84393",
        "bundle_tagline": "Love better. Connect deeper. Fight smarter.",
        "books": [
            {"num": 1,  "title": "Attachment Styles",               "subtitle": "Why You Love the Way You Do"},
            {"num": 2,  "title": "Communication That Connects",     "subtitle": "Actually Being Heard by the People You Love"},
            {"num": 3,  "title": "Recovering From Infidelity",      "subtitle": "Can You Stay? Can You Go? Can You Heal?"},
            {"num": 4,  "title": "The Art of Healthy Conflict",     "subtitle": "Fighting Without Destroying the Relationship"},
            {"num": 5,  "title": "Loving Someone With Anxiety",     "subtitle": "How to Support Without Losing Yourself"},
            {"num": 6,  "title": "Rebuilding Trust",                "subtitle": "After It's Been Broken"},
            {"num": 7,  "title": "Intimacy After Trauma",           "subtitle": "Reconnecting When You've Shut Down"},
            {"num": 8,  "title": "Parenting as Partners",           "subtitle": "Staying a Couple While Raising Kids"},
            {"num": 9,  "title": "Dating After 35",                 "subtitle": "The Real Rules Nobody Told You"},
            {"num": 10, "title": "When to Leave, When to Stay",     "subtitle": "The Honest Questions to Ask Yourself"},
        ],
    },
    {
        "name": "The Calm Parent Series",
        "accent_hex": "#16A085",
        "bundle_tagline": "You can't pour from an empty cup — and neither can your kids.",
        "books": [
            {"num": 1,  "title": "The Regulated Parent",            "subtitle": "How Your Nervous System Shapes Your Child's"},
            {"num": 2,  "title": "Raising Emotionally Intelligent Kids","subtitle": "Feelings Are Data, Not Drama"},
            {"num": 3,  "title": "Screens and the Developing Brain","subtitle": "What the Research Actually Says"},
            {"num": 4,  "title": "Discipline That Doesn't Damage",  "subtitle": "Firm, Kind, and Actually Effective"},
            {"num": 5,  "title": "Raising Kids Who Can Fail",       "subtitle": "Resilience Over Perfection"},
            {"num": 6,  "title": "Parenting the Anxious Child",     "subtitle": "How to Help Without Making It Worse"},
            {"num": 7,  "title": "Talking to Kids About Hard Topics","subtitle": "Death, Race, Bodies, and Everything In Between"},
            {"num": 8,  "title": "The Teenage Brain",               "subtitle": "Why They Do What They Do"},
            {"num": 9,  "title": "Single Parenting With Intention", "subtitle": "Doing It Alone Without Doing It Wrong"},
            {"num": 10, "title": "Mindful Parenting",               "subtitle": "Showing Up When You're Running on Empty"},
        ],
    },
]

if __name__ == "__main__":
    print("Generating 10 bundle covers...\n")
    for series in SERIES:
        path = make_bundle_cover(series)
        print(f"  ✓ {series['name']}")
        print(f"    → {os.path.basename(path)}")
    print(f"\nAll saved to: {OUTPUT_DIR}")
