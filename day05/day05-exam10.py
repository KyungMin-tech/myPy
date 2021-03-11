# 딕셔너리 이용해서 학생번호 가지고 이름 찾기

def get_name(s_info, find_no):
    if find_no in s_info:
        return s_info[find_no]

    return "누구?"

sample_info = {
    39 : "Justine",
    14 : "John",
    20 : "Stone",
    68 : "Mike",
    100 : "Summer"
}

print(get_name(sample_info, 20))
print()
print(get_name(sample_info, 77))
