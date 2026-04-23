list1 = [10, 20, 30, 40, 50]

list2 = [sum(list1[0:x+1]) for x in range(0, len(list1))]
# x를 0부터 마지막 인덱스까지 반복
# 매번 list1[0:x+1] 구간의 합을 계산

print("원래 리스트: ", list1)
print("새로운 리스트: ", list2)

# 앞에서부터 계속 더해가는 누적합 리스트를 만드는 코드
# 누적값 리스트 만들기 Lab