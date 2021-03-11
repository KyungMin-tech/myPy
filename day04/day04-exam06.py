# 팩토리얼 구하기

def fact(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f

print(fact(3))
print()
print(fact(5))
