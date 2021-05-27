from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient('mongodb+srv://test:test@cluster0.llf1j.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client.business
# Issue the serverStatus command and print the results
# serverStatusResult = db.command("serverStatus")
# pprint(serverStatusResult)
print('f')
print(db)
print(db.reviews)
fivestar = db.reviews.find_one({'rating': 5})
print(fivestar)
