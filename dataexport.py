##TODO
## have mongo_import run after this script executes

import requests
import json
import datetime
import os
from dotenv import load_dotenv
load_dotenv()

headers = {
    "accept": "application/json",
    "Authorization": os.getenv("NFTPORT_API")
}
numNFTS = 5

topURL = url = f'https://api.nftport.xyz/v0/contracts/top?page_size={numNFTS}&page_number=1&period=24h&order_by=volume&chain=ethereum'

##API CALL TO GET TOP X# of NFT ADDRESSESS
response = requests.get(topURL, headers=headers)
data = response.json()
addresses = data["contracts"]


for item in addresses:
    try:
        url = f'https://api.nftport.xyz/v0/nfts/{item["contract_address"]}?chain=ethereum&page_number=1&page_size=50&include=metadata&include=file_information&include=rarity&include=last_sale_price&include=all&refresh_metadata=false'
        response = requests.get(url, headers=headers)
        data = response.json()
        data["date_pulled"] = datetime.datetime.now().strftime("%Y-%m-%d")
        with open(f'data_export/{datetime.datetime.now().strftime("%Y-%m-%d")}-{item["name"]}.json', 'w') as file:
            json.dump(data, file)
            print(f'File {item["name"]}.json was successfully created.')
    except Exception as error:
        print(f'Error creating file {item["name"]}.json: {str(error)}')
