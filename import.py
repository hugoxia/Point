import re
import pickle
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
collection = client.school.origin_school
new_db = client.school.new_schools
origin = collection.find(no_cursor_timeout=True)
pickle_file = open('schools.pkl', 'rb')
special = pickle.load(pickle_file)

fail_list = []
for s in special:
    result = collection.find_one({'name': s})
    if result is not None:
        new_db.insert(result)
    else:
        print(s)
        fail_list.append(s)
print(len(fail_list))

# for o in origin:
#     if '(' in o['name'] or '（' in o['name']:
#         name = re.split(r'[()|（）]', o['name'])[0]
#         result = collection.find_one({'name': name})
#         if result is not None:
#             continue
#         else:
#             out = re.split(r'-', name)[0]
#             if o['type'] == '高等院校':
#                 if '学院' in out:
#                     out = re.split(r'学院', out)[0] + '学院'
#                     result = collection.find_one({'name': out})
#                     if result is not None:
#                         continue
#                 if out not in special:
#                     out = re.split(r'大学', out)[0] + '大学'
#                 else:
#                     pass
#             elif '中学' in out and o['type'] == '中学':
#                 out = re.split(r'中学', out)[0] + '中学'
#                 if '大学' in out:
#                     out_list = re.split('大学|校区', out)
#                     out = out_list[0] + '大学' + out_list[-1]
#             elif '小学' in out and o['type'] == '小学':
#                 out = re.split(r'小学', out)[0] + '小学'
#             else:
#                 pass
#             o['name'] = out
#             r = new_db.find_one({'name': out})
#             if r is None:
#                 if o["type"] == "职业技术学校":
#                     if out in special:
#                         new_db.insert(o)
#                     else:
#                         pass
#                 elif o["type"] == "高等院校":
#                     if out in special:
#                         new_db.insert(o)
#                     else:
#                         pass
#                 else:
#                     new_db.insert(o)
#             else:
#                 pass
#     else:
#         out = re.split(r'-', o['name'])[0]
#         if o['type'] == '高等院校':
#             if '学院' in out:
#                 out = re.split(r'学院', out)[0] + '学院'
#             if out not in special:
#                 out = re.split(r'大学', out)[0] + '大学'
#             else:
#                 pass
#         elif '中学' in out and o['type'] == '中学':
#             out = re.split(r'中学', out)[0] + '中学'
#             if '大学' in out:
#                 out_list = re.split('大学|校区', out)
#                 out = out_list[0] + '大学' + out_list[-1]
#         elif '小学' in out and o['type'] == '小学':
#             out = re.split(r'小学', out)[0] + '小学'
#         else:
#             pass
#         o['name'] = out
#         r = new_db.find_one({'name': out})
#         if r is None:
#             if o["type"] == "职业技术学校":
#                 if out in special:
#                     new_db.insert(o)
#                 else:
#                     pass
#             elif o["type"] == "高等院校":
#                 if out in special:
#                     new_db.insert(o)
#                 else:
#                     pass
#             else:
#                 new_db.insert(o)
#         else:
#             pass

test = [{'city': '', 'name': '外交学院'}, {'city': '', 'name': '国际关系学院'}, {'city': '', 'name': '中国音乐学院'},
        {'city': '', 'name': '中央美术学院'}, {'city': '', 'name': '中央戏剧学院'}, {'city': '', 'name': '中国戏曲学院'},
        {'city': '', 'name': '北京电影学院'}, {'city': '', 'name': '北京舞蹈学院'}, {'city': '', 'name': '首钢工学院'},
        {'city': '', 'name': '中国科学院大学'}, {'city': '', 'name': '北京北大方正软件职业技术学院'}, {'city': '', 'name': '北京现代职业技术学院'},
        {'city': '', 'name': '天津音乐学院'}, {'city': '', 'name': '天津美术学院'}, {'city': '', 'name': '天津体育学院运动与文化艺术学院'},
        {'city': '', 'name': '天津师范大学津沽学院'}, {'city': '', 'name': '天津理工大学中环信息学院'}, {'city': '', 'name': '天津财经大学珠江学院'},
        {'city': '', 'name': '华北理工大学'}, {'city': '', 'name': '华北科技学院'}, {'city': '', 'name': '中国人民武装警察部队学院'},
        {'city': '', 'name': '北华航天工业学院'}, {'city': '', 'name': '防灾科技学院'}, {'city': '', 'name': '河北大学工商学院'},
        {'city': '', 'name': '华北理工大学轻工学院'}, {'city': '', 'name': '河北科技大学理工学院'}, {'city': '', 'name': '河北经贸大学经济管理学院'},
        {'city': '', 'name': '河北医科大学临床学院'}, {'city': '', 'name': '华北电力大学科技学院'}, {'city': '', 'name': '河北工程大学科信学院'},
        {'city': '', 'name': '河北工业大学城市学院'}, {'city': '', 'name': '燕山大学里仁学院'}, {'city': '', 'name': '河北农业大学现代科技学院'},
        {'city': '', 'name': '中国地质大学长城学院'}, {'city': '', 'name': '燕京理工学院'}, {'city': '', 'name': '河北建材职业技术学院'},
        {'city': '', 'name': '衡水职业技术学院'}, {'city': '', 'name': '渤海石油职业学院'}, {'city': '', 'name': '冀中职业学院'},
        {'city': '', 'name': '泊头职业学院'}, {'city': '', 'name': '宣化科技职业学院'}, {'city': '', 'name': '渤海理工职业学院'},
        {'city': '', 'name': '太原理工大学现代科技学院'}, {'city': '', 'name': '山西农业大学信息学院'}, {'city': '', 'name': '山西师范大学现代文理学院'},
        {'city': '', 'name': '中北大学信息商务学院'}, {'city': '', 'name': '太原科技大学华科学院'}, {'city': '', 'name': '山西医科大学晋祠学院'},
        {'city': '', 'name': '山西财经大学华商学院'}, {'city': '', 'name': '潞安职业技术学院'}, {'city': '', 'name': '忻州职业技术学院'},
        {'city': '', 'name': '山西运城农业职业技术学院'}, {'city': '', 'name': '朔州职业技术学院'}, {'city': '', 'name': '吕梁职业技术学院'},
        {'city': '', 'name': '河套学院'}, {'city': '', 'name': '内蒙古大学创业学院'}, {'city': '', 'name': '包头钢铁职业技术学院'},
        {'city': '', 'name': '扎兰屯职业学院'}, {'city': '', 'name': '沈阳化工大学'}, {'city': '', 'name': '大连医科大学'},
        {'city': '', 'name': '沈阳音乐学院'}, {'city': '', 'name': '鲁迅美术学院'}, {'city': '', 'name': '沈阳工业大学工程学院'},
        {'city': '', 'name': '中国医科大学临床医药学院'}, {'city': '', 'name': '大连医科大学中山学院'}, {'city': '', 'name': '辽宁师范大学海华学院'},
        {'city': '', 'name': '辽宁科技大学信息技术学院'}, {'city': '', 'name': '沈阳化工大学科亚学院'}, {'city': '', 'name': '辽宁机电职业技术学院'},
        {'city': '', 'name': '渤海船舶职业学院'}, {'city': '', 'name': '辽河石油职业技术学院'}, {'city': '', 'name': '沈阳北软信息职业技术学院'},
        {'city': '', 'name': '东北电力大学'}, {'city': '', 'name': '长春工业大学'}, {'city': '', 'name': '吉林化工学院'},
        {'city': '', 'name': '吉林农业大学'}, {'city': '', 'name': '北华大学'}, {'city': '', 'name': '通化师范学院'},
        {'city': '', 'name': '吉林师范大学'}, {'city': '', 'name': '白城师范学院'}, {'city': '', 'name': '吉林体育学院'},
        {'city': '', 'name': '长春大学'}, {'city': '', 'name': '长春工业大学人文信息学院'}, {'city': '', 'name': '长春理工大学光电信息学院'},
        {'city': '', 'name': '吉林师范大学博达学院'}, {'city': '', 'name': '长春大学旅游学院'}, {'city': '', 'name': '东北师范大学人文学院'},
        {'city': '', 'name': '长白山职业技术学院'}, {'city': '', 'name': '东北石油大学'}, {'city': '', 'name': '伊春职业学院'},
        {'city': '', 'name': '牡丹江大学'}, {'city': '', 'name': '大庆职业学院'}, {'city': '', 'name': '上海戏剧学院'},
        {'city': '', 'name': '上海欧华职业技术学院'}, {'city': '', 'name': '南京艺术学院'}, {'city': '', 'name': '中国矿业大学徐海学院'},
        {'city': '', 'name': '南京大学金陵学院'}, {'city': '', 'name': '南京理工大学紫金学院'}, {'city': '', 'name': '中国传媒大学南广学院'},
        {'city': '', 'name': '南京工业大学浦江学院'}, {'city': '', 'name': '南京师范大学中北学院'}, {'city': '', 'name': '南京医科大学康达学院'},
        {'city': '', 'name': '苏州大学文正学院'}, {'city': '', 'name': '苏州大学应用技术学院'}, {'city': '', 'name': '苏州科技学院天平学院'},
        {'city': '', 'name': '南京邮电大学通达学院'}, {'city': '', 'name': '南通大学杏林学院'}, {'city': '', 'name': '南京审计学院金审学院'},
        {'city': '', 'name': '宿迁学院'}, {'city': '', 'name': '民办明达职业技术学院'}, {'city': '', 'name': '南通职业大学'},
        {'city': '', 'name': '沙洲职业工学院'}, {'city': '', 'name': '九州职业技术学院'}, {'city': '', 'name': '硅湖职业技术学院'},
        {'city': '', 'name': '应天职业技术学院'}, {'city': '', 'name': '太湖创意职业技术学院'}, {'city': '', 'name': '炎黄职业技术学院'},
        {'city': '', 'name': '正德职业技术学院'}, {'city': '', 'name': '钟山职业技术学院'}, {'city': '', 'name': '江南影视艺术职业学院'},
        {'city': '', 'name': '金肯职业技术学院'}, {'city': '', 'name': '常州轻工职业技术学院'}, {'city': '', 'name': '建东职业技术学院'},
        {'city': '', 'name': '江海职业技术学院'}, {'city': '', 'name': '金山职业技术学院'}, {'city': '', 'name': '中国美术学院'},
        {'city': '', 'name': '公安海警学院'}, {'city': '', 'name': '浙江大学城市学院'}, {'city': '', 'name': '浙江工业大学之江学院'},
        {'city': '', 'name': '浙江师范大学行知学院'}, {'city': '', 'name': '宁波大学科学技术学院'}, {'city': '', 'name': '浙江理工大学科技与艺术学院'},
        {'city': '', 'name': '浙江海洋学院东海科学技术学院'}, {'city': '', 'name': '湖州师范学院求真学院'}, {'city': '', 'name': '温州大学瓯江学院'},
        {'city': '', 'name': '中国计量学院现代科技学院'}, {'city': '', 'name': '温州大学城市学院'}, {'city': '', 'name': '衢州职业技术学院'},
        {'city': '', 'name': '浙江农业商贸职业学院'}, {'city': '', 'name': '蚌埠学院'}, {'city': '', 'name': '池州学院'},
        {'city': '', 'name': '安徽新华学院'}, {'city': '', 'name': '安徽财经大学商学院'}, {'city': '', 'name': '安徽大学江淮学院'},
        {'city': '', 'name': '安徽工业大学工商学院'}, {'city': '', 'name': '安徽农业大学经济技术学院'}, {'city': '', 'name': '安徽师范大学皖江学院'},
        {'city': '', 'name': '安徽医科大学临床医学院'}, {'city': '', 'name': '阜阳师范学院信息工程学院'}, {'city': '', 'name': '淮南联合大学'},
        {'city': '', 'name': '民办万博科技职业学院'}, {'city': '', 'name': '亳州师范高等专科学校'}, {'city': '', 'name': '安庆职业技术学院'},
        {'city': '', 'name': '徽商职业学院'}, {'city': '', 'name': '黄山职业技术学院'}, {'city': '', 'name': '皖西卫生职业学院'},
        {'city': '', 'name': '皖北卫生职业学院'}, {'city': '', 'name': '武夷学院'}, {'city': '', 'name': '闽南师范大学'},
        {'city': '', 'name': '闽南理工学院'}, {'city': '', 'name': '福建师范大学闽南科技学院'}, {'city': '', 'name': '福建农林大学东方学院'},
        {'city': '', 'name': '阳光学院'}, {'city': '', 'name': '厦门大学嘉庚学院'}, {'city': '', 'name': '福州大学至诚学院'},
        {'city': '', 'name': '福建师范大学协和学院'}, {'city': '', 'name': '福建农林大学金山学院'}, {'city': '', 'name': '闽西职业技术学院'},
        {'city': '', 'name': '黎明职业大学'}, {'city': '', 'name': '福建电力职业技术学院'}, {'city': '', 'name': '闽北职业技术学院'},
        {'city': '', 'name': '湄洲湾职业技术学院'}, {'city': '', 'name': '宁德职业技术学院'}, {'city': '', 'name': '漳州卫生职业学院'},
        {'city': '', 'name': '闽江师范高等专科学校'}, {'city': '', 'name': '东华理工大学'}, {'city': '', 'name': '井冈山大学'},
        {'city': '', 'name': '江西服装学院'}, {'city': '', 'name': '南昌大学科学技术学院'}, {'city': '', 'name': '华东交通大学理工学院'},
        {'city': '', 'name': '东华理工大学长江学院'}, {'city': '', 'name': '江西理工大学应用科学学院'}, {'city': '', 'name': '江西师范大学科学技术学院'},
        {'city': '', 'name': '赣南师范学院科技学院'}, {'city': '', 'name': '江西财经大学现代经济管理学院'}, {'city': '', 'name': '赣西科技职业学院'},
        {'city': '', 'name': '共青科技职业学院'}, {'city': '华东', 'name': '中国石油大学'}, {'city': '', 'name': '聊城大学东昌学院'},
        {'city': '', 'name': '山东师范大学历山学院'}, {'city': '', 'name': '中国石油大学胜利学院'}, {'city': '', 'name': '济南大学泉城学院'},
        {'city': '', 'name': '北京电影学院现代创意媒体学院'}, {'city': '', 'name': '齐鲁工业大学'}, {'city': '', 'name': '临沂大学'},
        {'city': '', 'name': '山东艺术学院'}, {'city': '', 'name': '齐鲁医药学院'}, {'city': '', 'name': '山东警察学院'},
        {'city': '', 'name': '烟台南山学院'}, {'city': '', 'name': '齐鲁理工学院'}, {'city': '', 'name': '齐鲁师范学院'},
        {'city': '', 'name': '威海职业学院'}, {'city': '', 'name': '潍坊职业学院'}, {'city': '', 'name': '东营职业学院'},
        {'city': '', 'name': '淄博职业学院'}, {'city': '', 'name': '济南职业学院'}, {'city': '', 'name': '华北水利水电大学'},
        {'city': '', 'name': '新乡学院'}, {'city': '', 'name': '铁道警察学院'}, {'city': '', 'name': '黄河交通学院'},
        {'city': '', 'name': '河南师范大学新联学院'}, {'city': '', 'name': '信阳师范学院华锐学院'}, {'city': '', 'name': '安阳师范学院人文管理学院'},
        {'city': '', 'name': '新乡医学院三全学院'}, {'city': '', 'name': '河南科技学院新科学院'}, {'city': '', 'name': '河南职业技术学院'},
        {'city': '', 'name': '漯河职业技术学院'}, {'city': '', 'name': '中州大学'}, {'city': '', 'name': '开封大学'},
        {'city': '', 'name': '焦作大学'}, {'city': '', 'name': '黄河水利职业技术学院'}, {'city': '', 'name': '周口职业技术学院'},
        {'city': '', 'name': '嵩山少林武术职业学院'}, {'city': '', 'name': '永城职业学院'}, {'city': '', 'name': '武汉音乐学院'},
        {'city': '', 'name': '汉口学院'}, {'city': '', 'name': '湖北大学知行学院'}, {'city': '', 'name': '江汉大学文理学院'},
        {'city': '', 'name': '湖北工业大学工程技术学院'}, {'city': '', 'name': '武汉工程大学邮电与信息工程学院'},
        {'city': '', 'name': '长江大学工程技术学院'}, {'city': '', 'name': '长江大学文理学院'}, {'city': '', 'name': '湖北民族学院科技学院'},
        {'city': '', 'name': '湖北师范学院文理学院'}, {'city': '', 'name': '文华学院'}, {'city': '', 'name': '郧阳师范高等专科学校'},
        {'city': '', 'name': '长江职业学院'}, {'city': '', 'name': '仙桃职业学院'}, {'city': '', 'name': '随州职业技术学院'},
        {'city': '', 'name': '咸宁职业技术学院'}, {'city': '', 'name': '长江工程职业技术学院'}, {'city': '', 'name': '江汉艺术职业学院'},
        {'city': '', 'name': '鄂东职业技术学院'}, {'city': '', 'name': '三峡电力职业学院'}, {'city': '', 'name': '三峡旅游职业技术学院'},
        {'city': '', 'name': '天门职业学院'}, {'city': '', 'name': '湖南工学院'}, {'city': '', 'name': '湘潭大学兴湘学院'},
        {'city': '', 'name': '湖南工业大学科技学院'}, {'city': '', 'name': '湖南科技大学潇湘学院'}, {'city': '', 'name': '南华大学船山学院'},
        {'city': '', 'name': '湖南商学院北津学院'}, {'city': '', 'name': '湖南农业大学东方科技学院'}, {'city': '', 'name': '中南林业科技大学涉外学院'},
        {'city': '', 'name': '湖南文理学院芙蓉学院'}, {'city': '', 'name': '湖南理工学院南湖学院'}, {'city': '', 'name': '湖南工程学院应用技术学院'},
        {'city': '', 'name': '长沙理工大学城南学院'}, {'city': '', 'name': '株洲师范高等专科学校'}, {'city': '', 'name': '保险职业学院'},
        {'city': '', 'name': '邵阳职业技术学院'}, {'city': '', 'name': '娄底职业技术学院'}, {'city': '', 'name': '湖南艺术职业学院'},
        {'city': '', 'name': '潇湘职业学院'}, {'city': '', 'name': '湘西民族职业技术学院'}, {'city': '', 'name': '益阳职业技术学院'},
        {'city': '', 'name': '长沙电力职业技术学院'}, {'city': '', 'name': '湘南幼儿师范高等专科学校'}, {'city': '', 'name': '岭南师范学院'},
        {'city': '', 'name': '星海音乐学院'}, {'city': '', 'name': '仲恺农业工程学院'}, {'city': '', 'name': '广东海洋大学寸金学院'},
        {'city': '', 'name': '华南农业大学珠江学院'}, {'city': '', 'name': '广东工业大学华立学院'}, {'city': '', 'name': '东莞理工学院城市学院'},
        {'city': '', 'name': '南方科技大学'}, {'city': '', 'name': '北京师范大学-香港浸会大学联合国际学院'}, {'city': '', 'name': '潮汕职业技术学院'},
        {'city': '', 'name': '民办南华工商学院'}, {'city': '', 'name': '私立华联学院'}, {'city': '', 'name': '罗定职业技术学院'},
        {'city': '', 'name': '阳江职业技术学院'}, {'city': '', 'name': '揭阳职业技术学院'}, {'city': '', 'name': '公安边防部队高等专科学校'},
        {'city': '', 'name': '广西艺术学院'}, {'city': '', 'name': '广西大学行健文理学院'}, {'city': '', 'name': '广西民族大学相思湖学院'},
        {'city': '', 'name': '广西师范大学漓江学院'}, {'city': '', 'name': '广西师范学院师园学院'}, {'city': '', 'name': '百色职业学院'},
        {'city': '', 'name': '梧州职业学院'}, {'city': '', 'name': '三亚学院'}, {'city': '', 'name': '琼台师范高等专科学校'},
        {'city': '', 'name': '四川美术学院'}, {'city': '', 'name': '四川外国语大学重庆南方翻译学院'}, {'city': '', 'name': '四川音乐学院'},
        {'city': '', 'name': '成都学院'}, {'city': '', 'name': '成都理工大学工程技术学院'}, {'city': '', 'name': '四川大学锦城学院'},
        {'city': '', 'name': '西南财经大学天府学院'}, {'city': '', 'name': '西南科技大学城市学院'}, {'city': '', 'name': '西南交通大学希望学院'},
        {'city': '', 'name': '民办四川天一学院'}, {'city': '', 'name': '四川化工职业技术学院'}, {'city': '', 'name': '雅安职业技术学院'},
        {'city': '', 'name': '广安职业技术学院'}, {'city': '', 'name': '川北幼儿师范高等专科学校'}, {'city': '', 'name': '巴中职业技术学院'},
        {'city': '', 'name': '川南幼儿师范高等专科学校'}, {'city': '', 'name': '遵义师范学院'}, {'city': '', 'name': '贵阳中医学院时珍学院'},
        {'city': '', 'name': '贵州大学科技学院'}, {'city': '', 'name': '贵州大学明德学院'}, {'city': '', 'name': '贵州师范大学求是学院'},
        {'city': '', 'name': '遵义医学院医学与科技学院'}, {'city': '', 'name': '六盘水职业技术学院'}, {'city': '', 'name': '毕节幼儿师范高等专科学校'},
        {'city': '', 'name': '云南艺术学院'}, {'city': '', 'name': '云南大学滇池学院'}, {'city': '', 'name': '云南大学旅游文化学院'},
        {'city': '', 'name': '昆明理工大学津桥学院'}, {'city': '', 'name': '云南师范大学文理学院'}, {'city': '', 'name': '云南艺术学院文华学院'},
        {'city': '', 'name': '滇西科技师范学院'}, {'city': '', 'name': '公安消防部队高等专科学校'}, {'city': '', 'name': '咸阳师范学院'},
        {'city': '', 'name': '西安音乐学院'}, {'city': '', 'name': '西安美术学院'}, {'city': '', 'name': '商洛学院'},
        {'city': '', 'name': '西安欧亚学院'}, {'city': '', 'name': '西安交通大学城市学院'}, {'city': '', 'name': '西北大学现代学院'},
        {'city': '', 'name': '陕西科技大学镐京学院'}, {'city': '', 'name': '西安工业大学北方信息工程学院'}, {'city': '', 'name': '西北工业大学明德学院'},
        {'city': '', 'name': '长安大学兴华学院'}, {'city': '', 'name': '西安理工大学高科学院'}, {'city': '', 'name': '西安科技大学高新学院'},
        {'city': '', 'name': '杨凌职业技术学院'}, {'city': '', 'name': '陕西铁路工程职业技术学院'}, {'city': '', 'name': '西北师范大学知行学院'},
        {'city': '', 'name': '兰州交通大学博文学院'}, {'city': '', 'name': '兰州理工大学技术工程学院'}, {'city': '', 'name': '兰州石化职业技术学院'},
        {'city': '', 'name': '庆阳职业技术学院'}, {'city': '', 'name': '青海大学昆仑学院'}, {'city': '', 'name': '宁夏理工学院'},
        {'city': '', 'name': '宁夏民族职业技术学院'}, {'city': '', 'name': '新疆艺术学院'}, {'city': '', 'name': '新疆大学科学技术学院'},
        {'city': '', 'name': '新疆农业大学科学技术学院'}, {'city': '', 'name': '新疆医科大学厚博学院'}, {'city': '', 'name': '石河子大学科技学院'},
        {'city': '', 'name': '新疆机电职业技术学院'}, {'city': '', 'name': '新疆轻工职业技术学院'}]
