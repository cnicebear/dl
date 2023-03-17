a = {-1: '2', 2: ['3', '4'], 4: ['5', '7']}
# print(list(a.values()).index(3))
for key, value in a.items():
    if value is None:
        continue
    if '7' in value:
        print(list(a.keys()).index(key))