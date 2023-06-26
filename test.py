import requests
import json
import datetime
import os
from dotenv import load_dotenv
load_dotenv()

NFTPORT_HEADERS = {
        "accept": "application/json",
        "Authorization": os.getenv("NFTPORT_API")
    }
BLOCKSPAN_HEADERS = {
        "accept": "application/json",
        "X-API-KEY": os.getenv("BLOCKSPAN_API")
    }



top_url = f'https://api.nftport.xyz/v0/contracts/top?page_size={5}&page_number=1&period=24h&order_by=volume&chain=ethereum'

response = requests.get(top_url, headers=NFTPORT_HEADERS)
data = response.json()
addresses = []
for item in data["contracts"]:
    addresses.append(item["contract_address"])
print(addresses)




url = "https://api.blockspan.com/v1/nfts/contract/0x41f56b000fffe17943fb4c182c123767af71d005?chain=eth-main&include_current_owners=true&include_recent_price=true&page_size=50"
response = requests.get(url, headers=BLOCKSPAN_HEADERS)
data = response.json()
# print(data)
