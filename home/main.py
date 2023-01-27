import pymongo

client = pymongo.MongoClient("localhost", 27017)
# print(client.list_database_names())
db = client['NanditaDb']
# print(db)
collections = db['home_rhymes']
# print(collections)

one = collections.find({"word":"height"})
# print(list(one))
# for x in one:
#     l=list(x.keys())
#     print(l)
#     l2=list(x.values())
#     print(type(x.values()))
#     print(l2)
try:

        print(list(one)[0]['word'])
        print("word is already there")

except:
        print("word never submitted")


 