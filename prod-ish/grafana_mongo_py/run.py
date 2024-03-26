from pymongo import MongoClient
import urllib.parse
import datetime

username = urllib.parse.quote_plus("root")
password = urllib.parse.quote_plus("example")

client = MongoClient("172.27.0.2", 27017, username=username, password=password)
# client = MongoClient("mongodb//%s:%s172.27.0.2" % (username, password))
print(str(client))

# In MongoDB, databases hold one or more collections of documents. 
db = client["test-database"]
print(db)

# A collection is a group of documents stored in MongoDB, and can be thought of as roughly the equivalent of a table in a relational database.
collection = db["test-collection"]
print(str(collection))

post_1 = {
    "name": "tag1",
    "date": datetime.datetime.now(tz=datetime.timezone.utc),
    "value": 78
}
post_2 = {
    "name": "tag1",
    "date": datetime.datetime.now(tz=datetime.timezone.utc),
    "value": 78
}
print(post_1)
print(post_2)
print("Insert")

posts = db.posts
post_id_1 = posts.insert_one(post_1)
print(post_id_1)
post_id_2 = posts.insert_one(post_2)
print(post_id_2)

