import pymongo
import pprint
from bson.json_util import dumps
from pymongo import MongoClient

# url: mongodb+srv://<username>:<password>@<cloud location???>/<cluster???>
url = "mongodb+srv://m220student:m220password@mflix.8tenw.gcp.mongodb.net/test"
client = MongoClient(url)
# print client state
print(client.state)
# data base
sample_mflix_db = client.sample_mflix
# collection
movies_collection = sample_mflix_db.movies
# search one (test only, not very practical), find_one() return a document.
result = movies_collection.find_one()
# show result, using Bson.json_util.dumps to prettify it.
print(dumps(result, indent=2))
# search year 1991, find() return a curer of series of document.
result = movies_collection.find({"year": 1991}, )
# show result, using Bson.json_util.dumps to prettify it.
# careful, pretty too long print.
# print(dumps(result, indent=2))

# search year 1982, project it(only take id, title, year) on the server part,
# find() return a curer of series of document.
result = movies_collection.find({"year": 1982}, {"title": 1, "year": 1})
# show result, using Bson.json_util.dumps to prettify it.
print(dumps(result, indent=2))
