from pymongo import MongoClient
import pandas as pd
import json
import os
from termcolor import colored

def import_content(filepath):
    client = MongoClient("mongodb://localhost:27017/")
    gm_review = client["google_map_review"]
    collection_name = 'wangsteak' 
    collection = gm_review[collection_name]

    data = pd.read_csv(filepath)
    data_json = json.loads(data.to_json(orient='records'))
    collection.drop()
    collection.insert_many(data_json)
    print(colored('Finish', 'cyan'))


if __name__ == "__main__":
    filepath = '../data/newest_gm_reviews.csv' 
    import_content(filepath)