import pymongo


client = pymongo.MongoClient("localhost", 27017)
db = client["NanditaDb"]
col1 = db["home_rhymes"]
colR = db["home_rejected"]
colA = db["home_accepted"]

Accepted_list = list(col1.find({"is_accepted": True}))
print(Accepted_list)

Rejected_list = list(col1.find({"is_accepted": False}))
print(Rejected_list)


# if (Accepted_list != []):
result1 = colA.insert_many(Accepted_list)
# else:
result = colR.insert_many(Rejected_list)





    
for j in colA.find():
    print(j)

for x in colR.find():
    print(x)

for i in col1.find():
    col1.delete_one(i)

