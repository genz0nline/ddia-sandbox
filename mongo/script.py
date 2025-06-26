from pymongo import MongoClient
from pymongo.cursor import Code
from pprint import pprint

client = MongoClient(
    host='localhost',
    port=27017,
)

db = client.get_database('test')

observations = db.observations

print("==== All animals ====")
for animal in observations.find():
    pprint(animal)

pipeline = [
    {"$match": {"family": "Sharks"}},
    {"$project": {"_id": True, "month": {"$substr": ["$observationTimestamp", 0, 7]}, "numAnimals": True}},
    {"$group": {"_id": "$month", "value": {"$sum": "$numAnimals"}}},
]

print("\n\n==== Sharks ====")
for shark in observations.aggregate(pipeline):
    pprint(shark)
