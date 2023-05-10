import requests
import json


headers = {
    "accept": "application/json",
    "Authorization": "671f012a-921d-43d6-9b84-2a2421525c1f"
}

# addresses = [{"name": "MAYC", "address": "0x60e4d786628fea6478f785a6d7e704777c86a7c6"},
# {"name": "BAYC", "address": "0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d"},
# {"name": "Azuki", "address": "0xed5af388653567af2f388e6224dc7c4b3241c544"},
# {"name": "Moonbirds", "address": "0x23581767a106ae21c074b2276d25e5c3e136a68b"}]

topURL = url = "https://api.nftport.xyz/v0/contracts/top?page_size=1&page_number=1&period=24h&order_by=volume&chain=ethereum"


response = requests.get(topURL, headers=headers)
data = response.json()
addresses = data["contracts"]


for item in addresses:
    url = f'https://api.nftport.xyz/v0/nfts/{item["contract_address"]}?chain=ethereum&page_number=1&page_size=50&include=metadata&include=file_information&include=rarity&include=last_sale_price&include=all&refresh_metadata=false'
    response = requests.get(url, headers=headers)
    data = response.json()
    with open(f'data_export/{item["name"]}.json', 'w') as file:
        json.dump(data, file)
