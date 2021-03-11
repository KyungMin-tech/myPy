# 랜덤으로 거북이 이동하기

# 거북이 모듈과 랜덤모듈을 변수에 넣어두고
# 거북이 모양으로 스피드는 최고 속도
# 500 번 반복 하는데 1부터 359까지의 랜덤숫자범위를 정하고
# 그에 맞게 거북이 머리방향 조절
# 거리도 5에서 19까지 랜덤 숫자 법위를 정하고
# 그에맞게 거리이동 

import turtle as t
import random as r

t.shape("turtle")
t.speed(0)

for x in range(500):
    num = r.randint(1, 360)
    t.setheading(num)
    distance = r.randint(5,19)
    t.forward(distance)
