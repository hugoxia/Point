# coding=utf-8
import re
import pickle
import requests
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
collection = client.school.quanguo_schools
pickle_file = open('xingzheng.pkl', 'rb')
districts = pickle.load(pickle_file)

# code = [{'number': 141202, 'mean': '中学'},
#         {'number': 141203, 'mean': '小学'}]
# {'number': 141201, 'mean': '高等院校'}
# {'number': 141206, 'mean': '职业技术学校'}

key = '8734a771f5a4a097a43e96d42f1cc393'

for element in districts:
    origin_url = 'http://restapi.amap.com/v3/place/text?city={0}&' \
                 'types=141202|141203&citylimit=true&output=json&offset=50&page=1&' \
                 'key={1}&extensions=all'.format(element, key)
    api_result = requests.get(origin_url).json()
    if api_result["status"] == '0':
        raise Exception(api_result['info'])
    else:
        pass
    count = int(api_result['count'])
    if count == 0:
        pass
    elif count > 50:
        if count % 50 == 0:
            page = count // 50
        else:
            page = count // 50 + 1
        for p in range(1, page + 1):
            url = 'http://restapi.amap.com/v3/place/text?city={0}&' \
                  'types=141202|141203&citylimit=true&output=json&offset=50&page={1}&' \
                  'key={2}&extensions=all'.format(element, p, key)
            api_result = requests.get(url).json()
            if api_result["status"] == '0':
                raise Exception(api_result['info'])
            else:
                pass
            for a in api_result['pois']:
                result = {
                    "province": a["pname"],
                    "city": a["cityname"],
                    "district": a["adname"],
                    "name": a["name"],
                    "type": a['type'].split(';')[-1],
                    "address": a["address"],
                    "location": a["location"],
                }
                collection.insert(result)
    else:
        for a in api_result['pois']:
            result = {
                "province": a["pname"],
                "city": a["cityname"],
                "district": a["adname"],
                "name": a["name"],
                "type": a['type'].split(';')[-1],
                "address": a["address"],
                "location": a["location"],
            }
            collection.insert(result)
