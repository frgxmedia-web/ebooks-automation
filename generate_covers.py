"""
Cover Image Generator — All 100 Ebooks
Produces 1800x2700 JPG covers (6×9 @ 300 dpi) for every book.
Design: dark premium base, series accent colour geometry, bold Poppins typography.
"""

from PIL import Image, ImageDraw, ImageFont
import os, math

FONT_DIR = os.path.join(os.path.dirname(__file__), "fonts")
BASE_DIR = os.path.dirname(__file__)

W, H = 1800, 2700   # 6 × 9 @ 300 dpi

# ── helpers ───────────────────────────────────────────────────────────────────
def font(style, size):
    files = {
        "bold":     "Poppins-Bold.ttf",
        "regular":  "Poppins-Regular.ttf",
        "italic":   "Poppins-Italic.ttf",
        "semibold": "Poppins-SemiBold.ttf",
        "light":    "Poppins-Light.ttf",
    }
    return ImageFont.truetype(os.path.join(FONT_DIR, files[style]), size)

def hex_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def wrap(draw, text, fnt, max_w):
    """Word-wrap text to fit max_w pixels. Returns list of lines."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        test = (cur + " " + w).strip()
        bb = draw.textbbox((0, 0), test, font=fnt)
        if bb[2] - bb[0] > max_w and cur:
            lines.append(cur)
            cur = w
        else:
            cur = test
    if cur:
        lines.append(cur)
    return lines

def text_w(draw, text, fnt):
    bb = draw.textbbox((0, 0), text, font=fnt)
    return bb[2] - bb[0]

def centred(draw, text, fnt, y, colour, shadow=True):
    tw = text_w(draw, text, fnt)
    x = (W - tw) // 2
    if shadow:
        draw.text((x + 5, y + 5), text, fill=(0, 0, 0, 80), font=fnt)
    draw.text((x, y), text, fill=colour, font=fnt)

# ── cover renderer ────────────────────────────────────────────────────────────
def make_cover(title, subtitle, series_name, book_num, accent_hex, out_path):
    ac  = hex_rgb(accent_hex)
    bg  = (12, 12, 28)                # deep navy

    # ── base image (RGBA so alpha blending works) ────────────────────────────
    img  = Image.new("RGBA", (W, H), (*bg, 255))
    draw = ImageDraw.Draw(img)

    # ── decorative geometry ──────────────────────────────────────────────────
    # large circle top-right (visible glow)
    circ = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    cd   = ImageDraw.Draw(circ)
    r = 900
    cd.ellipse([W - 300 - r, -350 - r, W - 300 + r, -350 + r], fill=(*ac, 55))
    img = Image.alpha_composite(img, circ)

    # medium circle bottom-left
    circ2 = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    cd2   = ImageDraw.Draw(circ2)
    r2 = 700
    cd2.ellipse([-350 - r2, H - 200 - r2, -350 + r2, H - 200 + r2], fill=(*ac, 40))
    img = Image.alpha_composite(img, circ2)

    # vertical stripe cluster, right side
    stripe = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd     = ImageDraw.Draw(stripe)
    for i in range(18):
        x0 = W - 280 + i * 9
        sd.rectangle([x0, 0, x0 + 4, H], fill=(*ac, 12))
    img = Image.alpha_composite(img, stripe)

    draw = ImageDraw.Draw(img)

    # ── top accent bar ───────────────────────────────────────────────────────
    bar_h = 155
    draw.rectangle([0, 0, W, bar_h], fill=(*ac, 255))
    f_series = font("regular", 46)
    s_upper  = series_name.upper()
    centred(draw, s_upper, f_series, (bar_h - 46) // 2 + 4,
            (255, 255, 255, 255), shadow=False)

    bbar_h = 170
    content_top    = bar_h + 80
    content_bottom = H - bbar_h - 60

    # ── measure title ────────────────────────────────────────────────────────
    pad = 110
    max_title_w = W - pad * 2

    if   len(title) <= 18: f_title = font("bold", 185)
    elif len(title) <= 30: f_title = font("bold", 155)
    elif len(title) <= 45: f_title = font("bold", 125)
    elif len(title) <= 60: f_title = font("bold", 105)
    else:                  f_title = font("bold",  88)

    title_lines = wrap(draw, title, f_title, max_title_w)
    lh_title    = int(f_title.size * 1.20)

    # ── measure subtitle ─────────────────────────────────────────────────────
    max_sub_w = W - 160
    if   len(subtitle) <= 45: f_sub = font("italic", 70)
    elif len(subtitle) <= 75: f_sub = font("italic", 60)
    else:                     f_sub = font("italic", 52)

    sub_lines = wrap(draw, subtitle, f_sub, max_sub_w)
    lh_sub    = int(f_sub.size * 1.38)

    # ── measure book number + hairline ───────────────────────────────────────
    f_num    = font("light", 44)
    num_h    = 44
    gap_num  = 40         # space after number line
    div_gap  = 52         # space above/below the divider line
    div_h    = 5

    # total content height
    total_h = (num_h + gap_num
               + len(title_lines) * lh_title
               + div_gap + div_h + div_gap
               + len(sub_lines) * lh_sub)

    available = content_bottom - content_top
    start_y   = content_top + max(0, (available - total_h) // 2)

    # ── book number ──────────────────────────────────────────────────────────
    draw.text((pad, start_y), f"No. {book_num:02d}",
              fill=(*ac, 220), font=f_num)
    # thin hairline after number
    hl_y = start_y + num_h + 18
    draw.rectangle([pad, hl_y, W - pad, hl_y + 3], fill=(*ac, 160))

    cur_y = hl_y + gap_num - 15

    # ── title ────────────────────────────────────────────────────────────────
    for line in title_lines:
        tw = text_w(draw, line, f_title)
        x  = (W - tw) // 2
        # subtle shadow
        draw.text((x + 6, cur_y + 6), line, fill=(0, 0, 0, 80),  font=f_title)
        draw.text((x, cur_y),         line, fill=(255, 255, 255), font=f_title)
        cur_y += lh_title

    # ── divider with diamond ─────────────────────────────────────────────────
    cur_y += div_gap - lh_title // 4
    draw.rectangle([pad, cur_y, W - pad, cur_y + div_h], fill=(*ac, 255))
    mx = W // 2
    d  = 16
    draw.polygon([(mx, cur_y - d + 2), (mx + d, cur_y + 2),
                  (mx, cur_y + d + 3), (mx - d, cur_y + 2)], fill=(*ac, 255))
    cur_y += div_h + div_gap

    # ── subtitle ─────────────────────────────────────────────────────────────
    for line in sub_lines:
        centred(draw, line, f_sub, cur_y, (*ac, 235), shadow=False)
        cur_y += lh_sub

    # ── bottom bar ───────────────────────────────────────────────────────────
    draw.rectangle([0, H - bbar_h, W, H],           fill=(*ac, 255))
    draw.rectangle([0, H - bbar_h, W, H - bbar_h + 6], fill=(0, 0, 0, 50))
    f_bot = font("light", 35)
    centred(draw, "educational purposes only  ·  not professional advice",
            f_bot, H - bbar_h + 68, (255, 255, 255, 210), shadow=False)

    # ── save ─────────────────────────────────────────────────────────────────
    img.convert("RGB").save(out_path, "JPEG", quality=96)
    print(f"  ✓ {os.path.basename(out_path)}")


# ── all 100 books ─────────────────────────────────────────────────────────────
SERIES = [
    {
        "name": "The Somatic Reset Series",
        "accent": "#4FC3F7",
        "folder": "1 - The Somatic Reset Series",
        "books": [
            (1,  "The Vagus Nerve Reset",            "A 30-Day Protocol to Heal Your Nervous System"),
            (2,  "Somatic Exercises for Anxiety",    "Release Tension and Rewire Your Stress Response"),
            (3,  "The Dopamine Reset",               "Reclaiming Focus, Motivation and Calm in a Distracted World"),
            (4,  "Burnout to Baseline",              "A Somatic Guide to Recovering When You Have Nothing Left"),
            (5,  "Sleep from the Inside Out",        "Rewiring the Nervous System for Deep, Natural Rest"),
            (6,  "When Grief Lives in the Body",     "Somatic Practices for Moving Through Loss"),
            (7,  "ADHD and the Nervous System",      "Understanding the Wiring Behind the Chaos"),
            (8,  "Chronic Pain and the Nervous System", "The Missing Piece in Pain Management"),
            (9,  "Trauma Release Exercises",         "A Guided Body-Based Approach to Healing"),
            (10, "The Perimenopause Reset",          "Somatic Practices for Hormonal Transitions"),
        ],
    },
    {
        "name": "The GLP-1 Lifestyle Series",
        "accent": "#00B894",
        "folder": "2 - The GLP-1 Lifestyle Series",
        "books": [
            (1,  "The GLP-1 Nutrition Guide",        "Eating for Maximum Results on Semaglutide and Tirzepatide"),
            (2,  "GLP-1 for Women Over 40",          "Navigating Weight Loss, Hormones, and Midlife Changes"),
            (3,  "Managing GLP-1 Side Effects",      "A Practical Guide to Nausea, Fatigue, and More"),
            (4,  "Strength Training on GLP-1",       "Protecting Your Muscle While Losing Fat"),
            (5,  "GLP-1 Meal Prep Made Simple",      "Batch Cooking for Smaller Appetite and Real Life"),
            (6,  "Long-Term Success on GLP-1",       "Building the Habits That Last Beyond the Medication"),
            (7,  "Hair Loss and GLP-1",              "What's Happening and What to Do About It"),
            (8,  "GLP-1 and Mental Health",          "Mood, Anxiety, and the Gut-Brain Connection"),
            (9,  "GLP-1 on a Budget",               "Making the Most of Medication Without Breaking the Bank"),
            (10, "The GLP-1 Fasting Protocol",       "Combining Intermittent Fasting with Your Medication"),
        ],
    },
    {
        "name": "The ADHD Blueprint Series",
        "accent": "#FF6B6B",
        "folder": "3 - The ADHD Blueprint Series",
        "books": [
            (1,  "The ADHD Entrepreneur",            "Build a Business That Works With Your Brain, Not Against It"),
            (2,  "ADHD for Freelancers",             "Systems, Pricing, and Getting Things Done Without a Boss"),
            (3,  "The ADHD Parent",                  "Raising Kids When Your Own Brain Won't Stay Still"),
            (4,  "ADHD and Money",                   "Why Managing Finances Feels Impossible and What Actually Helps"),
            (5,  "ADHD in Relationships",            "How to Connect, Communicate, and Stop the Cycles"),
            (6,  "The Late-Diagnosed Woman",         "Understanding ADHD When You've Spent Decades Coping Alone"),
            (7,  "ADHD and Creativity",              "How Your Distractible Brain Is Wired for Original Thinking"),
            (8,  "ADHD + AI",                        "Using Artificial Intelligence to Work Smarter With Your Brain"),
            (9,  "ADHD Burnout Recovery",            "What Happens When You Can't Compensate Anymore"),
            (10, "The ADHD Sales Engine",            "Building a Career in Sales When Focus Is Your Challenge"),
        ],
    },
    {
        "name": "The Money Healing Series",
        "accent": "#F7B731",
        "folder": "4 - The Money Healing Series",
        "books": [
            (1,  "The Scarcity Mindset Fix",         "Rewire Your Relationship with Money from the Inside Out"),
            (2,  "Debt Without Shame",               "A Practical and Emotional Guide to Getting Out and Staying Out"),
            (3,  "First-Generation Wealth",          "Building Generational Money When No One Taught You How"),
            (4,  "The Emotional Spender",            "Understanding and Changing the Habits That Keep You Broke"),
            (5,  "Side Income Without Burnout",      "Real Ways to Earn More Without Wrecking Your Life"),
            (6,  "Money and Mental Health",          "The Hidden Link Between Your Finances and Your Wellbeing"),
            (7,  "Negotiating Your Worth",           "How to Ask for More — and Actually Get It"),
            (8,  "The Minimalist Budget",            "Spend Less, Stress Less, and Still Have a Life"),
            (9,  "Investing for People Who Don't Trust the Market", "A Skeptic's Guide to Building Wealth Anyway"),
            (10, "Couples and Money",                "How to Stop Fighting About Finances and Start Building Together"),
        ],
    },
    {
        "name": "The Hormone Reset Series",
        "accent": "#9B59B6",
        "folder": "5 - The Hormone Reset Series",
        "books": [
            (1,  "Cortisol and the Body Under Stress",   "Understanding Your Stress Hormone and How to Work With It"),
            (2,  "Estrogen in Balance",                  "What Every Woman Needs to Know About Her Most Talked-About Hormone"),
            (3,  "Thyroid Health Simplified",            "Understanding the Gland That Runs Your Metabolism"),
            (4,  "Perimenopause Without Panic",          "What's Happening, Why It Matters, and What You Can Do"),
            (5,  "Insulin Resistance Explained",         "What It Is, Why It Happens, and How to Reverse It"),
            (6,  "Testosterone for Women",               "The Hormone You Weren't Told About — and Why It Matters"),
            (7,  "Gut Hormones and the Hunger Code",     "Leptin, Ghrelin, and the Science of Why You Eat"),
            (8,  "Cycle Syncing",                        "How to Work With Your Hormonal Rhythm Instead of Against It"),
            (9,  "Men's Hormonal Health",                "Testosterone, Stress, Fatigue, and the Things Nobody Tells You"),
            (10, "Hormones After 50",                    "Navigating Menopause, Andropause, and the Long-Term Picture"),
        ],
    },
    {
        "name": "The AI Professional Series",
        "accent": "#2D9CDB",
        "folder": "6 - The AI Professional Series",
        "books": [
            (1,  "AI for the Overwhelmed Professional",  "Cut Your Workload in Half Using Tools You Already Have"),
            (2,  "Prompt Engineering for Non-Coders",    "How to Talk to AI Like You Know What You're Doing"),
            (3,  "AI for Freelancers",                   "Work Smarter, Earn More, and Scale Without Burning Out"),
            (4,  "AI Writing for Content Creators",      "How to Create More Without Sounding Like a Bot"),
            (5,  "AI for Small Business Owners",         "Practical Tools to Run Your Business Without a Big Team"),
            (6,  "AI Ethics for Everyday Users",         "How to Use Powerful Tools Responsibly"),
            (7,  "The AI Job Search",                    "Land Interviews Faster Using Tools Your Competition Isn't Using Yet"),
            (8,  "AI for Educators and Trainers",        "Save Hours, Engage More, and Teach Better"),
            (9,  "AI Tools Compared",                    "ChatGPT, Claude, Gemini, and More — What to Use When"),
            (10, "Future-Proofing Your Career with AI",  "The Skills, Mindset, and Strategy for Staying Relevant"),
        ],
    },
    {
        "name": "The Inner Healing Series",
        "accent": "#E17055",
        "folder": "7 - The Inner Healing Series",
        "books": [
            (1,  "Healing After Childhood Wounds",       "How the Past Lives in the Present — and What to Do About It"),
            (2,  "The Boundaries Blueprint",             "How to Say No Without Guilt and Yes Without Resentment"),
            (3,  "Self-Compassion in Practice",          "How to Be on Your Own Side"),
            (4,  "Anger: Understanding the Fire Within", "What Your Anger Is Telling You — and How to Listen"),
            (5,  "Loneliness and the Art of Connection", "Understanding Modern Disconnection and Finding Your Way Back"),
            (6,  "The Highly Sensitive Person's Guide to Thriving", "Understanding Your Trait and Building a Life That Works"),
            (7,  "Forgiveness Is for You",               "Letting Go Without Letting Anyone Off the Hook"),
            (8,  "Emotional Intelligence at Work and Home", "Understanding and Using Your Emotions Well"),
            (9,  "Finding Purpose After Loss",           "Navigating Grief, Change, and Identity"),
            (10, "The Anxiety Reset",                    "Understanding, Managing, and Transforming Your Relationship With Worry"),
        ],
    },
    {
        "name": "The Career Reset Series",
        "accent": "#27AE60",
        "folder": "8 - The Career Reset Series",
        "books": [
            (1,  "Burned Out and Starting Over",         "Leave Quietly, Land Intentionally, Don't Make the Same Mistake Twice"),
            (2,  "The Introverted Professional",         "How to Advance Without Pretending to Be Someone Else"),
            (3,  "Negotiating at Every Career Stage",    "From First Job to Executive Compensation"),
            (4,  "Remote Work Mastery",                  "Thrive, Advance, and Stay Visible When You're Not in the Room"),
            (5,  "The Career in Your 40s",               "Why It's Not Too Late for a Reinvention and How to Pull It Off"),
            (6,  "Building a Personal Brand That Actually Works", "How to Become Known for What You're Best At"),
            (7,  "Difficult Conversations at Work",      "How to Say Hard Things Without Making Everything Harder"),
            (8,  "Leadership Without Authority",         "Lead, Influence, and Drive Results When You're Not the Boss"),
            (9,  "The Consultant Mindset",               "Think Like an Independent Expert and Get Paid Like One"),
            (10, "Work-Life Integration",                "Why 'Balance' Is the Wrong Frame — and What Actually Works"),
        ],
    },
    {
        "name": "The Relationship Reset Series",
        "accent": "#E84393",
        "folder": "9 - The Relationship Reset Series",
        "books": [
            (1,  "Attachment Styles and Why You Love the Way You Do", "Understanding Your Relational Blueprint"),
            (2,  "Communication That Actually Connects", "The Relationship Skills That Nobody Teaches You"),
            (3,  "Recovering From Infidelity",           "What It Takes to Heal — Whether You Stay or Go"),
            (4,  "The Art of Healthy Conflict",          "Turn Arguments Into Connection Instead of Destruction"),
            (5,  "Loving Someone With Anxiety",          "How to Support Your Partner Without Losing Yourself"),
            (6,  "Rebuilding Trust",                     "How Trust Is Broken, How It's Repaired, and What It Costs to Skip Either Step"),
            (7,  "Intimacy After Trauma",                "Reclaiming Connection After Your Body Said No"),
            (8,  "Parenting as Partners",                "How to Stay Connected When a Child Changes Everything"),
            (9,  "Dating After 35",                      "What Changes, What Stays the Same, and How to Find Someone Real"),
            (10, "When to Leave and When to Stay",       "The Honest Questions That Help You Decide"),
        ],
    },
    {
        "name": "The Calm Parent Series",
        "accent": "#16A085",
        "folder": "10 - The Calm Parent Series",
        "books": [
            (1,  "The Regulated Parent",                 "How Your Nervous System Shapes Your Child's"),
            (2,  "Raising Emotionally Intelligent Kids", "How to Teach Feelings Before They Become Problems"),
            (3,  "Screens, Social Media, and the Developing Brain", "What the Research Actually Says — and What to Do"),
            (4,  "Discipline That Doesn't Break the Relationship", "Effective Boundaries Without Shame or Fear"),
            (5,  "Raising Kids Who Can Fail",            "Building Resilience in a World That Makes It Too Easy"),
            (6,  "Parenting the Anxious Child",          "Calm Strategies for the Child Who Worries Too Much"),
            (7,  "Talking to Kids About Hard Topics",    "Death, Divorce, Race, Sex, and Everything Else You've Been Avoiding"),
            (8,  "The Teenage Brain",                    "Understanding Adolescence So You Can Actually Survive It"),
            (9,  "Single Parenting With Intention",      "Raising Children Well When You're the Only Parent in the Room"),
            (10, "Mindful Parenting",                    "How to Be Present With Your Children in a World Designed to Pull You Away"),
        ],
    },
]

# ── run ───────────────────────────────────────────────────────────────────────
total = 0
for s in SERIES:
    folder = os.path.join(BASE_DIR, s["folder"])
    print(f"\n── {s['name']}")
    for num, title, subtitle in s["books"]:
        out = os.path.join(folder, f"cover_{num:02d}.jpg")
        make_cover(title, subtitle, s["name"], num, s["accent"], out)
        total += 1

print(f"\n✓ {total} covers generated.")
