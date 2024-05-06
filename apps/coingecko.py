import requests
import components.private as p

url = "https://api.coingecko.com/api/v3/coins/list"

headers = {"x-cg-demo-api-key": p.coingecko_apikey}

response = requests.get(url, headers=headers)

with open('../textfiles/coingecko.log', 'w', encoding='utf-8') as outfile:
    print(response.text, file=outfile)