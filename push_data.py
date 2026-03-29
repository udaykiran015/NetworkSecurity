import os
import json 
import sys
import pymongo
import pandas as pd
import numpy as np
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from dotenv import load_dotenv
load_dotenv()

mongo_url=os.getenv("MONGO_DB_URL")
#print(mongo_url)

import certifi
ca=certifi.where()

class NetworkSecurityDataPush():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    def csv_to_json(self,filepath):
        try:
            data=pd.read_csv(filepath)
            data.reset_index(drop=True, inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    def json_to_mongodb(self, records, database_name, collection_name):
        try:
            # 1. Connect (Better to do this in __init__, but if doing it here:)
            client = pymongo.MongoClient(mongo_url, tlsCAFile=ca)
            
            # 2. Access DB and Collection using local variables
            db = client[database_name]
            coll = db[collection_name]

            # 3. Perform the actual insertion
            result = coll.insert_many(records)
            
            # 4. Return the ACTUAL number of inserted documents
            count = len(result.inserted_ids)
            
            return count

        except Exception as e:
            raise NetworkSecurityException(e, sys)
if __name__=="__main__":
    FILE_PATH="Network_Data\phisingData.csv"
    DATABASE_NAME="NetworkSecurity"
    COLLECTION_NAME="PhishingData"
    obj=NetworkSecurityDataPush()
    records=obj.csv_to_json(FILE_PATH)
    print(records[0])
    count=obj.json_to_mongodb(records, DATABASE_NAME, COLLECTION_NAME)
    print(f"Inserted {count} records into MongoDB collection '{COLLECTION_NAME}' in database '{DATABASE_NAME}'.")
    
