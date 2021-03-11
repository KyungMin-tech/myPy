import turtle as t

#삼각형 그리기
t.color("red")
for x in range(3) :
    t.forward(100)
    t.left(120)

#사각형 그리기
t.color("green")
t.pensize(3)
for x in range(4) :
    t.forward(100)
    t.left(90)

#원 그리기
t.color("blue")
t.pensize(5)
t.circle(50)
