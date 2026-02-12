# Business profile input (for campaign building)

The skill should load this from a user-provided file or ask questions interactively.

## Minimal fields
- **business_name**
- **website_url**
- **primary_offer** (what you sell)
- **target_customer**
- **top_locations** (countries/cities)
- **primary_goal** (leads / sales / signups)
- **monthly_budget**

## Optional fields
- **brand_voice** (tone)
- **key_competitors**
- **top_keywords** (if known)
- **conversion_actions** (form submit, purchase, call)

## Example JSON
```json
{
  "business_name": "ColorMatchAI",
  "website_url": "https://colormatchai.com",
  "primary_offer": "AI-powered personal color analysis",
  "target_customer": "fashion-conscious users who want their season/palette",
  "top_locations": ["US", "UK", "DE"],
  "primary_goal": "purchases",
  "monthly_budget": 1500,
  "brand_voice": "clear, confident, helpful",
  "conversion_actions": ["purchase", "sign_up"],
  "top_keywords": ["color analysis", "seasonal color analysis", "personal color palette"]
}
```
