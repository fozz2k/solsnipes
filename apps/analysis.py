# The goal of this file is to analyze the data
import components.tokenClass as tc
import ast

"""

Stage 1: Analyzing marketcap data from birdeye

"""
# Path to your .log file in the saved folder
file_path = '../textfiles/saved/30k-300k.log'

with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
    data = ast.literal_eval(content)

# Create a list to hold instances of token
tokens = []

for entry in data:
    if entry['liquidity'] > entry['market_cap'] * 2:
        tokens.append(tc.Token(entry['name'], entry['symbol'], entry['liquidity'], entry['market_cap'], entry['24h_change_percent'], entry['24h_usd_volume']))

# Print the tokens
with open('../textfiles/potential_tokens.log', 'w', encoding='utf-8') as outfile:
    for token in tokens:
        out = f"{token.name} Marketcap: {token.mc} Liquidity: {token.liquidity})"
        print(out, file=outfile)

"""

Stage 2: Analyze the top 100 Solana coins from Coinranking

"""

# Path to your .log file in the saved folder
file_path = '../textfiles/saved/coinranking.log'

with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
    data = ast.literal_eval(content)

# Create a list to hold instances of token
tokens = []
vol24h = 0
mc = 0

for entry in data:
    tokens.append(tc.CoinrankingToken(entry['name'], entry['symbol'], entry['price'], entry['marketCap'], entry['change'], entry['24hVolume']))
    vol24h += int(entry['24hVolume'])
    mc += int(entry['marketCap'])
# Datapoint from the top 100 mc coins
print(vol24h/mc)