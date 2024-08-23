import pymongo

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
# if this uri is shared , we can hit the server from any system
uri = "mongodb+srv://alekhyamsl:tabVo7XKP5GOP2fA@cluster0.0g30o.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
print(client)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

data =  [
        {
            "item": "canvas",
            "qty": 100,
            "size": {"h": 28, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "journal",
            "qty": 25,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mat",
            "qty": 85,
            "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mousepad",
            "qty": 25,
            "size": {"h": 19, "w": 22.85, "uom": "cm"},
            "status": "P",
        },
        {
            "item": "notebook",
            "qty": 50,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "P",
        },
        {
            "item": "paper",
            "qty": 100,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "D",
        },
        {
            "item": "planner",
            "qty": 75,
            "size": {"h": 22.85, "w": 30, "uom": "cm"},
            "status": "D",
        },
        {
            "item": "postcard",
            "qty": 45,
            "size": {"h": 10, "w": 15.25, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketchbook",
            "qty": 80,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketch pad",
            "qty": 95,
            "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
            "status": "A",
        },
    ]
database = client['myinfo']
collection = database['inventory']
#collection.insert_many(data)
"""
records = collection.find()
for i in records:
    print(i)
"""
# find records with status as A
"""
d = collection.find({"status":"A"})
for i in d:
    print(i)
"""
# find records with status as A or P
"""
d1 = collection.find({"status":{"$in":['A','P']}})
for i in d1:
    print(i)
"""
# find records with status greater than A
"""
d2 = collection.find({"status":{"$gt" : 'A'}})
for i in d2:
    print(i)
"""
# find records with qty greater than equal to 75
"""
d3 = collection.find({"qty":{"$gte" : 75}})
for i in d3:
    print(i)
"""
# other keywords $lte(less than equal to ),$lt(less than)
# find records with item = sketch pad and qty = 95
"""
d4 = collection.find({"item" : "sketch pad","qty" : 95})
for i in d4:
    print(i)
"""
# find records with item = sketch pad or qty greater than 75
"""
d5 = collection.find({"$or" :  [{"item" : "sketch pad"},{"qty" : {"$gte" : 75}}]})
for i in d5:
    print(i)
"""
# updating records in momgodb using update_one, update_many
# update item value to sri if item = canvas
"""
collection.update_one({"item":"canvas"},{"$set" : {"item" : "sri"}})
d6 = collection.find({"item":"sri"})
for i in d6:
    print(i)
"""
"""
collection.delete_one({"item":"sri"})
d6 = collection.find({"item":"sri"})
for i in d6:
    print(i)
"""
"""
when searching inside the mongodb directly we can use as below in filter box
{"item" : "sketch pad"} filters records with item = sketch pad
{"qty" : {"$gte" : 75}} filters records with qty >= 75

we can store images as well in mongodb but in form of base 64

we can perform joins with aggregation operations

NO need to close DB collection in case of Mongo
"""