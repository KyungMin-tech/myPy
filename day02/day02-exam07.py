# 랜덤으로 나온 숫자 더해서 맞추는 프로그램 만들기

# 랜덤모듈을 받고
# a와 b 숫자를 1에서 100까지 랜덤숫자를 만들고
# 그숫자들의 덧셈에 대한 답을 입력했을때
# 답이 맞으면 정답입니다.
# 답이 틀리면 머징? 이라고 출력해보기

import random
a = random.randint(1, 100)
b = random.randint(1, 100)

print(a, "+", b, "=")
x = input()
result = int(x)

if a + b == result:
    print("정답입니다.")

else:
    print("머징?")
