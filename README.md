# Google Ads Ops Skill

A focused OpenClaw skill for **Google Ads audit, optimization, and campaign build** workflows.

## What it does
- **Audit**: diagnose performance issues with clear, prioritized fixes
- **Optimize**: suggest budget, keyword, and ad improvements
- **Build**: generate campaign/ad group/keyword structures from a business profile

## Required inputs
You’ll need Google Ads API access:
- Developer token
- OAuth client_id / client_secret / refresh_token
- Login customer ID (and optional customer ID)

**Where to put config:**
- Prefer **env vars** (local only) — see `.env.example`, or
- A **local JSON file** you pass at runtime

See `references/google_ads_setup.md` for exact fields + examples.

## Business profile
Campaign builds use a business profile file (or Q&A prompt). Schema is in:
- `references/business_profile.schema.md`

## Files
```
SKILL.md
references/
  google_ads_setup.md
  business_profile.schema.md
scripts/
```

## Usage (after packaging)
This skill is intended to be packaged into a `.skill` file and loaded by OpenClaw.

```bash
scripts/package_skill.py /path/to/google-ads-ops
```

---
**Note:** Never commit credentials. Store secrets locally (env vars or local JSON file).
