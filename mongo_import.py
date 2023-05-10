import os
from dotenv import load_dotenv
load_dotenv()

for filename in os.listdir("./data_export"):
    print(filename)
    if filename.endswith(".json"):
        os.chdir('./data_export')
        os.system(f'mongoimport --uri {os.getenv("MONGO_URI")} --collection nft_test --type json --file {filename}')
