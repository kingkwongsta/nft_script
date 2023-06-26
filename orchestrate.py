##create a summary of the number of files exported and imported

from dataexport import get_top_addresses, download_top_nfts as download_top_nfts_dataexport
from mongo_import import import_to_mongodb
from blockspan_export import download_top_nfts as download_top_nfts_blockspan


# download_top_nfts_blockspan(5)

download_top_nfts_dataexport(40)
import_to_mongodb("web3", "nft_top_eth")

