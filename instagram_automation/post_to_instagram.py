"""
Post to Instagram via Graph API.
Handles:
  - Carousel posts (multiple images → each uploaded separately → carousel container → publish)
  - Story posts (single image → story container → publish)
"""

import os
import time
import hashlib
import requests


# ── Image hosting via Cloudinary ──────────────────────────────────────────────
def upload_image(image_path: str) -> str:
    """Uploads to Cloudinary (free 25GB/month), returns public HTTPS URL."""
    cloud_name = os.environ.get("CLOUDINARY_CLOUD_NAME", "")
    api_key    = os.environ.get("CLOUDINARY_API_KEY", "")
    api_secret = os.environ.get("CLOUDINARY_API_SECRET", "")

    if not all([cloud_name, api_key, api_secret]):
        raise ValueError("CLOUDINARY_CLOUD_NAME / CLOUDINARY_API_KEY / CLOUDINARY_API_SECRET not set")

    ts  = int(time.time())
    sig = hashlib.sha1(f"timestamp={ts}{api_secret}".encode()).hexdigest()

    with open(image_path, "rb") as f:
        resp = requests.post(
            f"https://api.cloudinary.com/v1_1/{cloud_name}/image/upload",
            data={"api_key": api_key, "timestamp": ts, "signature": sig},
            files={"file": f},
            timeout=60,
        )

    if resp.status_code != 200:
        raise RuntimeError(f"Cloudinary upload failed ({resp.status_code}): {resp.text[:300]}")

    url = resp.json().get("secure_url", "")
    if not url:
        raise RuntimeError("No secure_url in Cloudinary response")
    print(f"    ↑ uploaded: {url}")
    return url


# ── Create a single media container ───────────────────────────────────────────
def create_media_container(ig_user_id: str, access_token: str,
                            image_url: str,
                            is_carousel_item: bool = False,
                            media_type: str = "IMAGE") -> str:
    params = {
        "image_url":    image_url,
        "access_token": access_token,
    }
    if is_carousel_item:
        params["is_carousel_item"] = "true"
    if media_type != "IMAGE":
        params["media_type"] = media_type

    resp = requests.post(
        f"https://graph.instagram.com/v21.0/{ig_user_id}/media",
        params=params,
        timeout=30,
    )
    if resp.status_code != 200:
        raise RuntimeError(f"Container creation failed: {resp.text[:300]}")

    container_id = resp.json().get("id")
    if not container_id:
        raise RuntimeError("No container ID in response")
    return container_id


# ── Publish a container ────────────────────────────────────────────────────────
def publish_container(ig_user_id: str, access_token: str,
                      container_id: str) -> str:
    time.sleep(3)   # brief pause before publish
    resp = requests.post(
        f"https://graph.instagram.com/v21.0/{ig_user_id}/media_publish",
        params={
            "creation_id":  container_id,
            "access_token": access_token,
        },
        timeout=30,
    )
    if resp.status_code != 200:
        raise RuntimeError(f"Publish failed: {resp.text[:300]}")
    return resp.json().get("id", "")


# ── Post a carousel ────────────────────────────────────────────────────────────
def post_carousel(slide_paths: list[str], caption: str,
                  access_token: str, ig_user_id: str) -> dict:
    """
    Posts a multi-image carousel.
    Returns: {"success": bool, "post_id": str}
    """
    try:
        # Upload all slide images
        item_ids = []
        for i, path in enumerate(slide_paths):
            print(f"  Uploading slide {i+1}/{len(slide_paths)}...")
            image_url = upload_image(path)
            item_id = create_media_container(ig_user_id, access_token,
                                             image_url, is_carousel_item=True)
            item_ids.append(item_id)
            time.sleep(1)

        # Create carousel container
        print("  Creating carousel container...")
        carousel_resp = requests.post(
            f"https://graph.instagram.com/v21.0/{ig_user_id}/media",
            params={
                "media_type":   "CAROUSEL",
                "children":     ",".join(item_ids),
                "caption":      caption,
                "access_token": access_token,
            },
            timeout=30,
        )
        if carousel_resp.status_code != 200:
            raise RuntimeError(f"Carousel container failed: {carousel_resp.text[:300]}")

        carousel_id = carousel_resp.json().get("id")
        if not carousel_id:
            raise RuntimeError("No carousel container ID returned")

        print(f"  Publishing carousel {carousel_id}...")
        post_id = publish_container(ig_user_id, access_token, carousel_id)
        print(f"  ✓ Carousel posted! ID: {post_id}")
        return {"success": True, "post_id": post_id, "type": "carousel"}

    except Exception as e:
        print(f"  ✗ Carousel error: {e}")
        return {"success": False, "error": str(e), "type": "carousel"}


# ── Post a story ───────────────────────────────────────────────────────────────
def post_story(image_path: str, access_token: str, ig_user_id: str) -> dict:
    """
    Posts a single image as an Instagram Story.
    Note: Stories via Graph API require instagram_content_publish permission.
    """
    try:
        print("  Uploading story image...")
        image_url = upload_image(image_path)

        # Create story container (media_type=IMAGE for photo story)
        resp = requests.post(
            f"https://graph.instagram.com/v21.0/{ig_user_id}/media",
            params={
                "image_url":    image_url,
                "media_type":   "IMAGE",
                "access_token": access_token,
            },
            timeout=30,
        )
        if resp.status_code != 200:
            raise RuntimeError(f"Story container failed: {resp.text[:300]}")

        container_id = resp.json().get("id")
        if not container_id:
            raise RuntimeError("No story container ID")

        # Publish to stories endpoint
        time.sleep(2)
        pub_resp = requests.post(
            f"https://graph.instagram.com/v21.0/{ig_user_id}/media_publish",
            params={
                "creation_id":  container_id,
                "access_token": access_token,
            },
            timeout=30,
        )
        if pub_resp.status_code != 200:
            raise RuntimeError(f"Story publish failed: {pub_resp.text[:300]}")

        story_id = pub_resp.json().get("id", "")
        print(f"  ✓ Story posted! ID: {story_id}")
        return {"success": True, "post_id": story_id, "type": "story"}

    except Exception as e:
        print(f"  ✗ Story error: {e}")
        return {"success": False, "error": str(e), "type": "story"}
