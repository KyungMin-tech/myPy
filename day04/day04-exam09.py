# 숫자 n개 중 최대값 찾기를 재귀 호출로 만들기

def find_max(a, n):
    if n == 1:
        return a[0]
    max_n_1 = find_max(a, n-1)
    if max_n_1 > a[n-1]:
        return max_n_1
    else:
        return a[n-1]
        

v = [17, 21, 92, 55, 36]

print(find_max(v, len(v)))
    
    
