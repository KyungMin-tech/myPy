# 최대값 찾기

def find_max(a): # a는 리스트로 값의 목록
    n =len(a)
    maxvalue = a[0]
    for i in range(1, n):
        if a[i] > maxvalue:
            maxvalue = a[i]
    return maxvalue

def find_max_idx(a):
    n =len(a)
    max_idx = 0
    for i in range(1, n):
        if a[i] > a[max_idx]:
            max_idx = i
    return max_idx


value = [17, 18, 92, 33, 105, 77, 21, 8]

print(find_max(value))
print()
print(find_max_idx(value))

            
