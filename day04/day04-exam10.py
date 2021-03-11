# 피보나치 수열

def fibo(n):
    if n <= 1:
        return n # n = 0 -> 0 n = 1 -> 1
    return fibo(n-2) + fibo(n-1)

print(fibo(0))
print(fibo(1))
print(fibo(2))
print(fibo(3))
print(fibo(4))
print(fibo(5))
print(fibo(6))
print(fibo(7))
print(fibo(8))
print(fibo(9))
