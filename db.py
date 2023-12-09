import pymongo

class Database:
    def __init__(self, mongo_url):
        self.mongo_client = pymongo.MongoClient(mongo_url)
        self.db = self.mongo_client.get_database("watermark_bot_db")  # Replace with your preferred database name
        self.users_collection = self.db.get_collection("users")

    def get_user(self, chat_id):
        return self.users_collection.find_one({"chat_id": chat_id})

    def update_user(self, chat_id, subscribed=False):
        user_data = {"chat_id": chat_id, "subscribed": subscribed}
        self.users_collection.update_one({"chat_id": chat_id}, {"$set": user_data}, upsert=True)
