from pymongo import MongoClient
client = MongoClient()
db = client['buyabledb']

def user_signup(user_info):
	
	db['users'].insert_one(user_info)

def search_user_by_username(username):
	filter_query = {'username' : username}
	results = db["users"].find(filter_query)

	if(results.count() > 0):
		return results.next()
	else:
		return None
