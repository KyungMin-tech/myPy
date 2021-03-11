# 수치형 자료형과 문자열 자료형의 특징

# 자료형이란?
    # 프로그래밍이란 자료(Data)를 처리하는 일을 주로 함
    # 파이썬에서는 자료를 손쉽게 다룰 수 있도록 내장 자료형을 제공

    # 숫자(수치)자료형 - 정수(int), 실수(float), 복소수(complex)
    # 불(Bool)자료형 - True, False
    # 군집 자료형 - 문자열(str), 리스트(list), 튜플(tuple), 사전(dict), 집합(set)

    # 내장 자료형의 구분
        # 1. 기억 장소의 크기
        # 2. 저장되는 데이터의 형태
        # 3. 저장방식
        # 4. 값의 범위

        # 직접 표현
            # 데이터를 표현(정수, 실수 등)
        # 시퀀스
            # 여러 데이터를  포함(순서가 있음)
        # 매핑
            # 여러 데이터를 포함(순서가 없음)

    # 객체지향형 자료형 또한 객체와 래퍼런스(Reference)로 관리

a = 1
b = 1

print(id(a))
print(id(b))

a = 2
print(id(a))

# 정수 자료형(int)
# 소수점이 없는 숫자(양수, 0, 음수)

a = 0
print(type(a))
print(a)

b = -11
print(type(b))
print(b)

# 기본으로 10진수
a = 12345   # 10진수
print(type(a))
print(a)

b = 0b11    # 2진수
print(type(b))
print(b)

c = 0o12    # 8진수
print(type(c))
print(c)

d = 0X23    # 16진수
print(type(d))
print(d)

# 내장 함수 int()를 활용해 정수 자료형으로 변경 가능
a = "123"
print(type(a))
print(a)

b = int(a)
print(type(b))
print(b)

#범위의 제한이 없음
a = 9223372036854775808045146362345
print(type(a))
print(a)

# 실수 자료형(float)
# 소수점이 있는 숫자
a = float("0.12")
print(type(a))
print(a)

# 지수 표현 가능(e)
b = 2e-4
print(type(b))
print(b)

# 내장함수 float()를 활용해 실수 자료형으로 변경 가능
c = 3e3
print(type(c))
print(c)

# 복소수 자료형(complex)
# 실수와 허수로 구성된 숫자
a = 10 + 2j
print(type(a))
print(a)

# 실수부 + 허수부j
b = 5 - 4j
print(type(b))
print(b)

# 파이썬의 문자열 자료형
# 문자, 단어 등으로 구성된 문자들의 집합
a = '1'
print(type(a))
print(a)

# 큰 따옴표("")와 작은 따옴표('')모두 사용 가능
b = "Hello, World !"
print(type(b))
print(b)

# 내장 함수str()을 활용해 문자열 자료형을 변경 가능
c = 12345
c = str(c)
print(type(c))
print(c)

# 문자열 안에 따옴표를 넣는 방법
# 이스케이프 문자 사용 (\)

a = "안녕하세요"
print(a)

d = "\'안녕하세요\""
print(d)

# 따옴표를 다르게 사용
print(a)
b = "'안녕하세요'"
print(b)
c = '"안녕하세요"'
print(c)

a = "안녕하세요 \n제 이름은 민경민입니다. \n잘 부탁 드립니다."
print(a)

a = """안녕하세요
제 이름은 민경민입니다.
잘 부탁드립니다."""
print(a)

# 숫자연산자
# 사칙 연산자(덧셈, 뺄셈, 곱셉, 나눗셈)
# 숫자를 나누고, 소수점 이하의 자릿수를 버리는 나누기 연산자(//)
# 나머지 연산자 (%)
# 내장 함수를 활용해 연산자와 같은 출력 가능 
divmod(5,3)
# 제곱 연산자(**) pow( , )
# 복합 대입 연산자 (+=, -=, *=, /=, %=, **=)

# math모듈 사용
# Tab 키를 눌러 활용할 수 있는 함수 목록 확인 가능
import math

#상용로그
print(math.log10(10))

# 제곱근
print(math.sqrt(8))

# 연결 연산자 (+)
# 반복 연산자 (*)
print('2' * 3)
print('안녕하세요' *3)

# 선택 연산자(인덱싱)
a = '안녕하세요'
print(a[0])
# 문자열은 시퀀스 자료형으로 인덱스가 있고, 인덱스로 값의 접근이 가능
print(a[-1])
# 범위 선택 연산자(슬라이싱)
print(a[1:3])
# 변수[시작(이상):끝(미만):스텝]
print(a[0:5:2])
