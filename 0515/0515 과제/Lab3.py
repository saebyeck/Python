class Car:
    def __init__(self, speed, color, model): # # 객체 생성할 때 속도, 색상, 모델 저장
        self.speed = speed
        self.color = color
        self.model = model

    def drive(self): # 자동차 주행 상태 
        self.speed = 60


myCar = Car(0, "blue", "E-class") # 자동차 객체 생성

print("자동차 객체를 생성하였습니다.")
print("자동차의 속도는", myCar.speed) # 현재 속도 출력
print("자동차의 색상은", myCar.color) # 자동차 색상 출력
print("자동차의 모델은", myCar.model) # 자동차 모델 출력

myCar.drive() # drive 함수 실행
print("자동차의 속도는", myCar.speed) # 변경된 속도 출력

# 자동차 클래스 정의 Lab