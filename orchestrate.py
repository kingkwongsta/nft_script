##create a summary of the number of files exported and imported

from dataexport import get_top_addresses, download_top_nfts as download_top_nfts_dataexport
from mongo_import import import_collection_to_mongodb
from blockspan_export import download_top_nfts as download_top_nfts_blockspan
from sales_data import download_sales_data

# download_top_nfts_blockspan(5)

download_top_nfts_dataexport(40)
import_collection_to_mongodb("web3", "eth_top_nfts")

download_sales_data(40)
import_collection_to_mongodb("web3", "eth_top_sales")