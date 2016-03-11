#coding=utf-8
import pickle
import requests
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
collection = client.school.origin_schools
pickle_file = open('new_area.pkl', 'rb')
area = pickle.load(pickle_file)

code = [{'number': 141201, 'mean': '高等院校'},
        {'number': 141202, 'mean': '中学'},
        {'number': 141203, 'mean': '小学'},
        {'number': 141206, 'mean': '职业技术学校'}]

# keys = ['3d0471d211746088206aaf1638e74278',
#         'cf7b53d57939c09aa449efdb9ea2848b',
#         'f1f097ee0123fa093dd021567bbc4814',
#         '55e8734699bd808deb7b241669dc09a3',
#         'c80d4b1457d23a6d01e3c820b6cdcf88',
#         'df01758d5ba565e8b4b6c02db0da403e',
#         '7da0cc4932a9a656e99c8a228f01cade',
#         '17f09916a4fc949da67c0ca86a813bbc',
#         '8ff524452971755d6357f0fbcf7cb962',
#         '42b3bafdb8b20ca51e412d0d8a91bff1',
#         '324eb6320c4b71960bb6b28e8f7979a0',
#         '2f9fd93a6d483072ae4379dd371a2425'
#         ]

key = 'fe44aff795f5c287eb070781a3108d09'
for a in area:
    province = a['province']
    for l in a['lower']:
        city = l['city']

        try:
            for d in l['lower']:
                for c in code:
                    headers = {'content-type': 'application/json', 'Host': '123.56.115.168'}
                    origin_url = 'http://restapi.amap.com/v3/place/text?city=%s&keywords=%s' % (city, d) + \
                                 '&types=%s&citylimit=true&output=json&offset=50&page=%s' % (c['number'], 1) + \
                                 '&key=' + key + '&extensions=all'
                    api_result = requests.get(origin_url, headers=headers).json()
                    if api_result["status"] == '0':
                        raise Exception(api_result['info'])
                    else:
                        pass
                    # if api_result["status"] == '0':
                    #
                    #     if keys.index(key) < 12:
                    #         key = keys[keys.index(key) + 1]
                    #     else:
                    #         print('oh~oh~,key用完了....')
                    count = int(api_result['count'])
                    if count == 0:
                        pass
                    elif count > 50:
                        if count % 50 == 0:
                            page = count // 50
                        else:
                            page = count // 50 + 1
                        for p in range(1, page + 1):
                            url = 'http://restapi.amap.com/v3/place/text?city=%s&keywords=%s' % (city, d) + \
                                  '&types=%s&citylimit=true&output=json&offset=50&page=%s' % (c['number'], p) + \
                                  '&key=' + key + '&extensions=all'
                            api_result = requests.get(url, headers=headers).json()
                            if api_result["status"] == '0':
                                raise Exception(api_result['info'])
                            else:
                                pass
                            # if api_result["status"] == '0':
                            #     if keys.index(key) < 12:
                            #         key = keys[keys.index(key) + 1]
                            #     else:
                            #         print('oh~oh~,key用完了....')
                            for a in api_result['pois']:
                                result = {
                                    "province": a["pname"],
                                    "city": a["cityname"],
                                    "district": a["adname"],
                                    "name": a["name"],
                                    "type": c['mean'],
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
                                "type": c['mean'],
                                "address": a["address"],
                                "location": a["location"],
                            }
                            collection.insert(result)
        except KeyError:
            for c in code:
                headers = {'content-type': 'application/json'}
                origin_url = 'http://restapi.amap.com/v3/place/text?city=%s' % city + \
                             '&types=%s&citylimit=true&output=json&offset=50&page=%s' % (c['number'], 1) + \
                             '&key=' + key + '&extensions=all'
                api_result = requests.get(origin_url, headers=headers).json()
                if api_result["status"] == '0':
                    raise Exception(api_result['info'])
                else:
                    pass
                # if api_result["status"] == '0':
                #     if keys.index(key) < 12:
                #         key = keys[keys.index(key) + 1]
                #     else:
                #         print('oh~oh~,key用完了....')
                count = int(api_result['count'])
                if count == 0:
                    pass
                elif count > 50:
                    if count % 50 == 0:
                        page = count // 50
                    else:
                        page = count // 50 + 1
                    for p in range(1, page + 1):
                        url = 'http://restapi.amap.com/v3/place/text?city=%s' % city + \
                              '&types=%s&citylimit=true&output=json&offset=50&page=%s' % (c['number'], p) + \
                              '&key=' + key + '&extensions=all'
                        api_result = requests.get(url, headers=headers).json()
                        if api_result["status"] == '0':
                            raise Exception(api_result['info'])
                        else:
                            pass
                        # if api_result["status"] == '0':
                        #     if keys.index(key) < 12:
                        #         key = keys[keys.index(key) + 1]
                        #     else:
                        #         print('oh~oh~,key用完了....')
                        for a in api_result['pois']:
                            result = {
                                "province": a["pname"],
                                "city": a["cityname"],
                                "district": a["adname"],
                                "name": a["name"],
                                "type": c['mean'],
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
                            "type": c['mean'],
                            "address": a["address"],
                            "location": a["location"],
                        }
                        collection.insert(result)
