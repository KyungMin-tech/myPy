# 시간 재는 프로그램 만들기
# time모듈을 import 하고
# 엔터를 입력받으면 시작해서
# 다시 엔터를 누르면 끝나는 시간을 재서
# 실제 시간 몇 초로 출력하
# 차이는 절대값이용해서 몇 초로 출력해보기

import time

input("엔터를 누르고 30초를 셉니다.")
start = time.time()

input("30초에 다시 엔터를 누르세요.")
end = time.time()

result = end - start
print("실제시간 :", result, "초")
print("차이 :", abs(result-30), "초")
