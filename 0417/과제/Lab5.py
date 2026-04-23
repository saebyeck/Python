numbers = [1,2,3,4,5,6,7,8,9,10]
reversed = numbers[::-2]
print(reversed)

# [::-2], 뒤에서 2칸씩 선택 => [10, 8, 6, 4, 2]

numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
numbers[1:] = [ ]
print(numbers)
# [1:] = [], 1번 인덱스 이후 삭제 => [1]

# 첫 번째는 추출, 두 번째는 삭제(리스트 변경)
# 리스트 슬라이싱 Lab