from pymongo import MongoClient
from config import Config


class DbPlay:

	def __init__(self):
		self.client = MongoClient(Config.DATABASE_CONFIG['host'], Config.DATABASE_CONFIG['port'])
		db = self.client.test
		self.collection = db.data

	def data_processing(self):
		# da = [
		# 		{"username": "robert",
		# 		"math": 98,
		# 		"science": 98,
		# 		"english": 77
		# 		},
		# 		{"username": "peter",
		# 		"math": 98,
		# 		"science": 78,
		# 		"english": 78
		# 		},
		# 		{"username": "max",
		# 		"math": 98,
		# 		"science": 68,
		# 		"english": 73
		# 		},
		# 		{"username": "alexa",
		# 		"math": 67,
		# 		"science": 68,
		# 		"english": 87
		# 		},
		# 		{"username": "martin",
		# 		"math": 83,
		# 		"science": 73,
		# 		"english": 71
		# 		}
		# 	]
		# self.collection.insert_many(da)

		for i in self.collection.find():
			total = i['science']+i['english']+i['math']
			self.collection.update({"_id": i['_id']}, { "$set":{ "total":total}})
			# print(i)


		# print(self.collection.find())
		# db.collection.aggregate({ $group : { _id: null, max: { $max : "$total" }}})
		highest=self.collection.find_one(sort=[("total", -1)])
		del highest['_id']
		del highest['total']
		
		self.client.close()

		return highest
		

if __name__ == '__main__':
	OBJ = DbPlay()
	print(OBJ.data_processing())