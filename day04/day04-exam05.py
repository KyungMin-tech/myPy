# n명을 입력하면 두명을 뽑아서 짝지어서 그 조합을 출력

def print_pairs(a):
    n = len(a)
    for i in range(0, n-1):
        for j in range(i + 1, n):
            print(a[i], "--", a[j])

name = ["홍길동", "사오정", "저팔계", "손오공"]

print_pairs(name)
