# 삽입정렬

def find_ins_idx(r, v):
    for i in range(0, len(r)):
        if v < r[i]:
            return i

    return len(r)

def ins_sort(a):
    result = []
    while a:
        value = a.pop(0)
        ins_idx = find_ins_idx(result, value)
        result.insert(ins_idx, value)
    return result
    
data = [2, 4, 5, 1, 3]
# [77, 33, 55, 66, 25, 97, 98, 100, 26]
print(ins_sort(data))
