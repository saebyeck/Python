stack = [] # 비어있는 리스트 (스택 역할)

for i in range(3): # 3번 반복하면서 과일 이름 입력받고 리스트에 추가
    f = input("과일을 입력하시오: ")
    stack.append(f)

for i in range(3):
    print(stack.pop()) # pop() 맨 마지막 요소 꺼내면서 삭제
    
    
    # 입력은 순서대로, 출력은 거꾸로 나오는 코드
    # 리스트로 스택 흉내내기 랩
