from dataexport import get_top_addresses, download_top_nfts
from mongo_import import import_to_mongodb

download_top_nfts(10)
import_to_mongodb("web3", "nft_top_eth")