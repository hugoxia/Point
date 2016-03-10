import pickle
with open('school.txt', 'r') as f:
    txt = f.read()
    text = txt.strip()
    result = txt.splitlines()
    pickle_file = open('schools.pkl', 'wb')
    pickle.dump(result, pickle_file)
    pickle_file.close()
