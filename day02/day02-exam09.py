# 1부터 100 까지의 랜덤 숫자 맞추기

# 랜덤 모듈을 받고
# 숫자를 랜덤으로 만들면 그걸 입력해서 맞추는 프로그램을 while문과 for문으로 만들기
# 기회는 4번만 하고
# 맞추면 기회 번 만엔 정답
# 크면 너무커요
# 작으면 너무작아요
# 기회 4번이 끝나면 4번의 기회동안 못 맞추었어요 라고 출력 해보기 

import random

n = random.randint(1, 5)

count = 1

while count <=4:
    x = input("맞춰보세요 :")
    g = int(x)

    if g == n:
        print(count, "번 만에 정답")
        break;

    if g > n:
        print("너무 커요")

    if g < n:
        print("너무 작아요")

    count = count + 1

if count > 4:
    print("4번의 기회동안 못 맞추었어요.")

n = random.randint(1, 5)

for count in range(1, 5):
    x = input("맞춰 봐 :")
    g = int(x)

    if g == n:
        print(count, "번 만에 정답")
        break;

    if g > n:
        print("너무 커")

    if g < n:
        print("너무 작어")

    count = count + 1

if count > 4:
    print("그것도 못 맞추냐?")
        
