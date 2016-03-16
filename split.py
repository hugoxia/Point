import pickle
with open('xingzheng', 'r') as f:
    txt = f.read()
    text = txt.strip()
    result = txt.splitlines()
    pickle_file = open('xingzheng.pkl', 'wb')
    pickle.dump(result, pickle_file)
    pickle_file.close()
