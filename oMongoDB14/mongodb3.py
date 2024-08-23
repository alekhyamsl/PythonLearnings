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
database = client['myinfo']
collection = database['alekhya']
"""
record = collection.find()
for i in record:
    print(i)
"""
# getting only records having companyname
"""
record1 = collection.find({"companyname" : "inueron"})
for j in record1:
    print(j)
"""
record2 = collection.find({"courses_offered" : {"$gt" : "e"}})

for k in record2:
    print(k)