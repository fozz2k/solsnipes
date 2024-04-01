import requests
import private as p
import json

# Get url for token list
tokenlist = "https://public-api.birdeye.so/public/tokenlist?sort_by=v24hUSD&sort_type=desc"
# Get list of headers from Solana chain
headers = {"x-chain": "solana", "X-API-KEY": p.apikey}
# Make request
listings = requests.get(tokenlist, headers=headers)
# Write to file in listings.json
with open("listings.json", "w") as outfile:
    json.dump(listings.text, outfile, indent=4)

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

# Write to info.txt
with open('info.txt', 'w') as file:
    for i in range(len(addresses)):
        file.write(' '.join(map(str, [names[i], symbols[i], decimals[i], lastTradeUnixTimes[i], liquiditys[i], logoURIs[i], mcs[i], v24hChangePercents[i], v24hUSDs[i]])) + '\n')