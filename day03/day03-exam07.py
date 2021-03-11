# 도형에서의 확률 시뮬레이션
import random

# 원주율 
total = 1000000
ev = 0

for i in range(total) :
    x = random.random() # 0<= x < 1 실수
    y = random.random()
    if x*x + y * y <= 1.0 :
        ev = ev + 1

print((ev/total) * 4)
