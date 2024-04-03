# The purpose of this file is to analyze the top 100 solana coins. 
# Hopefully we can come up with useful data that we can train our machine learning model with.
import pprint as pp
import requests
import components.private as p

headers = {
  'x-access-token': p.coinranking_apikey
}

# Assuming you have the UUID for Solana, replace 'SOLANA_UUID' with it
params = {
    'limit': '100',  # Number of coins to fetch
    'blockchains[]': 'solana',  # UUID for the Solana blockchain
}

response = requests.get('https://api.coinranking.com/v2/coins', headers=headers, params=params)

if response.status_code == 200:
    data = response.json().get('data', {})
    coins = data.get('coins', [])
    
    # Printing out some details of the top 100 Solana coins
    with open('../textfiles/coinranking.log', 'w', encoding='utf-8') as outfile:
        pp.pprint(coins, stream=outfile)
        # for coin in coins:
        #     out = f"Name: {coin['name']}, Symbol: {coin['symbol']}, Market Cap: {coin['marketCap']}, Price: {coin['price']}, 24h Volume: {coin['24hVolume']}"
        #     print(out, file=outfile)
else:
    print(f"Failed to fetch data: {response.status_code}")