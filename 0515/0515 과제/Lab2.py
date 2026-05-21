import math

class Circle: # Circle 클래스를 정의함.
    def __init__(self, radius = 0): # 객체 생성할 때 반지름 저장함.
        self.radius = radius

    def getArea(self): # 원의 넓이 구하기
        return math.pi * self.radius * self.radius

    def getPerimeter(self): # 원의 둘레 구하기
        return 2 * math.pi * self.radius


c = Circle(10) # # Circle 객체를 생성함.
print("원의 면적", c.getArea())
print("원의 둘레", c.getPerimeter())

# 원 클래스 정의 Lab
