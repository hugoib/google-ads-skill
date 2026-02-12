#!/usr/bin/env python3
import os
import sys
from google.ads.googleads.client import GoogleAdsClient

REQUIRED = [
    'GOOGLE_ADS_DEVELOPER_TOKEN',
    'GOOGLE_ADS_CLIENT_ID',
    'GOOGLE_ADS_CLIENT_SECRET',
    'GOOGLE_ADS_REFRESH_TOKEN',
    'GOOGLE_ADS_LOGIN_CUSTOMER_ID',
    'GOOGLE_ADS_CUSTOMER_ID',
]

missing = [k for k in REQUIRED if not os.getenv(k)]
if missing:
    print('Missing env vars:', ', '.join(missing))
    sys.exit(1)

config = {
    'developer_token': os.getenv('GOOGLE_ADS_DEVELOPER_TOKEN'),
    'client_id': os.getenv('GOOGLE_ADS_CLIENT_ID'),
    'client_secret': os.getenv('GOOGLE_ADS_CLIENT_SECRET'),
    'refresh_token': os.getenv('GOOGLE_ADS_REFRESH_TOKEN'),
    'login_customer_id': os.getenv('GOOGLE_ADS_LOGIN_CUSTOMER_ID').replace('-', ''),
    'use_proto_plus': True,
}

client = GoogleAdsClient.load_from_dict(config)
customer_id = os.getenv('GOOGLE_ADS_CUSTOMER_ID').replace('-', '')

query = """
SELECT
  segments.date,
  metrics.impressions,
  metrics.clicks,
  metrics.ctr,
  metrics.cost_micros,
  metrics.conversions,
  metrics.conversions_value
FROM customer
WHERE segments.date DURING LAST_30_DAYS
"""

ga_service = client.get_service('GoogleAdsService')

response = ga_service.search_stream(customer_id=customer_id, query=query)

impr = clicks = conv = conv_value = cost_micros = 0
for batch in response:
    for row in batch.results:
        impr += row.metrics.impressions
        clicks += row.metrics.clicks
        conv += row.metrics.conversions
        conv_value += row.metrics.conversions_value
        cost_micros += row.metrics.cost_micros

cost = cost_micros / 1_000_000
ctr = (clicks / impr * 100) if impr else 0
cpc = (cost / clicks) if clicks else 0
cpa = (cost / conv) if conv else 0
roas = (conv_value / cost) if cost else 0

print('Last 30 days summary')
print('Impressions:', impr)
print('Clicks:', clicks)
print('CTR:', round(ctr, 2), '%')
print('Cost:', round(cost, 2))
print('CPC:', round(cpc, 2))
print('Conversions:', round(conv, 2))
print('CPA:', round(cpa, 2))
print('Conv value:', round(conv_value, 2))
print('ROAS:', round(roas, 2))
