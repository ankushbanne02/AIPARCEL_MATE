from pymongo import MongoClient

class MongoDBAgent:
    def __init__(self, uri: str, db_name: str, default_collection: str):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.default_collection_name = default_collection

    def get_default_collection(self):
        return self.db[self.default_collection_name]


if __name__ == "__main__":
    MONGO_URI = "mongodb://localhost:27017"
    MONGO_DB = "ASD"
    DEFAULT_COLLECTION = "2025-05-13"

    mongo_agent = MongoDBAgent(MONGO_URI, MONGO_DB, DEFAULT_COLLECTION)
    collection = mongo_agent.get_default_collection()

    # Pipeline to return a single JSON object with counts per event type
    pipeline = [
    {'$unwind': '$events'},
    {'$group': {'_id': '$events.type', 'count': {'$sum': 1}}},
    {'$group': {'_id': 0, 'counts': {'$push': {'k': '$_id', 'v': '$count'}}}},
    {'$replaceRoot': {'newRoot': {'$arrayToObject': '$counts'}}},
    {'$facet': {
        'message_counts': [
            {'$unwind': '$events'},
            {'$group': {'_id': '$events.type', 'count': {'$sum': 1}}},
            {'$group': {'_id': 0, 'counts': {'$push': {'k': '$_id', 'v': '$count'}}}},
            {'$replaceRoot': {'newRoot': {'$arrayToObject': '$counts'}}}
        ],
        'total_parcels': [
            {'$match': {'entrance_state': '2'}},
            {'$count': 'total_docs'}
        ]
    }}
]


    try:
        result = list(collection.aggregate(pipeline))
        if result:
            print("✅ Output:", result[0])  # result is a list with one dict
        else:
            print("⚠️ No data found")
    except Exception as e:
        print("❌ Error:", e)
