import re
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
collection = client.school.gaode_shaanxi
new_db = client.school.five_gaode_shaanxi
origin = collection.find({}, {
    "province": 1, "city": 1, "district": 1, "name": 1,
    "type": 1, "address": 1, "location": 1, "_id": 1})
special = [
    '西北大学',
    '西安交通大学',
    '西北工业大学',
    '西安理工大学',
    '西安电子科技大学',
    '西安工业大学',
    '西安建筑科技大学',
    '西安科技大学',
    '西安石油大学',
    '陕西科技大学',
    '西安工程大学',
    '长安大学',
    '西北农林科技大学',
    '陕西中医药大学',
    '陕西师范大学',
    '延安大学',
    '西安外国语大学',
    '西北政法大学',
    '西安邮电大学',
    '陕西理工学院',
    '宝鸡文理学院',
    '咸阳师范学院',
    '渭南师范学院',
    '西安体育学院',
    '西安音乐学院',
    '西安美术学院',
    '西安文理学院',
    '榆林学院',
    '商洛学院',
    '安康学院',
    '西安培华学院',
    '西安财经学院',
    '西安航空学院',
    '西安医学院',
    '西安欧亚学院',
    '西安外事学院',
    '西安翻译学院',
    '西京学院',
    '西安思源学院',
    '陕西国际商贸学院',
    '陕西服装工程学院',
    '西安交通工程学院',
    '西安交通大学城市学院',
    '西北大学现代学院',
    '西安建筑科技大学华清学院',
    '西安财经学院行知学院',
    '陕西科技大学镐京学院',
    '西安工业大学北方信息工程学院',
    '延安大学西安创新学院',
    '西安电子科技大学长安学院',
    '西北工业大学明德学院',
    '长安大学兴华学院',
    '西安理工大学高科学院',
    '西安科技大学高新学院',
    '陕西学前师范学院',
    '陕西工业职业技术学院',
    '杨凌职业技术学院',
    '西安电力高等专科学校',
    '陕西能源职业技术学院',
    '陕西国防工业职业技术学院',
    '西安航空职业技术学院',
    '陕西财经职业技术学院',
    '陕西交通职业技术学院',
    '陕西职业技术学院',
    '西安高新科技职业学院',
    '西安城市建设职业学院',
    '陕西铁路工程职业技术学院',
    '宝鸡职业技术学院',
    '陕西航空职业技术学院',
    '陕西电子信息职业技术学院',
    '陕西邮电职业技术学院',
    '西安海棠职业学院',
    '西安汽车科技职业学院',
    '西安东方亚太职业技术学院',
    '陕西警官职业学院',
    '陕西经济管理职业技术学院',
    '西安铁路职业技术学院',
    '咸阳职业技术学院',
    '西安职业技术学院',
    '商洛职业技术学院',
    '汉中职业技术学院',
    '延安职业技术学院',
    '渭南职业技术学院',
    '安康职业技术学院',
    '铜川职业技术学院',
    '陕西青年职业学院',
    '陕西工商职业学院',
    '陕西电子科技职业学院',
    '陕西旅游烹饪职业学院',
    '西安医学高等专科学校',
    '榆林职业技术学院',
    '陕西艺术职业学院']

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
            out = out.split('陕西省')[-1]
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
        out = out.split('陕西省')[-1]
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
