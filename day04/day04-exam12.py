# 순차탐색

def search_list(a, x):
    n = len(a)
    for i in range(0, n):
        if x == a[i]:
            return i

    return -1
    

v = [17, 22, 93, 93, 56, 78, 85, 41, 45, 88, 99]
print(search_list(v, 85))
print()
print(search_list(v, 44))
print()
print(search_list(v, 93)) # [2, 3]
