import turtle as t

# 거북이로 그림 그리기
# 각도를 입력 받고
# 배경은 검정 색은 노랑 스피드는 최고속도로 맞춘 후
# for문을 이용해서 200만큼하고 길이는 범위만큼 오르게
# 각도만큼 돌아가게 만들고(정다각형의 각도-1도)

# angle = 89
angle = input("몇 도 = ")
angle = int(angle)

t.bgcolor("black")
t.color("yellow")
t.speed(0)
t.hideturtle()
for x in range(200):
    t.fd(x)
    t.left(angle)
