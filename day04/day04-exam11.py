# 하노이 탑 프로그램 

def hanoi(n, from_pos, to_pos, aux_pos):
    # 원반의 개수가 한개일 때는 바로 옮기면 되므로 
    if n == 1:
        print(from_pos, "->", to_pos)
        return

    # 원반 n-1개를 aux_pos(보조기둥)으로 이동(to_pos 보조기둥이 됨)
    hanoi(n-1, from_pos, aux_pos, to_pos)

    # 가장 큰 원반이 목적지로 이동
    print(from_pos, "->", to_pos)

    # aux_pos에 있는 원반 n-1개를 목적지로 이동(from_pos보조기둥이 됨)
    hanoi(n-1, aux_pos, to_pos, from_pos)
    
print("========================")
print("하노이의 탑 프로그램")
print("\t\t-홍길동") # 문제에서 원하는 이름이 홍길동이여서 홍길동으로 설정
print("========================")
print()
#print("n = 1") 
#hanoi(1, 1, 3, 2) # 1->3
#print()
#print("n = 2")
#hanoi(2, 1, 3, 2) # 1->2 1->3 2->3
#print()
#print("n = 3")
#hanoi(3, 1, 3, 2) # 1->3 1->2 3->2 1->3 2->1 2->3 1->3
#print() <- 이런식으로 미리 테스트해봤습니
print("n = 4")
hanoi(4, 1, 3, 2)

