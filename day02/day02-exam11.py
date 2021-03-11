# 거북이를 이용해 다각형 만들기

# 함수의 이름은 polygon
# 인자 하나를 받으면 360를 그 값을 나눈 다각형 그리기
# 변의 길이는 100
import turtle as t

def polygon(n):
    for x in range(n):
        t.forward(100)
        t.left(360/n)

# 함수의 이름은 polygon2
# 인자 두개를 받는데 하나는 360에 그 값을 나누는 인자 하나는 거리 인자
# 를 받아서 다각형 그리기

def polygon2(n, a):
    for x in range(n):
        t.forward(a)
        t.left(360/n)

polygon(3)
polygon(5)

t.up()
t.fd(100)
t.down()

polygon2(3, 75)
polygon2(5, 100)
