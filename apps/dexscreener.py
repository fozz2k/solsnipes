import requests

url =  "https://api.dexscreener.com/latest/dex/tokens/"

address = "0x2170Ed0880ac9A755fd29B2688956BD959F933F8"
headers = {}

response = requests.get(url + address, headers=headers)

with open('../textfiles/dexscreener.log', 'w', encoding='utf-8') as outfile:
    print(response.text, file=outfile)