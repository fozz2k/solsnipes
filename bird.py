# This is a base template for using the BirdEye API to get token data

import requests
import private as p
import pandas as pd
import pprint as pp
import json

# Get url for token list sorted by 24h change percent
tokenlist = "https://public-api.birdeye.so/defi/tokenlist?sort_by=v24hChangePercent&sort_type=desc"
# Get list of headers from Solana chain
# Replace p.apikey with your apikey from birdeye
# https://bds.birdeye.so/
headers = {"x-chain": "solana", "X-API-KEY": p.apikey}
# Make request
listings = requests.get(tokenlist, headers=headers)

# write to pandas and check if status code is 200
if listings.status_code == 200:
    data = listings.json()['data']
    with open("listings.log", "w") as outfile:
        pp.pprint(data, outfile)
    
    df = pd.DataFrame(data)

    csv_file_path = 'bird.csv'
    df.to_csv(csv_file_path, index=False)
    print (f"Data saved to {csv_file_path}")
else:
    print("Error: ", listings.status_code)
    exit()

# Load data to json object
data = json.loads(listings.text)

# Initialize lists for each attribute
addresses = []
names = []
symbols = []
decimals = []
lastTradeUnixTimes = []
liquiditys = []
logoURIs = []
mcs = []
v24hChangePercents = []
v24hUSDs = []

# Extract data
for token in data['data']['tokens']:
    addresses.append(token['address'])
    names.append(token['name'])
    symbols.append(token['symbol'])
    decimals.append(token['decimals'])
    lastTradeUnixTimes.append(token['lastTradeUnixTime'])
    liquiditys.append(token['liquidity'])
    logoURIs.append(token['logoURI'])
    mcs.append(token['mc'])
    v24hChangePercents.append(token['v24hChangePercent'])
    v24hUSDs.append(token['v24hUSD'])


# Example of printing all tokens with market cap greater than 30,000
indexes = []

for i in range(len(addresses)):
    if type(mcs[i]) == float and mcs[i] > 30000:
        indexes.append(i)

for x in indexes:
    print(names[x], symbols[x], mcs[x])