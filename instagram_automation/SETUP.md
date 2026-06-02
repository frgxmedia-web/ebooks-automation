# Instagram Automation — Setup Guide

## What this does
- Posts to 10 Instagram pages automatically, 2x per day
- Generates unique content (quotes, tips, previews) using Gemini 2.0 Flash (free)
- Creates custom 1080×1080 branded post images using Pillow
- Runs on GitHub Actions (completely free, zero server cost)
- Logs every post to `posts/post_log.jsonl`

---

## Step 1: Create 10 Instagram Business Accounts

For each series, create a new Instagram account:

| Account Username | Series |
|---|---|
| @somaticresetbooks | The Somatic Reset Series |
| @glp1lifestylebooks | The GLP-1 Lifestyle Series |
| @adhdblueprintbooks | The ADHD Blueprint Series |
| @moneyhealingbooks | The Money Healing Series |
| @hormoneresetbooks | The Hormone Reset Series |
| @aiprofessionalbooks | The AI Professional Series |
| @innerhealingbooks | The Inner Healing Series |
| @careerresetbooks | The Career Reset Series |
| @relationshipresetbooks | The Relationship Reset Series |
| @calmparentbooks | The Calm Parent Series |

**For each account:**
1. Create with a new email (use Gmail aliases: yourname+somatic@gmail.com etc.)
2. Go to Settings → Account → Switch to Professional Account → Creator or Business
3. Connect to a Facebook Page (create a new one if needed — just a dummy page)
4. Set the bio to the matching bio_cta text in config.py
5. Add your Payhip/Etsy bundle link in bio

---

## Step 2: Get Instagram Graph API Credentials

For each Instagram account:

1. Go to [developers.facebook.com](https://developers.facebook.com)
2. Create a Meta App → Consumer type → Add Instagram product
3. Go to **Instagram → Basic Display → Add an Instagram Test User** (add your account)
4. OR use **Instagram Graph API** (for Business accounts):
   - Add the Instagram account as an asset in your Meta App
   - Get a **Page Access Token** (long-lived, 60 days, refreshable)
   - Get your **Instagram User ID** (go to `https://graph.facebook.com/me?access_token=YOUR_TOKEN`)

**Token refresh:** Tokens expire every 60 days. Re-run the setup or use the token refresh endpoint.

---

## Step 3: Get Free API Keys

### Gemini 2.0 Flash (FREE)
1. Go to [aistudio.google.com](https://aistudio.google.com)
2. Click "Get API Key"
3. Create a new API key — **free tier: 15 requests/minute, 1M requests/day** ✓

### imgbb (FREE image hosting)
1. Go to [api.imgbb.com](https://api.imgbb.com)
2. Sign up free → Get API key
3. Free tier: unlimited uploads, images hosted publicly ✓

---

## Step 4: Push to GitHub

```bash
cd /Users/shivaadinath/Desktop/ebooks
git init
git add .
git commit -m "initial commit: 100 ebooks + instagram automation"
git remote add origin https://github.com/YOUR_USERNAME/ebooks-automation.git
git push -u origin main
```

---

## Step 5: Add GitHub Secrets

In your repo → Settings → Secrets and variables → Actions → New repository secret:

Add ALL of these:

```
GEMINI_API_KEY          = your-gemini-api-key
IMGBB_API_KEY           = your-imgbb-key

IG_TOKEN_SOMATIC        = your-instagram-access-token
IG_USER_ID_SOMATIC      = your-instagram-user-id

IG_TOKEN_GLP1           = ...
IG_USER_ID_GLP1         = ...

IG_TOKEN_ADHD           = ...
IG_USER_ID_ADHD         = ...

IG_TOKEN_MONEY          = ...
IG_USER_ID_MONEY        = ...

IG_TOKEN_HORMONE        = ...
IG_USER_ID_HORMONE      = ...

IG_TOKEN_AI             = ...
IG_USER_ID_AI           = ...

IG_TOKEN_INNER          = ...
IG_USER_ID_INNER        = ...

IG_TOKEN_CAREER         = ...
IG_USER_ID_CAREER       = ...

IG_TOKEN_RELATIONSHIP   = ...
IG_USER_ID_RELATIONSHIP = ...

IG_TOKEN_CALM           = ...
IG_USER_ID_CALM         = ...
```

---

## Step 6: Test with Dry Run

In GitHub → Actions → "Instagram Auto-Post" → Run workflow:
- Set `dry_run` to `true`
- Set `series` to `1`
- Run it — check the artifact log to confirm image + caption were generated

---

## Step 7: Go Live

Remove the dry_run flag. The workflow runs automatically:
- **9:00 AM UTC** (4am ET / 1am PT)
- **6:00 PM UTC** (2pm ET / 11am PT)

That's **20 posts/day** across all 10 pages.

---

## Bundle Selling Strategy

**Start with The Somatic Reset Series bundle:**
- Create a Payhip product: "Complete Somatic Reset Series (10 Books)"
- Price at $27–$47 (vs $4.99 each = perceived value of $49.90)
- Upload all 10 PDFs as a zip
- Put the Payhip link in @somaticresetbooks bio
- Every post drives traffic to that one link

**Expand:** Add one series bundle per week as each page grows.

---

## Costs

| Tool | Cost |
|------|------|
| GitHub Actions | FREE (2000 min/month free) |
| Gemini 2.0 Flash | FREE (1M requests/day) |
| imgbb | FREE |
| Instagram | FREE |
| **Total** | **$0/month** |
