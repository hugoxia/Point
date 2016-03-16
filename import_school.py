from operator import itemgetter
import re
import pickle
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
origin_client = MongoClient('123.56.115.168', 27017)
origin_school = client.data.origin_schools
gaoxiao = client.data.gaoxiao
all_school = origin_client.school.all_schools
localhost = client.data.all_schools
high_school = client.data.high_school
new_db = client.data.test_two_schools
origin = localhost.find({}, {'_id': 0, 'name': 1, 'type': 1, 'province': 1, 'city': 1}, no_cursor_timeout=True)
origin_list = []
# step 2
# for element in origin:
#     origin_list.append(element)
#
#
# for element in origin_list:
#     element['name'] = element['name'].split('(')[0]
#     element['name'] = element['name'].split('（')[0]
#     if '-' in element['name']:
#         element['name'] = element['name'].split('-')[0] + element['name'].split('-')[1]
#     if '小学' in element['name']:
#         element['name'] = re.split('小学', element['name'])[0] + '小学'
#     if '中学' in element['name']:
#         element['name'] = re.split('中学', element['name'])[0] + '中学'
#     if len(element["name"]) <= 3:
#         continue
#
#     result = localhost.find_one({'name': element['name'], 'province': element['province'], 'city': element['city']})
#     if result is None:
#         localhost.insert(element)


# step 4 -> sort name
for s in origin:
    s['len'] = len(s['name'])
    origin_list.append(s)

origin_list = sorted(origin_list, key=itemgetter('len'), reverse=True)

for s in origin_list:
    if s['len'] == 2:
        continue
    else:
        del s['len']
        new_db.insert(s)

# step 1
# for element in origin:
#     if element['province'] in ["香港特别行政区", "澳门特别行政区", "台湾省"]:
#         continue
#     if "公司" in element["name"] or "基地" in element['name'] or "批发部" in element["name"]:
#         continue
#     origin_list.append(element)
#
#
# for element in origin_list:
#     if element['type'] in ['中学', '小学']:
#         high_school.insert(element)


