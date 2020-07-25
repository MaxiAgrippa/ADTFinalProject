import pymongo
import pprint
from bson.json_util import dumps
from pymongo import MongoClient
# TEST:
from pymongo import *

# url: mongodb+srv://<username>:<password>@<cloud location???>/<cluster???>
url = "mongodb+srv://m220student:m220password@mflix.8tenw.gcp.mongodb.net/test"
client = MongoClient(url)
# print client state
# print(client.state)
# # data base
# sample_mflix_db = client.sample_mflix
# # collection
# movies_collection = sample_mflix_db.movies
# # search one (test only, not very practical), find_one() return a document.
# result = movies_collection.find_one()
# # show result, using Bson.json_util.dumps to prettify it.
# print(dumps(result, indent=2))
# # search year 1991, find() return a curer of series of document.
# result = movies_collection.find({"year": 1991}, )
# # show result, using Bson.json_util.dumps to prettify it.
# # careful, pretty too long print.
# # print(dumps(result, indent=2))
#
# # search year 1982, project it(only take id, title, year) on the server part,
# # find() return a curer of series of document.
# result = movies_collection.find({"year": 1982}, {"title": 1, "year": 1})
# # show result, using Bson.json_util.dumps to prettify it.
# print(dumps(result, indent=2))

# remove duplicate data test
sample_data = {"array": [{"item": "item001"},
                         {"item": "item002"},
                         {"item": "item003"},
                         {"item": "item004"},
                         {"item": "item001"},
                         {"item": "item002"},
                         {"item": "item003"},
                         {"item": "item004"}], "noise": "123123123"}
# client.Test["test"].insert_one(sample_data)
# client.Test["test"].drop()
# pipeline = [
#     {'$project': {
#         'array.item': 1}},
#     {'$unwind': {
#         'path': '$array'}},
#     {'$group': {
#         '_id': '$array',
#         'dups': {
#             '$addToSet': '$_id'},
#         'count': {
#             '$sum': 1}}},
#     {'$match': {
#         '_id': {
#             '$ne': ''},
#         'count': {
#             '$gt': 1}}},
# ]
# result = client.Test["test"].aggregate(pipeline)
# for doc in result:
#     print(doc)
# print(dumps(result, indent=2))
# FAIL
# ERROR: Data Structure Error Find, Need to adjust our data structure(schema)

# index = IndexModel(["item", ASCENDING])
#
result = client.Test["test"].create_index([("array.item", 1)], unique="true")
print(dumps(result, indent=2))
