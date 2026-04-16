def getIntRange(a, b, msg):
    x =-100
    while x < a or x > b:
        x = int(input(msg))
    return x

m = getIntRange(1, 12, "월을 입력하시오(1부터 12사이의 값): ")
d = getIntRange(1, 31, "일을 입력하시오(1부터 31사이의 값): ")
print(f"입력된 날짜는 {m}월 {d}일입니다.")