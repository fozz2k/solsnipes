"""

This file is used to get a list of coins between a certain market cap.
The list is then saved to a file called coinlist.log in the textfiles folder.
This file uses API calls so only run it when you need to update the list of coins.
Rename the .log file and move it to the saved folder and then use the filter.py file to filter the list of coins.
Enjoy sniping SOL coins!

"""

import pprint as pp
import components.request as request

# Set the min market cap and offset
# The offset is our guess of where we should start searching from
max_cap = 300000
min_cap = 30000
offset = 1920
coins = request.get_coins(max_cap, min_cap, offset)

# Format the data to be printed nicely to coinlist.log in the textfiles folder
coins_data = [
    {'name': x.name, 'symbol': x.symbol, 'market_cap': x.mc, 'liquidity': x.liquidity, 
     '24h_change_percent': x.v24hChangePercent, '24h_usd_volume': x.v24hUSD}
    for x in coins
]

with open('../textfiles/coinlist.log', 'w', encoding='utf-8') as outfile:
    pp.pprint(coins_data, stream=outfile)