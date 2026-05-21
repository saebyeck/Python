from random import randint

class Dice:

    def __init__(self, x, y): # 위치 (x, y)
        self._x = x
        self._y = y
        self._size = 30 # 크기 30 고정
        self._value = 1 # 처음 값 1

    def read_dice(self): # 현재 주사위 값 반환
        return self._value

    def print_dice(self): # 주사위 값 출력
        print("주사위의 값=", self._value)

    def roll_dice(self): # 1~6 랜덤 값으로 주사위 굴리기
        self._value = randint(1, 6)


d = Dice(100, 100)
d.roll_dice()
d.print_dice()

# 주사위 속성 -> 주사위의 값(value), 주사위의 위치(x, y), 주사위의 크기(size)
# 주사위의 동작 ->  주사위를 생성하는 연산(__init__), 주사위를 던지는 연산(roll_dice), 주사위의 값을 읽는 연산(read_dice), 주사위를 화면에 출력하는 연산(print_dice)
# 주사위 클래스 Lab 
