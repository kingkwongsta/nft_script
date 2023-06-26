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

##function to get the top number of NFTs
def get_top_addresses(numNFTS):
    top_url = f'https://api.nftport.xyz/v0/contracts/top?page_size={numNFTS}&page_number=1&period=24h&order_by=volume&chain=ethereum'

    ##API CALL TO GET TOP X# of NFT ADDRESSESS
    response = requests.get(top_url, headers=HEADERS)
    data = response.json()
    addresses = data["contracts"]
    return addresses


def download_top_nfts(numNFTS):
    
    addresses = get_top_addresses(numNFTS)
    json_files = []
    


    for item in addresses:
        try:
            url = f'https://api.blockspan.com/v1/nfts/contract/{item["contract_address"]}?chain=eth-main&include_current_owners=true&include_recent_price=true&page_size=50'
            response = requests.get(url, headers=HEADERS)
            data = response.json()
            data["date_pulled"] = datetime.datetime.now().strftime("%Y-%m-%d")
            filename = f'{datetime.datetime.now().strftime("%Y-%m-%d")}-{item["name"]}.json'
            with open(f'data_export/{filename}', 'w') as file:
                json.dump(data, file)
                print(f'File {filename} was successfully created.')
                json_files.append(filename)
        except Exception as error:
            print(f'Error creating file {item["name"]}.json: {str(error)}')

    return json_files

    download_top_nfts(5)