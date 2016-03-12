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
client = MongoClient('192.168.1.90', 27017)
collection = client.test.schools


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


@app.route('/')
def index():
    return render_template('test.html', x_y=None, first=None, second=None, address=None)


@app.route('/test', methods=['GET', 'POST', 'PUT'])
def test():
    if request.method == 'POST':
        x_y = request.form['x_y']
        lat1 = re.split(',', x_y)[0]
        lng1 = re.split(',', x_y)[1]
        url_address = 'http://restapi.amap.com/v3/geocode/regeo?key=2f9fd93a6d483072ae4379dd371a2425&location=' + \
                      lat1 + ',' + lng1 + '&poitype=141201|141202|141203|141206' + \
                      '&extensions=all&batch=true&roadlevel=1'
        url = 'http://restapi.amap.com/v3/place/around?key=2f9fd93a6d483072ae4379dd371a2425&location=' \
              + lat1 + ',' + lng1 + \
              '&radius=300&keywords=&types=141201|141202|141203|141206&offset=50&page=1&extensions=base'
        address = requests.get(url_address).json()
        addr = {}
        addr["name"] = address["regeocodes"][0]["formatted_address"]
        try:
            addr["keyword"] = address["regeocodes"][0]["aois"][0]["name"]
        except IndexError:
            addr["keyword"] = None
        print(url)
        r = requests.get(url)
        t = r.json()
        get_school = []
        if addr["keyword"] is not None:
            get_school.append(addr["keyword"])
        for s in t["pois"]:
            get_school.append(s['name'].replace('-', ''))
        result = collection.find({}, {"city": 1, "name": 1, "_id": 1, "location": 1})
        data = []
        second = []
        for r in result:
            data.append(r['name'])
        for element in get_school:
            match_list = []
            for i in data:
                if i in element:
                    match_list.append(i)
                else:
                    continue
            if len(match_list) > 0:
                second.append(match_list[0])
            else:
                pass

        f = lambda x, y: x if y in x else x + [y]

        second = reduce(f, [[], ] + second)
        print(get_school)
        print(second)
        if len(get_school) == 0:
            get_school = None

        if len(second) == 0:
            second = None

    return render_template('test.html', x_y=x_y, first=get_school, second=second, address=addr)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9999)

