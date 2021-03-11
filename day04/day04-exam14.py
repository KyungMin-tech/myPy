# 학생번호와 이름을 리스트로 주었을 때 이때 학생번호를 
# 입력하면 학생번호에 해당하는 이름을 순차탐색 하여 
# 찾아서 돌려주는 프로그램

def get_name(stu_no, stu_name, find_no):
    n = len(stu_no)
    for i in range(0, n):
        if find_no == stu_no[i]:
            return stu_name[i]
        
    return "누구?"

sample_no = [33, 14, 76, 100]
sample_name = ["홍길동", "손오공", "사오정", "저팔계"]
print(get_name(sample_no, sample_name, 76))
print()
print(get_name(sample_no, sample_name, 88))
