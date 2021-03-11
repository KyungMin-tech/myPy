# 1부터 n까지의 합 구하기 재귀 호출로 만들기

def sum_n(n):
    if n == 0 :
        return 0
    return sum_n(n-1) + n

print(sum_n(10))
print()
print(sum_n(100))

