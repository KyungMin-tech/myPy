# 마우스로 찍어서 이동

import turtle as t

t.speed(0)
t.pensize(2)
t.hideturtle()
t.onscreenclick(t.goto)
