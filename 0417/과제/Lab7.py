salaries = [200, 250, 300, 280, 500] # 직원 급여 리스트
 
def modify(values, factor): # 리스트(values)와 배수(factor)를 받아서 수정하는 함수
    for i in range(len(values)): # 리스트 길이만큼 반복 (인덱스로 접근)
        values[i] = values[i] * factor # factor만큼 곱해서 리스트 자체를 변경
 
print("인상전", salaries)
modify(salaries, 1.3)
print("인상후", salaries)



# 리스트의 모든 값을 일정 비율로 증가시키는 함수
# 리스트 변경 함수 Lab