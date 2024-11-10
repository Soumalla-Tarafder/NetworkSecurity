import os,sys,json,certifi
import pandas as pd
import numpy as np
import pymongo
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException
from dotenv import load_dotenv
load_dotenv()
MONGO_DB_URL = os.getenv('MONGO_DB_URL')
MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')

#print(MONGO_DB_URL,MONGODB_PASSWORD)

ca = certifi.where()


class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def csv_to_json_converter(self,filePath):
        try:

            data = pd.read_csv(filePath)
            #print(data)
            data.reset_index(drop=True,inplace=True)
            #print(data)
            records = list(json.loads(data.T.to_json()).values())
            return records
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def insert_data_to_mongodb(self,records,database,collection):
        try:
            
            self.database = database
            self.collection = collection
            self.records = records

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            return (len(self.records))

        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
if __name__ == "__main__":
    FILE_PATH = "Network_Data/phisingData.csv"
    DATABASE = "NetworkData"
    COLLECTION = "PHISINGDATA"
    dataextractor = NetworkDataExtract()
    records = dataextractor.csv_to_json_converter(FILE_PATH)
    no_of_records = dataextractor.insert_data_to_mongodb(records=records,database=DATABASE,collection=COLLECTION)

    print(no_of_records)