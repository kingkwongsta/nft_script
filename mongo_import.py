import os
from dotenv import load_dotenv
load_dotenv()

os.chdir('./data_export')

for filename in os.listdir("."):
    if filename.endswith(".json"):
        try:
            os.system(f'mongoimport --uri {os.getenv("MONGO_URI")} --collection nft_test --type json --file {filename}')
            print(f'successfully imported {filename}')
        except Exception as error:
            print(f'Error importing {filename}: {str(error)}')