# 이분탐색

def binary_search(a, x):
    start = 0
    end = len(a) - 1

    while start <= end:
        mid = (start + end) // 2
        if x == a[mid]:
            return mid
        elif x > a[mid]:
            start = mid + 1
        else:
            end = mid -1

    return -1
    

data = [1, 4, 9, 16, 25, 36, 49, 64, 81]

print(binary_search(data, 36))
print()
print(binary_search(data, 4))
print()
print(binary_search(data, 50))
