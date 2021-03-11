# 세미콜론(;)을 활용해 한 줄에 여러 변수 값을 할당할 수 있음
# ';'은 문장이 끝났음을 의

a = 1 ; b = 2 ; c = 3
print(a)
print(b)
print(c)

# 두 변수의 값을 콤마, 등호를 활용해 서로 바꿀 수 있음

a =1; b =2
print(a,b)

a , b = b, a
print(a, b)

a = 1
print(a)

a += 10
print(a)

a -= 5
print(a)

# 사칙연산자를 함께 활용해 새로운 값을 할당할 수 있음

b = 2; c = 3
a = b+c
print(a)

# 표현식이 아닌 할당문은 할당할 수 없음
# b = 2; c = 3
# a = (b=b+c)
# print(a)

# 역슬래시(\)를 사용해 한 줄을 여러줄로 표현할 수 있음
# 코딩이 길어져 한줄에 표현하기 어려운 경우 사용할 수 있음

a = 1
b = 2

print(a + \
      b)

# 예약어(Keyword)란?
    # 파이썬에서 이미 문법적인 용도로 사용을 하고 있기 때문에 변수 등의 식별자로 사용할 수 없는 단어들
    # 예약어는 변수로 사용할 수 없음
    # False = 1

# 파이썬의 기본 모듈 중 하나인 Keyword모듈을 import해서 확인가능
import keyword
print(keyword.kwlist)
# 예약어의 개수는 총 33개

# 내장 함수란?
    # 파이썬에서는 자주 사용되는 함수를 내장 함수라는 이름으로 기본적으로 제공

# 대표적인 내장 함수
    # max, min, type, len,range, str, int...
# type() : 해당 식별자의 타입을 확인할 수 있음

a = 1
print(type(a))

a = "문자"
print(type(a))

a = 1+4j
print(type(a))

#len() : 객체의 길이를 알 수 있음

a = '1234'
print(len(a))

a = [1,2,3,4,5]
print(len(a))

# max(), min() : 최대값,최소값을 출력함

print(max("abcedfg"))
print(min("12345"))

    
