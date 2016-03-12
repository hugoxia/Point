from operator import itemgetter
import re
import pickle
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
collection = client.school.four_gaode_shaanxi
new_db = client.school.schools
origin = collection.find({}, {'_id': 0}, no_cursor_timeout=True)
origin_list = []

for s in origin:
    origin_list.append(s)

origin_list = sorted(origin_list, key=itemgetter('name'), reverse=True)

for s in origin_list:
    new_db.insert(s)
