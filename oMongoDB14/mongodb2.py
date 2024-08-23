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

data = {
    "name" : "chaitanya",
    "email": "sri@gmail.com",
    "subject" : ["pega","data science","data analytics"]
}

# client is the connectivity that we created
# we can create database with the help client
database = client['myinfo'] # myinfo is the database
# inside database we create tabels, views
# here in mongodb we create collections(which is table in sql)
collection = database['alekhya']
# inside collection we can store document(data)
collection.insert_one(data)

data1 = {
    "name" : "alekhya",
    "email": "sri1@gmail.com",
    "subject" : ["testing","data science","data analytics"]
}

list_of_records = [
    {
        "companyname" : "inueron",
        "product" : "affordable AI",
        "courses_offered" : "ML with deployment"
    },

    {
       "companyname": "inueron",
       "product": "affordable AI",
        "courses_offered": "deep learning"
    },

    {
        "companyname": "inueron",
        "product": "masters program",
        "courses_offered": "data science masters program"
}
]
collection.insert_one(data1)
collection.insert_many(list_of_records)
# for every document an unique ID is created or we can give unique ID to every document
data2 = {
    "coffee": {
        "region": [
            {"id":1,"name":"John Doe"},
            {"id":2,"name":"Don Joeh"}
        ],
        "country": {"id":2,"company":"ACME"}
    },
    "brewing": {
        "region": [
            {"id":1,"name":"John Doe"},
            {"id":2,"name":"Don Joeh"}
        ],
        "country": {"id":2,"company":"ACME"}
    }


}
collection.insert_one(data2)

collection1 = database['sri']
collection1.insert_one(data2)

record = collection.find()
for i in record:
    print(i)
