"""
Main runner — called by GitHub Actions
  09:00 UTC → carousel post (book A)
  12:00 UTC → story (bundle cover)
  18:00 UTC → carousel post (book B, different from A)

Usage:
  python run_posts.py                      # auto-detect slot from current UTC hour
  python run_posts.py --slot carousel1     # force first carousel slot
  python run_posts.py --slot carousel2     # force second carousel slot
  python run_posts.py --slot story         # force story slot
  python run_posts.py --series 1           # run for one series only
  python run_posts.py --dry-run            # generate everything, skip posting
"""

import os
import sys
import json
import argparse
import random
from datetime import datetime, timezone

from config import SERIES_PAGES
from generate_carousel import generate_carousel
from post_to_instagram import post_carousel, post_story

LOG_FILE = os.path.join(os.path.dirname(__file__), "posts", "post_log.jsonl")
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)


# ── Book selector — ensures carousel 1 and 2 don't repeat the same book ───────
def pick_books_for_today(series_config: dict) -> tuple[int, int]:
    """
    Deterministically picks two different book numbers for today.
    Uses date + series_id as seed so it's reproducible within the same day.
    """
    today = datetime.now(timezone.utc).strftime("%Y%m%d")
    seed  = int(today) + series_config["series_id"] * 37
    rng   = random.Random(seed)
    nums  = list(range(1, 11))
    rng.shuffle(nums)
    return nums[0], nums[1]


def detect_slot() -> str:
    hour = datetime.now(timezone.utc).hour
    if hour < 11:
        return "carousel1"
    elif hour < 15:
        return "story"
    else:
        return "carousel2"


# ── Per-series runner ──────────────────────────────────────────────────────────
def run_series(series_config: dict, slot: str, dry_run: bool = False) -> dict:
    sid = series_config["series_id"]
    print(f"\n{'='*58}")
    print(f"  Series {sid}: {series_config['name']}")
    print(f"  Slot: {slot}  |  Dry run: {dry_run}")
    print(f"{'='*58}")

    access_token = os.environ.get(series_config["ig_access_token_env"], "")
    ig_user_id   = os.environ.get(series_config["ig_user_id_env"], "")

    book_a, book_b = pick_books_for_today(series_config)

    if slot == "story":
        # Story: just the bundle cover, no Gemini call needed
        from generate_carousel import make_story_slide, save_jpg, OUTPUT_DIR
        from datetime import datetime as dt
        ts  = dt.now().strftime("%Y%m%d_%H%M%S")
        story_img  = make_story_slide(series_config)
        story_path = os.path.join(OUTPUT_DIR, f"s{sid:02d}_story_{ts}.jpg")
        save_jpg(story_img, story_path)
        print(f"  ✓ Story image: {os.path.basename(story_path)}")

        result = {
            "series_name": series_config["name"],
            "slot": slot,
            "story_path": story_path,
        }

        if dry_run:
            result["posted"] = False
            result["dry_run"] = True
        elif not access_token or not ig_user_id:
            print(f"  ⚠  Credentials not set — skipping post")
            result["posted"] = False
            result["error"] = "missing_credentials"
        else:
            post_result = post_story(story_path, access_token, ig_user_id)
            result.update(post_result)
            result["posted"] = post_result["success"]

    else:
        # Carousel post
        book_num = book_a if slot == "carousel1" else book_b
        carousel = generate_carousel(series_config, book_num=book_num)

        result = {
            "series_name": series_config["name"],
            "slot":        slot,
            "book_title":  carousel["book_title"],
            "book_num":    carousel["book_num"],
            "slide_paths": carousel["slide_paths"],
        }

        if dry_run:
            print(f"  [DRY RUN] Would post carousel for Book {book_num}: {carousel['book_title']}")
            print(f"  Caption preview: {carousel['caption'][:180]}...")
            result["posted"] = False
            result["dry_run"] = True
        elif not access_token or not ig_user_id:
            print(f"  ⚠  Credentials not set — skipping post")
            result["posted"] = False
            result["error"] = "missing_credentials"
        else:
            post_result = post_carousel(
                carousel["slide_paths"],
                carousel["caption"],
                access_token,
                ig_user_id,
            )
            result.update(post_result)
            result["posted"] = post_result["success"]

    log_result(result)
    return result


def log_result(result: dict):
    entry = {
        "timestamp":   datetime.utcnow().isoformat(),
        "series_name": result.get("series_name"),
        "slot":        result.get("slot"),
        "book_title":  result.get("book_title"),
        "book_num":    result.get("book_num"),
        "posted":      result.get("posted"),
        "post_id":     result.get("post_id"),
        "dry_run":     result.get("dry_run", False),
        "error":       result.get("error"),
    }
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")


# ── Entry point ────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--slot",    choices=["carousel1", "carousel2", "story"],
                        default=None, help="Which slot to run (auto-detected if not set)")
    parser.add_argument("--series", type=int, default=None,
                        help="Run for one series only (1–10)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Generate content + images but don't post to Instagram")
    args = parser.parse_args()

    slot = args.slot or detect_slot()
    pages = [s for s in SERIES_PAGES if s["series_id"] == args.series] \
            if args.series else SERIES_PAGES

    if not pages:
        print(f"Series {args.series} not found")
        sys.exit(1)

    results      = []
    success_count = 0

    for series_config in pages:
        try:
            result = run_series(series_config, slot=slot, dry_run=args.dry_run)
            results.append(result)
            if result.get("posted") or result.get("dry_run"):
                success_count += 1
        except Exception as e:
            print(f"  ✗ Unexpected error for {series_config['name']}: {e}")
            results.append({"series_name": series_config["name"], "error": str(e)})

    print(f"\n{'='*58}")
    print(f"  Done. {success_count}/{len(pages)} successful  |  slot: {slot}")
    print(f"  Log → {LOG_FILE}")
    print(f"{'='*58}")


if __name__ == "__main__":
    main()
