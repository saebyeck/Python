scores = [10.0, 9.0, 8.3, 7.1, 3.0, 9.0]

print("제거전", scores)
scores.remove(max(scores))  # 가장 큰 값 하나 제거
scores.remove(min(scores))  # 가장 작은 값 하나 제거
print("제거후", scores)


# 콘테스트 평가 Lab 
# 최댓값 1개 + 최솟값 1개를 제거한 리스트를 만드는 코드