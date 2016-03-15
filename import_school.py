from operator import itemgetter
import re
import pickle
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
collection = client.data.school
new_db = client.data.test_schools
origin = collection.find({}, {'_id': 0, 'name': 1, 'type': 1, 'province': 1, 'city': 1}, no_cursor_timeout=True)
origin_list = []

for s in origin:
    s['len'] = len(s['name'])
    origin_list.append(s)

origin_list = sorted(origin_list, key=itemgetter('len'), reverse=True)

for s in origin_list:
    if s['len'] == 2:
        continue
    if s['province'] in ["香港特别行政区", "澳门特别行政区", "台湾省"]:
        continue
    if "公司" in s["name"] or "基地" in s['name'] or "批发部" in s["name"]:
        continue
    else:
        del s['len']
        new_db.insert(s)
