menu = 0
friends = []

while menu != 9: # 9를 입력하기 전까지 계속 반복
    print("--------------------")
    print("1. 친구 리스트 출력")
    print("2. 친구추가")
    print("3. 친구삭제")
    print("4. 이름변경")
    print("9. 종료")

    menu = int(input("메뉴를 선택하시오: "))

    if menu == 1: # 현재 친구 목록 출력
        print(friends)

    elif menu == 2: # 입력받은 이름을 리스트에 추가
        name = input("이름을 입력하시오: ")
        friends.append(name)

    elif menu == 3: # 삭제할 이름 입력, 리스트에 있는지 확인 (in) ,있으면 삭제, 없으면 메시지 출력
        del_name = input("삭제하고 싶은 이름을 입력하시오: ")
        if del_name in friends:
            friends.remove(del_name)
        else:
            print("이름이 발견되지 않았음")

    elif menu == 4: # 기존 이름 입력 -> 존재 여부 확인 -> 있으면 인덱스 찾기 -> 새로운 이름 교체
        old_name = input("변경할 이름을 입력하시오: ")
        if old_name in friends:
            new_name = input("새로운 이름을 입력하시오: ")
            index = friends.index(old_name)
            friends[index] = new_name
        else:
            print("이름이 발견되지 않았음")

print("프로그램 종료")

# 사용자 입력을 받아 친구 목록을 추가/삭제/수정하는 반복형 프로그램
# 친구 관리 프로그램 Lab