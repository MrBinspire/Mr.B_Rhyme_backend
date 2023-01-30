import pymongo


client = pymongo.MongoClient("localhost", 27017)
db = client["NanditaDb"]
col1 = db["home_rhymes"]


