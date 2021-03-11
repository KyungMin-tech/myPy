# 순차탐색으로 찾은 값이 여러개일때
# 모든 위치를 리스트로 돌려주는 프로그램

def search_list(a, x):
    n = len(a)
    result = []
    for i in range(0, n):
        if x == a[i]:
            result.append(i)

    return result

v = [17, 22, 93, 93, 56, 78, 85, 41, 45, 88, 99]
print(search_list(v, 85))
print()
print(search_list(v, 44))
print()
print(search_list(v, 93))
