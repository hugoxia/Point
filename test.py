import requests
import json
import re
import math
import pymongo
from functools import reduce
from operator import itemgetter
from flask import Flask, session, redirect
from flask import render_template
from flask import request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('localhost', 27017)
collection = client.school.test_schools


def rad(d):
    return d * math.pi / 180.0


def distance(lat1, lng1, lat2, lng2):
    radlat1 = rad(lat1)
    radlat2 = rad(lat2)
    a = radlat1 - radlat2
    b = rad(lng1) - rad(lng2)
    s = 2 * math.asin(
        math.sqrt(math.pow(math.sin(a / 2), 2) + math.cos(radlat1) * math.cos(radlat2) * math.pow(math.sin(b / 2), 2)))
    earth_radius = 6378.137
    s = s * earth_radius
    return abs(s)


black_list = ('网络教育', '继续教育', '远程教育', '仙桃学院', '纺织服装学院', '教学部', '分部')

def guolv(t):
    for i in black_list:
        return False if i in t else True


@app.route('/')
def index():
    return render_template('test.html', x_y=None, first=None, second=None, address=None)


@app.route('/test', methods=['GET', 'POST', 'PUT'])
def test():
    if request.method == 'POST':
        x_y = request.form['x_y']
        url_address = 'http://restapi.amap.com/v3/geocode/regeo?key=fe44aff795f5c287eb070781a3108d09&location=' + \
                      x_y + '&poitype=141201|141202|141203|141206' + \
                      '&extensions=all&batch=false&roadlevel=1'
        url = 'http://restapi.amap.com/v3/place/around?key=fe44aff795f5c287eb070781a3108d09&' \
              'location={0}&radius=300&keywords=&types=141201|141202|141203|141206&' \
              'offset=50&page=1&extensions=base'.format(x_y)
        address = requests.get(url_address).json()
        addr = {}
        get_school = ()
        if address['status'] == "1":
            for element in ["province", "city", "district"]:
                try:
                    addr[element] = address["regeocode"]["addressComponent"][element]
                except IndexError or KeyError:
                    addr[element] = []
            try:
                addr["keyword"] = address["regeocode"]["aois"][0]["name"]
            except IndexError or KeyError:
                addr["keyword"] = None
            if addr['city'] == []:
                addr['city'] = addr['province']
                addr['name'] = addr['province']+addr['city']
        else:
            raise Exception(address['info'])
        if addr["keyword"] is not None:
            get_school = (addr["keyword"],)
        school_name = requests.get(url).json()
        if school_name['status'] == "1":
            try:
                pois = school_name["pois"]
            except IndexError or KeyError:
                pois = None
        else:
            raise Exception(school_name['info'])
        if pois is None or pois == []:
            pass
        else:
            get_school += tuple(filter(guolv, (i['name'] for i in pois)))
            print(get_school)
            get_school = tuple(i.replace('-', '') for i in get_school)
        result = collection.find({
            "city": addr["city"]
        }, {"name": 1, "_id": 0})

        data = []
        schools = []
        for element in result:
            data.append(element['name'])
        for element in get_school:
            match_list = []
            for i in data:
                if element.startswith(i) or (i.endswith(element) and i[0:2] == "上海"):
                    match_list.append(i)
                else:
                    continue
            if len(match_list) > 0:
                schools.append(match_list[0])
            else:
                pass
        f = lambda x, y: x if y in x else x + [y]
        schools = reduce(f, [[], ] + schools)
        if schools == []:
            schools.append(addr['city'])

    return render_template('test.html', x_y=x_y, first=get_school, second=schools, address=addr)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9999)
