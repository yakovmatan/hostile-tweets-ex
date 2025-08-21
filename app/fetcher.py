import os
import pymongo
from pymongo.errors import PyMongoError

class Fetcher:

    def __init__(self):
        self.collection_name = os.getenv("MONGODB_COLLECTION", "tweets")

        try:
            mongo_user = os.getenv("MONGODB_USER","IRGC")
            mongo_password = os.getenv("MONGODB_PASSWORD", "iraniraniran")
            mongo_db = os.getenv("MONGODB_DATABASE","IranMalDB")

            self.client = pymongo.MongoClient(f"mongodb+srv://{mongo_user}:{mongo_password}@{mongo_db}.gurutam.mongodb.net/")

            self.db = self.client[mongo_db]
        except PyMongoError as e:
            raise RuntimeError(f"MongoDB connection error: {e}")

    def get_data(self):
        try:
            collection = self.db[self.collection_name]
            return list(collection.find({}, {"_id": 0}))
        except PyMongoError as e:
            return {"error": "database_error", "Error reading data": e}

if __name__ == '__main__':
    d = DataLoader()
    c = d.get_data()
    print(c)

