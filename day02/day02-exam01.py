import turtle as t

# 숫자를 입력 받으면 그 숫자만큼 반지름 80인 원 그리기
# 원이 살짝 틀어진다  
# 배경은 검정에 색은 빨강 속도는 0
# for문 이용하기

# n = 50
n = input("몇 번 = ")
n = int(n)

t.bgcolor("black")
t.color("red")
t.speed(0)
for x in range(n):
    t.circle(80)
    t.left(360/n)

