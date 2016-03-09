from functools import reduce
from operator import itemgetter

test = [{"a": '小明', "n": 1},
        {"a": '小白', "n": 3},
        {"a": '小黑', "n": 4},
        {"a": '小李', "n": 2},
        {"a": '小明', "n": 1},
        {"a": '小王', "n": 0}]

f = lambda x, y: x if y in x else x + [y]
test = reduce(f, [[], ] + test)
print(test)
t = reversed(sorted(test, key=itemgetter('n')))
new_list = []
for i in t:
    new_list.append(i['a'])

print(new_list)
