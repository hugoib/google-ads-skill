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

customer_service = client.get_service('CustomerService')
resource_names = customer_service.list_accessible_customers().resource_names
print('Accessible customers:')
for rn in resource_names:
    print(' -', rn)

print('OK')
