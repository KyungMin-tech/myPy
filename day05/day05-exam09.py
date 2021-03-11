# 동명이인 찾기 2

def find_same_name(a):
    name_dict = {}

    for name in a:
        if name in name_dict :
            name_dict[name] += 1
        else:
            name_dict[name] = 1

    result = set()
    for name in name_dict:
        if name_dict[name] >= 2:
            result.add(name)

    return result

name = ["Tom", "Jerry", "MIke", "Tom"]
print(find_same_name(name))
print()
name2 = ["Tom", "Jerry", "MIke", "Tom", "Jerry"]
print(find_same_name(name2))
