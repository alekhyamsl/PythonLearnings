import pymongo
"""
connecting to mongodb
go to google search for mongodb atlas -> cloud based one
there is mongodb compass which you can do locally in system
go to website -> login using google account
create cluster by selecting free version
then connect to application drivers
select driver(python) and version
copy the full driver code  
replace <password> with your password

installation of pymongo
execute pip install pymongo in terminal by selecting command prompt

"""

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
connecting pycharm code to github
go to google 
search for git download
download 64 bit standalone installer
install the application
close the pycharm and open again
Now login to github account
create repository
copy url https://github.com/alekhyamsl/MyFirstRepo.git
go to pycharm
select project
click to git  -> commit
give any comment and select files to be pushed
this files are not yet available in github
click on git -> push
click on define remote url
and provide URL of repository in github where the code needs to be pushed
click on push button
provide github login after the screen pops up
authorize it


how clone a repository
for this github repository needs to be made public 
and the repository URL can be seen in github by clicking on code button
click on git -> clone 
give the repository URL
click on clone

pull code
click on git -> pull
specify branch

"""
"""
notes

nosql means not only structured query language
In case of SQL we have to create scheme/tables at very first place in order to insert data
Here in nosql IAm not supposed to create any schemas(tables) to dump data
Nosql tries to store document based data Ex in form of json based data set
no complexity while firing queries for nosql
we can scale nosql db horizontally
mongodb is one of nosql db
others are cassandra



"""
