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

d = {"name":"alekhya",
     "emailID":"alekhyamsl@gmail.com",
     "surname":"kuchipudi"}

db = client['momgotest']
coll = db['test']
coll.insert_one(d)

"""

go to google 
search for git download
download 64 bit standalone installer
install the application
close the pycharm and open again
Now login to github account
create repository
copy url https://github.com/alekhyamsl/MyFirstRepo.git
"""

