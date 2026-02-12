# Google Ads API setup (inputs needed)

This skill requires Google Ads API access. Ask the user for these values (do NOT store secrets in repo):

## Required
- **Developer token** (from Google Ads → Tools & Settings → API Center)
- **OAuth client_id**
- **OAuth client_secret**
- **OAuth refresh_token**
- **Login customer ID** (Google Ads account id; optionally MCC id)

## How the skill should read credentials
Preferred: environment variables (local only) or a local JSON file path provided at runtime.

### Example env vars
- GOOGLE_ADS_DEVELOPER_TOKEN
- GOOGLE_ADS_CLIENT_ID
- GOOGLE_ADS_CLIENT_SECRET
- GOOGLE_ADS_REFRESH_TOKEN
- GOOGLE_ADS_LOGIN_CUSTOMER_ID
- GOOGLE_ADS_CUSTOMER_ID (optional if same as login)

### Example JSON (local only)
```json
{
  "developer_token": "...",
  "client_id": "...",
  "client_secret": "...",
  "refresh_token": "...",
  "login_customer_id": "123-456-7890",
  "customer_id": "123-456-7890"
}
```

## First actions after creds are available
- Validate access by listing accessible customers
- Pull account/campaign summary (last 30 days)
