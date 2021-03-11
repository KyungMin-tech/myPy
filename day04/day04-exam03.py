# 최소값 찾기

def find_min(a):
    n = len(a)
    minvalue = a[0]
    for i in range(1, n):
        if a[i] < minvalue:
            minvalue = a[i]
    return minvalue

def find_min_idx(a):
    n = len(a)
    min_idx = 0
    for i in range(1, n):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx
    

value = [17, 18, 92, 33, 105, 77, 21, 8]

print(find_min(value))
print()
print(find_min_idx(value))
