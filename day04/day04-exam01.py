# 1부터 n까지 연속한 숫자의 제곱을 구하는 프로그램

def sum_sq1(n):
    s = 0
    for i in range(1, n+1):
        s = s + i * i
    return s

def sum_sq2(n):
    return n * (n + 1) * (2 * n + 1) // 6

print(sum_sq1(10))
print(sum_sq1(100))
print()
print(sum_sq2(10))
print(sum_sq2(100))

