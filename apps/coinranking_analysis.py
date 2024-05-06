# The goal of this file is to analyze the data from coinranking
import components.tokenClass as tc
import ast
import pprint as pp

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
    tokens.append(tc.CoinrankingToken(entry['name'], entry['symbol'], entry['price'], entry['marketCap'], entry['change'], entry['24hVolume'], entry['tier'], entry['uuid']))
    if (int(entry['tier']) == 1):
        vol24h += int(entry['24hVolume'])
        mc += int(entry['marketCap'])
# Datapoint from the top 100 mc coins in the solana ecosystem
print(vol24h/mc)
"""

For Tier 1 coins, the ratio of 24h volume to market cap is 0.41747738315106764
For Tier 2 coins, the ratio of 24h volume to market cap is 0.02421421728260411
For Tier 3 coins, the ratio of 24h volume to market cap is 3.316752453320127e-10

"""

# for token in tokens:
#     uuid = token.uuid
#     mcs = []
#     mcs = hlm.highlowmc(uuid)
#     with open('../textfiles/saved/highlowmc.log', 'w', encoding='utf-8') as outfile:
#         out = f"{token.name} ({token.symbol}) - High: {mcs[0]}, Low: {mcs[1]}"
#         pp.print(out, file=outfile)