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



url3 = "https://eth-mainnet.g.alchemy.com/nft/v2/docs-demo/getNFTsForCollection?contractAddress=0xe785E82358879F061BC3dcAC6f0444462D4b5330&withMetadata=true"

response3 = requests.get(url3, headers=ALCHEMY_HEADERS)
print(response3.text)
