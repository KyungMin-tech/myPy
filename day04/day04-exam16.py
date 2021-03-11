# 선택정렬 알고리즘

def sel_sort(a):
    n = len(a)
    for i in range(0, n):
        min_idx = i
        for j in range(i+1, n):
            if a[j] < a[i]: # > 내림차순으로 바뀜
                min_idx = j
                a[i], a[min_idx] = a[min_idx], a[i]
            

data = [2, 4, 5, 1, 3]
sel_sort(data)
print(data)

data2 = [3, 1, 2]
sel_sort(data2)
print(data2)
