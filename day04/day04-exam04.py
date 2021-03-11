# 동명이인 찾기

def find_same_name(a):
    n = len(a)        
    result = set()
    for i in range(0, n -1):        
        for j in range(i + 1, n):            
            if a[i] == a[j]:
                result.add(a[i])
    return result
    

name = ["홍길동", "사오정", "저팔계", "손오공", "사오정", "손오공", "삼장법사"]

print(find_same_name(name))
