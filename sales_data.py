import requests
import json
import datetime
import os
import time
from dotenv import load_dotenv
load_dotenv()

HEADERS = {
        "accept": "application/json",
        "Authorization": os.getenv("NFTPORT_API")
    }

##function to get the top number of NFTs
def get_top_addresses(numNFTS):
    top_url = f'https://api.nftport.xyz/v0/contracts/top?page_size={numNFTS}&page_number=1&period=24h&order_by=volume&chain=ethereum'

    ##API CALL TO GET TOP X# of NFT ADDRESSESS
    response = requests.get(top_url, headers=HEADERS)
    data = response.json()
    addresses = data["contracts"]
    return addresses


def download_sales_data(numNFTS):
    
    addresses = get_top_addresses(numNFTS)
    json_files = []

    for item in addresses:
        try:
            url = f'https://api.nftport.xyz/v0/transactions/stats/{item["contract_address"]}?chain=ethereum'
            response = requests.get(url, headers=HEADERS)
            data = response.json()
            data["name"] = item["name"]
            data["date_pulled"] = datetime.datetime.now().strftime("%Y-%m-%d")
            filename = f'{datetime.datetime.now().strftime("%Y-%m-%d")}-{item["name"]}-sales.json'
            with open(f'data_export/{filename}', 'w') as file:
                json.dump(data, file)
                print(f'File {filename} was successfully created.')
                json_files.append(filename)
            time.sleep(0.5) #add delay
        except Exception as error:
            print(f'Error creating file {item["name"]}.json: {str(error)}')

    return json_files