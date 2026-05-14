import random

s = "0123456789"   # 대상 문자열(0~9까지 문자열 형태)
passlen = 4        # 비말번호 길이 -> 4자리

# sample()은 문자열 s에서 passlen개만큼 중복 없이 랜덤 선택
# join()은 선택된 문자들을 하나의 문자열로 합침
p = "".join(random.sample(s, passlen))

print(p)


# OTP 발생 프로그램 Lab 