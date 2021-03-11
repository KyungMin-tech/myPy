# Turtle Run Game

import turtle as t
import random

score = 0 #게임점수
playing = False # 게임이 실행 중인지 확인

# 악당 거북이 그리기
te = t.Turtle()
te.shape("turtle")
te.color("red") # 악당거북이의 색은 빨간색으로 설정
te.speed(9) # 악당 거북이의 속도를 9로 설정
te.up()
te.goto(0, 200)

# 먹이 그리기
ts = t.Turtle()
ts.shape("circle") 
ts.color("green") # 먹이의 모양은 초록색 채워진 원
ts.speed(0) 
ts.up()
ts.goto(0, -200)

# 방향키로 방향 전환을 하기 위한 함수들
def turn_right(): # 오른쪽으로 방향 전환
    t.setheading(0)

def turn_up(): # 위쪽으로 방향전환
    t.setheading(90)

def turn_left(): # 왼쪽으로 방향전환
    t.setheading(180)

def turn_down(): # 아래쪽으로 방향전환
    t.setheading(270)

# 게임을 시작하는 함수
def start():
    global playing
    if playing == False: # 처음 시작을 누르기전엔 False로 해준다
        playing = True # 시작시 게임을 시작
        t.clear()
        play()

# 실제 게임을 진행하는 함수
def play():
    global score
    global playing
    
    t.forward(10)

    if random.randint(1, 5) == 3: # 악당거북이가 랜덤 숫자중 3을 가리키면 
        ang = te.towards(t.pos()) # 내 거북이를 쫏아오도록 설정
        te.setheading(ang) # 각도를 내 거북이로 설정

    speed = score + 5 # 난이도 변화
    if speed > 15:  
        speed = 15
    te.forward(speed) # 점수가 오를 수록 악당거북이의 속도를 증가

    # 악당 거북이와 나의 거리가 12보다 작으면 잡힌것
    if t.distance(te) < 12:
        text = "Score : " + str(score)
        message("Game Over", text)
        playing = False
        score = 0
    # 먹이하고 나의 거리가 12보다 작으면 먹은 것    
    if t.distance(ts) < 12:
        score = score +1
        t.write(score)
        star_x = random.randint(-230, 230) # 먹이의 x좌표 랜덤 설정(범위 내에서)
        star_y = random.randint(-230, 230) # 먹이의 y좌표 랜덤 설정(범위 내에서)
        ts.goto(star_x, star_y) # 랜덤 설정한 좌표로 먹이 이동
        
    if playing:
        t.ontimer(play, 100)

def message(m1, m2): # 게임을 시작하기전 처음 문구설정 함수
    t.clear()
    t.goto(0, 100)
    t.write(m1, False, "center", ("", 20))
    t.goto(0, -100)
    t.write(m2, False, "center", ("", 15))
    t.home()

t.title("Turtle Run Game") # 타이틀 이름 설정  
t.setup(500, 500) # 너비 500 높이 500
t.bgcolor("orange") # 배경은 주황색
t.shape("turtle")
t.speed(10) # 내 거북이의 속도는 10 
t.up() # 내 거북이의 꼬리를 올려서 자취를 안남게 설정한다 
t.color("white") # 내거북이의 색은 하얀색

t.onkeypress(turn_right, "Right") # 키보드 오른쪽을 누르면 방향전환
t.onkeypress(turn_up, "Up") # 키보드 위쪽을 누르면 방향 전환
t.onkeypress(turn_left, "Left") # 키보드 왼쪽을 누르면 방향전환
t.onkeypress(turn_down, "Down") # 키보드 아래쪽으로 누르면 방향전환
t.onkeypress(start, "space") # 키보드 스페이스바를 누르면 게임시작

t.listen() # 키보드를 눌렀을때 그것을 듣고 수행

message("Turtle Run Game Start", "[Space]") #설정한 문구를 나타낸다

