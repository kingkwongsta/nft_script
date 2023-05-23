import os
from dotenv import load_dotenv
load_dotenv()

def import_to_mongodb(db, collection):
    ## move to folder to run terminal commands
    os.chdir('./data_export')

    ## for every file in the directory, check if a json file, then run monogoimport command
    for filename in os.listdir("."):
        if filename.endswith(".json"):
            print(f'****** {filename} ******')
            try:
                os.system(f'mongoimport --uri {os.getenv("MONGO_URI")} --db {db} --collection {collection} --type json "{filename}"')
                print(f'successfully imported {filename}')
            except Exception as error:
                print(f'Error importing {filename}: {str(error)}')

