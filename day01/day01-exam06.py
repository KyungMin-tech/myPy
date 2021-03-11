# [0-4] 까지 for문을 이용해서 출력하기
print("[0-4]")
for x in range(5):
    print(x)    

# 범위 [1-10] for문을 이용해서 출력하기
print("[1-10]")
for x in range(1, 11):
    print(x)

# 1에서 10까지의 합을 구하기(for문 이)
s = 0
for x in range(1, 11):
    s = s + x
    print("x = ", x, ", sum = ", s)
