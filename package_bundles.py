"""
Packages all 10 series bundles into zip files ready for Gumroad upload.
Each zip contains: all 10 PDFs + all 10 cover JPGs + a README

Output: /Users/shivaadinath/Desktop/ebooks/bundles/
"""

import os
import zipfile
import glob

BASE   = "/Users/shivaadinath/Desktop/ebooks"
OUT    = os.path.join(BASE, "bundles")
os.makedirs(OUT, exist_ok=True)

SERIES = [
    {"folder": "1 - The Somatic Reset Series",      "name": "Somatic_Reset_Series"},
    {"folder": "2 - The GLP-1 Lifestyle Series",    "name": "GLP1_Lifestyle_Series"},
    {"folder": "3 - The ADHD Blueprint Series",     "name": "ADHD_Blueprint_Series"},
    {"folder": "4 - The Money Healing Series",      "name": "Money_Healing_Series"},
    {"folder": "5 - The Hormone Reset Series",      "name": "Hormone_Reset_Series"},
    {"folder": "6 - The AI Professional Series",    "name": "AI_Professional_Series"},
    {"folder": "7 - The Inner Healing Series",      "name": "Inner_Healing_Series"},
    {"folder": "8 - The Career Reset Series",       "name": "Career_Reset_Series"},
    {"folder": "9 - The Relationship Reset Series", "name": "Relationship_Reset_Series"},
    {"folder": "10 - The Calm Parent Series",       "name": "Calm_Parent_Series"},
]

def make_readme(series_name: str, pdfs: list) -> str:
    book_list = "\n".join(f"  {i+1:02d}. {os.path.basename(p)}" for i, p in enumerate(pdfs))
    return f"""Thank you for your purchase!
{'='*50}

{series_name} — Complete 10-Book Bundle

WHAT'S INCLUDED
{book_list}

HOW TO READ
- Open any PDF with Adobe Acrobat, Preview (Mac),
  or any free PDF reader
- All files are print-ready (6x9 inches, 300 DPI)

IMPORTANT
These books are for educational purposes only.
They are not a substitute for professional,
medical, financial, or legal advice.

Questions? Contact us via Gumroad.
{'='*50}
"""

total_size = 0

for s in SERIES:
    folder_path = os.path.join(BASE, s["folder"])
    zip_name    = f"{s['name']}_Bundle.zip"
    zip_path    = os.path.join(OUT, zip_name)

    # Collect PDFs and covers
    pdfs   = sorted(glob.glob(os.path.join(folder_path, "*.pdf")))
    covers = sorted(glob.glob(os.path.join(folder_path, "cover_*.jpg")))

    if not pdfs:
        print(f"  ⚠  No PDFs found in: {s['folder']}")
        continue

    print(f"\n  Packaging: {s['folder']}")
    print(f"    PDFs:   {len(pdfs)}")
    print(f"    Covers: {len(covers)}")

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        # README at root
        zf.writestr("README.txt", make_readme(s["folder"], pdfs))

        # PDFs in /Books/
        for pdf in pdfs:
            zf.write(pdf, os.path.join("Books", os.path.basename(pdf)))

        # Covers in /Covers/ (bonus — buyers love having cover art)
        for cover in covers:
            zf.write(cover, os.path.join("Covers", os.path.basename(cover)))

    size_mb = os.path.getsize(zip_path) / (1024 * 1024)
    total_size += size_mb
    print(f"    ✓ {zip_name}  ({size_mb:.1f} MB)")

print(f"\n{'='*50}")
print(f"All 10 bundles packaged in: {OUT}")
print(f"Total size: {total_size:.1f} MB")
print(f"{'='*50}")
print("\nNext: upload each zip to Gumroad as a product.")
