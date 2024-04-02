import pprint as pp
import components.req as req

# Set the min market cap and offset
# The offset is our guess of where we should start searching from
max_cap = 340000
min_cap = 300000
offset = 1900
coins = req.get_coins(max_cap, min_cap, offset)

# Format the data to be printed nicely to coinlist.log in the textfiles folder
coins_data = [
    {'name': x.name, 'symbol': x.symbol, 'market_cap': x.mc, 
     '24h_change_percent': x.v24hChangePercent, '24h_usd_volume': x.v24hUSD}
    for x in coins
]

with open('../textfiles/coinlist.log', 'w', encoding='utf-8') as outfile:
    pp.pprint(coins_data, stream=outfile)