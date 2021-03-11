# 함수의 이름은 sum_func
# sum_func는 숫자 n를 받아서 0부터 숫자 n까지 합을
# 구해서 리턴해주는 함수 입니다.

def sum_func(n):
    s = 0
    for x in range(1, n+1):
        s = s + x
    return s

print(sum_func(10))

# 함수의 이름은 factorial
# factorial은 숫자 n을 받아서 1부터 n까지의 곱을
# 구해서 리턴해주는 함수 입니다.
 
def factorial(n):
    fact = 1
    for x in range(1, n+1):
        fact = fact * x
    return fact

print(factorial(10))

