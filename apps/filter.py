import json
import components.tokenClass as tc
import ast

# Path to your .log file
file_path = '../textfiles/saved/30k-300k.log'

with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
    data = ast.literal_eval(content)  # Convert string representation back to list

# Create a list to hold instances of token
tokens = []

for entry in data:
    tokens.append(tc.sToken(entry['name'], entry['symbol'], entry['liquidity'], entry['market_cap'], entry['24h_change_percent'], entry['24h_usd_volume']))

# Print the tokens
for token in tokens:
    print(token.name)