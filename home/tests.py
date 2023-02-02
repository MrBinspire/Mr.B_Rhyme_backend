import pymongo


client = pymongo.MongoClient("localhost", 27017)
db = client["NanditaDb"]
col1 = db["auth_user"]
col2 = db["auth_user_groups"]

user_info = col2.find({"id":5})
val = list(user_info)[0]['group_id']
print(val)
# user_dictionary = user_list[0]
# print(user_dictionary)
if (val == 2):
    print("Normal user")
else:
    print("Admin")


