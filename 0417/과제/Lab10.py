# 리스트 컴프리헨션
result = [(x, y, z) 
          for x in range(1, 30) 
          for y in range(x, 30) 
          for z in range(y, 30) 
          if x**2 + y**2 == z**2] # 직각삼각형의 세 변 (x, y, z)
 
# 일반 for문
new_list = []
for x in range(1, 30): # 중복 제거 + 순서 정리,  x ≤ y ≤ z
    for y in range(x, 30):
        for z in range(y, 30):
            if x**2 + y**2 == z**2:
                new_list.append((x, y, z))

print(new_list)



# 1~29 사이에서 피타고라스 정리를 만족하는 (x, y, z) 조합을 찾는 코드
# 피타고라스 삼각형 Lab