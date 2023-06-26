import requests
import json
import datetime
import os
from dotenv import load_dotenv
from eth_address import top_nft

load_dotenv()

NFTPORT_HEADERS = {
        "accept": "application/json",
        "Authorization": os.getenv("NFTPORT_API")
    }
BLOCKSPAN_HEADERS = {
        "accept": "application/json",
        "X-API-KEY": os.getenv("BLOCKSPAN_API")
    }
ALCHEMY_HEADERS = {
        "accept": "application/json",
        "apiKey": os.getenv("ALCHEMY_API")
    }



# url = "https://api.blockspan.com/v1/nfts/contract/0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D?chain=eth-main&include_current_owners=true&include_recent_price=true&page_size=50"
# response = requests.get(url, headers=BLOCKSPAN_HEADERS)
# data = response.json()
# print(data)

# for item in top_nft:
#     url = f'https://api.blockspan.com/v1/nfts/contract/{item["address"]}?chain=eth-main&include_current_owners=true&include_recent_price=true&page_size=25'
#     response = requests.get(url, headers=BLOCKSPAN_HEADERS)
#     data = response.json()
#     print(url)
#     print(data)



url = "https://docs-demo.quiknode.pro/"
5
6payload = json.dumps({
7  "id": 67,
8  "jsonrpc": "2.0",
9  "method": "qn_fetchNFTsByCollection",
10  "params": [{
11    "collection": "0x60E4d786628Fea6478F785A6d7e704777c86a7c6",
12    "omitFields": [
13      "imageUrl",
14      "traits"
15    ],
16    "page": 1,
17    "perPage": 10
18  }]
19})
20headers = {
21  'Content-Type': 'application/json'
22}
23
24response = requests.request("POST", url, headers=headers, data=payload)
25
26print(response.text)