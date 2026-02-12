---
name: google-ads-ops
description: Google Ads campaign audit, optimization, and build workflows using the Google Ads API. Use when the user wants to analyze account performance, optimize campaigns/keywords/ads, or build new campaigns from a business profile.
---

# Google Ads Ops

## Overview
Run Google Ads audits, optimizations, and new campaign builds using Google Ads API data. This skill focuses on: (1) account/campaign diagnostics, (2) concrete optimization recommendations, and (3) structured campaign build plans based on a business profile.

## Workflow (high‑level)
1) **Access & scope**
   - Load credentials (env or local JSON)
   - Confirm account/customer id
2) **Audit**
   - Pull last 7/30/90 day metrics
   - Identify spend, CTR, CVR, CPA, ROAS issues
   - Flag structural problems (too many broad keywords, low QS, ad/landing mismatch)
3) **Optimize**
   - Provide prioritized fixes with expected impact
   - Suggest negative keywords, bid/budget changes, ad copy tests
4) **Build**
   - Use business profile to create campaign structure, ad groups, keywords, ads
   - Provide launch checklist + measurement plan

## Inputs required
- **Google Ads API credentials** (developer token + OAuth)
- **Account/customer id**
- **Business profile** (file or Q&A)

See:
- `references/google_ads_setup.md`
- `references/business_profile.schema.md`

## Output expectations
- **Audit**: concise table of key metrics + 3–7 prioritized fixes
- **Optimization**: concrete actions (what, why, impact, how to implement)
- **Build**: campaign structure (campaign → ad groups → keywords → ads), plus tracking notes

## Safety / rules
- Never store credentials in repo.
- Always confirm budget caps and conversion goals before recommending spend changes.
- If data is missing or API access fails, ask for credentials or business profile.

## Examples (trigger phrases)
- “Audit my Google Ads account.”
- “Optimize our search campaigns.”
- “Build a Google Ads campaign for this business.”
- “Use this business profile file to create campaigns.”
