import pickle
with open('xingzheng.txt', 'r') as f:
    txt = f.read()
    result = txt.splitlines()
    new_result = []
    for i in result:
        if '\xa0' in i:
            i = i.replace('\xa0', '')
            new_result.append(i)
    new_result = list(set(new_result))
    pickle_file = open('xingzheng.pkl', 'wb')
    pickle.dump(new_result, pickle_file)
    pickle_file.close()

