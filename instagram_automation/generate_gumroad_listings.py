"""
Generates Gumroad product listing copy for all 10 bundle products.
Run this once and paste into Gumroad.
"""

from config import SERIES_PAGES

PRICE = 37  # bundle price in USD

def generate_listing(series: dict) -> str:
    books = series["books"]
    book_list = "\n".join(
        f"  {b['num']:02d}. {b['title']} — {b['subtitle']}"
        for b in books
    )

    return f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PRODUCT: {series['name']} — Complete 10-Book Bundle
PRICE: ${PRICE}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

HEADLINE:
{series['bundle_tagline']}

DESCRIPTION:
This isn't a single ebook. It's a complete 10-book series covering every angle of {series['niche'].split(',')[0].strip()}.

Each book is written for real people — not textbooks, not clinical jargon. Clear, practical, and easy to read at your own pace.

What's included:
{book_list}

Format: PDF (all 10 books delivered instantly)
Reading level: General audience
Length: Each book is a focused, practical guide

Whether you're just starting to explore this topic or you've been at it for a while and want something more structured — this bundle covers it all.

━━━━━━━━━━
FAQ:
Q: How do I get the books?
A: Instantly after purchase — you'll get a download link for all 10 PDFs.

Q: Are these printable?
A: Yes. All PDFs are formatted for both screen reading and printing.

Q: Is this advice?
A: These books are for educational purposes only. They are not a substitute for professional, medical, financial, or legal advice.
━━━━━━━━━━

TAGS: {', '.join(h.lstrip('#') for h in series['hashtags'][:6])}
"""

if __name__ == "__main__":
    output_path = "gumroad_listings.txt"
    with open(output_path, "w") as f:
        for series in SERIES_PAGES:
            listing = generate_listing(series)
            f.write(listing + "\n\n")
            print(f"✓ {series['name']}")

    print(f"\nAll listings saved to: {output_path}")
    print("Open it and paste each listing directly into Gumroad.")
