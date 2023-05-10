import os
from dotenv import load_dotenv
load_dotenv()

os.chdir('./data_export')

for filename in os.listdir("."):
    if filename.endswith(".json"):
        print(f'****** {filename} ******')
        try:
            # os.system(f'mongoimport --uri {os.getenv("MONGO_URI")} --collection nft_test --type json --file {filename}')
            os.system(f'mongoimport --uri {os.getenv("MONGO_URI")} --collection test2 --type json "{filename}"')
            print(f'successfully imported {filename}')
        except Exception as error:
            print(f'Error importing {filename}: {str(error)}')