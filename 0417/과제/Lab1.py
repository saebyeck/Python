STUDENTS = 5
lst = [] # lst: 성적을 저장할 리스트
count = 0 # 80점 이상 학생 수를 세는 변수

for i in range(STUDENTS): # 5번 반복하면서 점수를 입력받음
    value = int(input("성적을 입력하시요: "))
    lst.append(value)

print("\n성적 평균=", sum(lst) / len(lst)) # sum(lst): 총합, len(lst): 개수
print("최대점수=", max(lst))
print("최소점수=", min(lst))

for score in lst: # 80점 이상이면 count 증가
    if score >= 80:
        count += 1

print("80점 이상=", count)


# 학생 5명의 성적을 입력받아 통계를 계산
# 성적 처리 프로그램 Lab 