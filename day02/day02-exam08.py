# while문과 for문을 사용해서 1부터 10까지의 합 구하

# s = 0
# x = 1
# while x <=10:
#    s = s + x
#    print("x :", x, "sum :", s)
#    x= x + 1

s = 0
for x in range(1, 11):
    s = s + x
    print("x :", x, "sum :", s)
