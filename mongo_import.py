import os
from dotenv import load_dotenv
load_dotenv()

os.chdir('./data_export')

for filename in os.listdir("."):
    print(filename)
    if filename.endswith(".json"):
        os.system(f'mongoimport --uri {os.getenv("MONGO_URI")} --collection nft_test --type json --file {filename}')
