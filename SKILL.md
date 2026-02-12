---
name: google-ads-ops
description: Use when the user wants to run Google Ads campaigns with arbitrage strategy, A/B test target groups and value propositions, or needs week-by-week campaign optimization with hypothesis-driven experiments.
---

# Google Ads Ops

## Overview
Run Google Ads campaigns with an arbitrage mindset: test hypotheses, measure Cost per Order (CpO), and iterate weekly. Focus on conversions, not vanity metrics. Each experiment tests ONE bold change so results are attributable.

## When to Use
- User mentions Google Ads, AdSense, or paid acquisition
- User wants to optimize conversion performance
- User has budget for experiments and wants measurable ROI
- User is starting from scratch OR has existing campaigns

## Phase 1: Socratic Discovery (Initialization)
**Goal:** Uncover the user's business model and arbitrage opportunity through questions.

### Opening Questions (ask 3–5)
1) **Business model:** “What do you sell and what does each conversion earn you?” (unit economics)
2) **Target audience:** “Who buys this? Describe your ideal customer.”
   → Follow‑up: “What do they care about most when making this decision?”
3) **Value proposition:** “Why do customers choose you over alternatives?”
   → Follow‑up: “If you had to guess, what's the ONE thing that makes them convert?”
4) **Budget:** “What's your comfortable loss limit to learn what works?” (default: 30€ per experiment)
5) **Experience:** “Have you run ads before? What worked or didn't?” (assume 0, ask kindly)
6) **Target group size:** “How many potential customers exist for this? Local, national, global?”

### Transition to Execution
After 3–5 questions, pause and offer:
> “I have enough to propose initial experiments. We can proceed now, or I can ask 3 more questions to refine the strategy. What do you prefer?”

If user says **proceed** → Move to Phase 2.

### Exit Criteria for Discovery
- ✅ Unit economics understood (what you pay vs. what you earn per conversion)
- ✅ Target audience hypothesis defined
- ✅ Value proposition hypothesis defined
- ✅ Experiment budget confirmed
- ✅ User has chosen to proceed

## Phase 2: Hypothesis‑Driven Execution

### Budget Splitting Rule
**30€ per experiment.** Each experiment tests **ONE** hypothesis.

Example budget split (150€ total):
- Experiment A: 30€ — Test audience segment “fashion‑conscious millennials”
- Experiment B: 30€ — Test value prop “Save 2 hours per week”
- Experiment C: 30€ — Test keyword cluster “personal color analysis”
- Experiment D: 30€ — Test landing page variant A
- Experiment E: 30€ — Test bidding strategy (maximize clicks vs conversions)

### The ONE Change Rule
Each experiment changes exactly **one** variable. Never mix changes.

| ❌ Bad (mixed changes) | ✅ Good (single change) |
|------------------------|-------------------------|
| New audience + new ad copy | New audience (same ad copy) |
| New keywords + higher bids | New keywords (same bids) |
| New landing page + new CTA | New landing page (same CTA) |

**Why:** If results change, we must know WHAT caused it.

### Campaign Proposal Format
Before booking, present to user:

**Proposed Experiment: [Name]**
- **Hypothesis:** “[Audience/Value prop/Channel] will achieve [CpO target]”
- **What we're testing:** [Single variable]
- **Control (baseline):** [What we're comparing against]
- **Budget:** 30€ over 7 days
- **Target metrics:**
  - Expected CpO: [X]€
  - Target conversions: [Y]
- **Campaign structure:**
  - Audience: [segment]
  - Keywords: [list]
  - Ad copy: [variant]
  - Landing page: [URL]

**Proceed? (yes/no/modify)**

User approval → book campaign directly.

## Phase 3: Weekly Review Cycle

### Every 7 Days — Proactive report
```markdown
## Week [N] Performance Report

### Summary
- Spend: [X]€
- Conversions: [Y]
- Cost per Order (CpO): [Z]€
- Customer journey duration: [D] days

### Experiments & Outcomes
- Experiment A: [result + decision]
- Experiment B: [result + decision]
- Experiment C: [result + decision]

### Decisions (Next Actions)
- Kill: [experiment]
- Scale: [experiment]
- Iterate: [experiment]

### New Hypotheses for Next Week
- [Hypothesis 1]
- [Hypothesis 2]
```

## Resources
- API credentials & setup: `references/google_ads_setup.md`
- Business profile schema: `references/business_profile.schema.md`

## Safety / rules
- Never store credentials in repo.
- Always confirm budget caps and conversion goals before recommending spend changes.
- If data is missing or API access fails, ask for credentials or business profile.
