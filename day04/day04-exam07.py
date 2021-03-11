# 재귀호출로 팩토리얼 만들기

def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)

print(fact(3))
print()
print(fact(4))
print()
print(fact(5))
