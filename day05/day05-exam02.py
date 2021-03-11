# 삽입정렬을 오름차순 알고리즘

def ins_sort(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key

data = [26, 33, 97, 55, 77, 66, 25, 100]
#[2, 4, 5, 1, 3]
ins_sort(data)
print(data)
