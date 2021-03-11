import random

def make_question():
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    op = random.randint(1, 3)

    q = str(a)

    if op == 1 :
        q = q + "+"
    if op == 2 :
        q = q + "-"
    if op == 3 :
        q = q + "*"

    q = q + str(b)

    return q

sc1 = 0 # 정답 갯수
sc2 = 0 # 틀린거 갯수

for x in range(10):
    q = make_question()
    print(q)
    ans = input("=")
    r = int(ans)

    if eval(q) == r:
        print("정답입니다.")
        sc1 = sc1 + 1
    else:
        print("오답입니다.")
        sc2 = sc2 + 1

# print(sc1*10,"점 입니다.")
# if sc2==0:
#    print("만점입니다!!")

print("정답 : ", sc1, "오답 : " , sc2)
if sc2 == 0 :
    print("100점")
if sc2 == 1 :
    print("90점")
if sc2 == 2:
    print("80점")
if sc2 == 3:
    print("70점")
if sc2 == 4:
    print("60점")
if sc2 == 5:
    print("50점")
if sc2 == 6:
    print("40점")
if sc2 == 7:
    print("30점")
if sc2 == 8:
    print("20점")
if sc2 == 9:
    print("10점")
if sc2 == 10:
    print("0점")

# 10회전을 하고 100점 만점으로 해서
# 10문제가 출제되고요 7개 맞으면 70점 이런식으로
# 알려주는 것으로...고치세요


    
