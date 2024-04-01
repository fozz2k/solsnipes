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

if listings.status_code == 200:
    data = listings.json()['data']
    with open("filtered.log", "w", encoding='utf-8') as outfile:
        pp.pprint(data, outfile)
    
    # Creating a DataFrame
    df = pd.DataFrame(data['tokens'])

    # Filtering the DataFrame to only include rows where 'mc' (market cap) is greater than 30,000
    filtered_df = df[df['mc'] > 30000]

    # Save the filtered DataFrame to CSV
    csv_file_path = 'filtered.csv'
    filtered_df.to_csv(csv_file_path, index=False)
    print(f"Filtered data saved to {csv_file_path}")
else:
    print("Error: ", listings.status_code)
