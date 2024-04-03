import requests
import json
import components.private as p
import components.tokenClass as tc

def get_coins(max_cap = 1000000, min_cap = 0, offset = 0):
    initial_offset = offset
    # Get url for token list sorted by 24h change percent
    tokenlist = "https://public-api.birdeye.so/defi/tokenlist?sort_by=mc&sort_type=desc&offset="
    # Get list of headers from Solana chain
    # Replace p.apikey with your apikey from birdeye
    # https://bds.birdeye.so/
    headers = {"x-chain": "solana", "X-API-KEY": p.bird_apikey}
    coins = []
    while (True):
        # Make request
        listings = requests.get(tokenlist + str(offset), headers=headers)
        # Load data to json object
        data = json.loads(listings.text)

        # Extract data
        for token in data['data']['tokens']:
            if type(token['mc']) == float and token['mc'] > min_cap and token['mc'] < max_cap:
                coins.append(tc.FullToken(token['address'], token['name'], token['symbol'], token['decimals'], token['lastTradeUnixTime'], token['liquidity'], token['logoURI'], token['mc'], token['v24hChangePercent'], token['v24hUSD']))
            else:
                if len(coins) > 0:
                    return coins
        # You can change the value of 3000, but this just prevents an infinite loop
        if (offset > initial_offset + 3000):
            return coins
        offset += 50