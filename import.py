import re
import pickle
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
collection = client.school.schools
new_db = client.school.new_schools
origin = collection.find(no_cursor_timeout=True)
pickle_file = open('schools.pkl', 'rb')
special = pickle.load(pickle_file)

for o in origin:
    if '(' in o['name'] or '（' in o['name']:
        name = re.split(r'[()|（）]', o['name'])[0]
        result = collection.find_one({'name': name})
        if result is not None:
            continue
        else:
            out = re.split(r'-', name)[0]
            if o['type'] == '高等院校':
                if '学院' in out:
                    out = re.split(r'学院', out)[0] + '学院'
                    result = collection.find_one({'name': out})
                    if result is not None:
                        continue
                if out not in special:
                    out = re.split(r'大学', out)[0] + '大学'
                else:
                    pass
            elif '中学' in out and o['type'] == '中学':
                out = re.split(r'中学', out)[0] + '中学'
                if '大学' in out:
                    out_list = re.split('大学|校区', out)
                    out = out_list[0] + '大学' + out_list[-1]
            elif '小学' in out and o['type'] == '小学':
                out = re.split(r'小学', out)[0] + '小学'
            else:
                pass
            o['name'] = out
            r = new_db.find_one({'name': out})
            if r is None:
                if o["type"] == "职业技术学校":
                    if out in special:
                        new_db.insert(o)
                    else:
                        pass
                elif o["type"] == "高等院校":
                    if out in special:
                        new_db.insert(o)
                    else:
                        pass
                else:
                    new_db.insert(o)
            else:
                pass
    else:
        out = re.split(r'-', o['name'])[0]
        if o['type'] == '高等院校':
            if '学院' in out:
                out = re.split(r'学院', out)[0] + '学院'
            if out not in special:
                out = re.split(r'大学', out)[0] + '大学'
            else:
                pass
        elif '中学' in out and o['type'] == '中学':
            out = re.split(r'中学', out)[0] + '中学'
            if '大学' in out:
                out_list = re.split('大学|校区', out)
                out = out_list[0] + '大学' + out_list[-1]
        elif '小学' in out and o['type'] == '小学':
            out = re.split(r'小学', out)[0] + '小学'
        else:
            pass
        o['name'] = out
        r = new_db.find_one({'name': out})
        if r is None:
            if o["type"] == "职业技术学校":
                if out in special:
                    new_db.insert(o)
                else:
                    pass
            elif o["type"] == "高等院校":
                if out in special:
                    new_db.insert(o)
                else:
                    pass
            else:
                new_db.insert(o)
        else:
            pass
