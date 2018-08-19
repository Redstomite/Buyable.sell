from pymongo import MongoClient
client = MongoClient()
db = client['buyabledb']

def product_add(product_info):
	
	db['products'].insert_one(product_info)

