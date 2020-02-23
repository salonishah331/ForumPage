import pymongo
from pymongo import MongoClient
from .models import Post





client = MongoClient('mongo-dev-1.stackfolio.com', port=27017)
client.stackfolio_v1.authenticate('stackfolio-dev', 'HRSLjgyMrrJ4tHXq7d4GkQse', mechanism='SCRAM-SHA-1')
db = client['stackfolio_v1']



def getpost(roomID):
    x = db.postcollection.find({"RoomID" : roomID})
    return x

def createpost(text, roomID):
    y = db.postcollection.insert_one({"post" : text, "RoomID" : roomID})


def getroomids():
    roomIDs = db.roomcollection.find({}).distinct("_id")
    roomIDs = [ str(room) for room in roomIDs]
    if len(roomIDs) == 0:
        return createroom()
    return roomIDs


def createroom():
    x = db.roomcollection.insert_one({})
    return getroomids()





# collection = db["posts"]
# mydict = {"post" : "post"}
# x = collection.insert_one(mydict)

# for y in collection.find():
#   print(y)


# mydict = { "name": "John", "address": "Highway 37" }
# x = mycol.insert_one(mydict)
'''
.inserted_id -> holds ID of inserted document

myquery = { "address": { "$regex": "^S" } }
newvalues = { "$set": { "name": "Minnie" } }

x = mycol.update_many(myquery, newvalues)





'''



