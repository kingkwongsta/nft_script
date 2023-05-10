import os
from dotenv import load_dotenv
load_dotenv()

db = "test"
collection = "test2"

os.chdir('./data_export')

for filename in os.listdir("."):
    if filename.endswith(".json"):
        print(f'****** {filename} ******')
        try:
            os.system(f'mongoimport --uri {os.getenv("MONGO_URI")} --db {db} --collection {collection} --type json "{filename}"')
            print(f'successfully imported {filename}')
        except Exception as error:
            print(f'Error importing {filename}: {str(error)}')