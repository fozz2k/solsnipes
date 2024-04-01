import requests
import private as p

url = "https://public-api.birdeye.so/public/amm_supported"

headers = {"X-API-KEY": p.apikey}

response = requests.get(url, headers=headers)

print(response.text)