# 리스트 자료형

l = list()
print(l, type(l))

l = [1, 2, 3]
print(type(l))
print(l)

# 문자열과 같이 인덱스와 슬라이싱 연산 가능
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l[0])

print(l[5])

print(l[len(l)-1])

# 요소의 값 변경 가능
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l[0] = 99
print(l)

l[1] = [1, 2, 3]
l[2] = "문자"
print(l)

# 여러 함수의 사용
l = [1, 2, 3, 4, 5]
print(l)
l.append(6)
print(l)

l = ['a', 'b', 'c', 'd']
print(l)
l.remove('b')
print(l)

# 튜플 자료형 : 다양한 자료형을 순차적으로 저장하는 집합적 자료형
t = tuple()
print(t, type(t))

t = (1, 2, 3)
print(type(t))
print(t)

# 리스트와 비슷한 자료형: 인덱싱, 슬라이싱 등의 연산 가능
l = [1, 2, 3]
t = (1, 2, 3)
print(l, type(l))
print(t, type(t))
print(l[0], l[0:2])
print(t[0], t[0:2])
print(l + l)
print (t + t)

# 리스트와 차이점: 값의 변경이 불가능
l = [1, 2, 3]
t = (1, 2, 3)
print(l, (type(l)))
print(t, (type(t)))

l[0] = 5
print(l)
# t[0] = 5
# print(t)

# 사전자료형 ; 키를 이용하여 값을 저장하는 자료형
d = dict()
print(d, type(d))
d = {
    'a' : 1,
    'b' : 2,
    'c' : 3
}
print(type(d))
print(d)

# 정수형 인덱스가 아닌 키와 값으로 자료를 저장
d = {
    1 : 1,
    'a' : [1, 2, 3],
    (1, 2) : "aaa" # 사전 자료형의 키 값은
                    #변경 불가능한 객체(튜플 자료형 포함)가 볼 수 있음
}
print(d)


