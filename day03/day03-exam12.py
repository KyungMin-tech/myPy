# 1부터 n까지의 합을 구하기

def sum_n1(n):
    s = 0
    for i in range(1, n+1):
        s = s + i
    return s

def sum_n2(n):
    return n * (n+1) // 2

print(sum_n1(10))
print(sum_n1(100))
print()
print(sum_n2(10))
print(sum_n2(100))
