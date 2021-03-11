import turtle as t
# 거북이로  도형그리기
# 입력으로 숫자를 입력 받으면 컬러는 보라색으로 도형안에도 칠해진 형태로
# 거리 50
# for문 사용

# n = 5
n = input("몇 각형?")
n = int(n)

t.color("purple")
t.begin_fill()
for x in range(n):
    t.fd(50)
    t.lt(360/n)
t.end_fill()
