board = [[' ' for x in range(3)] for y in range(3)]

while True:
    # 게임 보드를 그린다.
    for r in range(3):
        print(" " + board[r][0] + " | " + board[r][1] + " | " + board[r][2])
        if r != 2:
            print("---|---|---")

    x = int(input("다음 수의 x좌표를 입력하시오: "))
    y = int(input("다음 수의 y좌표를 입력하시오: "))
    #  # 사용자로부터 좌표를 입력을 받음。

    if board[x][y] != ' ': # 이미 차있으면 다시 입력 (continue)
        print("잘못된 위치입니다.")
        continue
    else:
        board[x][y] = 'X'

    # 컴퓨터가 놓을 위치를 결정
    done = False
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ' and not done:
                board[i][j] = 'O'
                done = True
                break
# 사용자는 원하는 위치, 컴퓨터는 첫 번째 빈 칸에 자동으로 두는 구조
# Tic-Tac-Toe 게임 Lab