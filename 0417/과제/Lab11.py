transposed = []
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("원래 행렬=", matrix)

# 열의 개수만큼 반복한다.
for i in range(len(matrix[0])): # matrix[0] = [1,2,3] → 길이 3
    transposed_row = []
    
    for row in matrix:  # 각 행을 하나씩 꺼냄
        transposed_row.append(row[i])  # 각 행에서 i번째 값만 뽑아서 모음
    
    transposed.append(transposed_row)

print("전치 행렬=", transposed)

# 열 기준으로 값을 모아서 행으로 바꾸는 코드 
# 전치 행렬 계산 Lab