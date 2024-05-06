# The goal of this file is to analyze the data from birdeye
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

