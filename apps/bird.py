# This is a base template for using the BirdEye API to get token data
# Probably ignore this file for now and refer to main

import requests
import components.private as p
import pandas as pd
import pprint as pp
import json
import components.tokenClass as tc

# Get url for token list sorted by 24h change percent
tokenlist = "https://public-api.birdeye.so/public/tokenlist?sort_by=v24hUSD&sort_type=desc"
# Get list of headers from Solana chain
# Replace p.apikey with your apikey from birdeye
# https://bds.birdeye.so/
headers = {"x-chain": "solana", "X-API-KEY": p.bird_apikey}
# Make request
listings = requests.get(tokenlist, headers=headers)

# write to pandas and check if status code is 200
if listings.status_code == 200:
    data = listings.json()['data']
    with open("../textfiles/listings.log", "w", encoding='utf-8') as outfile:
        pp.pprint(data, outfile)
    
    df = pd.DataFrame(data)

    csv_file_path = '../textfiles/bird.csv'
    df.to_csv(csv_file_path, index=False)
    print (f"Data saved to {csv_file_path}")
else:
    print("Error: ", listings.status_code)
    exit()

# Load data to json object
data = json.loads(listings.text)

tokens = []
total_mc = 0
total_liquidity = 0
total_vol = 0

# Extract data
for token in data['data']['tokens']:
    tokens.append(tc.FullToken(token['address'], token['decimals'], token['lastTradeUnixTime'], token['logoURI'], token['name'], token['symbol'], token['mc'], token['liquidity'], token['v24hChangePercent'], token['v24hUSD']))
    total_mc += token['mc']
    total_liquidity += token['liquidity']
    total_vol += token['v24hUSD']
print(total_liquidity/total_mc)
print(total_vol/total_mc)
