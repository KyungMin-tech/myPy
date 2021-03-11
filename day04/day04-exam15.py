# 주어진 리스트에서 작은 수부터 큰 수 순서로 배열하는 정렬

def find_min_idx(a):
    n = len(a)
    min_idx = 0
    for i in range(1, n):
        if a[i] < a[min_idx]:
            min_idx = i
            
    return min_idx

def sel_sort(a):
    result = []
    while a:
        min_idx = find_min_idx(a)
        value = a.pop(min_idx)
        result.append(value)

    return result    

data = [35, 8, 1, 88, 17]
print(sel_sort(data))
