import turtle as t

d = 100 # 변수 d에다가 100이란 값을 저장
t.speed(3)
#삼각형 그리기 color는 red
t.color("red")
for x in range(3):
    t.forward(d)
    t.left(120)

#사각형 그리기 color는 green, pensize는 3
t.color("green")
t.pensize(3)
for x in range(4):
    t.forward(d)
    t.left(90)


#원 그리기 color는 blue, pensize는 5 반지름 50
t.color("blue")
t.pensize(5)
t.circle(50)
